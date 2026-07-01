import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN", "8935917068:AAG0dg0P4y1klnG7gCj4HdXZbxRD7s3yPCo")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    text = (
        "🎰 Stake US — BONUS2026\n\n"
        "🔑 Promo code: BONUS2026\n"
        "🔗 Claim now: https://stake.us/?c=bonus2026\n\n"
        "🎁 What you get:\n\n"
        "💰 Free Gold Coins on signup\n"
        "⚡ Stake Cash — no deposit required\n"
        "🎮 Exclusive bonus for new US players\n\n"
        "📋 How to claim:\n\n"
        "1️⃣ Sign up via the link above\n"
        "2️⃣ Enter code BONUS2026 at registration\n"
        "3️⃣ Free coins credited instantly to your account\n\n"
        "✅ Good luck!"
    )
    bot.reply_to(message, text)

print("Stake US bot started...")
bot.infinity_polling()
