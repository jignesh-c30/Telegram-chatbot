from department import department
from telegram import *
from telegram.ext import *


class automobile(department):
    def __init__(self,automobile_semester,):
        self.automobile_semester=automobile_semester

    def automobile_info(update:Update, context:CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text=''' 
        Under Mechanical Department
The students are exposed to various relevant topics like design of automobile components (both manual and computer aided), types of fuels used in automobiles with their property analysis, different types energy losses in the vehicle. 
Latest technology and standards used in engine design and manufacturing,air conditioning in the automobiles, dynamics of motor vehicles, vibration analysis, etc, besides the standard relevant mechanical engineering subjects like strength of materials, manufacturing technology, fluid mechanics, heat transfer, industrial engineering, workshop technology.
 
It works closely with the best minds in the automotive industry along with the major automobile companies in India to establish a favorable environment for the automobile engineering students and professionals to manufacture and produce the best automobiles for the different sectors of the society.
        
        
        ''')

    def automobile_semester(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='auto_sem_1_2' ,url="https://drive.google.com/drive/folders/1C7OeEg7Ep7t5ZX93UzFgsspi0pLaqQvw?usp=sharing")
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='auto_sem_3', url="https://drive.google.com/drive/folders/1mZ0wzB2ecAQy-Rbm2Wbgc8k_rrRzdoQy?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='auto_sem_4',url="https://drive.google.com/drive/folders/1jBXNljqiyZkUdK_FMtoiuGIMQ6Ngmj4Z?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='auto_sem_5',url="https://drive.google.com/drive/folders/1TXR3TA9ygHMFRLWgxWl2E1onMUK4EbXR?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='auto_sem_6',url="https://drive.google.com/drive/folders/1SAlU2PcqTihHb6s6YmSBdsDd9MakLMnh?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='auto_sem_7',url="https://drive.google.com/drive/folders/1UL7NBunGakbNcc5wTzk874yHfDRlq1hU?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='auto_sem_8',url="https://drive.google.com/drive/folders/11f7gUlR4PT_zhb1IvYYvENbWGmBJa0Qz?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)



    def automobile_paper(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='auto_sem_1_2' ,url="https://drive.google.com/drive/folders/1C7OeEg7Ep7t5ZX93UzFgsspi0pLaqQvw?usp=sharing")
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='auto_3', url="https://drive.google.com/drive/folders/1mZ0wzB2ecAQy-Rbm2Wbgc8k_rrRzdoQy?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='auto_4',url="https://drive.google.com/drive/folders/1jBXNljqiyZkUdK_FMtoiuGIMQ6Ngmj4Z?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='auto_5',url="https://drive.google.com/drive/folders/1TXR3TA9ygHMFRLWgxWl2E1onMUK4EbXR?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='auto_6',url="https://drive.google.com/drive/folders/1SAlU2PcqTihHb6s6YmSBdsDd9MakLMnh?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='auto_7',url="https://drive.google.com/drive/folders/1UL7NBunGakbNcc5wTzk874yHfDRlq1hU?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='auto_8',url="https://drive.google.com/drive/folders/11f7gUlR4PT_zhb1IvYYvENbWGmBJa0Qz?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)



   

        