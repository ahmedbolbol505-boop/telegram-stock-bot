import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# حط هنا التوكن بتاع البوت بتاعك من BotFather
TOKEN = "YOUR_BOT_TOKEN"

# دالة تجيب سعر السهم من API مجاني
def get_stock_price(symbol):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
    data = requests.get(url).json()
    try:
        price = data["quoteResponse"]["result"][0]["regularMarketPrice"]
        currency = data["quoteResponse"]["result"][0]["currency"]
        return f"سعر {symbol} الآن: {price} {currency}"
    except:
        return "⚠️ رمز السهم غير صحيح أو غير متاح حالياً."

# دالة الأمر /price
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("اكتب رمز السهم بعد الأمر /price مثل: /price AAPL")
        return
    symbol = context.args[0].upper()
    result = get_stock_price(symbol)
    await update.message.reply_text(result)

# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("price", price))

print("✅ Bot is running...")
app.run_polling()
