if __name__ == '__main__':
    from models import storage
    print("=========== Get user by its ID =============")
    user = storage.all().values()
    for user in user:
        print(user.id, user.username, user.job_title)
    print(user.username, user.email, user.job_title)
    print("=========== END =============")
    print("=========== Get user by its ID =============")
    user = storage.get_user_by_id(id=1)
    print(user.username, user.email, user.job_title)
    print("=========== END =============")

    print("=========== Get user by its JOB_TITLE =============")
    users = storage.get_users_by_job_title("Data")
    for user in users:
        print(user.username, user.email, user.job_title)
    print("=========== END =============")

