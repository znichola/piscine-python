from pandas import DataFrame, read_csv
from urllib.error import HTTPError
import sys


def load(path: str) -> DataFrame | None:
    '''Load csv data from a file, returns a pandas DataFrame'''
    try:
        data = read_csv(path)
        print(f"Loading dataset of dimention {data.shape}")
    except Exception as e:
        if type(e) is FileNotFoundError or type(e) is ValueError:
            print(f"->load_csv.py: {e}", file=sys.stderr)
            return None
        elif type(e) is HTTPError:
            print(f"->load_csv.py: {e} with \"{path}\"", file=sys.stderr)
            return None
        raise
    return data
