# Email Impacta: gabriela.abreu@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    for x in range(2, n//2+1):
        if n % x == 0:
            return False
    return True


def lista_primos(n):
    primos = []
    for y in range(2, n):
        if eh_primo(y):
            primos.append(y)

    return primos


def conta_primos(n):
    pass


def eh_armstrong(n):
    pass


def eh_quase_armstrong(n):
    pass


def lista_armstrong(n):
    pass


def eh_perfeito(n):
    pass


def lista_perfeitos(n):
    pass
