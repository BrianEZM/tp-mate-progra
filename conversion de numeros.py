def decimal_a_binario(numero):
    return bin(numero).replace("0b","")

def decimal_a_octal(numero):
    return oct(numero)[2:]
            
def decimal_a_hexadecimal(numero):
    return hex(numero)[2:]
                        
numero=int(input("Ingrese un numero:"))



print(f"el numero {numero} a binario es: {decimal_a_binario(numero)}")
print(f"el numero {numero} a octal es: {decimal_a_octal(numero)}")
print(f"el numero {numero} a hexadecimal es: {decimal_a_hexadecimal(numero)}")














