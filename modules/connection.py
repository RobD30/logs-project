import psycopg2


def get_connection():
    db = psycopg2.connect("dbname=postgres user=postgres password=postgres")
    return db.cursor()