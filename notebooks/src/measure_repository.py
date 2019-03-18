from src import repository_adapter
import pandas as pd
import numpy as np


def get_measures(metering_point_id, date_from, date_to):

    query = """SELECT DISTINCT
                        result as value,            
                        date
                FROM air.air_quality_measures
                WHERE date >= '%s' and date <= '%s'
                AND metering_point_id = %s
                ORDER BY date ASC;
                """ % (date_from, date_to, metering_point_id)

    return repository_adapter.run_sql(
        query,
        [
            "value",
            "date"
        ]
    )



