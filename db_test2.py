# Import storage at the top (if circular dependency is fixed)
from models import storage
from models.Technology import Technology

if __name__ == '__main__':
    from models.User import User

    # Output for creating technologies
    print("=========== Create technologie =============")
    # Example of creating a user and technology (uncomment when ready)
    # user = User(username="saadsgh123", email="saadsgh123@gmail.com", password="saad")
    # tech1 = Technology(name="Python", picture="/static/images/python.png")
    # user.technology.append(tech1)
    # user.save()
    print("=========== END =============\n")

    # Output for adding a list of skills and assigning them to a user
    print("=========== Add a list of skills & assign them to a user =============")
    # Example for adding skills to a user (uncomment when ready)
    # skills = ["Python", "JavaScript", "HTML"]
    # user = User(id="", username="anasaad", email="anasaad@gmail.com", password="saad")
    # for skill in skills:
    #     tech = Technology(name=skill, picture="/static/images/python.png")
    #     user.technology.append(tech)
    # user.save()
    print("=========== END =============\n")

    # Output for getting user skills from the user_tech_table
    print("=========== Get user skills =============")
    tech_user = storage.all(User).values()
    for v in tech_user:
        for tech in v.technology:
            print(v.username, tech.name)
    print("=========== END =============\n")

    print("=========== Get list of skills =============")
    techs = storage.get_all_tech()
    print(f"type: {type(techs)}")
    for tech in techs:
        print(tech.id, tech.name)
    print("=========== END =============\n")

    print("=========== Create new technology =============")
    # tech1 = storage.create_new_technology("js", "")
    # print(tech1.id, tech1.name)
    print("=========== END =============\n")

    print("=========== Search for a tech by name =============")
    tech2 = storage.get_tech_by_name("Python")
    print(tech2.id)
    print("=========== END =============\n")
