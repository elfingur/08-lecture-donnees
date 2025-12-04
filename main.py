#### Imports et définition des variables globales


"""
Module de lecture et traitement de listes numériques depuis un fichier CSV.
Contient des fonctions pour lire, extraire et analyser des données sous forme de listes d'entiers.
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, 'r', encoding = "utf8") as fichier:
        ligness = fichier.readlines()
        for ligne in ligness :
            element = ligne.strip().split(';')
            ll = []
            for chiffre in element :
                chiffre = chiffre.strip()
                ll.append(int(chiffre))
            l.append(ll)
    return l

def get_list_k(data, k):
    """
    Retourne la k-ième liste du jeu de données.

    Args:
        data (list): Liste de listes d'entiers.
        k (int): Indice de la liste à retourner.

    Returns:
        list: La k-ième liste.
    """
    return data[k]

def get_first(l):
    """
    Retourne le premier élément d'une liste.

    Args:
        l (list): Liste d'entiers.

    Returns:
        int: Le premier élément de la liste.
    """
    return l[0]

def get_last(l):
    """
    Retourne le dernier élément d'une liste.

    Args:
        l (list): Liste d'entiers.

    Returns:
        int: Le dernier élément de la liste.
    """
    return l[-1]

def get_max(l):
    """
    Retourne le maximum d'une liste.

    Args:
        l (list): Liste d'entiers.

    Returns:
        int: Le maximum de la liste.
    """
    return max(l)

def get_min(l):
    """
    Retourne le minimum d'une liste.

    Args:
        l (list): Liste d'entiers.

    Returns:
        int: Le minimum de la liste.
    """
    return min(l)

def get_sum(l):
    """
    Retourne la somme des éléments d'une liste.

    Args:
        l (list): Liste d'entiers.

    Returns:
        int: La somme des éléments de la liste.
    """
    return sum(l)

#### Fonction principale


def main():
    """
    Fonction principale : teste les fonctions de lecture et de traitement des listes.
    """
    data_main = read_data(FILENAME)
    for i, liste in enumerate(data_main):
        print(f"Liste {i}: {liste}")
    k_main = 0
    print(f"Liste {k_main}: {get_list_k(data_main, k_main)}")
    print(f"Premier élément: {get_first(data_main[k_main])}")
    print(f"Dernier élément: {get_last(data_main[k_main])}")
    print(f"Maximum: {get_max(data_main[k_main])}")
    print(f"Minimum: {get_min(data_main[k_main])}")
    print(f"Somme: {get_sum(data_main[k_main])}")




if __name__ == "__main__":
    main()
