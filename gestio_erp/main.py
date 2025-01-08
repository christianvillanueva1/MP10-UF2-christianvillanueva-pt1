from errors import ERRProducteExistent, ERRProducteInexistent
from models.client import Client
from models.comanda import Comanda
from models.producte import Producte

# Creació d'objectes de tipus Producte
bicicleta = Producte("Bicicleta")
casc = Producte("Casc")
guants = Producte("Guants")
maillot = Producte("Maillot")
roda = Producte("Roda")
pantalons = Producte("Pantalons")
patinet = Producte("Patinet")

# Creació del client Anna amb les seves comandes
anna = Client(1, "Anna", "anna@gmail.com", [])
comanda101 = Comanda(101, [], "Pendent")
comanda102 = Comanda(102, [], "Pendent")
anna.afegir_comanda(comanda101)
anna.afegir_comanda(comanda102)

# Afegir productes a les comandes d'Anna
comanda101.afegir_producte(bicicleta, 1)
comanda101.afegir_producte(casc, 2)
comanda102.afegir_producte(guants, 1)

# Creació del client Pere amb les seves comandes
pere = Client(2, "Pere", "pere@gmail.com", [])
comanda103 = Comanda(103, [], "Pendent")
comanda104 = Comanda(104, [], "Pendent")
pere.afegir_comanda(comanda103)
pere.afegir_comanda(comanda104)

# Afegir productes a les comandes de Pere
comanda103.afegir_producte(maillot, 1)
comanda103.afegir_producte(roda, 2)
comanda104.afegir_producte(guants, 2)

# Creació del client Joan (sense comandes inicials)
joan = Client(3, "Joan", "joan@gmail.com", [])

# Mostrar totes les comandes dels clients
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
if len(joan.comandes) > 0:
    for com in joan.comandes:
        com.llistar_productes()

# Intentar afegir un producte que ja existeix i gestionar l'excepció
try:
    anna.comandes[0].afegir_producte(bicicleta, 1)
except ERRProducteExistent as e:
    print(e)

# Intentar modificar la quantitat d'un producte que no existeix i gestionar l'excepció
try:
    anna.comandes[0].modificar_quantitat_producte(patinet, 2)
except ERRProducteInexistent as e:
    print(e)

# Afegir i modificar productes de forma correcta a la primera comanda d'Anna
anna.comandes[0].afegir_producte(pantalons, 1)
anna.comandes[0].modificar_quantitat_producte(casc, 4)
anna.comandes[0].modificar_estat("Enviada")

# Tornar a mostrar les comandes dels clients després dels canvis
print("COMANDES DELS CLIENTS")
anna.llistar_comandes()
if len(anna.comandes) > 0:
    for com in anna.comandes:
        com.llistar_productes()
