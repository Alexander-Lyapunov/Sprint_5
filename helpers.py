import random
import string


def random_user_name():
    name = (f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}")
    return name

def random_email():
    email = (f"{''.join(random.choice(string.ascii_lowercase) for i in range(9)) + "@gmail.com"}")
    return email

def random_password():
    password = (f"{''.join(random.sample(string.ascii_letters + string.digits, 6))}")
    return password
