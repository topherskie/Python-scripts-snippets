# fetch and insert data using xampp server


import pymysql

con = pymysql.connect(host="localhost", user="root", passwd="", database="ajax_name")
cursor = con.cursor()

email = input('enter email: ')
fname = input('enter firstname: ')
lname = input('enter lastname: ')
msg = input('enter comment: ')

if email != '' and fname != '' and lname != '' and msg != '':
    insert1 = ("INSERT INTO customer_feedback(email, firstname, lastname, messages) VALUES('{}', '{}', '{}','{}');".format(email, fname, lname, msg))
    cursor.execute(insert1)
    print('Successfully added comment!')
else:
    print('Error inserting, some data are missing..')

# queries for retrievint all rows
show_data = "SELECT * FROM customer_feedback"

#executing the quires
cursor.execute(show_data)
rows = cursor.fetchall()
for row in rows:
   print(row)

con.commit()
con.close()
