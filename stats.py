# Function to count number of words in a string of text
def get_num_words(text):
    # Split the text by whitespace and filter out empty strings
    words = [word for word in text.split() if word]
    return len(words)

def count_frequencies(text):
    # convert text and character to lowercase for case insensitive counting
    lower_text = text.lower()
    # count occurrences of the character and return as a dictionary
    return {char: lower_text.count(char) for char in set(lower_text)}

def get_sorted_frequencies(freq):
    def sort_on(item):
        return item["num"]
    sorted_list = []
    for char, count in freq.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
