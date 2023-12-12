import pymysql


def execute_query(query, params=(), database="ss34_proo", is_insert=False):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database=database,
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)

            if is_insert:
                connection.commit()
                return

            rows = cursor.fetchall()
            return rows
    finally:
        connection.close()
