def first_non_repeating_letter(string):
    unique_characters = [char for char in string if string.lower().count(char.lower()) == 1]
    return unique_characters[0] if unique_characters else ''
