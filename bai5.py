import socket
import subprocess
import yagmail
from datetime import datetime

EMAIL = "duy14022006l@gmail.com"
PASSWORD = "ihll lcwd rnkd uinu"

TO = "duy14022006l@gmail.com"

def get_ip():
    try:
        ip = subprocess.check_output(
            "hostname -I",
            shell=True
        ).decode().strip()
        return ip
    except:
        return "Không lấy được IP"

hostname = socket.gethostname()
ip = get_ip()

subject = "Raspberry Pi IP"

body = f"""
Raspberry Pi vừa khởi động

Tên máy: {hostname}

IP:
{ip}

Thời gian:
{datetime.now()}
"""

yag = yagmail.SMTP(EMAIL, PASSWORD)
yag.send(TO, subject, body)

print("Đã gửi Email.")
