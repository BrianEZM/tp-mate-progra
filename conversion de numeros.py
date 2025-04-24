def decimal_a_binario(numero):
    # Convierte un número decimal a su representación binaria.
    binario=""
    while numero > 0:
        # Obtiene el residuo al dividir por 2 (0 o 1) y lo agrega a la cadena binaria.
        binario= str(numero % 2) + binario
        # Divide el número entre 2 para continuar la conversión.
        numero= numero // 2
    return binario

def decimal_a_octal(numero):
    # Convierte un número decimal a su representación octal.
    octal=""
    while numero > 0:
        # Obtiene el residuo al dividir por 8 y lo agrega a la cadena octal.
        residuo= numero % 8
        octal= str(residuo) + octal
        # Divide el número entre 8 para continuar la conversión.
        numero=int(numero / 8)
    return octal

def obt_caracter(valor):
    # Convierte valores numéricos del 10 al 15 en sus equivalentes hexadecimales.
    valor= str(valor)
    equivalencias= {
        "10":"a",
        "11":"b",
        "12":"c",
        "13":"d",
        "14":"e",
        "15":"f",
        }
    if valor in equivalencias:
        # Retorna la letra correspondiente si el número está en el diccionario.
        return equivalencias[valor]
    else:
        return valor
               
def decimal_a_hexadecimal(numero):
    # Convierte un número decimal a su representación hexadecimal.
    hexadecimal=""
    while numero > 0:
        # Obtiene el residuo al dividir por 16 y lo convierte a su carácter hexadecimal si es necesario.
        residuo= numero % 16
        caracter= obt_caracter(residuo)
        hexadecimal=caracter + hexadecimal
        # Divide el número entre 16 para continuar la conversión.
        numero= int(numero / 16)
    return hexadecimal

# Solicita un número al usuario y lo convierte en diferentes bases.                        
numero=int(input("Ingrese un numero:"))


# Muestra los resultados en binario, octal y hexadecimal.
print(f"el numero {numero} a binario es: {decimal_a_binario(numero)}")
print(f"el numero {numero} a octal es: {decimal_a_octal(numero)}")
print(f"el numero {numero} a hexadecimal es: {decimal_a_hexadecimal(numero)}")














