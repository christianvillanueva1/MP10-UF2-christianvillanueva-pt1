from errors import ERRProducteExistent, ERRProducteInexistent

class Comanda:
    # Constant que defineix els estats possibles d'una comanda
    ESTATS = ["Enviada", "Pendent"]

    def __init__(self, id_comanda, productes, estat):
        # Comprova si l'estat és vàlid en inicialitzar la comanda
        if estat not in self.ESTATS:
            raise ValueError(f"L'estat {estat} no és vàlid. Els estats vàlids són: {self.ESTATS}")
        # Atributs de la comanda: identificador, llista de productes i estat
        self.id_comanda = id_comanda
        self.productes = productes  # Llista de tuples (producte, quantitat)
        self.estat = estat

    # Mètode per afegir un producte a la comanda
    def afegir_producte(self, producte, quantitat=1):
        # Comprova si el producte ja existeix en la comanda
        if producte in [p[0] for p in self.productes]:
            # Si el producte ja hi és, llança una excepció
            raise ERRProducteExistent(producte.nom)
        else:
            # Si no hi és, afegeix el producte amb la quantitat indicada
            self.productes.append((producte, quantitat))

    # Mètode per modificar la quantitat d'un producte existent
    def modificar_quantitat_producte(self, producte, quantitat):
        # Comprova si el producte no existeix en la comanda
        if producte not in [p[0] for p in self.productes]:
            # Si el producte no hi és, llança una excepció
            raise ERRProducteInexistent(producte.nom)
        else:
            # Si hi és, busca el producte i actualitza la seva quantitat
            for i, p in enumerate(self.productes):
                if p[0] == producte:
                    self.productes[i] = (producte, quantitat)
                    break

    # Mètode per llistar tots els productes de la comanda
    def llistar_productes(self):
        # Si no hi ha productes, mostra un missatge indicant-ho
        if len(self.productes) == 0:
            print("No hi ha productes")
        else:
            # Construeix una cadena amb tots els productes i les seves quantitats
            string_prd = ""
            for p in self.productes:
                if p != self.productes[-1]:  # Format per separar amb comes
                    string_prd += f"{p[0]}: {p[1]}, "
                else:
                    string_prd += f"{p[0]}: {p[1]}"
            # Mostra la llista de productes amb l'estat i l'ID de la comanda
            print(f"Comanda {self.id_comanda} [{self.estat}]: {string_prd}")

    # Mètode per modificar l'estat de la comanda
    def modificar_estat(self, estat):
        # Comprova si el nou estat és vàlid
        if estat not in self.ESTATS:
            raise ValueError(f"L'estat {estat} no és vàlid. Els estats vàlids són: {self.ESTATS}")
        # Actualitza l'estat de la comanda
        self.estat = estat

    # Mètode especial per retornar una representació en text de la comanda
    def __str__(self):
        return f"Comanda {self.id_comanda} [{self.estat}]"
