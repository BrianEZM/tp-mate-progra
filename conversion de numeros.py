def decimal_a_binario(numero):
    binario=""
    while numero > 0:
        binario= str(numero % 2) + binario
        numero= numero // 2
    return binario

def decimal_a_octal(numero):
    octal=""
    while numero > 0:
        residuo= numero % 8
        octal= str(residuo) + octal
        numero=int(numero / 8)
    return octal

def obt_caracter(valor):
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
        return equivalencias[valor]
    else:
        return valor
               
def decimal_a_hexadecimal(numero):
    hexadecimal=""
    while numero > 0:
        residuo= numero % 16
        caracter= obt_caracter(residuo)
        hexadecimal=caracter + hexadecimal
        numero= int(numero / 16)
    return hexadecimal
                        
numero=int(input("Ingrese un numero:"))



print(f"el numero {numero} a binario es: {decimal_a_binario(numero)}")
print(f"el numero {numero} a octal es: {decimal_a_octal(numero)}")
print(f"el numero {numero} a hexadecimal es: {decimal_a_hexadecimal(numero)}")














