from aiogram  import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import keyboardQuestions, keyboardGame

router = Router()

@router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboardQuestions)

@router.message(Command('help'))
async def process_help_command(message:Message):
    await message.answer(text=LEXICON_RU['/help'])