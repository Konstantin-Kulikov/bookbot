def count_words(txt):
    print(f'Found {len(txt.split())} total words')


def count_characters(txt):
    d = {}
    for char in txt:
        char = char.lower()
        if char not in d.keys():
            d[char] = 1
        else:
            d[char] += 1
    return d


def sort_dictionaries(d):
    lst = []
    for char in d:
        lst.append({'char': char, "num": d[char]})
    lst.sort(reverse=True, key=lambda x: x['num'])
    return lst
