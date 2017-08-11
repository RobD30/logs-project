from modules import connection


def get_top_three_authors():
    cursor = connection.get_connection()
    top_three_authors = """
        SELECT
        
    """
    cursor.execute(top_three_authors)
    return cursor.fetchall()


def format_top_three_articles():
    authors = get_top_three_authors()
    # Insert here