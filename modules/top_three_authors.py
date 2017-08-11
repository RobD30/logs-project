from modules import connection


def get_top_three_authors():
    cursor = connection.get_connection()
    top_three_authors = """
        SELECT name, author, title, path, COUNT(path) as hits
        From articles, log, authors
        WHERE log.path = CONCAT('/article/', articles.slug)
        AND articles.author = authors.id
        GROUP BY path, title, name, author
        ORDER BY hits DESC;    
    """
    cursor.execute(top_three_authors)
    return cursor.fetchall()


def format_top_three_articles():
    authors = get_top_three_authors()
    # Insert here