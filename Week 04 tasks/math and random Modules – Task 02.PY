
import random

Characters = "abcde12345@#$%"

Password = ""

for i in range(8):

    Password += random.choice(Characters)

print("Generated Password:", Password)
