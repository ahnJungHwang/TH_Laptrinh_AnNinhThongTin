import pytest
from securecrypto import hash_utils
from argon2.exceptions import VerifyMismatchError
from argon2 import PasswordHasher

def test_hash_password_and_verify():
    password = ""
    hashed = hash_utils.hash_password_secure(password)
    assert hashed is not None

    ph = PasswordHasher()
    try:
        ph.verify(hashed, password)
        verified = True
    except VerifyMismatchError:
        verified = False
    assert verified == True

def test_wrong_password_verification():
    password = ""
    wrong_pwd = "wrong"
    hashed = hash_utils.hash_password_secure(password)

    ph = PasswordHasher()
    try:
        ph.verify(hashed, wrong_pwd)
        verified = True
    except VerifyMismatchError:
        verified = False
    assert verified == False
