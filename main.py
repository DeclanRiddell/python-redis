"""
Author - Declan Riddell - 2024
"""

from python_redis import pythonRedis
import pandas as pd

if __name__ == '__main__':
    """Self Explanatory
    """

    pyRed = pythonRedis()
    df = pd.DataFrame()
    pythonRedis.menu(pyRed, df)