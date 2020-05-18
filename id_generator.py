import random
import string


def create_id():
    letters_and_digits = string.ascii_letters + string.digits
    id = ''.join(random.choice(letters_and_digits) for i in range(8))
    return id

