import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
    (User_Id TEXT, First_Name TEXT, Last_Name TEXT, Email_Address TEXT)''')

# connection.commit()
# connection.close()

# cursor.execute("insert into Users values ('1', 'Luke', 'Lopez', 'luke.lopez@gmail.com')")
userAdds = [('2', 'Matt', 'Finkel', 'matt.finks@hotmail.com'),
('3', 'Ang', 'Borikar', 'ang.bobo@gmail.com'),
('4', 'Matan', 'Shamir', 'matan@wiki.com'),
('5', 'Carrie', 'Lyman', 'carrie@lymandesigns.co')]
cursor.executemany('insert into Users Values (?,?,?,?)', userAdds)

users = cursor.execute("select Email_Address from Users")
for user in users:
    print(user)

connection.commit()
connection.close()