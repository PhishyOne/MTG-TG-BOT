import vertexai
import requests
import nltk
from mtgsdk import Card
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from vertexai.generative_models import GenerativeModel, ChatSession  # Import ChatSession
from nltk.corpus import brown
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Chat  # Import Chat here

project_id = "directed-will-431806-n0"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel("gemini-1.5-flash-001")

bot_token = "7354552066:AAE8IDXad2Qr7ElID5XNhOPLBnNB5N53Tb0"

# Initialize the Telegram bot
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

def process_user_message(update, context):
    message = update.message.text
    # Preprocess message (remove stop words, tokenize, etc.)
    words = [word for word in word_tokenize(message.lower()) if word not in stopwords.words('english')]

    if "card" in words:
        card_name = " ".join([word for word in words if word not in ["card", "what", "is", "im", "for", "called", "a", "looking"]])
        cards = Card.where(name=card_name).all()   
        card_list = " ".join(str(item) for item in cards)
        response = model.generate_content(
            "Here are some magic: the gatheting cards. Please list them with important information about them" + card_list
        )
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

    elif "set" in words:
        # ... handle set-related queries

    else:
        # Handle other intents or general conversation
        chat = model.start_chat()  # Create a ChatSession
        response = chat.send_message(message)  # Send the message to the chat
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

# Handle messages from users
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_user_message))

# Start the bot
updater.start_polling()
updater.idle()