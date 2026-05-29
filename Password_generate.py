import random, string
character = string.ascii_letters + string.punctuation + string.digits

passwordnum = int(input("How many numbers do you want?"))
password = "".join(random.choices(character, k= passwordnum))

print(password)