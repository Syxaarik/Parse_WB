from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}'
                         f'\nДанный бот позволяет сделать общую оценку товара на WB'
                         f'\nЧто позволит сделать правильный выбор перед покупкой.')