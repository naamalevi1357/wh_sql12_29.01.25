import sqlite3

db_name: str = "wh-29.01.25.db"

conn = sqlite3.connect(db_name)

cursor = conn.cursor()


cursor.execute("""CREATE TABLE garage (fix_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_number TEXT UNIQUE NOT NULL,
    car_problem TEXT NOT NULL,
    fixed BOOLEAN DEFAULT FALSE,
    owner_ph TEXT NOT NULL)""")



cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES
('23', 'Engine overheating after long drives', TRUE, '555-1023') ''');

conn.commit()
cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES
('34', 'Brake pads worn out, needs replacement', TRUE, '555-1034')''');
conn.commit()

cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES
('30', 'Check engine light on, possible sensor issue', TRUE, '555-1030')''')
conn.commit()

cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES
('24', 'Battery drains overnight, needs diagnosis', FALSE, '555-1024')''');
conn.commit()

cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES
('3', 'Strange noise from suspension when turning', FALSE, '555-1003')''')
conn.commit()

# 1:
car_number:int=int(input("what is car number? "))
problem:str=str(input("what is problem? "))
phone_number:str=str(input("what is phon nymber? "))

cursor.execute('INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES (?, ?, 0, ?)',
               (car_number, problem, phone_number))

conn.commit()

# 2:
car_number: int = int(input("what is car number? "))

cursor.execute('SELECT fixed FROM garage WHERE car_number = ?', (car_number,))

result = cursor.fetchone()

# if result:
#     print("The vehicle number is on the list")
# else:
#     print("The vehicle is not in the garage")
#

if result:
    fix_reselt = result[0]

    if fix_reselt == 1:
        print("The treatment is already over")
    else:
        cursor.execute('UPDATE garage SET fixed = 1 WHERE car_number = ?', (car_number,))
        conn.commit()
        print(f"Vehicle care status updated")
else:
    print("The vehicle is not in the garage")

# 3:

car_number: int = int(input("what is car number? "))

cursor.execute('SELECT fixed FROM garage WHERE car_number = ?', (car_number,))

result = cursor.fetchone()
if result:
    fix_reselt = result[0]
    if fix_reselt== 0:
        print("The treatment is not over yet")
    else:
        cursor.execute('SELECT owner_ph FROM garage WHERE car_number = ?', (car_number,))
        conn.commit()
        result1 = cursor.fetchone()
        for i in result1:
            print(tuple(i))
        print(f"The customer must be called to inform them that the vehicle is ready,{i}")
        cursor.execute(' delete from garage where car_number = ?', (car_number,))
        conn.commit()
else:
    print("The vehicle is not in the garage")

# 4:

cursor.execute('SELECT * FROM garage WHERE fixed = ?', (0,))
conn.commit()
result2 = cursor.fetchall()
for i in result2:
    print(tuple(i))



