# Integer
a = 10
b = 5
int_result = a + b
print(f"Integer result: {int_result}, \nType: {type(int_result)}")

integer_var = 10
int_sum = integer_var + 5
int_product = integer_var * 2
print(f"Integer Sum: {int_sum}, \nType: {type(int_sum)}")
print(f"Integer Product: {int_product}, \nType: {type(int_product)}")
print()

# Float
x = 3.14
y = 2.5
float_result = x * y
print(f"Float result: {float_result}, \nType: {type(float_result)}")

float_var = 20.5
float_sum = float_var + 4.5
float_division = float_var / 2
print(f"Float Sum: {float_sum}, \nType: {type(float_sum)}")
print(f"Float Division: {float_division}, \nType: {type(float_division)}")
print()

# String
str1 = "Hello"
str2 = "World"
str_result = str1 + " " + str2
print(f"String result: {str_result}, \nType: {type(str_result)}")

string_var = "Hello"
string_concatenation = string_var + " World"
string_repetition = string_var * 3
print(f"String Concatenation: {string_concatenation}, \nType: {type(string_concatenation)}")
print(f"String Repetition: {string_repetition}, \nType: {type(string_repetition)}")
print()

# Boolean
bool1 = True
bool2 = False
bool_result = bool1 and bool2
print(f"Boolean result: {bool_result}, \nType: {type(bool_result)}")

boolean_var = True
boolean_not = not boolean_var
boolean_and = boolean_var and False
print(f"Boolean NOT: {boolean_not}, \nType: {type(boolean_not)}")
print(f"Boolean AND: {boolean_and}, \nType: {type(boolean_and)}")
print()

# Mixed operations
mixed_result = a + x
print(f"Mixed result (int + float): {mixed_result}, \nType: {type(mixed_result)}")

# Type conversion
int_to_float = float(a)
print(f"Integer to Float: {int_to_float}, \nType: {type(int_to_float)}")

float_to_int = int(x)
print(f"Float to Integer: {float_to_int}, \nType: {type(float_to_int)}")

int_to_str = str(a)
print(f"Integer to String: {int_to_str}, \nType: {type(int_to_str)}")

bool_to_int = int(bool1)
print(f"Boolean to Integer: {bool_to_int}, \nType: {type(bool_to_int)}")
