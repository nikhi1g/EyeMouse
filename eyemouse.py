import pyautogui
from time import sleep
import example
from threading import Thread
Thread(target=example.onstart()).start()

clickconfidence = 0
while True:
    print('i')