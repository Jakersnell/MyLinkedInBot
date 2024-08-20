from time import sleep
from random import random

def sleep_rand(min_seconds: float, max_seconds: float) -> None:
    sleep(min_seconds + random() * max_seconds)