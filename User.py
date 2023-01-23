class User:
    def __init__(self, username, email, user_id):
        self._username = username
        self._email = email
        self._user_id = user_id

    def get_username(self):
        return self._username

    def get_email(self):
        return self._email

    def get_user_id(self):
        return self._user_id

    def set_username(self, new_username):
        self._username = new_username

    def set_email(self, new_email):
        self._email = new_email
