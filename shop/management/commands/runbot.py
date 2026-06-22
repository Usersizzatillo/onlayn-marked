import asyncio
from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command as AiogramCommand
from asgiref.sync import sync_to_async  
from shop.models import Product

API_TOKEN = '8928901916:AAEoNVd4lj4dUJ5QPy8A6mcr_GsHgogsNew'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Bazadan ma'lumot olishni sinxron qilib, uni async'ga o'giramiz
@sync_to_async
def get_products():
    return list(Product.objects.all())

@dp.message(AiogramCommand("start"))
async def start(message: types.Message):
    await message.answer("FoodMart botiga xush kelibsiz! \n/products buyrug'i orqali mahsulotlarni ko'ring.")

@dp.message(AiogramCommand("products"))
async def list_products(message: types.Message):
    products = await get_products()  # Endi await bilan chaqiramiz
    if not products:
        await message.answer("Hozircha mahsulotlar bazada yo'q.")
        return
    
    text = "📦 Bizdagi mahsulotlar:\n"
    for p in products:
        text += f"• {p.name} - {p.price} so'm\n"
    
    await message.answer(text)

class Command(BaseCommand):
    def handle(self, *args, **options):
        asyncio.run(dp.start_polling(bot))