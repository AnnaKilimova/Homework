
def call_times(func):


    def inner(*args, **kwargs):

        func(*args, **kwargs)



        with open('foo.txt', 'a') as f:
            f.write(f'{func} была вызвана' + ' ' + f'{c} раза.\n')

    return inner

count = 0

@call_times
def foo():
    global count

    count += 1

    return count

foo()
foo()

c = count

# count = 0
#
# @call_times
# def boo():
#
#     global count
#
#     count += 1
#
#     return count


# boo()
# def call_times(func):
#
#     def inner(*args, **kwargs):
#         print(f'{func} была вызвана')
#         func(*args, **kwargs)
#         print(f'{count} раза. \n')
#
#     return inner
#
# count = 0
#
# @call_times
# def foo():
#
#     global count
#
#     count += 1
#
#     return count
#
# foo()
# foo()