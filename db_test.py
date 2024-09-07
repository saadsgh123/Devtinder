if __name__ == '__main__':
    from models import storage

    users = storage.all().values()
    for user in users:
        print(user.username)
