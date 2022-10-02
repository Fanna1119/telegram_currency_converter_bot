from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def preset_keyboard(presets, handler):
    pre = [{"preset": preset, 'handler': handler} for preset in presets]

    buttons = [InlineKeyboardButton(
        preset['preset'], callback_data=str(preset)) for preset in pre]

    
    keyboard = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]

    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup

