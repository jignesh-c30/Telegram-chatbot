from department import department
from telegram import *
from telegram.ext import *


class computer(department):
    def __init__(self,Computer_semester,):
        self.Computer_semester=Computer_semester

    def Computer_info(update:Update, context:CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text='''
            VISION:
1) To provide value-based technology education in Computer Engineering.

MISSION
1) To bring out graduates who can solve challenges of industry and society by applying computing techniques.

2) To develop partnership with industries, government agencies and Research and Development organizations for knowledge and resource sharing.

3) To encourage faculties and students to participate in reputed conferences, workshops, seminars and other such technical activities.

4) To motivate students/graduates to be entrepreneurs.

5) To impart human and ethical values among students in the service of society.
            ''')


    def Computer_semester(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='comp_sem_1_2' ,url="https://drive.google.com/drive/folders/1wWC1XcTjg7-37TebQC_oclo_nZ4JVx58?usp=sharing")   
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='comp_3', url="https://drive.google.com/drive/folders/1FP-PV4JyQMthLbQ_rF_XTu7cG9wnosDB?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='comp_4',url="https://drive.google.com/drive/folders/1DRcnDXrDcnC19Cl0IkP2gqZ4ebUmbGDN?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='comp_5',url="https://drive.google.com/drive/folders/1DRcnDXrDcnC19Cl0IkP2gqZ4ebUmbGDN?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='comp_6',url="https://drive.google.com/drive/folders/1FM5bJzcOTRZeY9zhhXqWOUlsCt6mBklJ?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='comp_7',url="https://drive.google.com/drive/folders/1HJObkuFpUjnU5DlMu_g9ZM5-Oz3jUMcX?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='comp_8',url="https://drive.google.com/drive/folders/1TDeAKBgqNN9IWFpGh9hmzDgbzxp1oyRy?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def Computer_paper(update:Update, context:CallbackContext):
        keyboard =[
                [
                    InlineKeyboardButton("Sem 1, 2", callback_data='comp_sem_1_2' ,url="https://drive.google.com/drive/folders/1BorfR9XVK68Ew4o0vFzBrYCjQowQ2SAL?usp=sharing")
                ],
                [
                    InlineKeyboardButton("Sem 3", callback_data='comp_3', url="https://drive.google.com/drive/folders/1Vl2u9IJaEITVD1yMX7-4iGSKZcE9BNE2?usp=sharing"),
                    InlineKeyboardButton("Sem 4", callback_data='comp_4',url="https://drive.google.com/drive/folders/1K9eklVQfxM_jQ_gP03a3hP9gVVj0BoPx?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 5", callback_data='comp_5',url="https://drive.google.com/drive/folders/1fQw9dPfob8YaGNp_N2qh6_Ez7vdelToD?usp=sharing"),
                    InlineKeyboardButton("Sem 6", callback_data='comp_6',url="https://drive.google.com/drive/folders/1tJYzUw4PVVawWf1KQl_pdmdh9c35wSHK?usp=sharing"),
                ],
                [
                    InlineKeyboardButton("Sem 7", callback_data='comp_7',url="https://drive.google.com/drive/folders/1ub6OUg6CXTzzUhKqb7DvhF3Fi1gZVgDJ?usp=sharing"),
                    InlineKeyboardButton("Sem 8", callback_data='comp_8',url="https://drive.google.com/drive/folders/1xBiDSsG8vc217Jkl21HdaS9dhReJWMT4?usp=sharing"),
                ]

            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)
