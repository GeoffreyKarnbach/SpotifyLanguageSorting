from decision_tree import evaluate_language_for_text_own, evaluate_language_for_text_module

target_languages = ["English", "French", "German"]
lang_match = {"en": "English", "de": "German", "fr": "French"}

# Fetch test data from CSV file (creatable with the Jupyter Notebook)
with open("Data/minimal_languages.csv","r") as file:
    data = file.read()

items = data.split("\n")

test_data = []
for item in items:
    lang = item.split(",")[-1]

    if lang in target_languages:
        test_data.append([item.split(",")[:-1], item.split(",")[-1]])

entry_count = len(test_data)

custom_lang_detection_success_count = 0
module_lang_detection_success_count = 0

failure_rate_custom = 0
failure_rate_module = 0

# Go through every entry from the test data set and run both custom and language detection from module "langdetect"
for entry in test_data:
    entry_text = " ".join(entry[0])
    entry_label = entry[1]

    try:
        if evaluate_language_for_text_own(entry_text) == entry_label:
            custom_lang_detection_success_count += 1

    except Exception as e:
        failure_rate_custom += 1
    
    try:
        response = evaluate_language_for_text_module(entry_text)
        result = lang_match[response] if response in lang_match else response

        if result == entry_label:
            module_lang_detection_success_count += 1

    except Exception as e:
        failure_rate_module += 1

# Compute and print results

succes_rate_custom = custom_lang_detection_success_count / (entry_count - failure_rate_custom)
succes_rate_module = module_lang_detection_success_count / (entry_count - failure_rate_module)

print(f"Found a total of {entry_count} to test language recognition on:")

print(f"Success rate with custom decision tree: {round(succes_rate_custom*100, 2)} %")
print(f"Success rate with langdetect module: {round(succes_rate_module*100, 2)} %")