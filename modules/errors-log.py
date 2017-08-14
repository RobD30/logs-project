from modules import connection
# from modules import formatter


def get_top_three_articles():
    cursor = connection.get_connection()
    error_reports = """
        select time::date,
        SUM (
            CASE WHEN status = '200 OK'
            THEN 1
            ELSE 0
            End) AS success,
        SUM (
            CASE WHEN status  =  
    """
    cursor.execute(error_reports)
    return cursor.fetchall()

# def format_top_three_articles():
#     print("Top articles:")
#     formatter.repeat_separator()
#     for item in get_top_three_articles():
#         print("The total views for the article '" + str(item[2]) +
#               "', by the author '" + str(item[3]) +
#               "' on the page '" + str(item[1]) +
#               "' are " + formatter.format_num(item[0]) + '.')
#     formatter.repeat_separator()
