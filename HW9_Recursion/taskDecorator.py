counter = {}
def call_times(file_name):
    def inner(func):
        def wrapper():
          wrapper.count += 1
          counter[func.__name__] = wrapper.count
          with open(file_name, 'w') as f:
               for func_name, quantity in counter.items():
                  f.write(f'{func_name} была вызвана {quantity} раза.\n')
          return func()

        wrapper.count = 0

        return wrapper

    return inner

@call_times('foo.txt')
def foo():
    pass

@call_times('foo.txt')
def boo():
    pass

@call_times('calls.txt')
def doo():
    pass

foo()
boo()
foo()
foo()
boo()
dict.clear(counter)
doo()