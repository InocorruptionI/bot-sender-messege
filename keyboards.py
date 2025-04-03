from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router

router = Router

hi_ad_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Администратор', callback_data='admin'),
                                                        InlineKeyboardButton(text='Пользователь', callback_data='user')]])


main_ad_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Создать пост')],
                                           [KeyboardButton(text='Показать запланированные посты')],
                                           [KeyboardButton(text='Удалить все запланированные посты')]],
                                 resize_keyboard=True,
                                 one_time_keyboard=True)


