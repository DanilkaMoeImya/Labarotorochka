import datetime

from modeel import *



def init_v():
    a="Table don't created"
    with db:
        db.drop_tables([CLIENTS,ORDERS])
        db.create_tables([CLIENTS,ORDERS])
        a="Table created"
    return a
    
def fill_v():
    with db:
        clients = [{'name':'Ivan','city': 'Moscow', 'address':'Lenina12'},
                   {'name':'Sergey','city': 'Surgut', 'address':'Gagarina42'},
                   {'name':'Zahar','city': 'Magadan', 'address':'Stalina1'},
                   {'name':'Dima','city': 'Vologda', 'address':'Centralnay12'},
                   {'name':'Vera','city': 'Moscow', 'address':'Lenina12'},
                   {'name':'Vika','city': 'Rostov', 'address':'Tombova45'},
                   {'name':'Rita','city': 'Nyagan', 'address':'Rovnya41'},
                   {'name':'Lena','city': 'Kurgan', 'address':'Lenina22'},
                   {'name':'Slava','city': 'Moscow', 'address':'Stolichnaya12'},
                   {'name':'Danil','city': 'Surgut', 'address':'Lenina82'}]
        CLIENTS.insert_many(clients).execute()
    with db:   
        clients = CLIENTS.select() 
        orders=[{'client': clients[0],'date':datetime.date(2023, 1, 1),'amount': 10000,'description':'Hmmm.'},
                {'client': clients[1],'date':datetime.date(2023, 1, 2),'amount': 23333,'description':'Ughm.'},
                {'client': clients[2],'date':datetime.date(2023, 2, 3),'amount': 14000,'description':'Lol.'},
                {'client': clients[3],'date':datetime.date(2023, 2, 4),'amount': 1111,'description':':d'},
                {'client': clients[4],'date':datetime.date(2023, 1, 5),'amount': 102100,'description':':)'},
                {'client': clients[5],'date':datetime.date(2023, 1, 6),'amount': 12220,'description':'HoHoHo'},
                {'client': clients[6],'date':datetime.date(2023, 2, 1),'amount': 20000,'description':'Yep'},
                {'client': clients[7],'date':datetime.date(2023, 1, 10),'amount': 1100,'description':'Ha'},
                {'client': clients[8],'date':datetime.date(2023, 1, 1),'amount': 800,'description':'H.'},
                {'client': clients[9],'date':datetime.date(2023, 2, 1),'amount': 324,'description':'Hmmm.'}]
        ORDERS.insert_many(orders).execute()
def show_c():
    for client in CLIENTS.select():
        print(client.name,client.city,client.address)
    return CLIENTS.select().count()
def show_r():
    for order in ORDERS.select():
        print(order.client,order.date,order.amount,order.description)
    return ORDERS.select().count()
def vyvod():
    if parametr=="init":
        init_v()
    elif parametr == "fill":
        fill_v()   
    elif parametr == "show clients":
        show_c()    
    elif parametr == "show orders":
        show_r()
if __name__=="__main__":
    print("Insert parametr what you want")
    parametr=input()
    vyvod()

        




    

