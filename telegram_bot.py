import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

TOKEN = "8984452007:AAGrtN9lbu95fryh8pmwcKkEnXcelOucWss" # прием токена
bot = Bot(
	token=TOKEN,
	default=DefaultBotProperties(),
	session=None
) 
dp = Dispatcher() # включение "диспетчера"

@dp.message(CommandStart()) # "говорит диспетчеру" - следи за сообщением, если функцию включили - высылай то, что ниже 
async def command_start_handler(message: types.Message): # создание асинхронной функции, позволяет функции выполняться, не блокируя остальной код
	welcome_text = (
		f"Здравствуй, {message.from_user.full_name}!\n\n"
		"Я бот-портфолио. Здесь ты можешь узнать о моих навыках, обо мне и использовать различные команды"
	)
	await message.answer(welcome_text) # команда отправить текст обратно пользователю

async def main(): # проверка серверов
	print("Бот успешно запущен и готов к работе") 
	await dp.start_polling(bot) # спрашивает сервера, написали ли боту кто-то
if __name__ == "__main__": # проверка, запустили напрямую, а не импортировали в библиотеку как другой код, то выполняет то, что ниже
	asyncio.run(main()) #запускает маин, а она проверяет сервера