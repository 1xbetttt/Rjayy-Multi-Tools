# Copyright (c) Rjay
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner.
#     - Do not resell this tool, do not credit it to yours.
from Program.Config.Config import *
from Program.Config.Util import *

import colorama
from colorama import Fore, Style

Fore.GREEN  = Fore.MAGENTA

try:
    import webbrowser
    import re
    import pyzipper
    from tkinter import messagebox
except Exception as e:
    ErrorModule(e)

# --- Options ---
option_01 = "Website-Vulnerability-Scanner"
option_02 = "Website-Info-Scanner"
option_03 = "Website-Url-Scanner"
option_04 = "Ip-Scanner"
option_05 = "Ip-Port-Scanner"
option_06 = "Ip-Pinger"
option_07 = "Soon"
option_08 = "Soon"
option_09 = "Soon"

option_10 = "D0x-Create"
option_11 = "D0x-Tracker"
option_12 = "Get-Image-Exif"
option_13 = "Google-Dorking"
option_14 = "Username-Tracker"
option_15 = "Email-Tracker"
option_16 = "Email-Lookup"
option_17 = "Phone-Number-Lookup"
option_18 = "Ip-Lookup"
option_19 = "Instagram-Account"

option_20 = "Phishing-Attack"
option_21 = "Password-Zip-Cracked-Attack"
option_22 = "Password-Hash-Decrypted-Attack"
option_23 = "Password-Hash-Encrypted"
option_24 = "Search-In-DataBase"
option_25 = "Dark-Web-Links"
option_26 = "Ip-Generator"
option_27 = "Soon"
option_28 = "Soon"
option_29 = "Soon"

option_30 = "Virus-Builder"

option_31 = "Python-Obfuscator-(Premium)"
option_32 = "Discord-Rat-(Premium)"
option_33 = "Website-DoS-(Premium)"
option_34 = "Proxy-Scraper-(Premium)"
option_35 = "Soon"
option_36 = "Soon"
option_37 = "Soon"
option_38 = "Soon"
option_39 = "Soon"

option_40 = "Roblox-Cookie-Login"
option_41 = "Roblox-Cookie-Info"
option_42 = "Roblox-Id-Info"
option_43 = "Roblox-User-Info"
option_44 = "Soon"
option_45 = "Soon"
option_46 = "Soon"
option_47 = "Soon"
option_48 = "Soon"
option_49 = "Soon"

option_50 = "Discord-Token-Nuker"
option_51 = "Discord-Token-Info"
option_52 = "Discord-Token-Joiner"
option_53 = "Discord-Token-Leaver"
option_54 = "Discord-Token-Login"
option_55 = "Discord-Token-To-Id-And-Brute"
option_56 = "Discord-Token-Server-Raid"
option_57 = "Discord-Token-Spammer"
option_58 = "Discord-Token-Delete-Friends"
option_59 = "Discord-Token-Block-Friends"
option_60 = "Discord-Token-Mass-Dm"
option_61 = "Discord-Token-Delete-Dm"
option_62 = "Discord-Token-Status-Changer"
option_63 = "Discord-Token-Language-Changer"
option_64 = "Discord-Token-House-Changer"
option_65 = "Discord-Token-Theme-Changer"
option_66 = "Discord-Token-Generator"
option_67 = "Discord-Bot-Server-Nuker"
option_68 = "Discord-Bot-Invite-To-Id"
option_69 = "Discord-Server-Info"
option_70 = "Discord-Nitro-Generator"
option_71 = "Discord-Webhook-Info"
option_72 = "Discord-Webhook-Delete"
option_73 = "Discord-Webhook-Spammer"
option_74 = "Discord-Webhook-Generator"
option_75 = "Soon"
option_76 = "Soon"
option_77 = "Soon"
option_78 = "Soon"
option_79 = "Soon"
option_80 = "Soon"

option_next = "Next"
option_back = "Back"
option_site = "Site"
option_info = "Info"

# --- Text display (black & white only) ---
def make_option(num, text):
    return f"[{str(num).zfill(2)}] " + text.ljust(30)[:30].replace("-", " ")

option_01_txt = make_option(1, option_01)
option_02_txt = make_option(2, option_02)
option_03_txt = make_option(3, option_03)
option_04_txt = make_option(4, option_04)
option_05_txt = make_option(5, option_05)
option_06_txt = make_option(6, option_06)
option_07_txt = make_option(7, option_07)
option_08_txt = make_option(8, option_08)
option_09_txt = make_option(9, option_09)

option_10_txt = make_option(10, option_10)
option_11_txt = make_option(11, option_11)
option_12_txt = make_option(12, option_12)
option_13_txt = make_option(13, option_13)
option_14_txt = make_option(14, option_14)
option_15_txt = make_option(15, option_15)
option_16_txt = make_option(16, option_16)
option_17_txt = make_option(17, option_17)
option_18_txt = make_option(18, option_18)
option_19_txt = make_option(19, option_19)

option_20_txt = make_option(20, option_20)
option_21_txt = make_option(21, option_21)
option_22_txt = make_option(22, option_22)
option_23_txt = make_option(23, option_23)
option_24_txt = make_option(24, option_24)
option_25_txt = make_option(25, option_25)
option_26_txt = make_option(26, option_26)
option_27_txt = make_option(27, option_27)
option_28_txt = make_option(28, option_28)
option_29_txt = make_option(29, option_29)

option_30_txt = make_option(30, option_30)
option_31_txt = make_option(31, option_31)
option_32_txt = make_option(32, option_32)
option_33_txt = make_option(33, option_33)
option_34_txt = make_option(34, option_34)
option_35_txt = make_option(35, option_35)
option_36_txt = make_option(36, option_36)
option_37_txt = make_option(37, option_37)
option_38_txt = make_option(38, option_38)
option_39_txt = make_option(39, option_39)

option_40_txt = make_option(40, option_40)
option_41_txt = make_option(41, option_41)
option_42_txt = make_option(42, option_42)
option_43_txt = make_option(43, option_43)
option_44_txt = make_option(44, option_44)
option_45_txt = make_option(45, option_45)
option_46_txt = make_option(46, option_46)
option_47_txt = make_option(47, option_47)
option_48_txt = make_option(48, option_48)
option_49_txt = make_option(49, option_49)

option_50_txt = make_option(50, option_50)
option_51_txt = make_option(51, option_51)
option_52_txt = make_option(52, option_52)
option_53_txt = make_option(53, option_53)
option_54_txt = make_option(54, option_54)
option_55_txt = make_option(55, option_55)
option_56_txt = make_option(56, option_56)
option_57_txt = make_option(57, option_57)
option_58_txt = make_option(58, option_58)
option_59_txt = make_option(59, option_59)

option_60_txt = make_option(60, option_60)
option_61_txt = make_option(61, option_61)
option_62_txt = make_option(62, option_62)
option_63_txt = make_option(63, option_63)
option_64_txt = make_option(64, option_64)
option_65_txt = make_option(65, option_65)
option_66_txt = make_option(66, option_66)
option_67_txt = make_option(67, option_67)
option_68_txt = make_option(68, option_68)
option_69_txt = make_option(69, option_69)

option_70_txt = make_option(70, option_70)
option_71_txt = make_option(71, option_71)
option_72_txt = make_option(72, option_72)
option_73_txt = make_option(73, option_73)
option_74_txt = make_option(74, option_74)
option_75_txt = make_option(75, option_75)
option_76_txt = make_option(76, option_76)
option_77_txt = make_option(77, option_77)
option_78_txt = make_option(78, option_78)
option_79_txt = make_option(79, option_79)

option_back_txt = option_back + " [B]"
option_next_txt = option_next + " [N]"
option_site_txt = "[S] " + option_site
option_info_txt = "[I] " + option_info

menu1 = f""" ┌─ {option_info_txt}                                                                                               {option_next_txt} ─┐
 ├─ {option_site_txt} ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │
 └─┬─────────┤ Network Scanner ├─────────┬──────────────┤ Osint ├──────────────┬────────────┤ Utilities ├────────────┴─
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {option_01_txt                    }├─ {option_10_txt                    }├─ {option_20_txt}
   ├─ {option_02_txt                    }├─ {option_11_txt                    }├─ {option_21_txt}
   ├─ {option_03_txt                    }├─ {option_12_txt                    }├─ {option_22_txt}
   ├─ {option_04_txt                    }├─ {option_13_txt                    }├─ {option_23_txt}
   ├─ {option_05_txt                    }├─ {option_14_txt                    }├─ {option_24_txt}
   └─ {option_06_txt                    }├─ {option_15_txt                    }├─ {option_25_txt}
                                         ├─ {option_16_txt                    }└─ {option_26_txt}
                                         ├─ {option_17_txt                    }
                                         ├─ {option_18_txt                    }
                                         └─ {option_19_txt                    }

"""

menu2 = f""" ┌─ {option_info_txt}                                                                                                {option_next_txt} ─┐
 ├─ {option_site_txt}  ┌───────────────┐                         ┌──────┐                              ┌────────┐    {option_back_txt} ─┤
─┴─┬──────────┤ Virus Builder ├──────────┬──────────────┤ Paid ├───────────────┬──────────────┤ Roblox ├──────────────┴─
   │          └───────────────┘          │              └──────┘               │              └────────┘
   └─ {option_30_txt                    }├─ {option_31_txt                    }├─ {option_40_txt}
           ├─ Stealer                    ├─ {option_32_txt                    }├─ {option_41_txt}
           ├─ Grabber                    ├─ {option_33_txt                    }├─ {option_42_txt}
           └─ Malware                    └─ {option_34_txt                    }└─ {option_43_txt}                                    






"""

menu3 = f""" ┌─ {option_info_txt}                                                                                                {option_back_txt} ─┐
 ├─ {option_site_txt}                                           ┌─────────┐                                                    │
─┴─┬───────────────────────────────────────────────────┤ Discord ├────────────────────────────────────────────────────┘
   │                                                   └─────────┘                       
   ├─ {option_50_txt                    }┌─ {option_60_txt                    }┌─ {option_70_txt}
   ├─ {option_51_txt                    }├─ {option_61_txt                    }├─ {option_71_txt}
   ├─ {option_52_txt                    }├─ {option_62_txt                    }├─ {option_72_txt}
   ├─ {option_53_txt                    }├─ {option_63_txt                    }├─ {option_73_txt}
   ├─ {option_54_txt                    }├─ {option_64_txt                    }├─ {option_74_txt}
   ├─ {option_55_txt                    }├─ {option_65_txt                    }│
   ├─ {option_56_txt                    }├─ {option_66_txt                    }│
   ├─ {option_57_txt                    }├─ {option_67_txt                    }│
   ├─ {option_58_txt                    }├─ {option_68_txt                    }│
   ├─ {option_59_txt                    }├─ {option_69_txt                    }│
   └─────────────────────────────────────┴─────────────────────────────────────┘
"""

def Update():
    popup_version = ""
    try:
        if requests:
            new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', requests.get(url_config).text).group(1)
            if new_version != version_tool:
                webbrowser.open(f"https://guns.lol/xclsvmonx")
                colorama.init()
                input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Please install the new version of the tool: {white + version_tool + red} -> {white + new_version} ")
                popup_version = f"{red}New Version: {white + version_tool + red} -> {white + new_version}"
                colorama.deinit()
                Clear()
    except:
        pass

    return popup_version

menu_path = os.path.join(tool_path, "Program", "Config", "Menu.txt")

# Menus remain same as before, just using plain text vars above
# ... (menu1, menu2, menu3 definitions remain the same but without colors)

# --- Main menu loop ---
def Menu():
    popup_version = ""
    try:
        with open(menu_path, "r") as file:
            menu_number = file.read()
        menu_mapping = {"1": menu1, "2": menu2, "3": menu3}
        menu = menu_mapping.get(menu_number, menu1)
    except:
        menu = menu1
        menu_number = "1"

    banner = f"""
                            ██████╗       ██╗ █████╗ ██╗   ██╗██╗   ██╗
                            ██╔══██╗      ██║██╔══██╗╚██╗ ██╔╝╚██╗ ██╔╝
                            ██████╔╝      ██║███████║ ╚████╔╝  ╚████╔╝ 
                            ██╔══██╗ ██   ██║██╔══██║  ╚██╔╝    ╚██╔╝  
                            ██║  ██║ ╚█████╔╝██║  ██║   ██║     ██║    
                            ╚═╝  ╚═╝  ╚════╝ ╚═╝  ╚═╝   ╚═╝     ╚═╝
                                           RJAYY Multi Tools
{menu}"""
    return banner, menu_number

while True:
    try:
        Clear()
        banner, menu_number = Menu()
        Title(f"Rjayy Multi Tools - Menu {menu_number}")
        Slow(banner)

        choice = input(f" ┌──({username_pc}@rjayy)─[~/{os_name}/Menu-{menu_number}]\n └─$ ")

        # Navigation
        if choice.lower() in ['n', 'next']:
            menu_number = {"1": "2", "2": "3", "3": "1"}.get(menu_number, "1")
            with open(menu_path, "w") as file:
                file.write(menu_number)
            continue

        elif choice.lower() in ['b', 'back']:
            menu_number = {"2": "1", "3": "2"}.get(menu_number, "1")
            with open(menu_path, "w") as file:
                file.write(menu_number)
            continue

        elif choice.lower() in ['i', 'info']:
            StartProgram(f"{option_info}.py")
            continue

        elif choice.lower() in ['s', 'site']:
            StartProgram(f"{option_site}.py")
            continue

        elif choice == '30':
            if os_name == "Linux":
                print("\n[INFO] The builder virus is only compatible with Windows.")
                messagebox.showinfo("RJAY Multi Tools - Virus Builder", 
                                    "The builder virus is only compatible with Windows.")

            print("\n[INFO] Disable antivirus before building.")
            messagebox.showinfo("RJAY Multi Tools - Virus Builder", 
                                "Disable antivirus before building.")
            try:
                zip_file_path = os.path.join(tool_path, "Program", "FileDetectedByAntivirus", "Password(redtiger).zip")
                file_path = os.path.join(tool_path, "Program", "FileDetectedByAntivirus", "VirusBuilderOptions.py")
                output = os.path.join(tool_path, "Program", "FileDetectedByAntivirus")
                if not os.path.exists(file_path):
                    if os.path.exists(zip_file_path):
                        print(f"[INFO] Decompressing: Program\\FileDetectedByAntivirus\\Password(redtiger).zip")
                        with pyzipper.AESZipFile(zip_file_path) as zf:
                            zf.pwd = b'redtiger'
                            zf.extractall(output)
                        time.sleep(3)
                    else:
                        print("[ERROR] Files missing. Please reinstall.")
            except Exception as e:
                Error(e)
            continue  # para bumalik sa loop

        # Options dictionary
        options = {
            '01': option_01, '02': option_02, '03': option_03, '04': option_04,
            '05': option_05, '06': option_06, '07': option_07, '08': option_08,
            '09': option_09, '10': option_10, '11': option_11, '12': option_12,
            '13': option_13, '14': option_14, '15': option_15, '16': option_16,
            '17': option_17, '18': option_18, '19': option_19, '20': option_20,
            '21': option_21, '22': option_22, '23': option_23, '24': option_24,
            '25': option_25, '26': option_26, '27': option_27, '28': option_28,
            '29': option_29, '30': option_30, '31': option_31, '32': option_32,
            '33': option_33, '34': option_34, '35': option_35, '36': option_36,
            '37': option_37, '38': option_38, '39': option_39, '40': option_40,
            '41': option_41, '42': option_42, '43': option_43, '44': option_44,
            '45': option_45, '46': option_46, '47': option_47, '48': option_48,
            '49': option_49, '50': option_50, '51': option_51, '52': option_52,
            '53': option_53, '54': option_54, '55': option_55, '56': option_56,
            '57': option_57, '58': option_58, '59': option_59, '60': option_60,
            '61': option_61, '62': option_62, '63': option_63, '64': option_64,
            '65': option_65, '66': option_66, '67': option_67, '68': option_68,
            '69': option_69, '70': option_70, '71': option_71, '72': option_72,
            '73': option_73, '74': option_74, '75': option_75, '76': option_76,
            '77': option_77, '78': option_78, '79': option_79
        }

        # Ayusin ang input para sure tugma sa keys
        choice = choice.strip().zfill(2)

        if choice in options:
            StartProgram(f"{options[choice]}.py")
        else:
            ErrorChoiceStart()

    except Exception as e:
        Error(e)
