def sum_squares (x) :
    square = [i ** 2 for i in x]
    return sum(square)
print(sum_squares([1,2,3]))