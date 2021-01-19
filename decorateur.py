from itertools import permutations

def nombreIterationApp(*args, **kwargs):
    print()
    def decorator(func, *param, **param2):
        kwargs['nbApp'] = kwargs['nbApp'] + 1
        # return func(*param, **param2)

    return decorator


@nombreIterationApp(nbApp=1)
def powerset(liste):
    nb = 1
    test = []
    while nb < len(liste)+1:
        test = test + list(permutations(liste, nb))
        nb += 1

    print(test)

