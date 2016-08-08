def foo():
    m = 3
    def bar( b):
        a = 4
        return m + a + b

    return bar

bar = foo()
print bar(1)
bar2 = foo()
print bar2(2)

def generate_power_func(n):
    print "id(n): %X" % id(n)
    def nth_power(x):
        return x**n
    print "id(nth_power): %X" % id(nth_power)
    return nth_power

# raised_to_4 = generate_power_func(4)
# print raised_to_4(2)
# print raised_to_4.__closure__
# print type(raised_to_4.__closure__[0])
# print raised_to_4.__closure__[0].cell_contents