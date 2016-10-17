# # def outer_function():
# #     def inner_function():
# #         print "Hi"
# #     return inner_function
# #
# #
# # k=outer_function()
#
# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print "This is the wrapper {} ".format(original_function.__name__)
#         return original_function(*args,**kwargs)
#     return wrapper_function
#
# @decorator_function
# def display():
#     print "I am here "
#
# @decorator_function
# def display2():
#     print "I am here "
#
#
# @decorator_function
# def display3(a,b):
#     print "value of a is %s " %a
#
#
# # display()
# # display2()
# display3(12.001,45)
#
#
# # @decorator_function
# # def display3(a,b):
# #     print "I am here "





def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info('Ran with the arguments :{}, and kwargs : {}'.format(args,kwargs))
        return orig_func(*args,**kwargs)
    return wrapper

def my_timer(orig_func):
    import time,sys
    def wrapper(*args,**kwargs):
        t1=time.time()
        time.sleep(6)
        result=orig_func(*args,**kwargs)
        t2=time.time()-t1
        print ('{} ran in : {} seconds '.format(orig_func.__name__,t2))
        if t2>5:
            sys.exit()
    return wrapper


@my_logger
def display():
    print ("I am here ")

@my_logger
def display2():
    print ("I am here ")


@my_timer
def display3(a,b):
    print ("value of a is %s " %a)


display()
display2()
display3('John',45)


# @decorator_function
# def display3(a,b):
#     print "I am here "





