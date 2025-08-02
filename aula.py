vet = []

def par(vet):
    for i in range(len(vet)):
        if vet[i] % 2 == 0:
            return True
    return False
def media(vet):
    media = sum(vet) / len(vet)
    print(f"A media e {media}")
for i in range(10):
    vet.append(int(input("Digite 10 numeros: ")))

par(vet)
media(vet)