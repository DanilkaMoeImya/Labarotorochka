from main import init_v
import pytest
import modeel
from main import show_c
from main import show_r
import main 

def test_kolc():
    main.fill_v()
    assert show_c()>=10
    
def test_kolr():
    main.fill_v()
    assert show_r()>=10

def test_init_v():
    assert init_v()=="Table created"

def test_clients():
    assert modeel.CLIENTS.name == True
    assert modeel.CLIENTS.city == True
    assert modeel.CLIENTS.address == True

def test_orders(): 
    assert modeel.ORDERS.client == True
    assert modeel.ORDERS.amount ==True
    assert modeel.ORDERS.date == True
    assert modeel.ORDERS.description == True
