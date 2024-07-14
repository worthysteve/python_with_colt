# def sum_all_nums(a,b,c):
#     return a + b + c


# def sum_all_nums(a, *args):
def sum_all_nums(*args):
    # print(a)
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4,6,9,4,10))