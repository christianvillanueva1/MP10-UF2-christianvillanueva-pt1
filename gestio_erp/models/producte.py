class Producte:
    # Constructor de la classe Producte
    def __init__(self, nom):
        # Inicialitza l'atribut nom amb el nom del producte
        self.nom = nom

    # Mètode especial per retornar una representació en text del producte
    def __str__(self):
        # Retorna el nom del producte com una cadena de text
        return f"{self.nom}"
