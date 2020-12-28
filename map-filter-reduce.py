# map(func, seq) transforms each element with the function.
# filter(func, seq) returns all elements for which func evaluates to True.
# reduce(func, seq) repeatedly applies the func to the elements and returns a single value. func takes 2 args.

a = [1, 2, 3, 4]

#map
b = list(map(lambda x: x * 2, a))
# [2, 4, 6, 8]

#filter
c = list(filter(lambda x: (x%2 == 0), a))
# [2, 4]

#reduce
product_a = reduce(lambda x, y: x*y, a)
# 24
sum_a = reduce(lambda x, y: x+y, a)
#10