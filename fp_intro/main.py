# Author: Matt Ankerson
# Date: 22 April 2015

# Write a lambda expression that computes factorials. (Use reduce)
print(reduce(lambda x, y: x * y, range(1, 6)))


# Write a function that takes a string and a character and returns a new string that is the
# original string with all occurences of the character removed.
def remove_letter(c="h", st="hello world"):
    return filter(lambda x: x != c, st)

remove_a_letter = lambda st, c: filter(lambda x: x != c, st)
print(remove_a_letter("hello world", "o"))

# Write a function that is similar to the one above,
# but that returns the number of occurences of the character.
count_occurences = lambda st, c: len(filter(lambda x: x == c, st))
print(count_occurences("hello world", "o"))


# Write a function that takes a string and a character and returns the number of words that start with the character.
def count_words(st, c):
    return len([word for word in st.split() if word.startswith(c)])
print(count_words("cracker crunch monday", "c"))

# Write a function that takes a string and a character and returns a new string
# that is the original string with all occurences of the character in uppercase.


# Write your own version of map (call it mymap) using a loop.


# Rewrite mymap using recursion.
