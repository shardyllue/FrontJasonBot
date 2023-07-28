from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

text = """  
JasonBot будет лучшим помощником для администрирования Телеграм-канала, он поможет автоматизировать рутину сразу в трех направлениях:

<b> — Постинг</b> для ведения каналов и чатов

<b>1.</b>  <i>Hасписание постов</i>
<b>2.</b>  <i>Отложенные публикации</i>
<b>3.</b>  <i>Все виды кнопок</i>
<b>4.</b>  <i>Реакции</i>
<b>5.</b>  <i>Возможность редактирования постов</i>

<b> — Закупы</b> 

<b>1.</b>  <i>создавайте креативы с автоматически
сгенерированной ссылкой, отправляйте админу канала для размещения и
отслеживайте статистику размещения</i>
<b>2.</b>  <i>бот автоматически рассчитает стоимость размещения по CPM, количество и цену подписчика и внесет данные в гугл-таблицу</i>

<b>Мы рядом, если нужна помощь @supportbot</b> 
"""

create = KeyboardButton(text="Создать")
channels = KeyboardButton(text="Мои каналы")

price = KeyboardButton(text="Цены")


kb_start = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [create],
        [price]
    ]
)


kb_main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [channels],
        [price]
    ]
)

