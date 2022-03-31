'''Translator'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """The function that translates from English to French"""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result().get("translations")[0].get("translation")

    return french_text


def french_to_english(french_text):
    """The function that translates from French to English"""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result().get("translations")[0].get("translation")

    return english_text
#MESSAGE = "Good morning, Carol. How are you? Would you like to take a walk?"
#print("\n" + MESSAGE + " ----------> " + str(english_to_french(MESSAGE)))
#print("\n" + MESSAGE + " ----------> " + str(french_to_english(MESSAGE)))
