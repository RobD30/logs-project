from modules import connection
from modules import formatter


def main():
    print_error_logs()
# Super duper radical change incoming

def get_status_log():
    cursor = connection.get_connection()
    error_reports = """
        WITH t AS
        (SELECT DATE(log.time) AS failureDate,
        ROUND((SUM(CASE WHEN
            SUBSTRING(log.status, 0, 4)::INTEGER >= 400
            THEN 1
            ELSE 0
            END
        )  * 100.0)::DECIMAL /
        (COUNT(log.status)), 1) AS totalFailures
        FROM log GROUP BY DATE(log.time)
        )
    SELECT CONCAT(t.totalFailures, '%') AS failure,
    TO_CHAR(t.failureDate, 'Month DD, YYYY') AS date
    FROM t
    GROUP BY t.totalFailures, t.failureDate
    HAVING t.totalFailures > 1;
    """
    cursor.execute(error_reports)
    return cursor.fetchall()


def print_error_logs():
    print("Errors:")
    formatter.repeat_separator()
    for item in get_status_log():
        print(item)
        print("The total errors for the date '" + str(item[1]) +
              "' are " + str(item[0]))
    formatter.repeat_separator()


if __name__ == '__main__':
    print_error_logs()
