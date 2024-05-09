def read_file(file_path: str):
    with open(f"./{file_path}", "r") as f:
        open_file = f.read()
        return open_file

def count_words(text: str):
    words = text.split()
    total_words = len(words)
    return total_words

def count_letters(text: str):
    count_of_characters = {}
    for _ in text:
        if _ not in count_of_characters and _.isalpha():
            count_of_characters[_] = 1
        elif _ in count_of_characters and _.isalpha():
            count_of_characters[_] += 1

    count_of_characters = dict(sorted(count_of_characters.items()))
    
    return count_of_characters

def print_the_report(ordered_characters, book_path, words_counted):
    header = "--- Begin report of {} ---\n{} words found in the document\n\n".format(book_path, words_counted)
    
    character_lines = "".join(
    ["The {} character was found {} times\n".format(char, count) for char, count in ordered_characters.items()]
    )
    
    footer = "--- End report ---"
    
    report = header + character_lines + footer
    
    return report

if __name__ == "__main__":
    file_path = "frankenstein.txt"
    file_content = read_file(file_path)
    words_counted = count_words(file_content)
    ordered_count_of_characters = count_letters(file_content)
    print(print_the_report(ordered_count_of_characters, file_path, words_counted))
