# reverse the string
# 1st method using slice
'''
    return string1[::-1]
def string_reverse(string1):
print string_reverse('hello')
'''


# https://github.com/eunki7/Python-Programs/blob/master/reverse.py
# 2nd method through list


def reverse(list):
    rlist = [];

    i = len(list) - 1

    while i >= 0:
        rlist.append(list[i])
        i = i - 1


print(i)
return rlist

print(reverse("anum"))
