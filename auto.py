# imported
import pyautogui, time, os

# install ---> pip install pyautogui

os.system("pip install pyautogui")
# ============================my message================================
def myInput():
    os.system("del message.txt")
    a = input("my message : ")
    with open('message.txt', 'a') as file:
        for tx in a:
            file.write(tx)
        file.close()
# ==========================spammer======================================
def spamer():
    time.sleep(3)
    with open('message.txt', 'r') as file:
        word = file.read()
        file.close()
# =============================start spam===============================
        while True:
            time.sleep(3)
            pyautogui.press("enter")
            for i in word:
                pyautogui.typewrite(i)
# =====================================================================
myInput()
value = input("start spam (y/n): ")
if value == "y":
    spamer()
elif value == "n":
    print("end")
else:
    print("erorrrrrr")