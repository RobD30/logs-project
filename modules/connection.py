import psycopg2


def get_connection(**kwargs):
    dbname = kwargs.get('dbname', 'postgres')
    user = kwargs.get('user', 'postgres')
    password = kwargs.get('password', 'postgres')
    db = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    return db.cursor()
