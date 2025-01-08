class Client:
    # Constructor de la classe Client
    def __init__(self, id, name, email, comandes):
        # Inicialitza els atributs del client: identificador, nom, correu electrònic i llista de comandes
        self.id = id
        self.name = name
        self.email = email
        self.comandes = comandes

    # Mètode per afegir una nova comanda a la llista de comandes del client
    def afegir_comanda(self, comanda):
        self.comandes.append(comanda)

    # Mètode per llistar les comandes del client
    def llistar_comandes(self):
        # Si no hi ha comandes, informa que el client no en té cap
        if len(self.comandes) == 0:
            print(f"El client {self.name} no té cap comanda")
        else:
            # Si hi ha comandes, indica el nombre total
            print(f"Comandes del client {self.name}: {len(self.comandes)}")

    # Mètode especial per retornar una representació del client com una cadena de text
    def __str__(self):
        return f"Client {self.id}: {self.name} ({self.email})"
