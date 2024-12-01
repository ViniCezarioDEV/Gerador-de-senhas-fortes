import random
import string
from pyperclip import copy
from colorama import init, Fore, Style
init(autoreset=True)
caracters = string.ascii_letters + string.digits + string.punctuation
tamanho_da_senha = int(input(f'{Style.BRIGHT}Lenght of Password: '))

senha = ''
for i in range(tamanho_da_senha):
  senha += random.choice(caracters)
print(f'{Style.BRIGHT}Password: {Style.NORMAL}{senha} {Fore.LIGHTYELLOW_EX}Has been Coppied.')
copy(senha)
input(f'{Style.BRIGHT}ENTER TO CLOSE')