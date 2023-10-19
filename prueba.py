import random
import string

def generate_random_strings_file(filename, num_strings):
    with open(filename, 'w') as f:
        for i in range(num_strings):
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            f.write(random_string + '\n')

generate_random_strings_file('random_strings.txt', 1000)