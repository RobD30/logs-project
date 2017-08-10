import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)

cursor = db.cursor()

top_three_articles = """
    SELECT title, path, count(path) AS hits
    FROM articles, log
    WHERE log.path = concat('/article/', articles.slug)
    GROUP BY title, path
    ORDER BY hits DESC LIMIT 3;
"""
cursor.execute(top_three_articles)

favorite_article = cursor.fetchall()

print(favorite_article)