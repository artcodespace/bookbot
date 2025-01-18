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
    path = "books/frankenstein.txt"
    print(f"--- Begin report of {path}")
    with open(path) as f:
        file_contents = f.read()

        print(f"{count_words(file_contents)} words found in the document\n")
        char_count = count_letters(file_contents)
        for char in char_count:
            if char.isalpha():  
                print(f"The '{char}' character was found {char_count[char]} times")


main()


