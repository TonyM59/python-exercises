#Doubler
#Write a method doubler(numbers) that takes an array of numbers and returns a new array
#where every element of the original array is multiplied by 2.


def doubler(numbers):
    output = []
    for x in numbers:
      output.append(x*2)
    print(output)
doubler([2,4,6])