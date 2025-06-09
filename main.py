import time
from app import emojis

def main():
    with emojis.unzip():
        print("Hello from gen-botpic!")
        time.sleep(2)


if __name__ == "__main__":
    main()
