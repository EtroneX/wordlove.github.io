
from random import seed
import sqlite3

from flask import session

def ajoute(user1,user2):
    db = sqlite3.connect('Wordle/database.db')
    cursor = db.cursor()
    cursor.execute(""" INSERT INTO Amis(user1,user2,demand) VALUES (?,?,'not_accepted') ;""",(user1,user2))
    db.commit()
    db.close()

def liste_amis(user):
    db = sqlite3.connect("Wordle/database.db")
    cursor= db.cursor()
    cursor.execute('''SELECT user1 FROM Amis WHERE user2=? AND demand = "accepted" ''',(user,))
    l1=cursor.fetchall()
    cursor.execute('''SELECT user2 FROM Amis WHERE user1 =? AND demand = "accepted" ''',(user,))
    l2=cursor.fetchall()
    db.close()
    return l1+l2

def liste_amis_attente(user):
    db = sqlite3.connect("Wordle/database.db")
    cursor= db.cursor()
    cursor.execute('''SELECT user2 FROM Amis WHERE user1 =? AND demand = "not_accepted" ''',(user,))
    l2=cursor.fetchall()
    db.close()
    return l2

def liste_demandes(user):
    db = sqlite3.connect('Wordle/database.db')
    cursor = db.cursor()
    cursor.execute(""" SELECT user1 FROM Amis WHERE demand='not_accepted' AND user2=?""",(user,))
    l1=cursor.fetchall()
    db.close()
    return l1

def accept_invit(user1,user2):
    db = sqlite3.connect('Wordle/database.db')
    cursor = db.cursor()
    cursor.execute(""" UPDATE Amis SET demand='accepted' WHERE user1=? AND user2=?;""",(user2,user1))
    cursor.execute("DELETE FROM Amis WHERE user1=? AND user2=?",(user1,user2))
    db.commit()
    db.close()

def refuse_invit(user1,user2):
    db = sqlite3.connect('Wordle/database.db')
    cursor = db.cursor()
    cursor.execute(""" DELETE FROM Amis WHERE user1=? AND user2=?;""",(user2,user1))
    db.commit()
    db.close()

def is_amis(user1,user2):
    db = sqlite3.connect('Wordle/database.db')
    cursor = db.cursor()
    cursor.execute(""" Select * FROM Amis WHERE user1=? AND user2=? AND demand="accepted";""",(user2,user1))
    l=cursor.fetchall()
    if len(l)!=0:
        return True
    cursor.execute(""" Select * FROM Amis WHERE user1=? AND user2=? AND demand="accepted";""",(user1,user2))
    l2=cursor.fetchall()
    if len(l2)!=0:
        return True

    db.commit()
    db.close()
    return False

def is_already_demanded(user1,user2):
    db = sqlite3.connect('Wordle/database.db')
    cursor = db.cursor()
    cursor.execute(""" Select * FROM Amis WHERE user1=? AND user2=? AND demand="not_accepted";""",(user2,user1))
    l=cursor.fetchall()
    if len(l)!=0:
        return True
    cursor.execute(""" Select * FROM Amis WHERE user1=? AND user2=? AND demand="not_accepted";""",(user1,user2))
    l2=cursor.fetchall()
    if len(l2)!=0:
        return True

    db.commit()
    db.close()
    return False