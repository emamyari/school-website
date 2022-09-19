from .Database import ConnectDb
from model.CallToAction import CallToAction


def DAO():
    rows = ConnectDb('''CallToAction''')
    for row in rows:
        a = CallToAction(row[0], row[1], row[2], row[3])
        # data = a.__dict__
    return a.__dict__
