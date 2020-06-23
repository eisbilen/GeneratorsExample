# Simple Generator
def my_simple_generator():
    k = 0
    yield k
    
    k = 1 
    yield k

    k = 2
    yield k

my_numbers = my_simple_generator()

print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
# Below call raises StopIteration as generator is fully iterated
# print(next(my_numbers))



# Defining Generators with Loop
def my_generator_with_loop(my_str):
    length = len(my_str)

    for k in range(length):
        yield my_str[k]

my_text = my_generator_with_loop("Coding")

for char in my_text:
    print(char)


# Defining Generators with Expressions
my_generator_expression = (number**2 for number in range(4))
print (sum(my_generator_expression))


# Defining Generator Pipeline
my_generator_01 = (number**2 for number in range(40))
my_generator_02 = (number-5 for number in my_generator_01)

print(sum(my_generator_02))