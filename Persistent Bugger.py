def persistence(n):
    if len(str(n)) == 1:
        return 0
    product = 1
    for num in str(n):
        product *= int(num)
    return  1 + persistence(product)
