from fastapi.testclient import TestClient
from main import app

# since the app is already defined in the main file we do not need to recreate another app here
# this is a great lesson here in the way that the apps link into each other dimeji
# take note of this important feature...since it is also the app we want to check
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call / search or /wiki"}
    # put in what should be returned into this for us to make sure that it is returning it


def test_read_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
