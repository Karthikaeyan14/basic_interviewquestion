"""#sorted
tests = [("login", 3.2), ("logout", 1.1), ("search", 2.4)]
t=sorted(tests,key=lambda item:item[1])
print(t)


"""

#max
"""max=lambda value_a,value_b:value_a if value_a>value_b else value_b
print(max(90,20))

#sum
sum=lambda a,b:a+b
print(sum(10,20))
#even_number
is_even=lambda a:"True" if a%2==0 else "False"
print(is_even(11))
"""
#   map(function, iterable, *iterables, strict=False)
times = [1.2, 0.8, 3.5, 2.1, 5.0, 0.9]
filter=list(map(int,times))
print(filter)