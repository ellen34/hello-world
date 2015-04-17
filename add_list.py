def add_list(numbers):
    total = 0
    for items in numbers:
        total = total + items
    return total


a = raw_input("Please enter a number: ")
b = raw_input("Please enter another number: ")
numbers = [int(a),int(b)]
print numbers
sum = add_list(numbers)
print sum
