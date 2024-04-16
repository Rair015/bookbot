def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{wordCount(file_contents)} words found in the document")
        print("")

        sort_dict(charCount(file_contents))
    
    print("--- End report ---")

def wordCount(text):
    words = []
    words = text.split()

    return len(words)

def charCount(text):
    count = dict()

    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list = []

    for char in dict.keys():
        if char.isalpha():
            print(f"The {char} character was found {dict[char]} times")
            list.append({"letter":char, "count":dict[char]})

    list.sort(reverse=True, key=sort_on)

    for char in list:
        print(f"The {char["letter"]} character was found {char["count"]} times")

    return list

main()