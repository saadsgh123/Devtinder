if __name__ == '__main__':
    from models import storage
    from models.School import School

    print("=========== Get all users =============")
    user = storage.all("User").values()
    for user in user:
        print(user.id, user.username, user.job_title)
    print(user.username, user.email, user.job_title)
    print("=========== END =============")
    print("=========== Get user by its ID =============")
    user = storage.get_user_by_id(id="123e4567-e89b-12d3-a456-426614174001")
    if user:
        print(user.id, user.email, user.job_title)
    else:
        print("doesn't exists")
    print("=========== END =============")

    print("=========== Get user by its JOB_TITLE =============")
    users = storage.get_users_by_job_title("Data")
    for user in users:
        print(user.username, user.email, user.job_title)
    print("=========== END =============")

    print("=========== Get user by its JOB_TITLE =============")
    schools = storage.all("School").values()
    if schools:
        for school in schools:
            print(school.id, school.name)
    else:
        print("doesn't exists")
    print("=========== END =============")


