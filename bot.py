import telebot
import google.generativeai as genai
import os

# الكود بيقرا التوكنات من Render تلقائي
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# تفعيل Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "هلا! انا بوت الكود الذكي 🤖\nارسل لي ايش تبغى اكتب لك كود")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = f"انت بوت مبرمج محترف. جاوب بالكود المطلوب واشرحه ببساطة بالعربي. لو فيه خطأ صلحه. سؤال المستخدم: {message.text}"
    
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = model.generate_content(prompt)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"صار خطأ: {e}")

print("البوت شغال...")
bot.polling(none_stop=True)