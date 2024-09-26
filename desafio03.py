# Definindo a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        # Propriedades da classe
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # Método para o ataque
    def atacar(self):
        # Definindo o ataque com base no tipo
        if self.tipo.lower() == "mago":
            ataque = "usou magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "usou espada"
        elif self.tipo.lower() == "monge":
            ataque = "usou artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou ataque padrão"
        
        # Exibindo a mensagem de ataque
        print(f"O {self.tipo} atacou e {ataque}!")

# Criando instâncias da classe Heroi
heroi1 = Heroi("Arthus", 30, "guerreiro")
heroi2 = Heroi("Merlin", 150, "mago")
heroi3 = Heroi("Shinobi", 25, "ninja")
heroi4 = Heroi("Lao", 40, "monge")

# Chamando o método atacar para cada herói
heroi1.atacar()  # O guerreiro atacou e usou espada!
heroi2.atacar()  # O mago atacou e usou magia!
heroi3.atacar()  # O ninja atacou e usou shuriken!
heroi4.atacar()  # O monge atacou e usou artes marcia
