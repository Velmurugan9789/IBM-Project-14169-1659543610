from random import *
import time
import os

file ="continous.wav"
while(True):
    temp = randint(1, 100)
    humidity = randint(1, 100)
    if (temp > 40 and humidity > 40):
        os.system(file)
        time.sleep(11)
    print('temperature',temp)
    print('humidity',humidity)
        


