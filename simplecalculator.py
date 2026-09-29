def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y



x_val = float(input("Enter x value: "))
y_val = float(input("Enter y value: "))

print(f"add({x_val}, {y_val}) > {add(x_val, y_val)}")
print(f"subtract({x_val}, {y_val}) > {subtract(x_val, y_val)}")
print(f"multiply({x_val}, {y_val}) > {multiply(x_val, y_val)}")
print(f"divide({x_val}, {y_val}) > {divide(x_val, y_val)}")
