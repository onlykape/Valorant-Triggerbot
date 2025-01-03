import platform, hashlib, ctypes, os, time, requests, subprocess, uuid
from termcolor import colored
from datetime import datetime
from dateutil.parser import parse

tanggal_waktu_berhenti = "2025-01-10 10:50:00" # thn-bln-tgl-jam
waktu_berhenti = parse(tanggal_waktu_berhenti)

if datetime.now() >= waktu_berhenti:
    ctypes.windll.user32.MessageBoxW(0,"Cheat Triggerbot Valorant Sudah Usang.","Triggerbot Expired.",0x30 | 0x1,)
    os._exit(1)

def get_hwid():
    system_info = platform.uname()
    hwid_str = f"{system_info.system}-{system_info.node}-{system_info.release}-{system_info.version}-{system_info.machine}".encode()
    hwid = hashlib.sha256(hwid_str).hexdigest()
    hwid_parts = [hwid[:8],hwid[8:12],hwid[12:16],hwid[16:20],hwid[-12:-1],]
    # Mengambil 12 karakter terakhir, kecuali karakter terakhir (agar format sesuai) | -1 sampai -11 | log -1
    formatted_hwid = "-".join(hwid_parts)
    return formatted_hwid

class CColor:
    Red = "\033[91m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Cyan = "\u001b[36m"
    White = "\033[0m"
Color = CColor()


def send_discord(hwid):
    device_model = platform.version()
    # device_model = platform.node()
    webhook_url = "https://discord.com/api/webhooks/1318845621892808714/4yZ8IAkw94qlLONjseYWjZUu__7NiwZJSIFLBUfjCjQNNMfQZoS3mhvIjTwlbcac3Gbz"
    data = {"content": f"{device_model}-{hwid}-Save To Use"}
    # data = {"content": f"{device_model}-{hwid}-Save To Use Development Mode"}
    requests.post(webhook_url, data=data)

def validate_password(password):
    hwid = get_hwid()
    return password == hwid

def save_hwid_to_token(hwid):
    with open("data\Akp", "w") as file:
        file.write(hwid)

def check_token_existence():
    return os.path.exists("data\Akp")

if __name__ == "__main__":
    hwid = get_hwid()
    text = colored(
        """
     ██╗██╗   ██╗ █████╗ ██╗      ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗   ██╗██╗   ██╗██╗██████╗ ██╗██████╗ 
     ██║██║   ██║██╔══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║██║   ██║██║██╔══██╗██║██╔══██╗
     ██║██║   ██║███████║██║     ██║     ███████║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║██████╔╝██║██║  ██║
██   ██║██║   ██║██╔══██║██║     ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝╚██╗ ██╔╝██║██╔═══╝ ██║██║  ██║
╚█████╔╝╚██████╔╝██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║   ██║    ╚████╔╝  ╚████╔╝ ██║██║██╗  ██║██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝    ╚═══╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                                                  
""", "white")  # , attrs=["bold"],
    print(text)
    max_attempts = 3
    if check_token_existence():
        # print("\nID sudah VALID.")
        # send_discord(hwid)
        os.startfile("2 Tugas Kelompok")
        os._exit(1)
    else:
        hwid = get_hwid()
        print(f"\nID Anda : {hwid}")
    for i in range(max_attempts):
        pwd = input("\n1. Copy ID-nya diatas.\n\n2. Dan Paste ID-nya dibawah ini\n   -> : ")
        save_hwid_to_token(hwid)
        # send_discord(hwid)
        os.system("cls")
        text = colored(
        """
     ██╗██╗   ██╗ █████╗ ██╗      ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗   ██╗██╗   ██╗██╗██████╗ ██╗██████╗ 
     ██║██║   ██║██╔══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║██║   ██║██║██╔══██╗██║██╔══██╗
     ██║██║   ██║███████║██║     ██║     ███████║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║██████╔╝██║██║  ██║
██   ██║██║   ██║██╔══██║██║     ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝╚██╗ ██╔╝██║██╔═══╝ ██║██║  ██║
╚█████╔╝╚██████╔╝██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║   ██║    ╚████╔╝  ╚████╔╝ ██║██║██╗  ██║██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝    ╚═══╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                                                  
""", "white") # , attrs=["bold"],
        print(text)
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        text = colored(
        """
     ██╗██╗   ██╗ █████╗ ██╗      ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗   ██╗██╗   ██╗██╗██████╗ ██╗██████╗ 
     ██║██║   ██║██╔══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║██║   ██║██║██╔══██╗██║██╔══██╗
     ██║██║   ██║███████║██║     ██║     ███████║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║██████╔╝██║██║  ██║
██   ██║██║   ██║██╔══██║██║     ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝╚██╗ ██╔╝██║██╔═══╝ ██║██║  ██║
╚█████╔╝╚██████╔╝██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║   ██║    ╚████╔╝  ╚████╔╝ ██║██║██╗  ██║██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝    ╚═══╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                                                  
""", "red") # , attrs=["bold"],
        print(text)
        print("Check Server in Discord...")
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        text = colored(
        """
     ██╗██╗   ██╗ █████╗ ██╗      ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗   ██╗██╗   ██╗██╗██████╗ ██╗██████╗ 
     ██║██║   ██║██╔══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║██║   ██║██║██╔══██╗██║██╔══██╗
     ██║██║   ██║███████║██║     ██║     ███████║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║██████╔╝██║██║  ██║
██   ██║██║   ██║██╔══██║██║     ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝╚██╗ ██╔╝██║██╔═══╝ ██║██║  ██║
╚█████╔╝╚██████╔╝██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║   ██║    ╚████╔╝  ╚████╔╝ ██║██║██╗  ██║██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝    ╚═══╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                                                  
""", "green",) # , attrs=["bold"],
        print(text)
        print("Check Server in Discord......")
        time.sleep(0.1)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        text = colored(
        """
     ██╗██╗   ██╗ █████╗ ██╗      ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗   ██╗██╗   ██╗██╗██████╗ ██╗██████╗ 
     ██║██║   ██║██╔══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║██║   ██║██║██╔══██╗██║██╔══██╗
     ██║██║   ██║███████║██║     ██║     ███████║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║██████╔╝██║██║  ██║
██   ██║██║   ██║██╔══██║██║     ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝╚██╗ ██╔╝██║██╔═══╝ ██║██║  ██║
╚█████╔╝╚██████╔╝██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║   ██║    ╚████╔╝  ╚████╔╝ ██║██║██╗  ██║██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝    ╚═══╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                                                  
""", "blue") # , attrs=["bold"],
        print(text)
        print("Check Server in Discord..........")
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        text = colored(
        """
     ██╗██╗   ██╗ █████╗ ██╗      ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗   ██╗██╗   ██╗██╗██████╗ ██╗██████╗ 
     ██║██║   ██║██╔══██╗██║     ██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║██║   ██║██║██╔══██╗██║██╔══██╗
     ██║██║   ██║███████║██║     ██║     ███████║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║██████╔╝██║██║  ██║
██   ██║██║   ██║██╔══██║██║     ██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ╚██╗ ██╔╝╚██╗ ██╔╝██║██╔═══╝ ██║██║  ██║
╚█████╔╝╚██████╔╝██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║   ██║    ╚████╔╝  ╚████╔╝ ██║██║██╗  ██║██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝     ╚═══╝    ╚═══╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                                                                  
""", "light_cyan",) # , attrs=["bold"],
        print(text)
        # print("ID Ditemukan!")
        time.sleep(0.1)
        if validate_password(pwd):
            time.sleep(0.1)
            print(f"Akses Dibuka!")
            # ctypes.windll.user32.MessageBoxW(0, "Akses Dibuka!", "Correct!", 0x40 | 0x1)
            os.startfile("Fisika")
            # os._exit(1)
            # Lanjutkan eksekusi program di sini
            break
        else:
            attempts_left = max_attempts - i - 1
            if attempts_left > 0:
                print(f"ID salah! Sisa percobaan: {attempts_left}")
            else:
                # print("")
                ctypes.windll.user32.MessageBoxW(0,"Anda telah mencapai batas percobaan. Akses ditolak.","Peringatan",0x10 | 0x1,)
                os._exit(1)