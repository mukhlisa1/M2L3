
import telebot
from config import token
from collections import defaultdict
from logic import quiz_questions

user_responses = {} 
points = defaultdict(int)

bot = telebot.TeleBot(token)

def send_question(chat_id):
    question = quiz_questions[user_responses[chat_id]]
    
    with open(question.image_question, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=question.text, reply_markup=question.gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        points[call.message.chat.id] += 1
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=None)
    
    user_responses[call.message.chat.id]+=1

    if user_responses[call.message.chat.id]>=len(quiz_questions):
        bot.send_message(call.message.chat.id,  f"The end, your points: {points[call.message.chat.id]}")
    else:
        send_question(call.message.chat.id)


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)


bot.infinity_polling()
