import csv

header_list = [
    'Div', 'Date', 'HomeTeam', 'AwayTeam', 
    'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 
    'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR'
]


def headers_columns(header_list, header_dataset):
    """
    Associe les index des colonnes d'en-têtes dans le jeu de données.

    Args:
        header_list (list): Liste des en-têtes à rechercher dans le jeu de données.
        header_dataset (list): Liste des en-têtes du jeu de données.

    Returns:
        dict: Un dictionnaire associant chaque en-tête de header_list 
        à son index correspondant dans header_dataset.

    Raises:
        ValueError: Si un en-tête de header_list n'est pas trouvé dans header_dataset.

    Note:
        Cette fonction parcourt les en-têtes de la liste header_list et crée un dictionnaire
        associant chaque en-tête à son index correspondant dans header_dataset, 
        uniquement pour les en-têtes présents dans header_list et header_dataset.
        Si un en-tête de header_list n'est pas trouvé dans header_dataset, une ValueError est levée.
    """
    header_dict = {}
    for header in header_list:
        if header in header_dataset:
            header_dict[header] = header_dataset.index(header)
        else:
            raise ValueError(f'{header} not found in header columns') 
    return header_dict


def extract_fields(csv_file, season):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        dataset = []
        for row in reader:
            # verifier les team name vide
            if len(row[2]) > 1 and len(row[3]) > 1:
                dataset.append(row)
    header_dataset = dataset.pop(0)
    result = []
    h = headers_columns(header_list=header_list, header_dataset=header_dataset)
    for row in dataset:
        r = (
            season, row[h[header_list[0]]], row[h[header_list[1]]], row[h[header_list[2]]], 
            row[h[header_list[3]]], row[h[header_list[4]]], row[h[header_list[5]]],
            row[h[header_list[6]]], row[h[header_list[7]]], row[h[header_list[8]]], 
            row[h[header_list[9]]], row[h[header_list[10]]], row[h[header_list[11]]], 
            row[h[header_list[12]]], row[h[header_list[13]]], row[h[header_list[14]]], 
            row[h[header_list[15]]], row[h[header_list[16]]], row[h[header_list[17]]], 
            row[h[header_list[18]]], row[h[header_list[19]]], row[h[header_list[20]]], 
            row[h[header_list[21]]]
        )
        result.append(r)
    return result
