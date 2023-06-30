from attribute_extractor import *

def evaluate_language_for_text(text):
    attributes = generate_attribute_array_from(text)
    print(attributes)

evaluate_language_for_text("Bonjour, je m'appelle Jean-Luc Picard. Je suis capitaine de l'Enterprise.")