from employee import Employee
import sqlite3

class DAO:

    def __init__(self, database ):
        self.__conn = sqlite3.connect(database)
        self.__cursor = self.__conn.cursor()


    def get_all(self):
        sql = 'SELECT * FROM employee'
        self.__cursor.execute(sql)

        rows = self.__cursor.fetchall()
        employees=[]
        for row in rows:
            p = Employee(id= row[0], name= row[1], position= row[2], salary= row[3], hire_date= row[4])
            employees.append(p)

        return employees


    def get_by_id(self, id):
        sql = '''
               SELECT id, name, position, hire_date
               FROM employee
               WHERE id = ?
           '''
        self.__cursor.execute(sql, (id,))

        row = self.__cursor.fetchone()
        if row :
            employee = Employee( id=row[0], name=row[1], position=row[2],salary=row[3], hire_date=row[4], )
        else:
            employee = None

        return employee

    def insert(self, employee : Employee):

        sql = '''
            INSERT INTO employee(name, position, salary, hire_date)
            VALUES(?, ? , ?, ?) 
        '''
        self.__cursor.execute(sql, (employee.name, employee.position, employee.set_salary(employee.salary), employee.hire_date))
        self.__conn.commit()

        return self.__cursor.lastrowid

    def update(self, employee):

        sql = '''
            UPDATE employee
            SET name = ?, position = ?, hire_date=?
            WHERE id = ?
        '''

        self.__cursor.execute(sql, (employee.name, employee.position, employee.set_salary(employee.salary), employee.hire_date))
        self.__conn.commit()

        return  self.__cursor.rowcount

    def delete(self, id):
        sql = '''
            DELETE FROM employee
            WHERE id = ?
        '''
        self.__cursor.execute(sql,(id,))
        self.__conn.commit()

        return self.__cursor.rowcount
