from services.decimal.decimal_converter import obt_caracter
# Esta función verifica si una cadena es un número binario válido, permitiendo opcionalmente un signo negativo.
def es_binario(numero_str):
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '01' for c in numero_str)

#Esta función convierte un número binario (como cadena) a su valor decimal correspondiente.
def binario_decimal(binario):
    i = len(binario) - 1
    j = 0
    decimal = 0
    while i >= 0:
        decimal = decimal + int(binario[i]) * (2 ** j)
        i -= 1
        j += 1
    return decimal

# Esta función convierte un número decimal a su representación octal (base 8).
def binario_octal(decimal):
    dividendo = decimal
    num_octal = ''
    while dividendo > 0:
        residuo = dividendo % 8
        num_octal = str(residuo) + num_octal
        dividendo = dividendo // 8
    return num_octal

    
# Esta función convierte un número decimal a su representación hexadecimal (base 16).
def binario_Hexa(decimal):
    dividendo = decimal
    num_hexa = ''
    while dividendo > 0:
        residuo = dividendo % 16
        caracter=obt_caracter(residuo)
        num_hexa = caracter + num_hexa
        dividendo = int(dividendo // 16)
    return num_hexa
