french_specific_words = ["de", "la", "et", "à", "des", "le", "les", "en", "que", "un", "vous", "est", "une", "dans", "par"]
english_specific_words = ["the", "of", "and", "to", "is", "that", "you", "as", "for", "are", "by"]
german_specific_words = ["Sie", "und", "ich", "zu", "das", "Ich", "dass", "nicht", "ist", "die", "wenn", "ein"]

german_special_chars = ["ä", "ö", "ü", "ß"]
french_special_chars = ["é", "è", "ê", "à", "â", "ù", "ô", "ç"]

def has_french_specific_word(text):
    french_specific_words_lower = [word.lower() for word in french_specific_words]
    french_specific_words_capitalize = [word.capitalize() for word in french_specific_words]
    french_specific_words_all = french_specific_words_lower + french_specific_words_capitalize
    
    for word in french_specific_words_all:
        if word in text.split(" "):
            return [True, "French"]
    
    return [False, "_"]

def has_english_specific_word(text):
    english_specific_words_lower = [word.lower() for word in english_specific_words]
    english_specific_words_capitalize = [word.capitalize() for word in english_specific_words]
    english_specific_words_all = english_specific_words_lower + english_specific_words_capitalize
    
    for word in english_specific_words_all:
        if word in text.split(" "):
            return [True, "English"]
    
    return [False, "_"]

def has_german_specific_word(text):
    german_specific_words_lower = [word.lower() for word in german_specific_words]
    german_specific_words_capitalize = [word.capitalize() for word in german_specific_words]
    german_specific_words_all = german_specific_words_lower + german_specific_words_capitalize
    
    for word in german_specific_words_all:
        if word in text.split(" "):
            return [True, "German"]
    
    return [False, "_"]

def has_german_special_char(text):
    for char in german_special_chars:
        if char in text:
            return [True, "German"]
    
    return [False, "_"]

def has_french_special_char(text):
    for char in french_special_chars:
        if char in text:
            return [True, "French"]
    
    return [False, "_"]

def percentage_capital_words_above_23(text):
    words = text.split(" ")
    capital_words = [word for word in words if len(word) > 0 and word[0].isupper()]
    percentage = len(capital_words) / len(words) * 100

    if percentage > 23:
        return [True, "German"]
    else:
        return [False, "Undetermined"]

def generate_attribute_array_from(text):
    """
    Returns a list of attributes from a given text

    The order of the attributes is:
    1. hasFrenchSpecificWord
    2. hasGermanSpecificWord
    3. hasEnglishSpecificWord
    4. hasGermanSpecialChar
    5. hasFrenchSpecialChar
    6. percentageCapitalWordsAbove23
    """
    return [
        has_french_specific_word(text),
        has_german_specific_word(text),
        has_english_specific_word(text),
        has_german_special_char(text),
        has_french_special_char(text),
        percentage_capital_words_above_23(text)
    ]

if __name__ == "__main__":
    print("This file is not meant to be run directly.")