from display_time import display_time
import os
with open('./example.txt', 'a') as f:
    f.write(f'The file was created at {display_time()}\n')

    if os.path.exists('./meant-to-remove.txt'):
        os.remove('./meant-to-remove.txt')
