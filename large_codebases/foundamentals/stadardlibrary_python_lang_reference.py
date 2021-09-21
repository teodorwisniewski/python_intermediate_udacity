import random

cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"

names = [n.replace("--","") for n in cat_string.split("--, --") ]

random_name = random.choice(names)
print(f'{random_name} is a good kitty.')