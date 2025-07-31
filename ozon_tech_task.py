def longest_palindrome(s: str) -> int:
    lst = [i for i in s]
    dictionary = {}
    lenght = 0
    flag = False
    for i in lst:
        dictionary[i] = lst.count(i)
    for value in dictionary.values():
        if value % 2 == 0:
            lenght += value
        else:
            lenght += value - 1
            flag = True
    if flag:
        lenght += 1
    return lenght

