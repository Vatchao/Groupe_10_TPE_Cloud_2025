import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("Au moins une option de caractères doit être sélectionnée.")
    # ici sa génére le mot de passe de facon aleatoire
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_boolean_input(prompt):
    while True:
        response = input(prompt).lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Erreur ! : veuillez entrer 'y' pour yes ou 'n' pour No.")
#demander les preferences de l'utilisateur 
try:
    print("")
    print("BIENVENUE SUR LE GENERATEUR DE MOT DE PASSE ")
    print("")
    print("#####################################################################")
    length = int(input("Entrez la longueur du mot de passe: "))
    
    use_uppercase = get_boolean_input("Inclure des majuscules ? (y/n): ")
    use_lowercase = get_boolean_input("Inclure des minuscules ? (y/n): ")
    use_digits = get_boolean_input("Inclure des chiffres ? (y/n): ")
    use_special_chars = get_boolean_input("Inclure des caractères spéciaux ? (y/n): ")
    print("#####################################################################")
    print("")
    #ça génére et affiche le mot de passe 
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    print("le Mot de passe généré est :", password)
    print("_____________________________________________________________________")
except ValueError as e:
    print("Erreur:", e)