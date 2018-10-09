x = 6

def example():
    print(x)
    # z, however, is a local variable.
    z = 5
    # this works
    print(z)

def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    x+=6

    # so there we attempted to take the x var and add 6 to it... but now
    # we are told that we cannot, as we're referencing the variable before
    # its assignment.

def example3():
    # what we do here is defined x as a global variable.
    global x
    # now we can:
    print(x)
    x+=5
    print(x)

#example()
#example2()
example3()