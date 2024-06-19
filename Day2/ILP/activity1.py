import os
os.system("cls")

word = "summer bootcamp"
print("original:", word)

print(word.title())
print(f"{word[0].title()}{word[1:-1]}{word[-1].capitalize()}")
print(word[7:11].replace("b","l"))
print(word[-4:].replace("p","e".capitalize()))
print(f"{word[-3].capitalize()}{word[5].capitalize()}")
print(word.replace(" ","").isalpha())
