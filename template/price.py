from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.types.web_app_info import WebAppInfo

text = """
30 дней вы можете использовать бота абсолютно бесплатно, после - потребуется приобрести подписку.

Стоимость подписки (за 1 подключенный канал): 

1 месяц - 250 руб 
3 месяца - 690 руб (230 руб / мес)
6 мес - 1290 руб (215 руб / мес)
12 месяцев - 2400 руб (200 руб / мес)
"""

more = InlineKeyboardButton(
    text="Подробно",
    web_app=WebAppInfo(
        url="https://tgtesterbot.ru/price"
    )
)


kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [more]
    ]
)