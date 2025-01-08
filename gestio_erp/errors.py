class ERRProducteExistent(Exception):
    # Classe d'excepció personalitzada per a productes ja existents
    def __init__(self, producte):
        # Crida al constructor de la classe base Exception amb un missatge personalitzat
        super().__init__(f"El producte {producte} ja existeix a la comanda.")

class ERRProducteInexistent(Exception):
    # Classe d'excepció personalitzada per a productes inexistents
    def __init__(self, producte):
        # Crida al constructor de la classe base Exception amb un missatge personalitzat
        super().__init__(f"El producte {producte} no existeix a la comanda.")
