if __name__ == '__main__':
    from models import storage

    print("=========== Get user by its ID =============")
    user = storage.get_user_by_id(id=1)
    print(user.username)
    print("=========== END =============")

    print("=========== Get user by its JOB_TITLE =============")
    user = storage.get_users_by_job_title("Full")
    print(user.username)
    print("=========== END =============")
