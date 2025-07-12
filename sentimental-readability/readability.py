from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = float(letters) / words * 100
    S = float(sentences) / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    grade = round(index)
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    letters = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
    return letters


def count_words(text):
    counter = 0
    track = False
    for i in range(len(text)):
        if text[i] != ' ' and track == False:
            counter += 1
            track = True
        elif text[i] == ' ':
            track = False
    return counter


def count_sentences(text):
    counter = 0
    for i in range(len(text)):
        if text[i] == '!' or text[i] == '.' or text[i] == '?':
            counter += 1
    return counter


main()
