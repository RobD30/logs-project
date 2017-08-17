from modules import connection
from modules import formatter


def get_top_three_articles():
    cursor = connection.get_connection()
    top_three_articles = ("""
        SELECT title, path, COUNT(path) AS hits, authors.name
        FROM articles
        JOIN authors
        ON articles.author = authors.id
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY title, path, authors.name
        ORDER BY hits DESC LIMIT 3;
    """)
    cursor.execute(top_three_articles)
    return cursor


def print_top_three_articles():
    print("Top articles:")
    formatter.repeat_separator()
    for items in get_top_three_articles():
        print(items)
        print("The total views for the article '" + str(items[0]) +
              "', by the author '" + str(items[3]) +
              "' on the page '" + str(items[1]) +
              "' are " + formatter.format_num(int(items[2])) + '.')
    formatter.repeat_separator()
