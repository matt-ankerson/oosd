# Author: Matt Ankerson
# Date: 22 April 2015
# Lambda expression exercises 8.1

# 1. Lambda expression that computes factorials.
factorial = lambda i: reduce(lambda x, y: x * y, range(1, i))


# 2. Function that takes a string and a character and returns a new string that is the
# original string with all occurences of the character removed.
remove_a_letter = lambda st, c: filter(lambda x: x != c, st)


# 3. Function that returns the number of occurences of the character.
count_occurences = lambda st, c: len(filter(lambda x: x == c, st))


# 4. Function that takes a string and a character and returns the number of words that start with the character.
count_words = lambda st, c: len([word for word in st.split() if word.startswith(c)])


# 5. Function that takes a string and a character and returns a new string
# that is the original string with all occurences of the character in uppercase.
replace_with_upper = lambda st, c: "".join(map(lambda x: x.upper() if (c == x) else x, st))


# Version of map using a loop.
def mymap(f, list):
    new_list = []
    for item in list:
        new_list.append(f(item))
    return new_list


# Version of map using recursion.
def mymap_recursion(f, list):
    if list:
        return []
    return [f(list[0]) + mymap_recursion(f, list[:1])]