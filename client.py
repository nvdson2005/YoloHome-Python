from Adafruit_IO import Client
from Adafruit_IO.errors import RequestError
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("AIO_USERNAME")
key = os.getenv("AIO_KEY")

if not username or not key:
    raise RuntimeError("Missing AIO_USERNAME or AIO_KEY in environment/.env")

aio = Client(username=username, key=key)

try:
    me = aio.username  # lightweight auth check
    print(f"Connected to Adafruit IO as: {me}")
except RequestError as e:
    print("Adafruit IO connection failed:", e)

try:
    feed = aio.feeds()
    print("Available feeds:")
    for f in feed:
        print(f" - {f.name} (key: {f.key})") 
except RequestError as e:
    print("Failed to receive data from feeds:", e)