def prettyprint(func):
    def wrapper(*args, **kwargs):
        print("#########")
        func()
        print("#########")
    return wrapper



if __name__=="__main__":
    @prettyprint
    def a():
        variable = 1000
        print("hello")
        print(variable)

    a()