from telegram import *
from telegram.ext import *


class department(object):

    def start_callback(update:Update,context:CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to GEC Rajkot bot!")
        context.bot.send_message(chat_id=update.effective_chat.id, text='''
        What you can get ???

    -> Study Material
    -> Previous year Questions paper 

''')
        context.bot.send_message(chat_id=update.effective_chat.id, text="For help Enter /botInfo")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /department")


        

    def greetings(update, context) -> None:
        update.message.reply_text("Good Morning!")

    def botInfo(update:Update,context:CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, 
        text='''
About College : 
    /about_college ,
    /collegeWebsite,
    /faculty

For Department: /department

For Study Materal :
    /Computer_semester ,
    /Mechanical_semester ,
    /Electrical_semester ,
    /elec_Com_semester ,
    /Civil_semester ,
    /Automobile_semester

For Info :
    /Computer_info ,
    /Mechanical_info ,
    /Electrical_semester ,
    /elec_Com_info ,
    /Civil_info ,
    /Automobile_info

For Paper :
    /Computer_paper ,
    /Mechanical_paper ,
    /Electrical_paper ,
    /elec_Com_paper ,
    /Civil_paper ,
    /Automobile_paper
''')
        
    def about_college(update:Update,context:CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='''
        WELCOME TO GEC Rajkot
GEC Rajkot was established by Government of Gujarat in the year 2004 with a vision to provide quality technical education to bring out technically competent, socially responsible, environmentally conscious and ethically sound engineers in tune with India’s vision to transform the nation into a developed country. Institute is located opposite to Kankot Village which is 15 minute drive from Rajkot City. Rajkot is central location of Saurashtra and Kutch region. This institute is approved by All India Council for Technical Education (AICTE) and affiliated to Gujarat Technological University, Ahmedabad. Institute offers programs in Electronics & Communication Engineering, Computer Engineering, Instrumentation and Control Engineering, Mechanical Engineering, Civil Engineering, Automobile Engineering and Electrical Engineering.

GEC Rajkot is putting the best efforts to create vibrant atmosphere to motivate students for learning and to make the institution a preferred destination for learners in the field of technical education. Institute has done significant progress in last decade and will continue to grow in future. GEC Rajkot has got well developed state of the art laboratories, library, language lab and computer centre under Technical Education Quality Improvement Programme (TEQIP-II. GEC Rajkot also promote innovations through Student Start-up and Innovation Policy (SSIP) initiative of State Government. GEC Rajkot has also got Centre of Excellence (CoE) in collaboration with SIEMENS to encourage research and development activities. GEC Rajkot is committed in taking constructive and purposeful actions to produce engineers who are life-long learners and contributors for the progress of Gujarat and India

VISION:
1) To bring out technically competent and socially responsible engineers.

MISSION:
1) To upgrade and enhance learning resources for delivering quality technical education.

2) To improve pedagogical skills and subject knowledge of the faculty members.

3) To fortify industry interaction for up gradation of the skills of students for meeting upcoming professional challenges.

4) To nurture innovative thinking and experimentation for addressing real life problems.

5) To practise and encourage high standards of professional ethics, transparency and accountability.

6) To take cognizance of social, ethical and environmental issues.
''')

    
    def collegeWebsite(update:Update,context:CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='''
Website Link:
    https://gecrajkot.ac.in/
    
        ''')


    def faculty(update:Update, context:CallbackContext):
        keyboard = [
                [
                    InlineKeyboardButton("Computer Engineering", callback_data='fac_1',url='https://gecrajkot.ac.in/computer-engineering/#faculties'),
                    InlineKeyboardButton("Mechenical Engineering", callback_data='fac_2',url='https://gecrajkot.ac.in/mechanical-engineering/#faculties'),
                ],
                [
                InlineKeyboardButton("Electrical Engineering", callback_data='fac_3',url='https://gecrajkot.ac.in/electrical-engineering/#faculties'),
                InlineKeyboardButton("Electronics & Communication Engineering", callback_data='fac_4',url='https://gecrajkot.ac.in/electronics-communication-engineering/#faculties')
                ],
                [
                    InlineKeyboardButton("Civil Engineering", callback_data='fac_5',url='https://gecrajkot.ac.in/civil-engineering/#faculties'),
                    InlineKeyboardButton("Automobile Engineering", callback_data='fca_6',url='https://gecrajkot.ac.in/automobile-engineering/#faculties'),
                ],
                [
                    InlineKeyboardButton("Instrumentation & Control Engineering", callback_data='fac_7',url='https://gecrajkot.ac.in/instrumentation-control/#faculties'),
                    InlineKeyboardButton("General Department", callback_data='fac_8',url='https://gecrajkot.ac.in/general/#faculties'),
                ]
            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)


    def branch(update:Update, context:CallbackContext):
        keyboard = [
                [
                    InlineKeyboardButton("Computer Engineering", callback_data='1'),
                    InlineKeyboardButton("Mechenical Engineering", callback_data='2'),
                ],
                [
                InlineKeyboardButton("Electrical Engineering", callback_data='3'),
                InlineKeyboardButton("Electronics & Communication Engineering", callback_data='4')
                ],
                [
                    InlineKeyboardButton("Civil Engineering", callback_data='5'),
                    InlineKeyboardButton("Automobile Engineering", callback_data='6'),
                ]
            ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)

    def button(update: Update, context: CallbackContext) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query
        query.answer()

        if query.data == '1':
            query.edit_message_text("Welcome to Computer Department")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Computer_info for Department Information")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Computer_semester for Study Materal")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Computer_paper for Previous Question Paper")

        if query.data == '2':
            query.edit_message_text("Welcome to Mechanical Department")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Mechanical_info for Department Information")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Mechanical_semester for Study Materal")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Mechanical_paper for Previous Question Paper")

        if query.data == '3':
            query.edit_message_text("Welcome to Electrical Department")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Electrical_info for Department Information")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Electrical_semester for Study Materal")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Electrical_paper for Previous Question Paper")

        if query.data == '4':
            query.edit_message_text("Welcome to Electronics & Communication Department")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /elec_Com_info for Department Information")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /elec_Com_semester for Study Materal")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /elec_Com_paper for Previous Question Paper")

        if query.data == '5':
            query.edit_message_text("Welcome to Civil Department")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Civil_info for Department Information")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Civil_semester for Study Materal")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Civil_paper for Previous Question Paper")

        if query.data == '6':
            query.edit_message_text("Welcome to Automobile Department")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Automobile_info for Department Information")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Automobile_semester for Study Materal")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /Automobile_paper for Previous Question Paper")