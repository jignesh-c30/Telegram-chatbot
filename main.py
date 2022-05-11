from telegram import *
from telegram.ext import *
from telegram.update import Update
import logging
import os

from computer import computer
from mechanical import mechanical
from department import department
from electrical import electrical
from civil import civil
from elec_com import elec_com
from automobile import automobile
from mechanical import mechanical

logging.basicConfig(level=logging.DEBUG,filename="std.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# PORT = int(os.environ.get('PORT', 5000))

def greet(user_input):
    answer = user_input.capitalize()
    return answer

def reply(update, context):
    user_input = update.message.text
    input_array=['hello','hi','Hello','Hi']
    if user_input in input_array:
        update.message.reply_text(greet(user_input))

def main() -> None:
    updater = Updater(token='1942062362:AAF7jYQMpFil9ULVfVmFsLinl6PgELDBGO0')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", department.start_callback))
    dispatcher.add_handler(CommandHandler("greetings", department.greetings))
    dispatcher.add_handler(CommandHandler("department",department.branch))
    dispatcher.add_handler(CommandHandler("Computer_info",computer.Computer_info))
    dispatcher.add_handler(CommandHandler("Computer_semester",computer.Computer_semester))
    dispatcher.add_handler(CommandHandler("Computer_paper",computer.Computer_paper))
    dispatcher.add_handler(CommandHandler("mechanical_info",mechanical.mechanical_info))
    dispatcher.add_handler(CommandHandler("Mechanical_semester",mechanical.Mechanical_semester))
    dispatcher.add_handler(CommandHandler("Mechanical_paper",mechanical.Mechanical_paper))
    dispatcher.add_handler(CommandHandler("electrical_info",electrical.electrical_info))
    dispatcher.add_handler(CommandHandler("Electrical_semester",electrical.Electrical_semester))
    dispatcher.add_handler(CommandHandler("Electrical_paper",electrical.Electrical_paper))
    dispatcher.add_handler(CommandHandler("automobile_info",automobile.automobile_info))
    dispatcher.add_handler(CommandHandler("automobile_semester",automobile.automobile_semester))
    dispatcher.add_handler(CommandHandler("automobile_paper",automobile.automobile_paper))
    dispatcher.add_handler(CommandHandler("civil_info",civil.civil_info))
    dispatcher.add_handler(CommandHandler("civil_semester",civil.civil_semester))
    dispatcher.add_handler(CommandHandler("civil_paper",civil.civil_paper))
    dispatcher.add_handler(CommandHandler("elec_com_info",elec_com.elec_com_info))
    dispatcher.add_handler(CommandHandler("elec_Com_semester",elec_com.elec_Com_semester))
    dispatcher.add_handler(CommandHandler("elec_Com_paper",elec_com.elec_Com_paper))
    dispatcher.add_handler(CallbackQueryHandler(department.button))
    dispatcher.add_handler(CommandHandler("botInfo",department.botInfo))
    dispatcher.add_handler(CommandHandler("about_college",department.about_college))
    dispatcher.add_handler(CommandHandler("collegeWebsite",department.collegeWebsite))
    dispatcher.add_handler(CommandHandler("faculty",department.faculty))
    dispatcher.add_handler(MessageHandler(Filters.text, reply))

    updater.start_polling()
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path='1758805627:AAHWjp0lHW5yYvEbhy19f3DBwPB9mS2Z1f0')

    # updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + '1758805627:AAHWjp0lHW5yYvEbhy19f3DBwPB9mS2Z1f0')
    updater.idle()

if __name__ == '__main__':
    main()