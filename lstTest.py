def test(a, b = []):
    #print b
    #b = []
    print id(a)
    print id(b)
    b.append(a)
    print a
    print b

test(1)
test(2)
test(3)