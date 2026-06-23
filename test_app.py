from app import app

def test_home_page():

    tester=app.test_client()

    responce=tester.get("/")

    assert responce.status_code==200

    assert b"Welcome to flask ci/cd Project" in responce.data
    
