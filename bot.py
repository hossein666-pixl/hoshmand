import openai
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# توکن ربات تلگرام
TELEGRAM_TOKEN = '7278576718:AAFbCmSzoWvaU41tRTdfLpN05ZKPy4hvFlA'

# کلید API OpenAI
openai.api_key = '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'

# پیکربندی لاگ‌گیری
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# تابع برای دستورات شروع
async def start(update: Update, context):
    await update.message.reply_text('سلام! من یک دستیار هوشمند هستم. چطور می‌توانم به شما کمک کنم؟')

# تابع برای ارسال پیام به OpenAI GPT
async def chat_with_gpt(update: Update, context):
    user_message = update.message.text

    # ارسال پیام به OpenAI و دریافت جواب
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # یا مدل‌های جدیدتر مانند gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        gpt_reply = response['choices'][0]['message']['content'].strip()
        await update.message.reply_text(gpt_reply)
    except Exception as e:
        await update.message.reply_text("خطا در ارتباط با OpenAI: " + str(e))

# ایجاد و پیکربندی ربات
application = Application.builder().token(TELEGRAM_TOKEN).build()

# ثبت هندلرها
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gpt))

# شروع ربات
application.run_polling()
