# Task 1. Reverse a negative integer and keep the negative sign at the beginning.

# def reverse_negative_interger(n:int):
#     string = str(n)
#     if string[0] == '-':
#         return '-' + string[:0:-1]
#     else:
#         return string[::-1]
#
# print(reverse_negative_interger(-123))
# print(reverse_negative_interger(456))
#

# Task 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.

# def are_anagrams(s1: str, s2: str):
#     s1 = s1.lower()
#     s2 = s2.lower()
#     if len(s1) == len(s2):
#         if sorted(s1) == sorted(s2):
#             return True
#     return False
#
#
# print(are_anagrams('racewef', 'acer'))
# print(are_anagrams('Cake', 'kace'))


# Level 2
# Task 3. Given a sentence, reverse the order of characters in each word.

# def reverse_words(sentence: str):
#     words = sentence.split(" ")
#     print(words)
#     new_words = [word[::-1]] for word in words:
#     print(new_words)
#     new_sentence = " ".join(new_words)
#     print(new_sentence)
#
#
# reverse_words('Im am going to the park today')



#     words = sentence.split(" ")
#     print(words)
#     new_words = [word[::-1] for word in words]
#     print(new_words)
#     new_sentence = " ".join(new_words)
#     print(new_sentence)
#
#
# reverse_words('Im am going to the park today')


# Task 4. Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

# def repeat_digits(s: str):
#     result = ""
#     for i in range(len(s)):
#        result += int(s[i]) * s[i]
#
#     return result
#
#
# print(repeat_digits('1234'))


# Task 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
# “y” is not considered a vowel for this task. The input string is always in lowercase.

# def shortcuts(s:str):
#     result = ''
#     vowel_list = ['a','e','i','o','u']
#     for i in range(len(s)):
#         if s[i] not in vowel_list:
#             result += s[i]
#     return result
#
# print(shortcuts('is this going to be the best day ever'))

