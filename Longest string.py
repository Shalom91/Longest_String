my_list = ['blood', 'air', 'fire', 'tutor']

def longest_string(word_list):
    longest_len = 0
    longest_words = []
    for word in my_list:
        if len(word) > longest_len:
            longest_len = len(word)
            longest_words = [word]
        elif len(word) == longest_len:
            longest_words.append(word)
    return longest_words

print(longest_string(my_list))
      
