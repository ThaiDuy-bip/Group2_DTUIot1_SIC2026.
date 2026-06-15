from gpiozero import LED
from time import sleep
ledR = LED(14)
ledG = LED(15)
ledY = LED(18)
while True:
    ledR.on()
    sleep(0.1)
    ledR.off()
    ledG.on()
    sleep(0.1)
    ledG.off()
    ledY.on()
    sleep(0.1)
    ledY.off()
