from telegram.ext import CommandHandler, MessageHandler, filters, Updater, Application
from telegram import Update
from youtubesearchpython import VideosSearch

key_token = "6342755577:AAFHcgxo5UCsu7y3NPf-GWtE_VmX90Edp1E"
def start_command(update: Update, context):
    update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
def help_command(update: Update, context):
    update.message.reply_text("Kirim pesan, bot akan membalas pesan..")

def text_message(update: Update, context):
    text_received = update.message.text.lower()
    print(f"Pesan diterima: {text_received}")
    
    if 'halo' in text_received:
        update.message.reply_text("Hallo juga")
    elif 'selamat malam' in text_received:
        update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'siapa kamu ?' in text_received:
        update.message.reply_text("Saya adalah bot")
    else:
        update.message.reply_text("Saya tidak mengerti")

def photo_message(update: Update, context):
    update.message.reply_text("Gambar kamu bagus")

def error(update: Update, context):
    print(f"Error: {context.error}")

def youtube_search_command(update: Update, context):
    if context.args:
        query = ' '.join(context.args)
        num_results = 5

        try:
            if context.args[-1].isdigit():
                num_results = int(context.args[-1])
                query = ' '.join(context.args[:-1])

            video_search = VideosSearch(query, limit=num_results)
            results = video_search.result()

            if results and 'result' in results and results['result']:
                response_text = f'Here are the top {num_results} results for "{query}" on YouTube:\n'
                for video in results['result']:
                    response_text += f"{video['title']}\n{video['link']}\n\n"
                update.message.reply_text(response_text)
        except Exception as e:
            print(f"Error searching YouTube: {e}")


if __name__ == '_main_':
    print('Bot is starting...')
    app = Application.builder().token(key_token).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('youtube', youtube_search_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT))

    # Error
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)