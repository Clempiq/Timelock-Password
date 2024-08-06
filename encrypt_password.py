from cryptography.fernet import Fernet
import datetime
import os
import logging
import argparse

# Configuration du logging
logging.basicConfig(level=logging.INFO)

# Générer une clé et l'écrire dans un fichier
try:
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    logging.info("Clé de chiffrement générée et stockée avec succès.")
except Exception as e:
    logging.error(f"Erreur lors de la génération de la clé : {e}")
    exit(1)

# Charger la clé
def load_key():
    try:
        return open("secret.key", "rb").read()
    except Exception as e:
        logging.error(f"Erreur lors du chargement de la clé : {e}")
        exit(1)

# Chiffrer le mot de passe
def encrypt_password(password, days):
    try:
        key = load_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(password.encode())

        # Stocker le mot de passe chiffré dans un fichier
        with open("mot_de_passe_chiffre.txt", "wb") as file:
            file.write(cipher_text)

        # Stocker la date de déblocage dans un fichier, chiffrée avec une autre clé (par exemple, un mot de passe maître)
        unlock_date = datetime.datetime.now() + datetime.timedelta(days=days)
        unlock_date_str = unlock_date.isoformat()
        master_key = Fernet.generate_key()  # Clé maître pour chiffrer la date de déblocage
        cipher_master = Fernet(master_key)
        encrypted_unlock_date = cipher_master.encrypt(unlock_date_str.encode())

        with open("unlock_date.txt", "wb") as date_file:
            date_file.write(encrypted_unlock_date)

        # Stocker la clé maître dans un endroit sûr (potentiellement sur un serveur ou une clé USB que tu caches)
        with open("master.key", "wb") as master_key_file:
            master_key_file.write(master_key)

        logging.info("Mot de passe chiffré et stocké avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors du chiffrement du mot de passe : {e}")
        exit(1)

# Configuration de argparse pour accepter un mot de passe et une durée en jours en argument
parser = argparse.ArgumentParser(description='Chiffre un mot de passe et le stocke de manière sécurisée.')
parser.add_argument('password', type=str, help='Le mot de passe à chiffrer')
parser.add_argument('days', type=int, help='Le nombre de jours de blocage')
args = parser.parse_args()

# Mot de passe à chiffrer et durée de blocage
password = args.password
days = args.days
encrypt_password(password, days)
