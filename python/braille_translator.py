# braille_translator.py

# Mapping of Braille to English letters and numbers
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital': '.....O',  # Braille symbol for capitalization
    'space': '......',    # Braille space
    'number': '.O.OOO',   # Braille number symbol
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mapping: from Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}

def is_braille(text):
    """Check if the input is in Braille format."""
    return all(char in ['O', '.'] for char in text)

def english_to_braille(english_text):
    """Convert English text to Braille."""
    result = []
    is_number_mode = False

    for char in english_text:
        if char.isupper():
            result.append(braille_alphabet['capital'])
            result.append(braille_alphabet.get(char.lower(), '......'))  # Handle unknown characters
        elif char.isdigit():
            if not is_number_mode:
                result.append(braille_alphabet['number'])
                is_number_mode = True  # Set flag to handle numbers
            result.append(braille_alphabet.get(char, '......'))  # Convert number
        elif char == ' ':
            result.append(braille_alphabet['space'])
            is_number_mode = False  # Reset number mode after space
        else:
            result.append(braille_alphabet.get(char, '......'))  # Convert letters
            is_number_mode = False  # Reset number mode after letters

    final_result = ''.join(result)
    return final_result

# Main block to execute the script from the command line
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        # Join all command-line arguments into a single string
        input_text = ' '.join(sys.argv[1:])
        translated_text = english_to_braille(input_text)  # Translate from English to Braille
        print(translated_text)  # Print only the translation
    else:
        print("Please provide a string to translate.")