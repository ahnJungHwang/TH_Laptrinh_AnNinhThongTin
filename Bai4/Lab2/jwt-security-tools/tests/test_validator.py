import os
from jwt_validator.validator import JWTValidator
import jwt
import datetime

def generate_token(key):
    payload = {"sub": "test", "exp": datetime.datetime.utcnow()
               + datetime.timedelta(minutes=5)}
    return jwt.encode(payload, key, algorithm="HS256")

def test_valid_token():
    valid_key = os.getenv("TEST_VALID_KEY", "secret123")
    token = generate_token(valid_key)
    validator = JWTValidator(valid_key)
    result = validator.validate(token)
    assert result["valid"] is True
    assert result["payload"]["sub"] == "test"

def test_invalid_signature():
    token = generate_token("wrong_signature_key")
    validator = JWTValidator("correct_signature_key")
    result = validator.validate(token)
    assert result["valid"] is False
