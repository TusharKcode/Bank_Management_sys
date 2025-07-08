class Blacklist:
    """Manages blacklisted accounts"""
    blacklisted_users = set()

    @staticmethod
    def add_to_blacklist(username):
        Blacklist.blacklisted_users.add(username)
        print(f"User {username} has been BLACKLISTED due to suspicious activity!")

    @staticmethod
    def is_blacklisted(username):
        return username in Blacklist.blacklisted_users

    @staticmethod
    def remove_from_blacklist(username):
        if username in Blacklist.blacklisted_users:
            Blacklist.blacklisted_users.remove(username)
            print(f"User {username} has been removed from the blacklist.")
        else:
            print(f"User {username} is not blacklisted.")

    @staticmethod
    def view_blacklisted_users():
        if not Blacklist.blacklisted_users:
            print("No users are currently blacklisted.")
        else:
            print("Blacklisted Users:")
            for user in Blacklist.blacklisted_users:
                print(f"- {user}")
