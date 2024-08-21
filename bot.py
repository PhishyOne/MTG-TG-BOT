import vertexai
import requests
import nltk
from mtgsdk import Card
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from vertexai.generative_models import GenerativeModel

# Import necessary classes from telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, TGChat

project_id = "directed-will-431806-n0"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel("gemini-1.5-flash-001")

bot_token = "7354552066:AAE8IDXad2Qr7ElID5XNhOPLBnNB5N53Tb0"

# Create a single ChatSession object
chat = model.start_chat()

def process_user_message(update, context):
    user_message = update.message.text.lower()
    words = [word for word in word_tokenize(user_message) if word not in stopwords.words('english')]

    if "card" in words:
        # Extract card name
        card_name = " ".join([word for word in words if word not in ["card", "what", "is", "im", "for", "called", "a", "looking"]])
        cards = Card.where(name=card_name).all()
        card_list = " ".join(str(item) for item in cards)
        response = model.generate_content(
            "Here are some Magic: the Gathering cards. Please list them with important information about them: " + card_list
        )
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

    #elif "set" in words:
        # ... handle set-related queries

    #else:
        # Use the existing ChatSession object
        response = chat.send_message(user_message)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

# Handle messages from users
dispatcher = Updater(bot_token, use_context=True).dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_user_message))

# Start the bot
updater.start_polling()
updater.idle()