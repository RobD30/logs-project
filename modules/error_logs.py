from modules import connection
from modules import formatter

def main():
    print_error_logs()


def get_status_log():
    cursor = connection.get_connection()
    # You need to join the logs to the path
    error_reports = """
        WITH t AS (
        SELECT time::DATE AS time,
        SUM (
            CASE WHEN status = '200 OK'
            THEN 1
            ELSE 0
            END) AS success,
        SUM (
            CASE WHEN status  =  '404 NOT FOUND'
            THEN 1
            ELSE 0
            END) AS error,
            log.path
        FROM log JOIN authors
        on log.path
        GROUP BY time::DATE, path)
        SELECT t.time, t.error, t.path, t.success
        FROM t
        JOIN articles
        ON t.path =
        CONCAT('/article/', articles.slug);
    """
    cursor.execute(error_reports)
    return cursor.fetchall()


def print_error_logs():
    print("Errors:")
    formatter.repeat_separator()
    for item in get_status_log():
        pass

    formatter.repeat_separator()

if __name__ == '__main__':
    main()