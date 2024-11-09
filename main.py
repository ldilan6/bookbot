


def main():
    book_path = "books/frankenstein.txt"
    get_text_of_book = get_book(book_path)
    get_num_words = count_words(get_text_of_book)
    
        #print(file_contents)
    get_count_of_chars = count_characters(get_text_of_book)
    get_report = report(get_count_of_chars)
    
    #print(get_count_of_chars)
    #print(count_words(file_contents))
    print(f"---Begin report of {book_path}---")
    print(f"{get_num_words} words found in the document")
    print_report = print_the_report(get_report)
    print("---End of report---")
    return 0
def get_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def count_words(file_string):
    
    words_arr = file_string.split()
    word_count = len(words_arr)
    #print(word_count)
    #pass    
    return word_count
def count_characters(file_string):
    file_string_to_lower = file_string.lower()
    char_dict = {}
    
    for char_text in file_string_to_lower:
        if(char_text in char_dict):
            
            char_dict[char_text] += 1
        else:
            
            char_dict[char_text] = 1
    return char_dict
def sort_on(char_dict):
    return char_dict["num"]
def report(dict):
    list_of_chars = []
    for character, count in dict.items():
        temp_char_dict = {"character": character, "num": count}
        if(character.isalpha()):
            list_of_chars.append(temp_char_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
def print_the_report(list_of_chars):
    for temp_char_dict in list_of_chars:
        print(f"The '{temp_char_dict['character']}' was found {temp_char_dict['num']} times")
main()