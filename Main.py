import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام رضوان! ربات فعاله و آماده‌ست ✅")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    # سیگنال نمونه:
    bot.reply_to(message, "📊 سیگنال آزمایشی:\n✅ خرید بیت‌کوین\n❌ فروش طلا")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "برای دریافت سیگنال بنویس: /signal")

bot.infinity_polling()
