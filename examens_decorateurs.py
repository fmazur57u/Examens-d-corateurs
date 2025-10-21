from functools import wraps


## Décorateur de Journalisation Simple
def journaliser(fonction):
    def enveloppe1(*args, **kwargs):
        argument = []
        for arg in args:
            argument.append(arg)
        for kwarg in kwargs:
            argument.append(kwarg)
        argument_str = tuple(argument)
        print(f"Appel de {fonction.__name__}{argument_str}")
        resultats = fonction(*args, **kwargs)
        return resultats

    return enveloppe1


@journaliser
def addition(a, b):
    return a + b


print(addition(3, 5))


## Décorateur de Mémorisation (Caching)
def memoriser(fonction):
    cache = {}

    def enveloppe2(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = fonction(*args, **kwargs)
        else:
            print(f"Utilisation directe de {key}")
        return cache[key]

    return enveloppe2


@memoriser
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(20))

# Combinaison de décorateurs


@journaliser
@memoriser
def addition1(a, b):
    return a + b


@memoriser
@journaliser
def addition2(a, b):
    return a + b


print(addition1(3, 5))
print(addition1(3, 5))
print(addition2(3, 5))
print(addition2(3, 5))

# Dans le premier cas on applique d'abords le décorateurs de mémorisation et ensuite la journalisation.
# Donc la premiére fonction à être journaliser ne serat pas addition1 mais l'enveloppe du décorateur de
# mémorisation. Dans l'autre cas, on applique d'abords la journalisation et ensuite la mémorisation et
# donc la journalisation va bien s'appliquer à la fonction addition2. Pour les deux cas la mémorisation
# va correctement fonctionner.
