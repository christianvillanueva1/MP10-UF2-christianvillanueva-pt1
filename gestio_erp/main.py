from errors import ERRProducteExistent, ERRProducteInexistent
from models.client import Client
from models.comanda import Comanda
from models.producte import Producte

bicicleta = Producte("Bicicleta")
casc = Producte("Casc")
guants = Producte("Guants")

maillot = Producte("Maillot")
roda = Producte("Roda")
pantalons = Producte("Pantalons")

patinet = Producte("Patinet")

anna = Client(1, "Anna", "anna@gmail.com", [])
comanda101 = Comanda(101, [], "Pendent")
comanda102 = Comanda(102, [], "Pendent")
anna.afegir_comanda(comanda101)
anna.afegir_comanda(comanda102)

comanda101.afegir_producte(bicicleta, 1)
comanda101.afegir_producte(casc, 2)

comanda102.afegir_producte(guants, 1)

pere = Client(2, "Pere", "pere@gmail.com", [])
comanda103 = Comanda(103, [], "Pendent")
comanda104 = Comanda(104, [], "Pendent")

pere.afegir_comanda(comanda103)
pere.afegir_comanda(comanda104)

comanda103.afegir_producte(maillot, 1)
comanda103.afegir_producte(roda, 2)
comanda104.afegir_producte(guants, 2)

joan = Client(3, "Joan", "joan@gmail.com", [])



print("COMANDES DELS CLIENTS")
anna.llistar_comandes()
if len(anna.comandes) > 0:
    for com in anna.comandes:
        com.llistar_productes()
pere.llistar_comandes()
if len(pere.comandes) > 0:
    for com in pere.comandes:
        com.llistar_productes()
joan.llistar_comandes()
if len(pere.comandes) > 0:
    for com in joan.comandes:
        com.llistar_productes()

try:
    anna.comandes[0].afegir_producte(bicicleta, 1)
except ERRProducteExistent as e:
    print(e)

try:
    anna.comandes[0].modificar_quantitat_producte(patinet, 2)
except ERRProducteInexistent as e:
    print(e)



anna.comandes[0].afegir_producte(pantalons, 1)
anna.comandes[0].modificar_quantitat_producte(casc, 4)
anna.comandes[0].modificar_estat("Enviada")
print("COMANDES DELS CLIENTS")
anna.llistar_comandes()
if len(anna.comandes) > 0:
    for com in anna.comandes:
        com.llistar_productes()

