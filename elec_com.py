from department import department
from telegram import *
from telegram.ext import *


class elec_com(department):
    def __init__(self,elec_com_semester,):
        self.elec_com_semester=elec_com_semester

    def elec_com_info(update:Update, context:CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text='''
        VISION
1) To bring out technically competent, responsible, ethical and environment friendly electronics and communication engineer for the society and industries. 

MISSION:
1) Developing technical competency in the students of electronics and communication engineering through hands on practice.

2) Imparting quality technical education to the students through advanced teaching learning process.

3) Creating vibrant atmosphere in the department to imbibe discipline, ethics and social responsibilities in students.

4) Facilitating students to work on innovative projects related to electronics and communication engineering.
        ''')

    def elec_Com_semester(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='elec_sem_1_2' ,url="https://drive.google.com/drive/folders/1dPkTIZ2I2HxS6Q53aToplyzJ-_isSewZ?usp=sharing")
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='elec_sem_3', url="https://drive.google.com/drive/folders/1P2tj-oagkVybzPjPUepCZmtpAfe6hFv5?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='elec_sem_4',url="https://drive.google.com/drive/folders/1N4ymNbYdjNEppdZWXo_g2yLRdvfuWPLn?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='elec_sem_5',url="https://drive.google.com/drive/folders/19IlHooCZkuQTtxyFj_cv3VWH4CkHhsYV?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='elec_sem_6',url="https://drive.google.com/drive/folders/1yHcg6NuKu5F6psBZ-NeAipkVniKrEmaJ?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='elec_sem_7',url="https://drive.google.com/drive/folders/1ozFuMmJcTpn7Emnmq4KMoLAS5fyIkKLQ?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='elec_sem_8',url="https://drive.google.com/drive/folders/1U8qHgnVE1ab_TsZ8Oy1fuxYFUGhRphE4?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def elec_Com_paper(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='elec_com_sem_1_2' ,url="https://drive.google.com/drive/folders/1dPkTIZ2I2HxS6Q53aToplyzJ-_isSewZ?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='elec_com_sem_3', url="https://drive.google.com/drive/folders/1P2tj-oagkVybzPjPUepCZmtpAfe6hFv5?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='elec_com_sem_4',url="https://drive.google.com/drive/folders/1N4ymNbYdjNEppdZWXo_g2yLRdvfuWPLn?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='elec_com_sem_5',url="https://drive.google.com/drive/folders/19IlHooCZkuQTtxyFj_cv3VWH4CkHhsYV?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='elec_com_sem_6',url="https://drive.google.com/drive/folders/1yHcg6NuKu5F6psBZ-NeAipkVniKrEmaJ?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='elec_com_sem_7',url="https://drive.google.com/drive/folders/1ozFuMmJcTpn7Emnmq4KMoLAS5fyIkKLQ?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='elec_com_sem_8',url="https://drive.google.com/drive/folders/1U8qHgnVE1ab_TsZ8Oy1fuxYFUGhRphE4?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)



   

        