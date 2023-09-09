## Development

1. Install [Python 3.11.4 amd64][https://www.python.org/downloads/].
1. Install packages.
    ```cmd
    pip install mss
    pip install requests
    ```
1. Edit variables on file `src/main`:
    - `CHAT_ID`.
    - `TELEGRAM_BOT_TOKEN`.
1. Run python script.
    ```cmd
    python src/main.py
    ```

## Production

On Windows 10:
1. `Win` + `R`.
1. `shell:startup`.
1. `Enter`.
1. Create file `start-as-daemon.bat`.
    ```bat
    @echo off
    start /B pythonw C:/[YourPath]/src/main.py
    exit
    ```
