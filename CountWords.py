
text = input("Text: ")

def count_words():
    spaces = 1
    for character in text:
        if character == " ":
            spaces += 1
    print((str(spaces) + " words"))

def count_character():
    print(str(len(text)) + " characters")

count_words()
count_character()