str = "the quick brown fox saw the other fox the end"

# 1. turn the string into a list of words
# 2. loop through the list and add each word as a key to a dictionary - with a value of 1 if it's the first occurence of the word, otherwise the value should indicate how many times that word has appeared
# 3 print outna report with the final count of occurences for each word

words_list = str.split()

words_count = {}

# for word in words_list:
#     if word not in words_count:
#         words_count[word] = 1
#     else:
#         words_count[word] += 1

for word in words_list:
    words_count[word] = words_count.get(word, 0) + 1

for key, value in words_count.items():
    print(key + ':', value)
