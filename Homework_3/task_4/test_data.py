import random
def generate_login():
    login = "user" + str(random.randrange(100))
    return login
def generate_age():
    return random.randrange(100)
def generate_status():
    return random.choice(['ACTIVE', 'BLOCKED', 'INACTIVE'])

def generate_user():
    return {
        'user': generate_login(),
        'age': generate_age(),
        'status': generate_status()
    }