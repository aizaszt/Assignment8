import sqlite3
from dao import DAO
from employee import Employee

if __name__ =='__main__':

    dao = DAO('employee.sqlite')

    employees = dao.get_all()

    for p in employees:
        print(p)

    p = dao.get_by_id(8)
    print(p)

    p=Employee(id=None, name='Meerim', position='Data Scientist', salary=900000, hire_date='06-02-24')
    id = dao.insert(p)
    p.id = id

    print(p)

    p = Employee(id=18, name='Meerim', position='Data Scientist', salary=900000, hire_date='06-02-24')
    row = dao.update(p)


    print(p, row)

    dao.delete(7)  