# names = input("Pleas enetr your name: ")
# print(f"\nHello, {names}")
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")
# age = input("How old are you: ")
# age = int(age)
# heigght = input("How tall are you: ")
# heigght = int(heigght)
# if heigght >= 160:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou will be able to ride when you are a little older")
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message =""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")
# current_number = 0
# while current_number < 10:
#     current_number +=1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# unconfirmed_users = ['alica', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print(f"Verifying_users: {current_users.title()}")
#     confirmed_users.append(current_users)
# print("\nThe following users have been confirmed:")
# for confirmed_users in confirmed_users:
#     print(confirmed_users.title())
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")



