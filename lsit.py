def announce(func):
    def wrapper():
        print("Before the call")
        func()
        print("After the call")
    return wrapper
@announce
def say_hello():
    print("Hello!")
say_hello()