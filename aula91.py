# Introdução às Generator functions em Python
#Como dito na aula anterior o Generator sabe pausar, o que é diferente de parar (return)
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # O yield é o que pausa.
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)