from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

mensaje = b"Hola Tadeo, este mensaje sera cifrado y firmado con RSA"

home_path = "../frontend/Home/home.html"

if os.path.exists(home_path):
    home_page = open(home_path).read()
    print(home_page)
else:
    print("Un error ha ocurrido")



