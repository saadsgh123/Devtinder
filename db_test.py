if __name__ == '__main__':
    from models import storage

    users = storage.all()
    for k, v in users.items():
        print(k, v)

