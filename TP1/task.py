
docs = {
    "D1": "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza.",
    "D2": "Five pizza were ready, but 3 bourak burned!",
    "D3": "We only had 8 chamiyya, no pizza, and one tea.",
    "D4": "Is 6 too much? I ate nine bourak lol."
}


digit_to_word = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten"
}


def normalize(text):
    
    text = text.lower()
    
    
    words = text.split()
    new_words = []
    
    for word in words:
       
        clean_word = word.strip(".,!?")
        
        
        if clean_word in digit_to_word:
            new_word = digit_to_word[clean_word]
        else:
            new_word = clean_word
        
        new_words.append(new_word)
    
    
    normalized_text = " ".join(new_words)
    
    return normalized_text



normalized_docs = {}

for key, value in docs.items():
    normalized_docs[key] = normalize(value)


for key, value in normalized_docs.items():
    print(key + ":", value)







#     line 36
# .strip(".,!?") only works for the start/end of a word
# it fails if punctuation is in the middle, example : "don't" or "U.S.A."

#     line 36
# Use string.punctuation bcz it's better than hardcoding marks manually

#     line 39
# btw, you can use .get() here to handle the dict lookup and the "else" in one line

#     line 46
# you can use a dict comprehension to normalize everything in one go
