from getpass import getuser

import rsa
import os
from cryptography.fernet import Fernet
from encryption import dir_path, bin_path


def chunks(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]


def get_key(is_private=False):
    path = dir_path if is_private else bin_path
    prefix = "pvt" if is_private else "pub"
    name = [item for item in os.listdir(path) if item.startswith(prefix)][0]
    file_path = path + name

    with open(file_path, "rb") as file:
        key = rsa.PrivateKey.load_pkcs1(file.read()) if is_private else rsa.PublicKey.load_pkcs1(file.read())

    return key


def encrypt(login, password):
    pub_key = get_key()
    username = "|" + getuser() + "|"
    token = login.encode() + username.encode() + password.encode()
    token = rsa.encrypt(token, pub_key)

    return token


def decrypt(token):
    pvt_key = get_key(True)
    username = "|" + getuser() + "|"

    data = rsa.decrypt(token, pvt_key).decode().split(username)
    login = data[0]
    password = data[1]

    return login, password
