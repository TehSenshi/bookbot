def word_count(book):
    word_list = book.split()
    length = len(word_list)
    return length

def char_count(book):
    book_lower = book.lower()
    sym_count = {}
    for sym in book_lower:
        if not sym in sym_count:
            sym_count[sym] = 0
        sym_count[sym] += 1
    return sym_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    keyed_dict = []
    for char in dict:
        keyed_dict.append({"char": char, "num": dict[char]})
    keyed_dict.sort(reverse=True, key=sort_on)
    return keyed_dict
