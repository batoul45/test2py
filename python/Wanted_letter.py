def most_wanted_letter(text):
    # First of all we need to Convert all characters to lowercase 
    text = text.lower()
    
    # Now we need to  keeps track of each letter we find in the input and how often it appears
    # So basicly every letter becomes a key , and its "value" is the count of that letter
    
    letter_list = {}
    
    # Next step is to count  occurrences of every letter in the text we have
    for letter in text:
        # It is necessery to verify if the character is a letter 
        if 'a' <= letter <= 'z' or 'а' <= letter <= 'я':  # Checks for both Latin and Cyrillic letters
            letter_list[letter] = letter_list.get(letter, 0) + 1
            
    # If we dont find any letters ,just  return a warning message
    if not letter_list:
        return "There are no letters in the string"
    
    # Find the letter with the highest frequency. In case of a tie, return the lexicographically first letter.
    max_frequency = max( letter_list.values())
    most_frequent_letter = min([char for char in letter_list if letter_list[char] == max_frequency])

    return f"The most popular letter is {most_frequent_letter}"

 #Testing with provided examples

print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))
