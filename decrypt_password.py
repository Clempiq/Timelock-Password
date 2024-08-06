from cryptography.fernet import Fernet
import datetime
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)

# Charger la clé
def load_key():
    try:
        return open("secret.key", "rb").read()
    except Exception as e:
        logging.error(f"Erreur lors du chargement de la clé : {e}")
        exit(1)

# Charger la clé maître
def load_master_key():
    try:
        return open("master.key", "rb").read()
    except Exception as e:
        logging.error(f"Erreur lors du chargement de la clé maître : {e}")
        exit(1)

# Déchiffrer le mot de passe
def decrypt_password():
    try:
        key = load_key()
        cipher_suite = Fernet(key)

        with open("mot_de_passe_chiffre.txt", "rb") as file:
            cipher_text = file.read()

        decrypted_password = cipher_suite.decrypt(cipher_text).decode()

        master_key = load_master_key()
        cipher_master = Fernet(master_key)

        with open("unlock_date.txt", "rb") as date_file:
            encrypted_unlock_date = date_file.read()
        
        unlock_date_str = cipher_master.decrypt(encrypted_unlock_date).decode()
        unlock_date = datetime.datetime.fromisoformat(unlock_date_str)

        # Formater la date de déblocage dans le format JJ/MM/AAAA HH:MM:SS
        formatted_unlock_date = unlock_date.strftime("%d/%m/%Y %H:%M:%S")

        if datetime.datetime.now() >= unlock_date:
            logging.info(f"Ton mot de passe est : {decrypted_password}")
        else:
            logging.info(f"Il n'est pas encore temps de déchiffrer le mot de passe. Tu pourras le faire le : {formatted_unlock_date}")
    except Exception as e:
        logging.error(f"Erreur lors du déchiffrement du mot de passe : {e}")
        exit(1)

decrypt_password()
