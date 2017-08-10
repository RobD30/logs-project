from modules import connection


def get_top_three_articles():
    cursor = connection.get_connection()
    top_three_articles = """
        SELECT title, path, count(path) AS hits
        FROM articles, log
        WHERE log.path = concat('/article/', articles.slug)
        GROUP BY title, path
        ORDER BY hits DESC LIMIT 3;
    """
    cursor.execute(top_three_articles)
    return cursor.fetchall()


def format_top_three_articles():
    articles = get_top_three_articles()
    # Insert here
