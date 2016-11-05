def outer_func():
    message='hi'

    def inner_function():
        print (message)
    return inner_function


outer_func()()
#my_func=outer_func()


