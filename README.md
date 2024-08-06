# Timelock Password

Timelock Password est un projet qui fournit un ensemble de scripts pour chiffrer un mot de passe, le stocker en toute sécurité, et le déchiffrer après une période spécifiée. Les scripts utilisent la bibliothèque `cryptography` pour assurer la sécurité du mot de passe.

## Prérequis

- Python 3.x
- Bibliothèque `cryptography`

## Installation

1. Clonez le dépôt ou téléchargez les scripts.
2. Installez les dépendances nécessaires avec pip :

    ```bash
    pip install cryptography
    ```

## Utilisation

### 1. Chiffrement du mot de passe

Le script `encrypt_password.py` permet de chiffrer un mot de passe et de le stocker de manière sécurisée. Vous pouvez spécifier le mot de passe à chiffrer et la durée de blocage en jours via la ligne de commande.

#### Syntaxe

    ```bash
    python encrypt_password.py <votre_mot_de_passe> <nombre_de_jours>
    ```

#### Exemple

    ```bash
    python encrypt_password.py "MonSuperMotDePasse" 10
    ```

#### Description

- Le script génère une clé de chiffrement et la stocke dans le fichier `secret.key`.
- Il chiffre le mot de passe fourni et le stocke dans `mot_de_passe_chiffre.txt`.
- Il génère une clé maître pour chiffrer la date de déblocage, qui est stockée dans `unlock_date.txt`.
- La clé maître est stockée dans `master.key`.
- La date de déblocage est définie pour le nombre de jours spécifié après l'exécution du script.

### 2. Déchiffrement du mot de passe

Le script `decrypt_password.py` permet de déchiffrer le mot de passe chiffré après que la date de déblocage soit atteinte.

#### Syntaxe

    ```bash
    python decrypt_password.py
    ```

#### Description

- Le script charge la clé de chiffrement à partir de `secret.key`.
- Il charge le mot de passe chiffré à partir de `mot_de_passe_chiffre.txt` et le déchiffre.
- Il charge la clé maître à partir de `master.key` et déchiffre la date de déblocage stockée dans `unlock_date.txt`.
- Si la date actuelle est supérieure ou égale à la date de déblocage, le mot de passe est affiché dans les logs.

## Exécution Automatique

### Utilisation de cron (Unix/Linux)

Pour exécuter le script de déchiffrement automatiquement à intervalles réguliers, vous pouvez utiliser cron.

1. Éditez la crontab :

    ```bash
    crontab -e
    ```

2. Ajoutez une ligne pour exécuter le script toutes les minutes :

    ```bash
    * * * * * /usr/bin/python3 /chemin/vers/votre/decrypt_password.py
    ```

### Utilisation du Planificateur de tâches (Windows)

1. Ouvrez le Planificateur de tâches.
2. Créez une nouvelle tâche de base.
3. Configurez-la pour qu'elle s'exécute toutes les minutes et spécifiez le chemin vers votre script Python.

## Sécurité

Assurez-vous de protéger les fichiers contenant les clés (`secret.key`, `master.key`) et les fichiers de données chiffrées (`mot_de_passe_chiffre.txt`, `unlock_date.txt`). Ne les partagez pas et stockez-les dans un endroit sécurisé.

## Auteurs

Ce projet a été réalisé par Clément Piquenet.
