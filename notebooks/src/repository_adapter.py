from mysql.connector import (connection)
import pandas as pd
import numpy as np


def connect():
    return connection.MySQLConnection(
        user='root',
        password='root',
        host='local.storage.air_data',
        port='3306',
        database='air'
    )


def run_sql(sql, result_fields):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(sql)
    data_set = cursor.fetchall()
    cursor.close()
    cnx.close()

    data_set = pd.DataFrame(
        np.array(data_set).reshape(-1, len(result_fields)),
        columns=result_fields
    )

    return data_set