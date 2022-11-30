from .Database import ConnectDb
from model.CallToAction import CallToAction


def DAO():
    rows = ConnectDb('''CallToAction''')
    for row in rows:
        data = CallToAction(row[0], row[1], row[2], row[3])
        data = data.__dict__
    return data
