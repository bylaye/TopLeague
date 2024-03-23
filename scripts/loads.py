import mysql.connector

"""Connection Server Database"""
def engine_connection(user, password, host='localhost', port=3306):
    cnx = mysql.connector.connect(
        user=user, password=password,
        host=host, port=port
    )
    return cnx


"""Creation Database"""
def create_database(cursor, db_name):
    try:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8' "
        )
        cursor.execute(f'USE {db_name}')
        return db_name
    except mysql.connector.Error as err:
        print(f'Failed creating database {err}')
        exit(1)


def create_table(cursor, tb_name):
    try:
        tb_description = table_description(tb_name)
        cursor.execute(tb_description)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)


def table_description(tb_name):
    return f"""
            CREATE TABLE IF NOT EXISTS {tb_name} 
            (
                `SEASON` CHAR(4), `LEAGUE` CHAR(5), `Date` CHAR(20),
                `HomeTeam` CHAR(50), `AwayTeam` CHAR(50),
                `FTHG` CHAR(5), `FTAG` CHAR(5), `FTR` CHAR(2),
                `HTHG` CHAR(5), `HTAG` CHAR(5), `HTR` CHAR(2),
                `HS` CHAR(5), `AS` CHAR(5), `HST` CHAR(5), `AST` CHAR(5),
                `HF` CHAR(5), `AF` CHAR(5), `HC` CHAR(5), `AC` CHAR(5),
                `HY` CHAR(5), `AY` CHAR(5), `HR` CHAR(5), `AR` CHAR(5),
                PRIMARY KEY (`SEASON`, `LEAGUE`, `HomeTeam`, `AwayTeam`)
            ) ENGINE=InnoDB
        """

def insert_data(cursor, tb_name, val):
    req = f"""
            INSERT INTO {tb_name} 
                (`SEASON`, `LEAGUE`, `Date`,  `HomeTeam`, `AwayTeam`, `FTHG`, `FTAG`, `FTR`, `HTHG`,
                  `HTAG`, `HTR`, `HS`, `AS`, `HST`, `AST`, `HF`, `AF`, `HC`, `AC`, `HY`, `AY`, `HR`, `AR` )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    cursor.executemany(req, val)