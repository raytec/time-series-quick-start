import pandas as pd
from sklearn.model_selection import TimeSeriesSplit


def validate(X: pd.DataFrame, y: pd.DataFrame, splits: int, callback):

    tscv = TimeSeriesSplit(n_splits=splits)
    for train_index, test_index in tscv.split(X):
        X_train = pd.DataFrame(X.values[train_index], columns=X.columns.values)
        X_test = pd.DataFrame(X.values[test_index], columns=X.columns.values)
        y_train = pd.DataFrame(y.values[train_index], columns=y.columns.values)
        y_test = pd.DataFrame(y.values[test_index], columns=y.columns.values)

        train_dataset = y_train.join(X_train)
        validation_dataset = y_test.join(X_test)

        callback(X, y, train_dataset, validation_dataset)
