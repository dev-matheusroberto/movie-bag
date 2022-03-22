from flask_bcrypt import generate_password_hash, check_password_hash


def hash_password(password):
    return generate_password_hash(password).decode('utf8')


def check_password(password_hash, password):
    return check_password_hash(password_hash, password)
