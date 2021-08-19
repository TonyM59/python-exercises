#Write a method fizz_buzz(max) that takes in a number max and returns an array containing all numbers greater
#than 0 and less than max that are divisible by either 4 or 6, but not both.

def fizz_buzz(max):
    nums = []
    for i in range(0, max):
        if((i % 4 == 0 and i % 6 != 0) or  (i % 4 != 0 and  i % 6 == 0)):
            nums.append(i)

            i += 1
    return nums
print(fizz_buzz(30))