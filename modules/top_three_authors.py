from modules import connection
from modules import formatter


def get_authors():
    cursor = connection.get_connection()
    authors = """
        SELECT name, COUNT(path) AS hits
        FROM articles, log, authors
        WHERE log.path = CONCAT('/article/', articles.slug)
        AND articles.author = authors.id
        GROUP BY name
        ORDER BY hits DESC;
    """
    cursor.execute(authors)
    return cursor.fetchall()


def print_authors():
    print("Top Authors:")
    formatter.repeat_separator()
    for item in get_authors():
        print("The total views for the article '" + str(item[6]) +
              "', by the author '" + str(item[0]) +
              "' on the page '" + str(item[0]) +
              "' are " + formatter.format_num(item[0]) + '.')
    formatter.repeat_separator()
