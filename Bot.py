import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_KEY = "6489617065:AAHMMMQlfe5xfZ25-qKlyRiOBQsAvRknmO0"

bot = Bot(token=BOT_KEY)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}!")

@dp.message()
async def echo_message(message: types.Message):



    # await message.reply(
    #     text="Aдольф гитлер прав"
    # )
    if message.text == "Aдольф гитлер не прав":
        await bot.send_message(
            chat_id=message.chat.id,
            text="Ты не прав, адольф гитлер был прав",
            reply_to_message_id=message.message_id,
        )
    elif message.text:
        # await message.reply(text=message.text)
        await bot.send_message(
            chat_id=message.chat.id,
            text="Хули ты сюда пишешь?",
            reply_to_message_id=message.message_id,
        )
    elif message.animation:
        await message.reply("Некаких гив")
    elif message.sticker:
        await message.reply("Не шли сука стикеры")
    else:
        await message.reply(text="Пиши блять текст")
    await bot.send_message(
        chat_id=message.chat.id,
        text="Иди нахуй",
        reply_to_message_id=message.message_id
    )


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

