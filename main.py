def main():

    #assign book path
    book_path = "books/frankenstein.txt"

    #calling the function to get content from file
    text = get_book_text(book_path)

    #calling the function to get numbers of words
    num_words = get_num_words(text)

    #calling function of getting occurences of letters
    chars_dict = get_chars_dict(text)

    #calling letters that is sorted in reverse
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

 
    print("--- Begin report of" + book_path + " ---")
    print(f'{num_words} words was found in the document')
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

#print end report
    print("--- End report ---")

#function to get length of words == words count
def get_num_words(text):
    words = text.split()
    return len(words)



def sort_on(d):
    return d["num"]



def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


#function to get turn string of text to dictionary of letter:occurences by adding 1 everytime that letter appear
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars




#1 open file and return content
def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
