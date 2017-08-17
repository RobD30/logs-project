from modules import connection
from modules import formatter


def get_top_three_authors():
    cursor = connection.get_connection()
    top_three_authors = """
        SELECT name, author, title, path, COUNT(path) AS hits
        FROM articles, log, authors
        WHERE log.path = CONCAT('/article/', articles.slug)
        AND articles.author = authors.id
        GROUP BY path, title, name, author
        ORDER BY hits DESC;
    """
    cursor.execute(top_three_authors)
    return cursor.fetchall()


def print_top_three_authors():
    print("Top Authors:")
    formatter.repeat_separator()
    for item in get_top_three_authors():
        print("The total views for the article '" + str(item[2]) +
              "', by the author '" + str(item[0]) +
              "' on the page '" + str(item[3]) +
              "' are " + formatter.format_num(item[4]) + '.')
    formatter.repeat_separator()
