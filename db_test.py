if __name__ == '__main__':
    from models import storage

    user = storage.get_user_by_id(id=1)
    print(user)


