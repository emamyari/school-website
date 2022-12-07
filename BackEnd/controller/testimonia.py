from dao.Database import ConnectDb
from model.Testimonialdeta import testimonial


def DAO():
    rows = ConnectDb('''testimonial''')
    for row in rows:
        a = testimonial(row[0], row[1], row[2],row[3],row[4])
        # data = a.__dict__
    return a.__dict__
 