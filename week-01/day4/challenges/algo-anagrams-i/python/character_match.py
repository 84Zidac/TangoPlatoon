# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
    str1 = sorted(string1.lower().replace(' ', ''))
    str2 = sorted(string2.lower().replace(' ', ''))
    return str1 == str2


# print(is_character_match('charm', 'march') == True)


# # Part 2
def anagrams_for(word, list_of_words):
    answer = []
    str1 = sorted(word.lower())
    for words in list_of_words:
        if str1 == sorted(words.lower()):
            answer.append(words)
    return answer


# list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

# print(anagrams_for("threads", list_of_words) == [
#       "threads", "trashed", "hardest", "hatreds"])
