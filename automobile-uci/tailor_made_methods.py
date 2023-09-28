import pandas as pd

def check_missing_values(df):
    """
    Retorna uma lista de tuplas, onde cada tupla contém o nome da coluna e o índice da linha com o valor `True`.

    Args:
        df: O DataFrame a ser verificado.

    Returns:
        Uma lista de tuplas.
    """

    # check for missing values in all columns
    is_missing = pd.isna(df)

    # iterate over columns
    missing_values = []
    for col in is_missing.columns:
        # check if any missing values
        if any(is_missing[col]):
            # add column name and line number with missing value to list
            missing_values.append((col, is_missing[col].idxmin()))

    return missing_values