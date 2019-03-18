from src import repository_adapter
import pandas as pd
import numpy as np


def business(y_pred, y_real):

    y_pred['predict'] = y_pred['predict'].apply(lambda x: float(x))
    y_real['value'] = y_real['value'].apply(lambda x: float(x))
    result_df = y_pred['predict'] - y_real['value']

    diff_plus = result_df.where(lambda x: x > 0).dropna()
    diff_minus = result_df.where(lambda x: x < 0).dropna()

    sum_diff_plus = sum(diff_plus)
    sum_diff_minus = sum(diff_minus)
    total_diff = abs(sum_diff_plus + sum_diff_minus)

    sum_real = sum(y_real['value'].values)

    print(total_diff)
    print(sum_real)

    return float(total_diff) / float(sum_real)


def smape(y_true, y_pred):
    y_true_dec = y_true['value'].map(lambda x: float(x))
    y_pred_dec = y_pred['predict'].map(lambda x: float(x))
    smape = np.mean(
        (
                (np.abs(y_pred_dec - y_true_dec) * 200) / (np.abs(y_pred_dec) + np.abs(y_true_dec))
        ).fillna(0)
    )
    print('SMAPE:')
    print(smape)
    return smape


