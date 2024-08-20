import vertexai
import requests
import nltk
from mtgsdk import Card
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from vertexai.generative_models import GenerativeModel
from nltk.corpus import brown

# TODO(developer): Update and un-comment below line
project_id = "directed-will-431806-n0"
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel("gemini-1.5-flash-001")

def process_user_message(message):
    # Preprocess message (remove stop words, tokenize, etc.)
    words = [word for word in word_tokenize(message.lower()) if word not in stopwords.words('english')]

            # Check for keywords or intents
    if "card" in words:
                        # Extract card name
        card_name = " ".join([word for word in words if word not in ["card", "what", "is", "im", "for", "called", "a", "looking"]])
        cards = Card.where(name=card_name).all()   
        card_list = " ".join(str(item) for item in cards)
        response = model.generate_content(
	    "Here are some magic: the gatheting cards. Please list them with important information about them" + card_list
        )
        print(response.text)

    elif "set" in words:
        set_name = " ".join([word for word in words if word not in ["set", "what", "is", "I/'m", "for", "called", "a", "looking"]])

user_message = "Im looking for a card called Krenko"
process_user_message(user_message)                              # ... other intents                                                      # ... other intents                                                                 # Example usag