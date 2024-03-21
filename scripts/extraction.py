import configparser
import os
import requests
from datetime import date, datetime


absolute_dir_path_file = os.path.abspath(os.path.dirname(__file__))
leagues = {
    'E0': 'Premier League',
    'I1': 'Seria A Italienne',
    'SP1': 'La Ligua Espagnole',
    'D1': 'Bundesliga Allemande',
    'F1': 'Ligue 1 France'
}
LIMIT_SEASON = 2007


def absolute_path_directory_data(parent_dir, name):
    """
    Creer et retourner le chemin absolu du répertoire de stockage.

    Args:
        parent_dir (str): Le chemin absolu du répertoire parent où le répertoire de stockage sera créé.
        name (str): Le nom du répertoire de stockage à créer.

    Returns:
        str: Le chemin absolu du répertoire de stockage.

    Note:
        Cette fonction prend en entrée le chemin absolu du répertoire parent 
        et le nom du répertoire de stockage à créer.
        Si le répertoire de stockage n'existe pas, il sera cree.
        Le chemin absolu du répertoire de stockage est retourné.
    """
    path_dir = os.path.join(parent_dir, name)
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)
    return os.path.abspath(path_dir)


def check_config_file():
    """
    Vérifie si le fichier de configuration existe. 
    Ce fichier stocke le variable repertoire de stockage des donnees

    Returns:
        str: Le chemin absolu du fichier de configuration s'il existe.

    Note:
        Cette fonction vérifie l'existence du fichier 
        de configuration 'config.ini' dans le répertoire 'config' spécifié.
        Si le fichier existe, le chemin absolu du fichier est renvoyé.
        Si le fichier n'existe pas, un message d'erreur est affiché 
        et le programme s'arrête avec un code de sortie non nul.
    """
    path_dir = os.path.join(absolute_dir_path_file, 'config')
    filename = os.path.join(path_dir, 'config.ini')
    if os.path.isfile(filename):
        return filename
    else:
        print(f"config file {filename} don't exists")
        exit(1)


def seasons(number_season=1):
    """
    Genere un list de saison en fonction du nombre de saison specifie
    
    Args:
        number_season (int, optional): Le nombre de saisons à générer. Par défaut, une seule saison est générée.
    
    Returns:
        list: Une liste de saisons de football, représentées sous forme d'années. 
        Chaque élément de la liste est une chaîne de caractères représentant une saison, 
        sous la forme "YYYY" (par exemple, "2021" pour la saison 2020-2021).
    
    Note:
        La fonction génère les saisons en fonction de l'année actuelle et des années précédentes, 
        en utilisant l'année actuelle et l'année précédente pour chaque saison. 
        Si le nombre de saisons spécifié est supérieur au nombre d'années écoulées 
        depuis l'année limite (définie par la constante LIMIT_SEASON), 
        la fonction avertit l'utilisateur que le nombre de saisons générées est limité par l'année limite. 
        Par exemple, si LIMIT_SEASON est définie sur 2010, et que le nombre de saisons demandé est de 15, 
        la fonction ne générera que des saisons à partir de 2010.

    Example:
        >>> seasons()
        ['2324']
        >>> seasons(3)
        ['2324', '2223', '2122']
        >>> seasons(20)
        WARNING: Limit season league year = 2007
        ['2324', '2223', '2122', '2021', '1920', '1819', '1718', '1617', '1516', 
        '1415', '1314', '1213', '1112', '1011', '0910', '0809', '0708']
    """

    current_year = date.today().year
    if (current_year - number_season) < LIMIT_SEASON:
        number_season = current_year - LIMIT_SEASON
        print(f'WARNING: Limit season league year = {LIMIT_SEASON}')
    seasons = []
    for i in range(number_season):
        year_before = current_year-1
        season = str(year_before)[2:] + str(current_year)[2:]
        seasons.append(season)
        current_year -= 1
    return seasons


def extract_data(league, season):
    """
    Télécharge les resultats des matchs par saison par ligue.

    Args:
        league (str): Le nom de la ligue pour laquelle les données doivent être extraites.
        season (str): La saison pour laquelle les données doivent être extraites.

    Returns:
        bytes: Les données des résultats des matchs téléchargées sous forme de contenu brut
        None: si une erreur survient.

    Note:
        Cette fonction télécharge les résultats des matchs 
        pour une ligue et une saison spécifiees a partir de l'URL
        Les données téléchargées sont renvoyées sous forme de contenu brut (bytes).
    """

    url = "https://www.football-data.co.uk/mmz4281"
    full_url = os.path.join(url, season, league)
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(e)
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)


def store_data(data, filename):
    """
    Stocke les données dans un fichier.

    Args:
        data (bytes): Les données à stocker, sous forme de contenu brut (bytes).
        filename (str): Le nom du fichier dans lequel les données seront stockees.

    Note:
        Cette fonction prend en entrée les données à stocker 
        et le nom du fichier dans lequel les données seront enregistrees.
        Les données sont enregistrées dans le fichier spécifié.
        Si une erreur survient lors de l'ouverture ou de l'écriture du fichier, l'erreur est affichee.
    """
    try:
        with open(filename, 'wb') as f:
            f.write(data)
    except IOError as err:
        print(err)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    
    config_file = check_config_file()
    config = configparser.ConfigParser()
    config.read(config_file)

    dirname_data = config.get('dirs', 'DIRNAME_DATA_EXTRACT')
    dir_data_extract = absolute_path_directory_data(absolute_dir_path_file, dirname_data)
    
    all_season = date.today().year - LIMIT_SEASON
    seasons = seasons(all_season)

    for season in seasons:
        count_league = 0
        print(f'Season {season}')
        start_extract_season = datetime.now()
        
        for league in leagues:
            count_league += 1
            start_extract_league = datetime.now()
            data = extract_data(league=league, season=season)
            d = absolute_path_directory_data(dir_data_extract, season)
            filename = os.path.join(d, season+'_'+league+'.csv' )
            store_data(data=data, filename=filename)
            
            time_league_extract = (datetime.now() - start_extract_league).total_seconds()
            print(f'Done {count_league}/{len(leagues)} : League {leagues[league]}, t = {time_league_extract} sec')
        
        time_season_extract = (datetime.now() - start_extract_season).total_seconds()
        print(f'Done Extraction Season {season} after {time_season_extract} seconds')