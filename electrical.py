from department import department
from telegram import *
from telegram.ext import *


class electrical(department):
    def __init__(self,Electrical_semester,):
        self.Electrical_semester=Electrical_semester

    def electrical_info(update:Update, context:CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text='''
        VISION:
1) To help build a knowledge-driven community built on intellectual competitiveness for global sovereignty. 

MISSION:
1) To become the first choice academic institution having highly meritorious students, a self-motivated faculty, sensitive management, operational within an atmosphere of state-of-the-art research, underlining academic collaboration, and worldwide association.

2) To cultivate graduates to be civically engaged entities who distinguish their accountability and role in their societies and the world.
        ''')

    def Electrical_semester(update:Update, context:CallbackContext):
        keyboard = [
            [
                InlineKeyboardButton("Sem 1, 2", callback_data='ele_sem_1_2',url="https://drive.google.com/drive/folders/1fvUjK-zULSzd2QzKu2OvC1ZQYJvUY99F?usp=sharing"),
            ],
            [
                InlineKeyboardButton("Sem 3", callback_data='ele_sem_3',url="https://drive.google.com/drive/folders/1IkRmIV6KfJ9tQF-9EGJiJbDQE8uJ1fNB?usp=sharing"),
                InlineKeyboardButton("Sem 4", callback_data='ele_sem_4',url="https://drive.google.com/drive/folders/1Pja40L9kYqWXRytw2Bi47E877hFs59Ms?usp=sharing")
            ],
            [
                InlineKeyboardButton("Sem 5", callback_data='ele_sem_5',url="https://drive.google.com/drive/folders/1wLv6Ln6vBroEQzJHXg7K25vkvEZ1jFzl?usp=sharing"),
                InlineKeyboardButton("Sem 6", callback_data='ele_sem_6',url="https://drive.google.com/drive/folders/1PcpgjCikKXgGorcGl0P7oWNmN2TSuGmQ?usp=sharing"),
            ],
            [
                InlineKeyboardButton("Sem 7", callback_data='ele_sem_7',url="https://drive.google.com/drive/folders/1F-lpcA27nQQHXQUH_vss_eFankmqCp0L?usp=sharing"),
                InlineKeyboardButton("Sem 8", callback_data='ele_sem_8',url="https://drive.google.com/drive/folders/1bS7pso328f6o2PAbZFTZ4HXpbFg5VsXw?usp=sharing"),
            ]

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def Electrical_paper(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='ele_sem_1_2' ,url="https://drive.google.com/drive/folders/1fvUjK-zULSzd2QzKu2OvC1ZQYJvUY99F?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='ele_3', url="https://drive.google.com/drive/folders/1IkRmIV6KfJ9tQF-9EGJiJbDQE8uJ1fNB?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='ele_4',url="https://drive.google.com/drive/folders/1Pja40L9kYqWXRytw2Bi47E877hFs59Ms?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='ele_5',url="https://drive.google.com/drive/folders/1wLv6Ln6vBroEQzJHXg7K25vkvEZ1jFzl?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='ele_6',url="https://drive.google.com/drive/folders/1PcpgjCikKXgGorcGl0P7oWNmN2TSuGmQ?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='ele_7',url="https://drive.google.com/drive/folders/1F-lpcA27nQQHXQUH_vss_eFankmqCp0L?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='ele_8',url="https://drive.google.com/drive/folders/1bS7pso328f6o2PAbZFTZ4HXpbFg5VsXw?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)
        
