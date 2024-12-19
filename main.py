import datetime
import time
from pathlib import Path

import requests
import schedule

HOSTNAME = "https://www.google.com/"
TIMEOUT = 5
LOG_FILE = Path("network_check.log")
ERRORS_LOG_FILE = Path("errors.log")

no_internet = False


def log_no_internet(log_file: Path, timestamp: str) -> None:
    with log_file.open("a", encoding="utf-8") as log:
        log.write(f"{timestamp} - ")


def log_internet_back(log_file: Path, timestamp: str) -> None:
    with log_file.open("a", encoding="utf-8") as log:
        log.write(f"{timestamp.split()[1]} (no internet)\n")


def ping(hostname: str, timeout: int, log_file: Path) -> bool:
    global no_internet
    log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{log_time}]", f"Pinging `{HOSTNAME}` ({timeout}s)...", end=" ")

    try:
        req = requests.get(hostname, timeout=timeout)
        if req.status_code == 200:
            print("success!")

            if no_internet:
                log_internet_back(log_file, log_time)
            no_internet = False

        else:
            print("no internet!")
            if not no_internet:
                log_no_internet(log_file, log_time)
            no_internet = True

    except Exception as e:
        print("no internet!")
        if not no_internet:
            log_no_internet(log_file, log_time)
        no_internet = True

        global ERRORS_LOG_FILE
        with ERRORS_LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"[{log_time}] {e!s}\n")


def main() -> None:
    schedule.every().minute.at(":00").do(ping, hostname=HOSTNAME, timeout=TIMEOUT, log_file=LOG_FILE)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
