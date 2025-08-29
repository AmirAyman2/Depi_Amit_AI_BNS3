import pandas as pd

# Data Type Functions
def check_data_types(df):
    """Return data types of all columns in DataFrame."""
    return df.dtypes

def convert_column_type(df, column, new_type):
    """Convert the data type of a specific column."""
    df[column] = df[column].astype(new_type)
    return df

# Missing Values Functions
def check_missing_values(df):
    """Return count of missing values in each column."""
    return df.isnull().sum()

def fill_missing_with_mean(df, column):
    """Fill missing values in a column with mean."""
    df[column].fillna(df[column].mean(), inplace=True)
    return df

def fill_missing_with_median(df, column):
    """Fill missing values in a column with median."""
    df[column].fillna(df[column].median(), inplace=True)
    return df

def fill_missing_with_mode(df, column):
    """Fill missing values in a column with mode."""
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)
    return df

def drop_missing_values(df, axis=0):
    """Drop rows (axis=0) or columns (axis=1) with missing values."""
    return df.dropna(axis=axis)
