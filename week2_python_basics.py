
### 1. Variables

# Create a variable named 'radius' and assign a value
radius = 20

# You can assign initial values referencing other variables
area = radius * radius * 3.14

print("The area for the circle of radius ", radius, "is ", area)

# data type of a variable is defined automatically and can be changed by values
test_var = "Hello World !"
print(type(test_var))
test_var = 1234
print(type(test_var))

# Quiz
var_a = 1
var_b = 1
var_c = var_a
var_a = var_a + 1
var_c = "hello world"
print(var_a, var_b, var_c)

# Various ways to declare variables
i = j = k = 1

k = 1
j = k
i = j

i, j, k = 1, 2-1, 0+1

# variable swaps
x = 1
y = 2
temp = x
x = y
y = temp
print(x, y)

x = 1
y = 2
x, y = y, x
print(x, y)


print("="*30)

### 2. Numbers
int_a, int_b, int_c, int_d  = 2, 321, -50, 0
print(type(int_a), type(int_b), type(int_c), type(int_d))
float_a, float_b, float_c, float_d = 2.0, 4.5, -51.4, 25e-5
print(type(float_a), type(float_b), type(float_c), type(float_d))
complex_a, complex_b = 5j, -3.1j
print(type(complex_a), type(complex_b))

### 3. Strings
example = "Python's String"
example2 = 'Python has "String"'
print(example)
print(example2)

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says"
print(food)
print(say)

# string with multiple lines
multi_line1 = '''
Life is too short
You need python
'''

multi_line2 = """
Life is too short
You need python
"""

multi_line_with_escape_code = "Life is too short \nYou need python"

print(multi_line1)


# escape codes
s = "Name\tAge"
print(s)

s2 = 'One\nTwo\nThree'
print(s2)

s3 = 'C:\\Users\\Q'
print(s3)


# string concatenation 1
s1 = "This is " + "one complete string"

#s_error = "Python" + 101

s_correct = "Python"+str(101)
print(s_correct)

# string concatenation 2
print("Experiments #1 finished.")
print("=" * 30)
print("Now experiments #2 starts.")

print(("-" * 2 + "*") * 3)

# String indexing
s = "hello"
print(s[0], s[1], s[2])

s = "markdown"
print(s[-1], s[-2], s[-3], s[-4])

# String slicing
a = "Life is too short, You need Python"
print(a[8:11])
print(a[8:200])
print(a[8:])
print(a[:10])

a = "Industrial Engineering Rocks...!"
print(a[8:13])
print(a[8:2023])
print(a[8:])
print(a[:13])
print(a[:])
print(a[:-5])
print(a[-7:-1])


# String is immutable
a = "Pithon"
#a[1] = "y"

a = a[:1] + "y" + a[2:]
print(a)

# String formatting
print("There are %d dogs. " % 5)
dogs_num = 10
print("There are %d dogs." % dogs_num)
print("There are %s dogs." % "Two")
print("There are %d %s dogs." %(2, "lovely"))

print("%.4f" % 3.123456)
print("%10.4f"%3.123456)

# Related functions
a = "this is example string line   "
a.count("e")
a.find("i")
a.find("z")
a.index("i")
a.index("z")

b = ','.join(a)
a.upper()
a.rstrip()
a.replace()
a.split()
a.split("example")






