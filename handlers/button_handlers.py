from telegram import Update
from telegram.ext import ContextTypes
from db_config import delete_preset
from .convert import convert_base
import ast

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_id = update.callback_query.from_user.id
   
    query = update.callback_query
    await query.answer()

    preset = ast.literal_eval(query.data)


    from_currency, to_currency, amount = preset['preset'].split()

    if (preset['handler'] == 'get'):
        response = convert_base(from_currency, to_currency, amount)
        await query.edit_message_text(text=response)

    elif (preset['handler'] == 'delete'):
        delete_preset(user_id, preset['preset'])
        await query.edit_message_text(text=f"deleted preset: {preset['preset']}")


        
