def count_words(text):
    words = text.split()

    return len(words)
        
def count_chars(text):
    chars = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 
        'z': 0, 
    }

    for char in text.lower():
        if char in chars:
            chars[char] += 1    
    
    return chars   

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    chars_list = []

    for char in dict:
        chars_list.append({"char": char, "count": dict[char]})
    
    chars_list.sort(reverse = True, key = sort_on)

    return chars_list

def main():
    file_contents = ""

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    chars = count_chars(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{count_words(file_contents)} words were found in the document \n")
    
    chars_list = dict_to_list(chars)

    for entry in chars_list:
        print(f"The '{entry['char']}' character was found {entry['count']} times")

    print("--- End report ---")


main()