import database.utils as db
import encryption.cryptography as crypto
import string
import secrets


def add(service, login="", password=""):
    service = create_name(service)
    login = "User" if login == "" else login
    password = generate_password() if password == "" else password
    token = crypto.encrypt(login, password)

    db.add(service, token)
    return service


def get(service):
    service = service.title().strip()
    item = db.get(service)
    data = crypto.decrypt(item.token)
    return data


def edit(service, login, password):
    login = "User" if login == "" else login
    password = generate_password() if password == "" else password
    token = crypto.encrypt(login, password)

    db.edit(service, token)


def create_name(service):
    service = service.title().strip()

    if db.service_exist(service):
        same = db.get_similar(service)
        n = same[-1].service[-1]
        number = int(n) + 1 if n.isdigit() else 1
        service += f" {number}"

    return service


def generate_password(length=15):
    symbols = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    symbols_len = len(symbols)

    password = "".join([symbols[secrets.randbelow(symbols_len)] for _ in range(length)])
    return password
