import sqlite3

peopleValues=(('Jean-Baptiste Zorg','Human',122),('Korben Dallas','Meat Popsicle',100),("Ak'not",'Mangalore',-5))

with sqlite3.connect(':memory:') as connection:
    c=connection.cursor()
    c.execute("CREATE TABLE Roster (Name TEXT ,Species TEXT ,IQ INT)")
    c.executemany("INSERT INTO Roster VALUES (?,?,?)",peopleValues)

    c.execute("UPDATE Roster SET Species='Human' WHERE Species='Meat Popsicle'")

    c.execute("SELECT Name,Species,IQ FROM Roster WHERE Species='Human'")
    while True:
        row=c.fetchone()
        if row is None:
            break
        print(row)
               
