divisor = float(input("Coloque o valor do divisor:").strip())
dividendo = float(input("Coloque o valor do dividendo").strip())
print("Este será o resultado da divisão e o resto da divisão:")
print(format(divisor//dividendo, ".4f"))
print(format(divisor % dividendo, ".4f"))