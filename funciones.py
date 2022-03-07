import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado=[]
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    # (1) anteriormente se cogía clients_list como una lista en vez de un diccionario y se intentaba insertar los datos
    # en la posición igual al nif de la persona, lo cual no tiene mucho sentido
    # (2) he usado el método update para insertar o actualizar en un diccionario nueva información
    clients_list.update({
        nif: {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    })

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    # (1) el error aparece a la hora de añadir cartas al diccionario
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones.update("repeticion"+str(i) : [])
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

cartas_iniciales = ["reina","guardia","asesino","obispo","alguacil","bufon","contable","adulador","baronesa","cardenal"]
combinaciones = repartir_cartas(cartas_iniciales,3)
print(combinaciones)