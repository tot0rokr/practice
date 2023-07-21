import signal
import time


def handler(signum, frame):
    print("handler")
    raise SystemExit

signal.signal(signal.SIGTERM, handler)


def main():
    print("main")
    while True:
        time.sleep(10000)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("interrupt")
    finally:
        print("terminate")

