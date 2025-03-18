magic_number = 42

user_number = int(input("Enter a number: "))

if user_number == magic_number:
  print("You found the magic number!")
elif user_number > magic_number:
  print("Too high!")
else:
  print("Too low!")


human_speed_multiplier = 5

user_speed = int(input("Enter your running speed: "))

if user_speed > (human_speed_multiplier * 25):
  print("You're a superhero!")
elif user_speed == (human_speed_multiplier * 25):
  print("You just made it!")
else:
  print("Keep training!")


user_number = int(input("Enter a number: "))

if user_number % 2 == 0:
  print("This is an even number!")
else:
  print("This is an odd number!")
