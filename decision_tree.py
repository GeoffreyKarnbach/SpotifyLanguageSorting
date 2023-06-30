from attribute_extractor import *
import langdetect

def evaluate_language_for_text_own(text):
    attributes = generate_attribute_array_from(text)

    for attr in attributes:
        if attr[0]:
            return attr[1]
    
    return "undefined"

def evaluate_language_for_text_module(text):
    return langdetect.detect(text)

if __name__ == "__main__":
    evaluate_language_for_text_own(input("Enter a text: "))