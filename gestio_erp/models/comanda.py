from errors import ERRProducteExistent, ERRProducteInexistent

class Comanda:
    ESTATS = ["Enviada", "Pendent"]

    def __init__(self, id_comanda, productes, estat):
        if estat not in self.ESTATS:
            raise ValueError(f"L'estat {estat} no és vàlid. Els estats vàlids són: {self.ESTATS}")
        self.id_comanda = id_comanda
        self.productes = productes
        self.estat = estat

    def afegir_producte(self, producte, quantitat=1):
        if producte in [p[0] for p in self.productes]:
            raise ERRProducteExistent(producte.nom)
            # print(f"El producte {producte} ja existeix a la comanda.")
        else:
            self.productes.append((producte, quantitat))

    def modificar_quantitat_producte(self, producte, quantitat):
        if producte not in [p[0] for p in self.productes]:
            # print(f"El producte {producte} no existeix a la comanda.")
            raise ERRProducteInexistent(producte.nom)
        else:
            for i, p in enumerate(self.productes):
                if p[0] == producte:
                    self.productes[i] = (producte, quantitat)
                    break

    def llistar_productes(self):
        if len(self.productes) == 0:
            print("No hi ha productes")
        else:
            string_prd = ""
            for p in self.productes:
                if p != self.productes[-1]:
                    string_prd += f"{p[0]}: {p[1]}, "
                else:
                    string_prd += f"{p[0]}: {p[1]}"
            print(f"Comanda {self.id_comanda} [{self.estat}]: {string_prd}")

    def modificar_estat(self, estat):
        if estat not in self.ESTATS:
            raise ValueError(f"L'estat {estat} no és vàlid. Els estats vàlids són: {self.ESTATS}")
        self.estat = estat

    def __str__(self):
        return f"Comanda {self.id_comanda} [{self.estat}]"