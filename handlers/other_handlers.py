from aiogram import Router
from aiogram.types import Message 

router = Router()


@router.message()
async def unknow_answer(message: Message):
    await message.answer('Я не знаю такой команыд.\n'
                         'Если вам что-то непонятно воспользуйтесь командой /help')