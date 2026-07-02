# -*- coding: utf-8 -*-
# test_encoder_khong_dau.py
import time
import RPi.GPIO as GPIO

# Cau hinh chan goc cua ban
CLK = 17  # Chan vat ly so 11
DT = 18   # Chan vat ly so 12

GPIO.setwarnings(False)
GPIO.cleanup() 

GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setmode(GPIO.BCM)
# Kich hoat dien tro keo len ben trong Raspberry Pi
GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

a = 10
print("========================================")
print("      TEST ENCODER DUNG NGAT PHAN CUNG  ")
print("========================================")
print(f"Gia tri ban dau a = {a}")
print("HAY XOAY NUM VAN NGAY BAY GIO... Nhan Ctrl+C de dung.\n")

# Ham nay tu dong chay ngam khi chan CLK thay doi trang thai
def encoder_changed(channel):
    global a
    clk_state = GPIO.input(CLK)
    dt_state = GPIO.input(DT)
    
    if clk_state == 0: # Riat xuong cua xung CLK
        if dt_state == 1:
            a += 1
            print(f"--> Xoay SANG PHAI (Tang) | a = {a}")
        else:
            a -= 1
            print(f"<-- Xoay SANG TRAI (Giam) | a = {a}")

# Dang ky ngat phan cung cho chan CLK de nhay nhat co the
GPIO.add_event_detect(CLK, GPIO.FALLING, callback=encoder_changed)

try:
    while True:
        # Vong lap chinh de trong, khong lam gi ca
        # Viec bat xung da co he thong tu dong lo ngam
        time.sleep(1)

except KeyboardInterrupt:
    print("\nDa dung test Encoder.")
    GPIO.cleanup()
    print("GPIO da ve trang thai mac dinh an toan.")
