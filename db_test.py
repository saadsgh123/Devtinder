

if __name__ == '__main__':
    from models import storage
    from models.School import School
    from models.User import User
    import sys

    print("=========== Get all users =============")
    users = storage.all(User).values()
    for user in users:
        print(user.id, user.username, user.job_title)
    print("=========== END =============")
    print("")
    print("=========== Get user by its ID =============")
    user = storage.get_user_by_id(id="123e4567-e89b-12d3-a456-426614174001")
    if user:
        print(user.id, user.email, user.job_title)
    else:
        print("doesn't exists")
    print("=========== END =============")
    print("")

    print("=========== Get user by its JOB_TITLE =============")
    users = storage.get_users_by_job_title("Data")
    for user in users:
        print(user.username, user.email, user.job_title)
    print("=========== END =============")
    print("")

    print("=========== Get user by its JOB_TITLE =============")
    schools = storage.all(School).values()
    if schools:
        for school in schools:
            print(school.id, school.name)
    else:
        print("doesn't exists")
    print("=========== END =============")
    print("")

    print("=========== Create a New user =============")
    data = {
        "username": "sys.argv[1]",
        "email": "sys.argv[2]",
        "job_title": "sys.argv[3]",
        "password": "sys.argv[4]",
        "country": "sys.argv[5]",
        "city": "sys.argv[6]",
        "Exp": 1
    }
    storage.create_user_profile(data)
    print(user.id, user.email, user.job_title)
    print("=========== END =============")
    print("")



