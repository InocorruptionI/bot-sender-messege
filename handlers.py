from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, User

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from mypy.state import state

from keyboards import *
import redis


redis_client = redis.Redis(host='localhost', port=6379, db=0)

router = Router()


class DataStates(StatesGroup):
    date_post = State()
    name_post = State()
    text_post = State()
    id_post = State()


@router.message(CommandStart())
async def start(message: Message):
    id_konst = 498037596
    if id_konst == message.from_user.id:
        await message.answer('Привет, выбери функционал: ', reply_markup=hi_ad_kb)
    else:
        await message.answer('Сорри чел, для обычных пользователей еще не придуман функционал...')


@router.callback_query(F.data == 'admin' or F.text == 'В главное меню')
async def main_hd(callback: CallbackQuery):
    await callback.message.answer('Выбери действие', reply_markup=main_ad_kb)


@router.message(F.text == 'Создать пост')
async def create_post_hd(message: Message, state: FSMContext):
    await message.answer('Введи название поста')
    await state.set_state(DataStates.name_post)


@router.message(DataStates.name_post)
async def save_postname(message: Message, state: FSMContext):
    await message.answer('Отлично, имя поста есть! \n Теперь пиши сам пост, пока что можно только словами, ну и цифрами'
                         'естественно')
    post_name = message.text
    await redis_client.set('new_post', value=post_name)
    await state.set_state(DataStates.text_post)




