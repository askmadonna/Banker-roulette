import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person = names[random_choice]
print(f"{person} is going to buy the meal today!")
