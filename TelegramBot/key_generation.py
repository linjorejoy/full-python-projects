# J8aHB8q3OoA0jSupCiR6mTk07IkQ2j8aXtvNSyo2Ugs=
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

pass_from_user = input("Write your password : ")
password = pass_from_user.encode()

my_salt = b'R\x8c!\x05\x1c\x839\xf1\xca\xfc\xfe\xbf\xe8\x8b\xe5\xc7'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=my_salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key.decode())