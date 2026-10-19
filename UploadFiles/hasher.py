from os import urandom
from hashlib import sha256, pbkdf2_hmac
from binascii import hexlify


def hash_string(text):
    salt = sha256(urandom(60)).hexdigest().encode('ascii')
    text_hash = pbkdf2_hmac('sha512', text.encode('utf-8'), salt, 100000)
    text_hash = hexlify(text_hash)
    return (salt + text_hash).decode('ascii')


def verify_input(stored_text, provided_text):
    salt = stored_text[:64]
    provided_hash = pbkdf2_hmac('sha512', provided_text.encode('utf-8'), salt.encode('ascii'), 100000)
    provided_hash = hexlify(provided_hash).decode('ascii')
    return provided_hash == stored_text[64:]


