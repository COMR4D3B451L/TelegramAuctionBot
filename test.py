# write test cases for the api in main.py

def test_api():
    response = requests.get('http://localhost:8000/')
    response.raise_for_status()
    data = response.json()
    assert data['message'] == 'Hello World'
    
def test_api2():
    response = requests.get('http://localhost:8000/users/telegram/123/')
    response.raise_for_status()
    data = response.json()
    assert data['TelegramUserId'] == '123'
    
def test_api3():
    response = requests.get('http://localhost:8000/items/123/')
    response.raise_for_status()
    data = response.json()
    assert data['id'] == '123'
    
def test_api4():
    response = requests.get('http://localhost:8000/users/123/items/')
    response.raise_for_status()
    data = response.json()
    assert data['id'] == '123'
    
    
def test_api5():
    response = requests.get('http://localhost:8000/users/123/')
    response.raise_for_status()
    data = response.json()
    assert data['id'] == '123'
    
def test_api6():
    response = requests.get('http://localhost:8000/users/123/bids/')
    response.raise_for_status()
    data = response.json()
    assert data['id'] == '123'
    
def test_api7():
    response = requests.get('http://localhost:8000/items/123/bids/')
    response.raise_for_status()
    data = response.json()
    assert data['id'] == '123'