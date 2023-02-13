import random
import string

caracters = string.ascii_letters + string.digits + string.punctuation
tamanho_da_senha = 8 #escolher o tamanho da senha

senha = ''
for i in range(tamanho_da_senha):
  senha += random.choice(caracters)
print(senha)
