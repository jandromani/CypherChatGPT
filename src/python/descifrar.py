from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# Clave secreta de 128 bits en formato hexadecimal
clave_secreta_hex = "5b76d0c8c5d5c4d6239c4cf98b4448e4"
clave_secreta = binascii.unhexlify(clave_secreta_hex)

# Función para descifrar el mensaje cifrado en AES-128
def descifrar(mensaje_cifrado_hex):
    mensaje_cifrado = bytes.fromhex(mensaje_cifrado_hex)
    cipher = AES.new(clave_secreta, AES.MODE_ECB)
    mensaje_descifrado = unpad(cipher.decrypt(mensaje_cifrado), AES.block_size)
    return mensaje_descifrado.decode('utf-8')

# Pedimos al usuario que introduzca el mensaje cifrado en formato hexadecimal
mensaje_cifrado_hex = input("Introduce el mensaje cifrado en formato hexadecimal: ")

# Desciframos el mensaje cifrado utilizando AES-128
mensaje_descifrado = descifrar(mensaje_cifrado_hex)

# Imprimimos el mensaje descifrado
print("Mensaje descifrado:", mensaje_descifrado)