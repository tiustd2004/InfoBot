from aiogram import Bot, Dispatcher,types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import URLInputFile

import asyncio

from aiogram.filters import Text, Command

from config import TOKEN_API

from aiogram.types import Message

from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(TOKEN_API)

dp = Dispatcher()

kb_0 = [
    [types.KeyboardButton(text ="💼Услуги")],
    [types.KeyboardButton(text = "📱Поддержка😄")],
    [types.KeyboardButton(text = "👟Топ кроссовок за сезон")] #Updates season
]



kb_2 = [
    [types.KeyboardButton(text ="🔨Ремонт🔨")],
    [types.KeyboardButton(text = "🧹Клининг🧹")],
    [types.KeyboardButton(text = "🦠Купить очищающие средства для обуви🦠")]
]

kb_3 = [
    [types.KeyboardButton(text ="+7-xxx-xxx-xx-xx")],
    [types.KeyboardButton(text = "Вебсайт🖥️")],
    [types.KeyboardButton(text = "VK💎")]
]


@dp.message(Command('start'))
async def cmd_start(message:types.Message):
    await message.answer('Привет😺! Я информационный бот🤖, который поможет тебе ознакомиться с вайбом нашей компании🌟' + '\n' + 'Нажми на эту надпись👉 /menu')
    await message.delete()
@dp.message(Command('menu'))
async def cmd_menu(message:types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_0)
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_0,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )

    await message.answer("⚡Твоё меню⚡", reply_markup=keyboard)
    await message.delete()

@dp.message(Text('💼Услуги'))
async def cmd_services(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_2)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_2,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )
    
    
    await message.answer("...", reply_markup=keyboard)
    await message.delete()

@dp.message(Text('📱Поддержка😄'))
async def cmd_support(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_3)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_3,
        resize_keyboard=True,
        input_field_placeholder="Выбери пункт меню"
    )
    await message.answer("...", reply_markup=keyboard)
    await message.delete()

@dp.message(Text('Вебсайт🖥️'))
async def cmd_support_1(message:types.Message, bot: Bot):
    markup_0 = InlineKeyboardBuilder()
    markup_0.row(types.InlineKeyboardButton(
        text="Сайт", url="https://project8107832.tilda.ws/")
    )
    await message.answer(
        'Вебсайт🖥️',
        reply_markup=markup_0.as_markup(),
    )
    await message.delete()

@dp.message(Text('VK💎'))
async def cmd_support_2(message:types.Message):
    markup_1 = InlineKeyboardBuilder()
    markup_1.row(types.InlineKeyboardButton(
        text="Паблик", url="https://vk.com/club222930100")
    )
    await message.answer(
        'VK💎',
        reply_markup=markup_1.as_markup(),
    )
    await message.delete()

@dp.message(Text('👟Топ кроссовок за сезон'))
async def cmd_support_3(message:types.Message):
    markup_2 = InlineKeyboardBuilder()
    markup_2.row(types.InlineKeyboardButton(
        text="Топ4ик", url="https://sneakerfreak.ru/muzhskie-letnie-krossovki-2023/")
    )
    await message.answer(
        '💎💎💎',
        reply_markup=markup_2.as_markup(),
    )
    await message.delete()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())