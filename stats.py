def get_num_words(booktext):
    split_text = booktext.split()
    word_count = len(split_text)
    return word_count

def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.lower() not in letter_count:
            letter_count[letter.lower()] = 1
        else:
            letter_count[letter.lower()] += 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sort_count(count):
    sorted_count = []
    for key in count:
        dict = {}
        dict["char"] = key
        dict["num"] = count[key]
        sorted_count.append(dict)
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count