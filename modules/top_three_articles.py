from modules import connection
from modules import formatter


def get_top_three_articles():
    cursor = connection.get_connection()
    top_three_articles = ("""
        SELECT title, path, count(path) AS hits
        FROM articles, log
        WHERE log.path = concat('/article/', articles.slug)
        GROUP BY title, path
        ORDER BY hits DESC LIMIT 3;
    """)
    cursor.execute(top_three_articles)
    return cursor


def print_top_three_articles():
    print("Top articles:")
    formatter.repeat_separator()
    for items in get_top_three_articles():
        print("The total views for the article '" + str(items[2]) +
              "', by the author '" + str(items[3]) +
              "' on the page '" + str(items[1]) +
              "' are " + formatter.format_num(items[0]) + '.')
    formatter.repeat_separator()
