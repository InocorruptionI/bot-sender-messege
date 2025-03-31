from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, User

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import admin_start_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    id_konst = 498037596
    if id_konst == message.from_user.id:
        await message.answer('Привет, выбери функционал: ', reply_markup=admin_start_kb)
    else:
        await message.answer('Сорри чел, для обычных пользователей еще не придуман функционал...')



