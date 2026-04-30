from app.core.security import create_access_token

# Mock inicial (laboratório)
FAKE_USER = {
    "username": "admin",
    "password": "123456"
}

def authenticate_user(username: str, password: str):
    if (
        username == FAKE_USER["username"] and
        password == FAKE_USER["password"]
    ):
        return {"sub": username}

    return None


def generate_token(user_data: dict) -> str:
    return create_access_token(user_data)