import os
import pandas as pd
import sqlite3

# File Reading Functions
def read_csv(file_path):
    """Read CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def read_excel(file_path, sheet_name=0):
    """Read Excel file into a pandas DataFrame."""
    return pd.read_excel(file_path, sheet_name=sheet_name)

def read_json(file_path, orient="records"):
    """Read JSON file into a pandas DataFrame."""
    return pd.read_json(file_path, orient=orient)

def read_db(db_path, table_name):
    """Read a table from SQLite DB into a pandas DataFrame."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df


# File Saving Functions
def save_csv(df, file_path, index=False):
    """Save DataFrame to CSV file."""
    df.to_csv(file_path, index=index)

def save_excel(df, file_path, sheet_name="Sheet1", index=False):
    """Save DataFrame to Excel file."""
    df.to_excel(file_path, sheet_name=sheet_name, index=index)

def save_json(df, file_path, orient="records"):
    """Save DataFrame to JSON file."""
    df.to_json(file_path, orient=orient)

def save_db(df, db_path, table_name, if_exists="replace", index=False):
    """Save DataFrame to SQLite DB."""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists=if_exists, index=index)
    conn.close()
