def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_count = {}
    for char in text:
        lower_case_char = char.lower()
        if lower_case_char in letter_count:
            letter_count[lower_case_char] += 1
        else:
            letter_count[lower_case_char] = 1
    return letter_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_letters(file_contents))

main()


