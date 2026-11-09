import requests

def send_telegram_message(message):
    # Replace with your actual Telegram Bot Token and Chat ID
    BOT_TOKEN = "9159122726:AAG6XqWqFcD4YbHn2XkFMZF3q7eW6kCgNU4"
    CHAT_ID = "8537372602"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Message sent successfully to Telegram!")
        return True
    else:
        print(f"Error occurred: {response.text}")
        return False

if __name__ == "__main__":
    # Test message to send via your bot
    user_input = "Hello! This is a test message sent from my app/script."
    send_telegram_message(user_input)
