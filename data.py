import sqlite3

con = sqlite3.connect('employee.db')
cObj = con.cursor()

# cObj.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY , name TEXT, salary REAL, department TEXT, position TEXT)")
# cObj = con.commit()

#Insert Data
cObj.execute("INSERT INTO employees VALUES (1,'Deep',500000,'Python','Developer')")
cObj = con.commit()


con.close()

