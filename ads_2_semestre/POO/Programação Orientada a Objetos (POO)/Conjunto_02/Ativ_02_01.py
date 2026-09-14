def ler_entrada (message, num1, num2):
    while True:
        try:
            entrada = int(input(f"{message}: "))
            if(min(num1, num2)<entrada<max(num1, num2)):
                return entrada;
            else:
                print(f"Você deve digitar um valor inteiro entre o {min(num1, num2)} e o {max(num1, num2)}")
        except ValueError:
            print(f"Você deve digitar um valor inteiro entre o {min(num1, num2)} e o {max(num1, num2)}")
num = ler_entrada("Digite um número", 5, 10)
print("Você digitou:", num)
