

def test_function_without_argument():
    x = 4
    if x%2 == 1:
        print("odd")
    else:
        print("even")

def test_function_with_arg(x):
    if x%2 == 1:
        print("odd")
    else:
        print("even")

def function_with_return(x):
    if x%2 == 1:
        return "odd"
        print("jdsasjdaojd")
    else:
        return "even"
    print("Hello")

if __name__ == "__main__":
    a = 6
    # test_function_without_argument()
    # test_function_with_arg(a)
    # x1 = test_function_with_arg(a)
    # print(x1)
    x2 = function_with_return(a)
    print(x2)