from aiogram.types import (
    KeyboardButton, Message, 
    ReplyKeyboardMarkup, ReplyKeyboardRemove
    )

from aiogram.utils.keyboard import ReplyKeyboardBuilder

kbBuilderGame: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kbBuilderQuestion: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

optionsGame: list = ['Камень', 'Ножницы', 'Бумага']
optionsQuestion: list = ['Давай', 'Не хочу']

buttonsGame: list[KeyboardButton] = [KeyboardButton(text=option) for option in optionsGame]
buttonsQuestion: list[KeyboardButton] = [KeyboardButton(text=option) for option in optionsQuestion]

keyboardGame: ReplyKeyboardMarkup = kbBuilderGame.row(*buttonsGame, width=1).as_markup(resize_keyboard=True)
keyboardQuestions: ReplyKeyboardMarkup = kbBuilderQuestion.row(*buttonsQuestion, width=1).as_markup(resize_keyboard=True)

