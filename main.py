def read_file(file_path: str):
    with open(f"./{file_path}", "r") as f:
        open_file = f.read()
        return open_file


def count_words(text: str):
    words = text.split()
    total_words = len(words)
    return total_words


def sanitize_list(list_to_sanitize):
    import re

    return [char for char in list_to_sanitize if re.match(r"[a-zA-Z]", char)]


def count_letters(text: str):
    lower_case_words = text.lower().split()
    all_characters = []

    # Iterate to find unique characters
    for word in lower_case_words:
        for character in word:
            all_characters.append(character)

    unsanitized_unique_characters = set(all_characters)

    unique_characters = sanitize_list(list(unsanitized_unique_characters))

    count_of_characters = {}
    # Create dictionary to count occurences
    for character in unique_characters:
        count_of_characters[character] = 0

    # Iterate to count the character occurences
    for word in lower_case_words:
        for character in word:
            if character in count_of_characters.keys():
                count_of_characters[character] += 1

    characters_sorted_by_occurance = []
    # Transform this single dictionary into a list of dicts
    for character in count_of_characters.keys():
        characters_sorted_by_occurance.append(
            {"name": character, "num": count_of_characters[character]}
        )

    # Define a function that can sort the list based on the `num` key
    def sort_on(dict):
        return dict["num"]

    characters_sorted_by_occurance.sort(reverse=True, key=sort_on)

    return characters_sorted_by_occurance


def print_the_report(ordered_characters, book_path, words_counted):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_counted} words found in the document")
    print("\n")
    for character_dict in ordered_characters:
        print(
            f"The {character_dict['name']} character was found {character_dict['num']} times"
        )
    print("--- End report ---")


if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    file_content = read_file(file_path)
    words_counted = count_words(file_content)
    ordered_count_of_characters = count_letters(file_content)
    print_the_report(ordered_count_of_characters, file_path, words_counted)
