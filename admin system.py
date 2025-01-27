class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._admin_access_level = 'admin'

    def get_admin_access_level(self):
        return self._admin_access_level

    def add_user(self, user_list, user):
        if user not in user_list:
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print(f"Пользователь {user.get_name()} уже существует.")

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"Пользователь {user.get_name()} удален.")
        else:
            print(f"Пользователь {user.get_name()} не найден.")

if __name__ == "__main__":
    user1 = User(1, "Алиска")
    user2 = User(2, "Егорка")

    admin = Admin(3, "Костик")

    users = []

    admin.add_user(users, user1)
    admin.add_user(users, user2)
    admin.add_user(users, user1)
    admin.remove_user(users, user1)
    admin.remove_user(users, user1)