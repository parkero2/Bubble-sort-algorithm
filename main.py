import random as r

unsorted_numbers = []
tempval = 0

for x in range(int(input("How many numbers in the list? "))):
    unsorted_numbers.append(r.randint(1, 10))
print(unsorted_numbers)

for y in range(len(unsorted_numbers)):
    for p in range(len(unsorted_numbers) - 1):
        if unsorted_numbers[p] > unsorted_numbers[p + 1]:
            tempval = unsorted_numbers[p]
            unsorted_numbers.pop(p)
            unsorted_numbers.insert(p + 1, tempval)
    print(unsorted_numbers)
