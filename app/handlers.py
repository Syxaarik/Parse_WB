from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()

class Form(StatesGroup):
    url = State()
    art = State()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}'
                         f'\nДанный бот позволяет сделать общую оценку товара на WB'
                         f'\nЧто позволит сделать правильный выбор перед покупкой.')


@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer(f'Вот перечень всех команд:'
                         f'\n/get_url - вставка ссылки для получение отзыва'
                         f'\n')


@router.message(Command('get_url'))
async def get_url(message: Message, state: FSMContext):
    await state.set_state(Form.url)
    await message.answer('Введи url товара'
                         '\nИ бот выдаст отзыв о товаре.')


@router.message(Form.url)
async def set_url(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    data = await state.get_data()
    await message.answer(f'Вот твой url: {data['url']}')
    await state.clear()
