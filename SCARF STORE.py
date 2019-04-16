import sqlite3
import datetime

now = datetime.datetime.now()

conn = sqlite3.connect('test.db')

def mainUI():
    print("--------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------")
    print("--w        w       w  eeeeee  ll        ccccccc    ooooo        m       m     eeeeee--")
    print("-- w      w w     w   ee      ll       ccccc     oo     oo     m m     m m    ee    --")
    print("--  w    w   w   w    eeeeee  ll      ccc       oo       oo   m   m   m   m   eeeeee--")
    print("--   w  w     w w     ee      ll       ccccc     oo     oo   m     m m     m  ee    --")
    print("--     w       w      eeeeee  lllllll   ccccccc    ooooo    m       m       m eeeeee--")
    print("--------------------------------------------------------------------------------------")
    print("--    sssss   ccccccc     aaa     rrrrr     fffffff                                 --")
    print("--   ss     ccccc        aa aa    rr   rr   ff                                      --")
    print("--  ssssss  ccc         aa   aa   rrrrrr    fffff                                   --")
    print("--      ss  ccccc      aaaaaaaaa  rr   rr   ff                                      --")
    print("--  sssss    ccccccc  aa       aa rr    rr  ff                                      --")
    print("--------------------------------------------------------------------------------------")
    print("--                                        sssss tttttt    ooooo    rrrrr    eeeeee  --")
    print("--                                       ss       tt    oo     oo  rr   rr  ee      --")
    print("--                                      ssssss    tt   oo       oo rrrrrr   eeeeee  --")
    print("--                                          ss    tt    oo     oo  rr   rr  ee      --")
    print("--                                      sssss     tt      ooooo    rr    rr eeeeee  --")
    print("--------------------------------------------------------------------------------------")
    print("--                            Connected and Ready To Go                             --")
    print("--------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------")

def closingUI():
    print("--------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------")
    print("--          gggggg      ooooo       ooooo    ddddd   bbbb    yy    yy eeeeee        --")
    print("--         gg         oo     oo   oo     oo  d    d  b   b    yy  yy  ee            --")
    print("--        gg    ggg  oo       oo oo       oo d     d bbbbb     yyyy   eeeeee        --")
    print("--        gg     gg   oo     oo   oo     oo  d    d  b    b     yy    ee            --")
    print("--         ggggggg      ooooo       ooooo    ddddd   bbbbbb     yy    eeeeee        --")
    print("--------------------------------------------------------------------------------------")
    print("--                            Disconnected, Bye Bye :D                              --")
    print("--------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------")

n=0

def logIn(n):
    while (n!=1):
        holds = conn.execute("SELECT username, password,status from LOGIN")
        print("\nPlease login before continue\n")
        username = input("enter username : ")
        password = input("enter password : ")
        for row in holds:
            if (username == row[0] and password == row[1]):
                print("login successful")
                name2=row[0]
                status=row[2]
                if(status.lower() == "staff"):
                    anss="yes"
                    while(anss.lower() == "yes" or anss.lower() == "y"):
                        selection3=int(input("1-Transaction 2-Add Member 3-Change Password : "))
                        if(selection3 == 1):
                            ans="yes"
                            while(ans.lower() == "yes" or ans.lower() == "y"):
                                calculatePrice(name2, status)
                                ans=input("New Customer ? yes or no ? : ")
                        elif(selection3 == 2):
                            addMember()
                        elif(selection3 == 3):
                            updatePassword()
                        anss = input("Next Customer ? yes or no ? : ")
                if(status.lower() == "admin"):
                    ansss = "yes"
                    while (ansss.lower() == "yes" or ansss.lower() == "y"):
                        selection=int(input("Choose task 1-Approve Member 2-Add New Staff 3-View Staff 4-Remove Staff 5-Remove Member : "))
                        if (selection == 1):
                            viewMember()
                            selection2=input("Continue ? yes or no ?")
                            if(selection2.lower()=="yes" or selection2.lower()=="y"):
                                rota="yes"
                                while(rota.lower() == "yes" or rota.lower() == "y"):
                                    appMember()
                                    rota=input("approve next member ? yes or no ?")
                        elif(selection == 2):
                            addStaff()
                        elif(selection == 3):
                            viewStaff()
                        elif (selection == 4):
                            removeStaff()
                        elif (selection == 5):
                            removeMember()
                        ansss=input("Other Task ? Yes or no ? :")
                n=1
                break
            elif (username != row[0] and password == row[1]):
                pass
            elif (username == row[0] and password != row[1]):
                pass
        if (n == 0):
            print("No user data found, check your username and password")

def calculatePrice(name2,status):
    holdw = conn.execute("SELECT id,status from MEMBER")
    data = []
    dataon = []
    newprice = 0
    discounted = 0
    priceB = 0
    priceN = 0
    priceF = 0
    priceD = 0
    priceaddon = 0
    quantityaddon = 0
    nodata = ""
    answer = "yes"
    addon = "yes"
    add = "yes"
    print("WELCOME",status.upper(),name2.upper())
    print("#---------------------------------------------------#")
    print("|                                                   |")
    print("|               CATALAOG SCARF STORE                |")
    print("|                                                   |")
    print("#---------------------------------------------------#")
    print("| CODENAME  | NAME                      | PRICE(RM) |")
    print("| aidijuma  | AIDIJUMA HIJAB            | 40.00     |")
    print("| lofahijab | NEELOFA HIJAB             | 80.00     |")
    print("| fareeda   | FAREEDA HIJAB             | 100.00    |")
    print("| duck      | dUck SCARF                | 130.00    |")
    print("|___________|___________________________|___________|")
    name = input("Enter Name : ")
    data.append(name)
    ic = input("Enter the IC number: ")
    id = int(input("Enter ID : "))
    data.append(ic)
    count = 1
    countadd = 1
    while (answer.lower() == "yes" or answer.lower() == "y"):
        brand = input("Enter type of tudung : ")
        data.append(brand)
        if brand.lower() == "aidijuma":
            print("Colours Avaiable")
            print("- choco lava")
            print("- grey sky morning")
            print("- coldplay")
            print("- butterfingers")
            colours = input("Enter colours : ")
            data.append(colours)
            quantity = int(input("Enter the quantity of Aidijuma Hijab : "))
            data.append(quantity)
            price = quantity * 40
            priceB += price

        elif brand.lower() == "lofahijab":
            print("Colours Avaiable")
            print("- choco lava")
            print("- grey sky morning")
            print("- coldplay")
            print("- butterfingers")
            colours = input("Enter colours : ")
            data.append(colours)
            quantity = int(input("Enter the quantity of Neelofa Hijab : "))
            data.append(quantity)
            price = quantity * 80
            priceN = price + priceN
        elif brand.lower() == "fareeda":
            print("Colours Avaiable")
            print("- choco lava")
            print("- grey sky morning")
            print("- coldplay")
            print("- butterfingers")
            colours = input("Enter colours : ")
            data.append(colours)
            quantity = int(input("Enter the quantity of Fareeda Hijab : "))
            data.append(quantity)
            price = quantity * 100
            priceF = price + priceF
        elif brand.lower() == "duck":
            print("Colours Avaiable")
            print("- choco lava")
            print("- grey sky morning")
            print("- coldplay")
            print("- butterfingers")
            colours = input("Enter colours : ")
            data.append(colours)
            quantity = int(input("Enter the quantity of dUck Scarf : "))
            data.append(quantity)
            price = quantity * 130
            priceD = price + priceD
        answer = input("Do you still want to shopping with us ? : ")
        if (answer.lower() == "yes" or answer.lower() == "y"):
            count += 1
    else:
        newprice += priceB + priceN + priceD + priceF
    addon = input("Do you want to add on? :")
    if (addon.lower() == "yes" or addon.lower() == "y"):
        print("masuk")
        add = "yes"
        while (add.lower() == "yes" or add.lower() == "y"):
            print("*---------------------------*")
            print("|         ADD-ON LIST       |")
            print("*---------------------------*")
            print("| -> Inner Scarf            |")
            print("| -> Brooch                 |")
            print("| -> Handsock               |")
            print("| -> Crystal                |")
            print("|___________________________|")
            tambahan = input("Enter add-on : ")
            dataon.append(tambahan)
            quantityaddon = int(input("Enter quantity of your addon : "))
            dataon.append(quantityaddon)
            priceaddon = (quantityaddon * 5) + priceaddon
            dataon.append(priceaddon)
            add = input("Do you want to buy add-on again")
            if (add == "yes"):
                countadd += 1
        newprice = newprice + priceaddon
        for rotate in holdw:
            if(id == rotate[0]):
                discounted = newprice - (newprice * 0.1)
            else:
                discounted = newprice
        data.append(newprice)
        data.append(discounted)
        print("*------------------------------------*\n")
        print("|                                    |\n")
        print("|       WELCOME TO SCARF STORE       |\n")
        print("|                                    |\n")
        print("*------------------------------------*\n")
        print(now.strftime("%Y-%m-%d %H:%M %p\n"))
        print("STAFF     : %s\n" % name2)
        print("NAME      : %s\n" % data[0])
        print("IC NUMBER : %s \n" % data[1])
        n = 2
        for row in range(0, count):
            print("BRAND     : %s \n" % data[n])
            print("COLOURS   : %s \n" % data[n + 1])
            print("QUANTITY  : %s \n" % data[n + 2])
            n += 3
        i = 0
        for hehe in range(0, countadd):
            print("ACCESSORIES(RM5) : %s \n" % dataon[i])
            print("QUANTITY OF ACCESSORIES :%s \n" % dataon[i + 1])
            i += 2
        print("TOTAL PRICE OF ACCESSORIES : %s \n" % dataon[i])
        print("TOTAL PRICE : %s \n" % data[n])
        print("AFTER DISCOUNT : %s \n" % data[n+1])

        file = open(ic + '.txt', 'a')
        file.write("*------------------------------------*\n")
        file.write("|                                    |\n")
        file.write("|       WELCOME TO SCARF STORE       |\n")
        file.write("|                                    |\n")
        file.write("*------------------------------------*\n")
        file.write(now.strftime("%Y-%m-%d %H:%M %p\n"))
        file.write("STAFF     : %s\n" % name2)
        file.write("NAME      : %s\n" % data[0])
        file.write("IC NUMBER : %s \n" % data[1])
        n = 2
        for row in range(0, count):
            file.write("BRAND     : %s \n" % data[n])
            file.write("COLOURS   : %s \n" % data[n + 1])
            file.write("QUANTITY  : %s \n" % data[n + 2])
            n += 3
        i = 0
        for hehe in range(0, countadd):
            file.write("ACCESSORIES(RM5) : %s \n" % dataon[i])
            file.write("QUANTITY OF ACCESSORIES :%s \n" % dataon[i + 1])
            i += 2
        file.write("TOTAL PRICE OF ACCESSORIES : %s \n" % dataon[i])
        file.write("TOTAL PRICE : %s \n" % data[n])
        file.write("AFTER DISCOUNT : %s \n" % data[n + 1])
        file.close()
    else:
        dataon.append(nodata)
        data.append(newprice)
        for rotate in holdw:
            if(id == rotate[0]):
                discounted = newprice - (newprice * 0.1)
            else:
                discounted = newprice
        data.append(discounted)
        print("*------------------------------------*\n")
        print("|                                    |\n")
        print("|       WELCOME TO SCARF STORE       |\n")
        print("|                                    |\n")
        print("*------------------------------------*\n")
        print(now.strftime("%Y-%m-%d %H:%M %p\n"))
        print("STAFF     : %s\n" % name2)
        print("NAME      : %s\n" % data[0])
        print("IC NUMBER : %s \n" % data[1])
        n = 2
        for row in range(0, count):
            print("BRAND     : %s \n" % data[n])
            print("COLOURS   : %s \n" % data[n + 1])
            print("QUANTITY  : %s \n" % data[n + 2])
            n += 3
        print("ACCESSORIES(RM5) : %s \n" % dataon[0])
        print("QUANTITY OF ACCESSORIES :%s \n" % dataon[0])
        print("TOTAL PRICE OF ACCESSORIES : %s \n" % dataon[0])
        print("TOTAL PRICE : %s \n" % data[n])
        print("AFTER DISCOUNT : %s \n" % data[n + 1])

        file = open(ic + '.txt', 'a')
        file.write("*------------------------------------*\n")
        file.write("|                                    |\n")
        file.write("|       WELCOME TO SCARF STORE       |\n")
        file.write("|                                    |\n")
        file.write("*------------------------------------*\n")
        file.write(now.strftime("%Y-%m-%d %H:%M %p\n"))
        file.write("STAFF     : %s\n" % name2)
        file.write("NAME      : %s\n" % data[0])
        file.write("IC NUMBER : %s \n" % data[1])
        n = 2
        for row in range(0, count):
            file.write("BRAND     : %s \n" % data[n])
            file.write("COLOURS   : %s \n" % data[n + 1])
            file.write("QUANTITY  : %s \n" % data[n + 2])
            n += 3
        file.write("ACCESSORIES(RM5) : %s \n" % dataon[0])
        file.write("QUANTITY OF ACCESSORIES :%s \n" % dataon[0])
        file.write("TOTAL PRICE OF ACCESSORIES : %s \n" % dataon[0])
        file.write("TOTAL PRICE : %s \n" % data[n])
        file.write("AFTER DISCOUNT : %s \n" % data[n + 1])
        file.close()


def viewMember():

    cursor = conn.execute("SELECT id, name, age, address, status from MEMBER")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("AGE = ", row[2])
        print("ADDRESS = ", row[3])
        print("STATUS = ", row[4], "\n")

def viewStaff():

    cursor2 = conn.execute("SELECT username, status from LOGIN")
    for row2 in cursor2:
        print("ID = ", row2[0])
        print("STATUS = ", row2[1], "\n")

def appMember():

    approve = conn.execute("SELECT id, status from MEMBER")
    id=int(input("Enter ID"))
    statuss="Approve"
    conn.execute('''UPDATE MEMBER SET STATUS = ? WHERE id = ? ''',(statuss, id))
    conn.commit()

def updatePassword():
    usern=input("Enter Staff Name : ")
    passww=input("Enter New Password : ")
    conn.execute('''UPDATE LOGIN SET PASSWORD = ? WHERE USERNAME = ? ''',(passww,usern))
    conn.commit()

def addMember():

    memID=int(input("Enter ID : "))
    memName=input("Enter Name : ")
    memAge=int(input("Enter Age : "))
    memAddress=input("Enter Address : ")
    memStatus="Pending"
    conn.execute("INSERT INTO MEMBER (ID,NAME,AGE,ADDRESS,STATUS) VALUES (?, ?, ?, ?, ?)",(memID,memName,memAge,memAddress,memStatus))
    conn.commit()

def addStaff():
    staName = input("Enter Name : ")
    staPassword = input("Enter Password : ")
    staStatus = "staff"
    conn.execute("INSERT INTO LOGIN (username,password,status) VALUES (?, ?, ?)",
                 (staName,staPassword, staStatus))
    conn.commit()

def removeMember():

    id3=int(input("Enter Member Id : "))
    conn.execute('DELETE FROM MEMBER WHERE id=?', (id3,))
    conn.commit()

def removeStaff():

    name3 = input("Enter Staff Name : ")
    conn.execute('DELETE FROM LOGIN WHERE username=?', (name3,))
    conn.commit()

mainUI()
logIn(n)
conn.close()
closingUI()