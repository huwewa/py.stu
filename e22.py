def add(a, b):
    print "%s + %s" % (a, b)
    return a + b

def sub(a, b):
    print "%s - %s" % (a, b)
    return a - b

def mul(a, b):
    print "%s * %s" % (a, b)
    return a * b

def div(a, b):
    print "%s / %s" % (a, b)
    return a / b

age = add(20, 8)
tall = sub(180, 9)
weight = mul(2, 30)
level = div(10, 5)

print "age = %s. tall = %s. weight = %s. level = %s." % (age, tall, weight, level)

print add(1, sub(100, mul(4, div(15, 3))))
