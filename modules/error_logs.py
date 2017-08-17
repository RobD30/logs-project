from modules import connection
from modules import formatter


# Bad name, this is not the top three articles
def get_top_three_articles():
    cursor = connection.get_connection()
    # You need to join the logs to the path
    error_reports = """
        SELECT time::DATE,
        SUM (
            CASE WHEN status = '200 OK'
            THEN 1
            ELSE 0
            END) AS success,
        SUM (
            CASE WHEN status  =  '404 NOT FOUND.'
            THEN 1
            ELSE 0
            END) AS error
        FROM log GROUP BY time::DATE;
    """
    cursor.execute(error_reports)
    return cursor.fetchall()


def print_error_logs():
    print("Top articles:")
    formatter.repeat_separator()
    for item in get_top_three_articles():
        pass

    formatter.repeat_separator()
