'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    i = 0
    length_of_leftover_words = len(word[1:len(word)])
    leftover_words = word[1:len(word)]
    if word[0:2] == 'th':
        count += 1
        i += 1
        return count_th(word[i:], count)
    elif length_of_leftover_words > 1:
        count = count_th(leftover_words, count)

    return count

    # TBC
wordtest = count_th('thelloththth')

print(wordtest)
