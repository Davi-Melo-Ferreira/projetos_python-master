import os
import random

os.system('cls')

# nump = random.randint(-10, 10)
# numg = random.randint(-100, 100)
# num_frc = (f'{nump}/{nump}')
# num_elv = (f'{nump}∧{nump}')
# sinais = ['+', '-', '.', '/'] 
# sinais_alt = random.choice(sinais)
# nums = [nump, numg, num_frc, num_elv]

for i in range(1, 3):
    equacao = 0
    nump = random.randint(-10, 10)
    numg = random.randint(-100, 100)
    num_frc = (f'{nump}/{nump}')
    num_elv = (f'{nump}∧{nump}')
    sinais = ['+', '-', '.', '/'] 
    sinais_alt = random.choice(sinais)
    nums = [nump, numg, num_frc, num_elv]
    nums_alt = random.choice(nums)