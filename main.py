from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram.ext import filters
from handlers.start import start
from handlers.help import list_currencies
from handlers.convert import convert
from handlers.presets import create_preset, retrieve_presets, delete_preset
from handlers.button_handlers import button_handler
from handlers.stats import info


app = ApplicationBuilder().token(
    "501469216:AAHXWA7VrKJjA7WJlPjspG6VDbuAyBqu2v4").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("currencies", list_currencies))
app.add_handler(CommandHandler("convert", convert))


# preset handlers
app.add_handler(CommandHandler("create", create_preset))

app.add_handler(CommandHandler("delete", delete_preset))


app.add_handler(CommandHandler("presets", retrieve_presets))

app.add_handler(CallbackQueryHandler(button_handler))

app.add_handler(CommandHandler("info", info))


app.run_polling()
