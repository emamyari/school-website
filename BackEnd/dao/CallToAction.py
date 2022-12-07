from .Database import ConnectDb
from model.CallToAction import CallToAction


def DAO():
    rows = ConnectDb('''CallToAction''')
    li = []
    for row in rows:
        print(row[0])
        data = CallToAction(row[1], row[2], row[3], row[4])
        data = data.__dict__
        li.append(data)
    return li
