from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from translator import tarjimon
token='6610324705:AAFrvMzMG6kf8jaUTQmmXpSSn3z-s8x5R_o'
bot=Bot(token=token)
db=Dispatcher(bot=bot)


@db.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer('Bot ishlamoqda!')


@db.message_handler(content_types='text')
async def message_send(message: types.Message):
    text=message.text
    tarjima=tarjimon(text=text)
    await message.answer(tarjima)


if __name__=='__main__':
    executor.start_polling(dispatcher=db)
