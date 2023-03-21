from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

# Clave secreta de 128 bits en formato hexadecimal
clave_secreta_hex = "5b76d0c8c5d5c4d6239c4cf98b4448e4"
clave_secreta = binascii.unhexlify(clave_secreta_hex)

# Función para cifrar el mensaje en AES-128
def cifrar(mensaje):
    cipher = AES.new(clave_secreta, AES.MODE_ECB)
    mensaje_cifrado = cipher.encrypt(pad(mensaje.encode('utf-8'), AES.block_size))
    return binascii.hexlify(mensaje_cifrado).decode('utf-8')

# Abrimos el archivo para leer el mensaje a cifrar
with open("cifrar.txt", "r", encoding="utf-8") as archivo:
    mensaje = archivo.read().strip()

# Ciframos el mensaje utilizando AES-128
mensaje_cifrado = cifrar(mensaje)

# Imprimimos el mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)