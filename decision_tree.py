from attribute_extractor import *

def evaluate_language_for_text(text):
    attributes = generate_attribute_array_from(text)
    print(attributes)

if __name__ == "__main__":
    evaluate_language_for_text(input("Enter a text: "))