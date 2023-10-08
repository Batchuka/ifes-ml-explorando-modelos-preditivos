import pandas as pd
import matplotlib as plt

def busca_registros_faltantes(df):
  """
  Função que encontra os registros de um dataframe que estão com algum valor faltante.

  Args:
    df: Dataframe a ser analisado.

  Returns:
    Dataframe com os registros que estão com algum valor faltante.
  """

  # Verifica se cada valor de uma coluna é um valor faltante.
  isna = df.isna()

  # Verifica se alguma coluna de uma linha contém um valor faltante.
  has_missing_values = isna.any(axis=1)

  # Seleciona as linhas que satisfazem a condição.
  df[has_missing_values]

  return df[has_missing_values]