# --- ОБРАБОТЧИКИ НАЧАЛА БОТА(выбор языка, выбор локации(авто, мануал), выбор критериев) ---

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram import F

from states.setup_state import StartPool, Processing
from keyboards.inline import get_language_keyboard, get_location_keyboard
from keyboards.reply import get_auto_location_keyboard
from utils.location_parse import get_city_by_coordinates, get_city_by_address
from locales import Lexicon

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(StartPool.language)
    lang = message.from_user.language_code
    await state.update_data(lang=lang)
    await message.answer(Lexicon.get(Lexicon.START_MESSAGE, lang), reply_markup=get_language_keyboard())

@router.callback_query(StartPool.language, F.data.startswith("lang_"))
async def language_choosen(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    lang = callback_query.data.split("_")[1]
    await state.update_data(lang=lang)

    text = Lexicon.ASK_LOCATION[lang]["ask_loc"]
    await callback_query.message.edit_text(text, reply_markup=get_location_keyboard(lang))

    await state.set_state(StartPool.location)

# Ожидание местоположения в текстовом виде
@router.callback_query(StartPool.location, F.data == "manual")
async def manual_location_choosing(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    user_data = await state.get_data()
    lang = user_data.get("lang", "en")

    text = Lexicon.ASK_LOCATION[lang]["loc"]
    await callback_query.message.edit_text(text)

    await state.set_state(StartPool.manual_location)

# Местоположение передано в текстовом виде, ожидание запроса
@router.message(StartPool.manual_location)
async def manual_location_receive(message: Message, state: FSMContext):
    user_data = await state.get_data()
    lang = user_data.get("lang", "en")

    city = await get_city_by_address(message.text, lang)

    if city:
        await state.update_data(city=city)
        text = f"{Lexicon.MANUAL_LOCATION[lang]} {city}. {Lexicon.GET_CRITERIA[lang]}"
        await message.answer(text)
        await state.set_state(Processing.criteria)
    else:
        await message.answer(Lexicon.GEOPY_FAILED[lang]["manual"])
        await state.set_state(StartPool.manual_location)

# Предложение отправить свою локацию по кнопке
@router.callback_query(StartPool.location, F.data == "auto")
async def auto_location_pressing(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    user_data = await state.get_data()
    lang = user_data.get("lang", "en")
    await callback_query.message.answer(Lexicon.get(Lexicon.AUTO_LOCATION, lang), reply_markup=get_auto_location_keyboard(lang))
    await state.set_state(StartPool.auto_location)

# Получение локации по кнопке, и ожидание критериев
@router.message(StartPool.auto_location, F.location)
async def auto_location_receive(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lng = message.location.longitude

    user_data = await state.get_data()
    lang = user_data.get("lang", "en")

    city = await get_city_by_coordinates(lat, lng, lang)

    if city:
        await state.update_data(city=city)
        text = f"{Lexicon.MANUAL_LOCATION[lang]} {city}. {Lexicon.GET_CRITERIA[lang]}"
        await message.answer(text)
        await state.set_state(Processing.criteria)
    else:
        await message.answer(Lexicon.get(Lexicon.GEOPY_FAILED, lang), reply_markup=ReplyKeyboardRemove())
        await state.set_state(StartPool.manual_location)