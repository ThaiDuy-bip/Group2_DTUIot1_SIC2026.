# -*- coding: utf-8 -*-
import time
import datetime
import RPi.GPIO as GPIO

# C?u hình chân GPIO
TRIG = 23
ECHO = 24
CLK = 17
DT = 18
LED = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
f = open("log.txt", 'a')
a = 10
clkLastState = GPIO.input(CLK)

def read_encoder():
    global a, clkLastState
    clkState = GPIO.input(CLK)
    dtState = GPIO.input(DT)
    if clkState != clkLastState:
        if dtState != clkState:
            a += 1
        else:
            a -= 1
        a = max(2, a)
    clkLastState = clkState


def read_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()
    
    timeout1 = time.time()
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
        if start_time - timeout1 > 0.1:
            return -1

    timeout2 = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
        if stop_time - timeout2 > 0.1:
            return -1

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return distance

def log_event(distance):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Canh bao: Co vat can o khoang cach {distance:.2f} cm (Nho hon a={a} cm)\n")
        #f.flush()
try:
    while True:
        read_encoder()
        dist = read_distance()
        
        if dist == -1:
            print("Loi cam bien va sai day!")
            time.sleep(0.5)
            continue
            
        print(f"Distance: {dist:.2f} cm | Target a: {a} cm")
        
        if dist < a:
            print(f"WARNING: {dist:.2f} < {a}")
            GPIO.output(LED, GPIO.HIGH)
            log_event(dist)
        else:
            GPIO.output(LED, GPIO.LOW)
            
        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
