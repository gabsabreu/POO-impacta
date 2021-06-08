class Ignicao():
    def ligar(self):
        return "Veiculo ligado"

    def desligar(self):
        return "Veiculo desligado"


class Frenagem():
    def brecar(self):
        return "Acionar todos os freios"


class Aceleracao():
    def velocidade(self):
        return "acelerando veiculo"

    def diminuir_velocidade(self):
        return "diminuindo velocidade do veiculo"


class Veiculo(Ignicao, Frenagem):
    def buzinar(self):
        return "Buzinando"

    def brecar(self):
        return "acionando freio dianteiro"


class VeiculoDois(Ignicao, Frenagem, Aceleracao):
    def brecar(self):
        return super().brecar()


Fusca = Veiculo()

print("Fusca", Fusca.ligar(), Fusca.buzinar())

Gol = VeiculoDois()

print(Gol.desligar(), Gol.brecar(), Gol.velocidade())
