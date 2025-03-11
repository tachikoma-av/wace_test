from app import create_app, db
import pytest
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.session.remove()
        db.drop_all()

# Тест получения всех сообщений
def test_get_messages(client):
    response = client.get('/messages/')
    assert response.status_code == 200
    assert response.json == []

# Тест создания сообщения
def test_create_message(client):
    response = client.post('/messages/', json={"user_id": 1, "content": "Hello"})
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["content"] == "Hello"

# Тест обновления сообщения
def test_update_message(client):
    # Создаем сообщение
    response = client.post('/messages/', json={"user_id": 1, "content": "Old message"})
    message_id = response.json["id"]
    
    # Обновляем его
    response = client.put(f'/messages/{message_id}', json={"content": "New message"})
    assert response.status_code == 200
    assert response.json["content"] == "New message"

# Тест удаления сообщения
def test_delete_message(client):
    response = client.post('/messages/', json={"user_id": 1, "content": "To delete"})
    message_id = response.json["id"]
    
    response = client.delete(f'/messages/{message_id}')
    assert response.status_code == 200
    assert response.json == {"message": "Deleted successfully"}
    
    response = client.get(f'/messages/{message_id}')
    assert response.status_code == 405

# Тест ошибки при отсутствии данных
def test_create_message_bad_request(client):
    response = client.post('/messages/', json={})
    assert response.status_code == 400