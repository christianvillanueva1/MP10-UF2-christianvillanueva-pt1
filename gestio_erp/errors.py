class ERRProducteExistent(Exception):
    def __init__(self, producte):
        super().__init__(f"El producte {producte} ja existeix a la comanda.")

class ERRProducteInexistent(Exception):
    def __init__(self, producte):
        super().__init__(f"El producte {producte} no existeix a la comanda.")