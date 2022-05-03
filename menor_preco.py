precos= [1000000, 46000, 16000, 46000, 17000]

atual = 0
maisBarato = 1000000

for n in (precos):
    if n <= maisBarato:
        maisBarato = n
    else:
        pass

print("\nO carro mais barato custa R${}.".format(maisBarato))