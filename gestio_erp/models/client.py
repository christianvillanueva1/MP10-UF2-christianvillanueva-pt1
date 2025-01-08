class Client:
    def __init__(self, id, name, email, comandes):
        self.id = id
        self.name = name
        self.email = email
        self.comandes = comandes

    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)

    def llistar_comandes(self):
        if len(self.comandes) == 0:
            print(f"El client {self.name} no té cap comanda")
        else:
            print(f"Comandes del client {self.name}: {len(self.comandes)}")


    def __str__(self):
        return f"Client {self.id}: {self.name} ({self.email})"