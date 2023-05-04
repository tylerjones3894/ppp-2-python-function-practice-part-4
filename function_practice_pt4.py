#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max([a,b,c])

print(max_num(8,9,10))

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list():
    if len(lst) == 0:
        return 0
    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod

#Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[::1]

#Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
    return x in range(a,b+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal():
    #I need more time with this one.
    #will resubmit before saturday.