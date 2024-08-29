from collections import Counter
import math 

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s.upper()):
        current = roman_dict.get(char, 0)  # Get the value, defaulting to 0 for any non-roman characters
        if current >= prev_value:
            total += current
        else:
            total -= current
        prev_value = current
    return total

def read_roman_numerals(file_path):
    with open(file_path, 'r') as file:
        content = file.read().replace('\n', ' ')
    return content

def split_numerals(content):
    segments = content.split(' M ')
    return segments

def convert_numerals_to_numbers(segments):
    numbers_list = []
    for segment in segments:
        numerals = segment.split()
        numbers = [roman_to_int(numeral) for numeral in numerals]
        numbers_list.append(numbers)
    return numbers_list

def calculate_frequency(content):
    numerals = content.split()
    frequency = {}
    for numeral in numerals:
        if numeral in frequency:
            frequency[numeral] += 1
        else:
            frequency[numeral] = 1
    return frequency

def convert_to_ascii(numbers_list):
    ascii_text = []
    for segment in numbers_list:
        # Ensure only printable ASCII characters are converted and concatenated
        segment_text = ''.join(chr(num % 256) for num in segment if num % 256 >= 32 and num % 256 <= 126)
        ascii_text.append(segment_text)
    return ascii_text

def vigenere_decrypt(ciphertext, keyword):
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    plaintext = ''
    for ct, k in zip(ciphertext, keyword_repeated):
        shift = ord(k) - ord('A')
        pt_char = chr((ord(ct) - shift) % 256)
        plaintext += pt_char
    return plaintext


def decrypt_transposition_cipher(text, key):
    num_of_columns = int(math.ceil(len(text) / float(key)))
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)
    plaintext = [''] * num_of_columns
    col = 0
    row = 0

    for symbol in text:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)




# Main execution
file_path = 'RomanNum.txt'
roman_content = read_roman_numerals(file_path)
frequency = calculate_frequency(roman_content)
segments = split_numerals(roman_content)
numbers_list = convert_numerals_to_numbers(segments)
ascii_output = convert_to_ascii(numbers_list)
all_data = ''.join(ascii_output)  # Combine all segments into one string

# Decrypt using Vigenère cipher with "Skittles" as the keyword
decrypted_message = vigenere_decrypt(all_data, 'Skittles')

# Example usage
decrypted_text = decrypt_transposition_cipher(all_data, key=7)  # Assuming a key of 7 for the sake of the example
print(decrypted_text)

print("Decrypted Message with 'Skittles' as keyword:", decrypted_message)
