import smtplib
import socket
import subprocess
from email.message import EmailMessage
from datetime import datetime

# Thông tin Gmail
EMAIL = "duy14022006l@gmail.com"
APP_PASSWORD = "ihll lcwd rnkd uinu"
RECEIVER = "duy14022006l@gmail.com"


def lay_ip():
    try:
        result = subprocess.run(
            ["hostname", "-I"],
            capture_output=True,
            text=True
        )

        ip_list = result.stdout.strip().split()

        if len(ip_list) == 0:
            return "Khong tim thay IP"

        return ip_list[0]

    except Exception:
        return "Loi lay IP"


def gui_email():
    ten_may = socket.gethostname()
    dia_chi_ip = lay_ip()
    thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    noi_dung = f"""
Raspberry Pi da khoi dong thanh cong.

Ten may: {ten_may}

Dia chi IP: {dia_chi_ip}

Thoi gian:
{thoi_gian}
"""

    message = EmailMessage()
    message["Subject"] = "Thong bao Raspberry Pi"
    message["From"] = EMAIL
    message["To"] = RECEIVER
    message.set_content(noi_dung)

    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL, APP_PASSWORD)
        smtp.send_message(message)
        smtp.quit()

        print("Gui email thanh cong!")

    except Exception as error:
        print("Gui email that bai!")
        print(error)


if __name__ == "__main__":
    gui_email()
