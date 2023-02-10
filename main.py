import datetime
import random
from modeel import *
from slovar import *




def init_v():
    a="Table don't created"
    with db:
        db.drop_tables([CLIENTS,ORDERS])
        db.create_tables([CLIENTS,ORDERS])
        a="Table created"
    return a

    
def fill_v():
    with db:
        clients = [{'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)},
                   {'name':random.choice(a),'city': random.choice(b), 'address':random.choice(c)}]
        CLIENTS.insert_many(clients).execute()
    with db:   
        clients = CLIENTS.select() 
        orders=[{'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)},
                {'client': clients[random.randrange(0,9,1)],'date':datetime.date(random.randrange(2020,2023,1),random.randrange(1,12,1), random.randrange(1,12,1)),'amount': random.randrange(1,30,1),'description':random.choice(v)}]
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

        




    

