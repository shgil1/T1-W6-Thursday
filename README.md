## Control Flow 
Order in which lines of code are executed in a program 

print("Hello, welcome to programming with Python")

a = 10
b = 5
result = a + b 

print(f"The result of adding {a} and {b} os {result}")

print("Thank you")


# Sequential control flow 
Execution of code statements one after another, in the order they appear in the program


# Conditional control flow/ Control flow
Execution of code statements based on some input 

if tomorrow is Saturday
    set alarm for 7
if tomorrow is Tuesday
    set alarm for 6


# Boolean Data Type Re-visit
Data type that has two values: True and False  
Boolean values are used to control the flow of the program

is_the_earth_flat = Flase

i_am_happy = True
print(i_am_happy)

# Comparison Operators / Relational Operators
Decide the relationship between the operands. Result of comparison is a boolean value (true/false)
x = 5 y = 7 z = 9

print(y ! =z)
if tomorrow == Saturday
    set alarm for 7
if tomorrow is Tuesday
    set alarm for 6

# if, elif, else
Simplest form of AI 
'if' checks the condition, if the true, the intended blocks get executed, if false, it skips the intended blocks

today = "Tuesday"

if today == "Monday":
    print("Set an alarm for 5 AM!")
elif today == "Tuesday":
    print("Set an alarm for 6 AM!")
if today == "Saturday":
    print("Set an alarm for 7 AM!")


temperature = 30

if temperature > 35:
    print("It's hot outside.")
elif temperature < 15:
    print("It's cold outside.")
else:
    print("The weather is mild.")

# pass 
Does nothing, just....passes..for now

temperature = 40

if temperature > 35:
    pass
elif temperature < 15:
    print("It's cold outside.")
else:
    print("The weather is mild.")

# Boolean Operators
AND, OR, NOT. Operands needs to be boolean as well 

AND: If both of them are true then the entire statement will be true, if any of them are false then it will be false 
OR: If either one of the operands are true then the entire statement will be true 
NOT: Works with one operand and reverses the operand value so if its true its false and if its false its true (UNO REVERSE!)

Nested ifs: if you have multiple conditions you can put a nested under a main block that it will check 

age = 20
has_permission = False

if age >= 18:
    if has_permission:
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("Access denied.")

if age >=18 and has_permission:
    print("Access granted.")
else:
    print("Access denied")

# Ternary Operator 
Condense series of code to one line, where applicable

print("Access granted.") if age >=18 and has_permission else print("Access denied.")


temperature = 30

if temperature > 30:
    message = "It's hot outside"
else:
    message = "It's not hot outside"

print(message)


message = "It's hot outside" if temperature > 30 else "It's not hot outside"

# Match-case
Control flow 

day_number = 3

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"

print(day_name)