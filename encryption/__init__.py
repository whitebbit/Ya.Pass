import os
dir_path = f'{os.environ["APPDATA"]}\\Ya.Pass\\'
bin_path = f'{os.getcwd()}\\bin\\'


def initialize():
    if os.path.exists(dir_path):
        return

    from cryptography.fernet import Fernet
    import rsa

    os.makedirs(dir_path)
    os.makedirs(bin_path)
    public_key, private_key = rsa.newkeys(2048)
    public_name, private_name = Fernet.generate_key().decode(), Fernet.generate_key().decode()

    with open(f"{dir_path}pvt{private_name}.pem", "wb") as file:
        file.write(private_key.save_pkcs1("PEM"))

    with open(f"{bin_path}pub{public_name}.pem", "wb") as file:
        file.write(public_key.save_pkcs1("PEM"))


initialize()
