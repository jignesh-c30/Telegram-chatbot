from department import department
from telegram import *
from telegram.ext import *


class mechanical(department):
    def __init__(self,Mechanical_semester,):
        self.Mechanical_semester=Mechanical_semester


    def mechanical_info(update:Update, context:CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text=''' 
        VISION:
1) Attain national recognition by providing quality education to the emerging generation of mechanical engineers to meet the current social and industrial needs.

MISSION:
1) Impart the fundamental theoretical and practical knowledge of the field.

2) Prepare technically competent and socially responsible engineers by engaging them in academic, co-curricular and extra-curricular activities.

3) Encourage the students for the progress of the nation by cultivating sustainable and innovative cutting edge technologies.
        ''')

    def Mechanical_semester(update:Update, context:CallbackContext):
        keyboard = [
            [
                InlineKeyboardButton("Sem 1, 2", callback_data='mech_sem_1' ,url="https://drive.google.com/drive/folders/1-QCAltGb_u_LPk4pFv4XpGYFjVMl3fGM?usp=sharing")
            ],
            [
                InlineKeyboardButton("Sem 3", callback_data='mech_sem_3',url="https://drive.google.com/drive/folders/1prJPUFWCxrIL0JoeYpR6I5eqBl5QUzpS?usp=sharing"),
                InlineKeyboardButton("Sem 4", callback_data='mech_sem_4',url="https://drive.google.com/drive/folders/1ZL3CZqMd1pPC2zLfBjhgYu7fF5xmqyDV?usp=sharing")
            ],
            [
                InlineKeyboardButton("Sem 5", callback_data='mech_sem_5',url="https://drive.google.com/drive/folders/1IvEUPh1M9RpNZbPSmzYRqOXezL0-6xJk?usp=sharing"),
                InlineKeyboardButton("Sem 6", callback_data='mech_sem_6',url="https://drive.google.com/drive/folders/1Xq8a_i_zsWaIlo2OH4obvPy3alv0WPUk?usp=sharing"),
            ],
            [
                InlineKeyboardButton("Sem 7", callback_data='mech_sem_7',url="https://drive.google.com/drive/folders/18kz84dkDWjFZ0VoCZP4ShpDh3n31pvyV?usp=sharing"),
                InlineKeyboardButton("Sem 8", callback_data='mech_sem_8',url="https://drive.google.com/drive/folders/1VYyi9DQjNq4nw491wZj7IdeZxbjwXQBB?usp=sharing"),
            ]

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def Mechanical_paper(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='mech_sem_1_2' ,url="https://drive.google.com/drive/folders/1-QCAltGb_u_LPk4pFv4XpGYFjVMl3fGM?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='mech_3', url="https://drive.google.com/drive/folders/1prJPUFWCxrIL0JoeYpR6I5eqBl5QUzpS?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='mech_4',url="https://drive.google.com/drive/folders/1ZL3CZqMd1pPC2zLfBjhgYu7fF5xmqyDV?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='mech_5',url="https://drive.google.com/drive/folders/1IvEUPh1M9RpNZbPSmzYRqOXezL0-6xJk?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='mech_6',url="https://drive.google.com/drive/folders/1Xq8a_i_zsWaIlo2OH4obvPy3alv0WPUk?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='mech_7',url="https://drive.google.com/drive/folders/18kz84dkDWjFZ0VoCZP4ShpDh3n31pvyV?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='mech_8',url="https://drive.google.com/drive/folders/1VYyi9DQjNq4nw491wZj7IdeZxbjwXQBB?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)

        
