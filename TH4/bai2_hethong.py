from gpiozero import LED
import matplotlib.pyplot as plt
#Cài thư viện
#sudo apt update
#sudo apt install python3-pip
#pip3 install matplotlib gpiozero

from collections import deque
import time

# LED nối GPIO17
led = LED(17)

plt.ion()

temps = deque(maxlen=30)

fig, ax = plt.subplots()

while True:
    # Đọc nhiệt độ CPU
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        temp = float(f.read()) / 1000

    temps.append(temp)

    # Vẽ đồ thị
    ax.clear()
    ax.plot(list(temps), marker='o')
    ax.set_title("CPU Temperature")
    ax.set_ylabel("Temperature (°C)")
    ax.set_ylim(20, 90)
    plt.pause(0.01)

    print(f"CPU Temp: {temp:.2f} °C")

    # Điều khiển LED
    if temp > 60:
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    else:
        led.off()
        time.sleep(1)
