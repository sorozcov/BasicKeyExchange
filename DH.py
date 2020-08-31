#Laboratorio 5
#Implementación Diffie Hellman usando librería

import pyDH
#Se crea las llaves privadas
d1 = pyDH.DiffieHellman()
d2 = pyDH.DiffieHellman()
#Se crea las llaves públicas
d1_pubkey = d1.gen_public_key()
d2_pubkey = d2.gen_public_key()
#Se crea las llaves compartidas
d1_sharedkey = d1.gen_shared_key(d2_pubkey)
d2_sharedkey = d2.gen_shared_key(d1_pubkey)
#Se revisa si es correcta la cominicación
print('Ambas llaves son iguales, es segura la comunicación:')
print(d1_sharedkey == d2_sharedkey)
