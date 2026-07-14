from flask import Flask
from threading import Thread
import telebot
from openai import OpenAI
import os

# 1. السيرفر الوهمي
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
  app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. كود البوت
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DEEPSEEK_API_KEY = os.getenv("GEMINI_API_KEY") # بنستخدم نفس المتغير عشان ما نغير في Render

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "هلا! انا بوت الكود الذكي 🤖\nارسل لي ايش تبغى اكتب لك كود")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = f"انت بوت مبرمج محترف. جاوب بالكود المطلوب واشرحه ببساطة بالعربي. سؤال: {message.text}"

    bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, f"صار خطأ: {e}")

print("البوت شغال...")
keep_alive()
bot.polling(none_stop=True)
