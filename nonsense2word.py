# Mapping of Persian characters to English keyboard characters based on QWERTY layout (or vice-versa)
persian_to_english_map = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p', 'ج': '[', 'چ': ']',
    'گ': "'", 'ک': ';', 'م': 'l', 'ن': 'k', 'ت': 'j', 'ا': 'h', 'ل': 'g', 'ب': 'f', 'ی': 'd', 'س': 's', 'ش': 'a', 'ظ': 'z', 
    'ط': 'x', 'ز': 'c', 'ر': 'v', 'ذ': 'b', 'د': 'n', 'پ': 'm', 'و': ',', '.': '.',
    'ْْ': 'Q', 'ٌ': 'W', 'ٍ': 'E', 'ً': 'R', 'ُ': 'T', 'ِ': 'Y', 'َ': 'U', 'ّ': 'I', ']': 'O', '[': 'P', '}': '{', '{': '}',
    '؛': "'", ':': ':', '«': 'L', '»': 'K', 'ة': 'J', 'آ': 'H', 'أ': 'G', 'إ': 'F', 'ي': 'D', 'ئ': 'S', 'ؤ': 'A', 'ك': 'Z', 
    'ط': 'X', 'ژ': 'C', 'ٰ': 'V', '‌': 'B', 'ٔ': 'N', 'ء': 'M', '>': '<', '<': '>', '؟': '?'
}

english_to_persian_map = {v: k for k, v in persian_to_english_map.items()}

def translate_persian_to_english(persian_text):
    translated_text = ''
    for char in persian_text:
        translated_text += persian_to_english_map.get(char, char)  # Keep the character if no mapping exists
    return translated_text

def translate_english_to_persian(english_text):
    translated_text = ''
    for char in english_text:
        translated_text += english_to_persian_map.get(char, char)
    return translated_text

# Infinite loop to keep asking the user until they enter a valid choice
while True:
    x = input("p2e or e2p: ").lower()

    if x == 'p2e':
        persian_input = input("Enter Persian text: ")
        translated_output = translate_persian_to_english(persian_input)
        print(f"Translated: {translated_output}")
        break
    elif x == 'e2p':
        english_input = input("Enter English text: ")
        translated_output = translate_english_to_persian(english_input)
        print(f"Translated: {translated_output}")
        break
    else:
        print("Invalid choice! Please enter 'p2e' or 'e2p'.")