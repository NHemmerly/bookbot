def count_characters(text):
    char_dict = {}
    for char in text:
        if not char.isalpha():
            continue
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    dict_sort = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    return dict(dict_sort)

def count_words(text):
    word_list = text.split()
    return len(word_list)

def print_report(text_path):
    print(f"--- Begin report of {text_path} ---")
    with open(text_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_dict = count_characters(file_contents)
        print(f"{word_count} words found in the document\n")
        for key in char_dict:
            print(f"The '{key}' character was found {char_dict[key]} times")
        

def main():
    frankenstein = "books/frankenstein.txt"
    print_report(frankenstein)
    

main()