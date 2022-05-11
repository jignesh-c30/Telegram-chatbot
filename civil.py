from department import department
from telegram import *
from telegram.ext import *

class civil(department):
    def __init__(self,civil_semester,):
        self.civil_semester=civil_semester

    def civil_info(update:Update, context:CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text=''' 
        VISION:
1) To transform the students into competent infrastructure engineers with social accountability.

MISSION:
1) To develop educational resources, proficiency and knowledge of the faculty members for providing quality technical education.

2) To build up effective industrial interaction for skill improvement of students for facing professional challenges.

3)To promote innovative ideas and conduct testing for solutions to real-life problems.

4)To spread awareness of societal issues.
        ''')

    def civil_semester(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='civil_sem_1_2' ,url="https://drive.google.com/drive/folders/1JV22I5GMQLxvoWxJottjGcpHQO2EE-C_?usp=sharing")
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='civil_sem_3', url="https://drive.google.com/drive/folders/1zzsFJCVVtezneu6lhX-1v6siMxLuqvLb?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='civil_sem_4',url="https://drive.google.com/drive/folders/1WRhIk1dHO4jNOnBM3zpQnfpv6hOG53CO?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='civil_sem_5',url="https://drive.google.com/drive/folders/1jx1lg1z1amgnxE2lLeeCVgfOQFC2QWlP?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='civil_sem_6',url="https://drive.google.com/drive/folders/1SKoYcU7RAedXutaaExCClJ4ESJOXLynH?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='civil_sem_7',url="https://drive.google.com/drive/folders/12XNy72k3L8CIY5FNlaxnZtBcLgujtghx?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='civil_sem_8',url="https://drive.google.com/drive/folders/1EIwUn76YDDMQsP7p-9uTDOY0GgEmBeg8?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def civil_paper(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='civil_sem_1_2' ,url="https://drive.google.com/drive/folders/1JV22I5GMQLxvoWxJottjGcpHQO2EE-C_?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='civil_3', url="https://drive.google.com/drive/folders/1zzsFJCVVtezneu6lhX-1v6siMxLuqvLb?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='civil_4',url="https://drive.google.com/drive/folders/1WRhIk1dHO4jNOnBM3zpQnfpv6hOG53CO?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='civil_5',url="https://drive.google.com/drive/folders/1jx1lg1z1amgnxE2lLeeCVgfOQFC2QWlP?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='civil_6',url="https://drive.google.com/drive/folders/1SKoYcU7RAedXutaaExCClJ4ESJOXLynH?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='civil_7',url="https://drive.google.com/drive/folders/12XNy72k3L8CIY5FNlaxnZtBcLgujtghx?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='civil_8',url="https://drive.google.com/drive/folders/1EIwUn76YDDMQsP7p-9uTDOY0GgEmBeg8?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)



   

        