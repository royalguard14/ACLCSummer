import random, os
os.system('cls')
print("Swertres!")


print("Enter your 3 Bet numbers (each between 0 and 9):")
user_numbers = []
for i in range(3):
    while True:
        try:
            num = int(input(f"Enter Bet number {i+1}: "))
            if num < 0 or num > 9:
                raise ValueError("Number must be between 0 and 9.")
            user_numbers.append(num)
            break
        except ValueError as e:
            print(e)

#result_numbers = [1,2,3]                       #for test onlu
result_numbers = random.sample(range(10), 3)    #for publish
print("Swertres Result:", result_numbers)


if user_numbers == result_numbers:
    print("You Win!")
elif user_numbers == result_numbers:
    print("You Partial Win!")
else:
    print("You lose!")
