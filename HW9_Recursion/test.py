# Сам декоратор-счётчик

def call_times(func):
    def inner(*args, **kwargs):
        inner.count += 1

        return func(*args, **kwargs)


    inner.count = 0
    return inner




# Функция, вызовы которой нужно считать

@call_times
def foo():
    print("Hello")


foo()
foo()
foo()


print(foo.count)