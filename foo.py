

def foo():
    global a
    a = 10
    print(a)


if __name__ == '__main__':
    # global a
    a = 5
    foo()
    print(a)
