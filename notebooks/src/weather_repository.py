from src import repository_adapter
import pandas as pd
import numpy as np


def add_raw_weather_data(date, raw_data, place_id):

    cnx = repository_adapter.connect()
    cursor = cnx.cursor()

    sql = "INSERT IGNORE INTO air.weather (raw_data, place_id, time) VALUES (%s, %s, %s)"
    val = (raw_data, place_id, date)
    cursor.execute(sql, val)
    cnx.commit()

    cursor.close()
    cnx.close()

    return cursor.lastrowid


def add_weather_measure_data(date, row):

    cnx = repository_adapter.connect()
    cursor = cnx.cursor()

    sql = "INSERT IGNORE INTO air.weather_measures (tempF, windspeedKmph, pressure, humidity, cloudcover, time) " \
          "VALUES (%s, %s, %s, %s, %s, %s)"
    val = (row['tempF'], row['windspeedKmph'], row['pressure'], row['humidity'], row['cloudcover'], date)
    cursor.execute(sql, val)
    cnx.commit()

    cursor.close()
    cnx.close()

    return cursor.lastrowid

