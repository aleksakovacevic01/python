# def greet_user():
#     print("Hello!")
# greet_user()
# def greet_user(username):
#     print(f"\nHello, {username.title()}")
# greet_user('Jesse')
# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie')
# def get_formatted_name(firste_name, last_name):
#     full_name = f"{firste_name} {last_name}"
#     print(full_name)
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# get_formatted_name('jimi', 'hendrix')
# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)
# def get_formatted_name(first_name, last_name, middle_name):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{fist_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return (person['first'])
# musician = build_person('jimi', 'hendrix')
# print(musician)
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me ypur name:")
#     f_name=input("First name: ")
#     l_name=input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\n{formatted_name}")
