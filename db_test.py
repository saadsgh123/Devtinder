if __name__ == '__main__':
    from models import storage

    users = storage.get_user_by_id(id=1)
    print(type(users))

