from aiogram import Router
from aiogram.filters import Text 

from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import keyboardGame, keyboardQuestions
import random

router: Router = Router()

@router.message(Text(text='Давай'))
async def go(message: Message):
    await message.answer(text=LEXICON_RU['Давай'], reply_markup=keyboardGame)

@router.message(Text(text='Не хочу'))
async def stop(message: Message):
    await message.answer(text=LEXICON_RU['Не хочу'])

@router.message(lambda message: message.text in LEXICON_RU['choice'])
async def choice(message: Message):
    choiced = random.choice(LEXICON_RU['choice'])
    await message.answer(choiced)
    if (LEXICON_RU['winning_map'][message.text] == choiced):
        await message.answer(text='Ты победил', reply_markup=keyboardQuestions)
    elif (message.text == choiced): 
        await message.answer(text='Ничья', reply_markup=keyboardQuestions)
    else:
        await message.answer(text='Ты проебал, дебил', reply_markup=keyboardQuestions)
