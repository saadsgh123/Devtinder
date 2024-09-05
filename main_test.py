from models import storage

if __name__ == '__main__':
    users = storage.all().values()
    users = list(users)
    print(users[0].job_title)

