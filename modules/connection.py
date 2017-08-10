import psycopg2


def get_connection():
    db = psycopg2.connect("database=postgres user=postgres password=Hellfreeze1")
    return db.cursor()