# Vul hier de naam van je programma in:
# test
#
# Vul hier jullie namen in:
# Jur.t.H
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------

