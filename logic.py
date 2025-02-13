import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Question:

    def __init__(self, text, answer_id, image_question, *options):
        self.text = text
        self.__answer_id = answer_id
        self.image_question = image_question
        self.options = options

    @property
    def get_real_name(self):
        return self.__real_name
    
    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)

        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
        return markup

# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "cat1.jpg", "Спят", "Пишут мемы"),
    Question("Почему котики мяукают?", 1, "cat4.jpg", "Вы им надоели", "Хотят играться"),
    Question("Как котики выражают свою любовь?", 0, "cat2.jpg", "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "cat3.jpg", "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]
