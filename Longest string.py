my_list = ['blood', 'air', 'fire', 'yuyuy']

def longest_string(word_list):
    longest_len = 0
    longest_words = []
    for s in my_list:
        if len(s) > longest_len:
            longest_len = len(s)
            longest_words = [s]
        elif len(s) == longest_len:
            longest_words.append(s)
        print(longest_words)

longest_string(my_list)

      