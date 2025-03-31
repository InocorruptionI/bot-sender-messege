from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router

router = Router

admin_start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Администратор', callback_data='admin'),
                                                        InlineKeyboardButton(text='Пользователь', callback_data='user')]])