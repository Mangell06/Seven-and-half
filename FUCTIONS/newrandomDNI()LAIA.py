import random

def NewRandomDNI():
    """
    Genera un DNI válido español con números aleatorios.
    Devuelve una cadena en formato '12345678A'.
    """
    # Tabla de letras para calcular la letra del DNI
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"

    # Generar un número aleatorio de 8 dígitos
    numero_dni = random.randint(10000000, 99999999)

    # Calcular la letra correspondiente
    indice_letra = numero_dni % 23
    letra_dni = letras_dni[indice_letra]

    # Devolver el DNI completo
    return f"{numero_dni}{letra_dni}"

print(NewRandomDNI())
