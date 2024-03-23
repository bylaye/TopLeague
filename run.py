import os
import configparser
import scripts.extraction
from scripts.treatement import extract_fields
import scripts.loads as db



path = os.path.abspath(os.path.dirname(__file__))
path_data = os.path.join(path, 'data')


def dirs_storage_data(parent_dir=path_data, name=None):
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
    path_dir = os.path.join(path, 'config')
    filename = os.path.join(path_dir, 'config.ini')
    if os.path.isfile(filename):
        return filename
    else:
        print(f"config file {filename} don't exists")
        exit(1)


if __name__ == '__main__':

    seasons = scripts.extraction.all_seasons()
    leagues = scripts.extraction.leagues

    config_file = check_config_file()
    config = configparser.ConfigParser()
    config.read(config_file)

    db_engine = 'db_mysql'
    db_user = config.get(db_engine, 'USER')
    db_host = config.get(db_engine, 'HOST')
    db_password = config.get(db_engine, 'PASSWORD')
    db_port = config.get(db_engine, 'PORT')
    db_name = config.get(db_engine, 'DB_NAME')
    tb_name = config.get(db_engine, 'TB_NAME')

    cnx = db.engine_connection(db_user, db_password, db_host, db_port)
    cursor = cnx.cursor()
    cnx.database = db.create_database(cursor, db_name)
    db.create_table(cursor, tb_name)

    for season in seasons:
        print(f'Season {season}')
        dir_season = dirs_storage_data(name=season)

        for league in leagues:
            print(f'League {league}')
            data_extracted = scripts.extraction.extract_data(league, season)
            filename = f'{season}_{league}.csv'
            f = os.path.join(dir_season, filename)
            scripts.extraction.store_data(data_extracted, f)
            data = extract_fields(f, season)
            db.insert_data(cursor, tb_name, data)
        cnx.commit()
        print(f'Done Import Season {season}')
    cnx.close()
