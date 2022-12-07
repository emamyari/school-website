from .Database import ConnectDb
from model.Slider import Slider


def DAO():
    rows = ConnectDb('''CallToAction''')
    for row in rows:
        data = Slider(row[0], row[1], row[2], row[3], row[4], row[5])
        data = data.__dict__
    return data
