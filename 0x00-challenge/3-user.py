#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """


    def __init__(self):
        """
        Initialize a new user:
        - assigned an unique `id`
        """
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - `None` if `pwd` is `None`
        - `None` if `pwd` is not a string
        - Hash `pwd` in MD5 before assign to `__password`
        """
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Valid password:
        - `False` if `pwd` is `None`
        - `False` if `pwd` is not a string
        - `False` if `__password` is `None`
        - Compare `__password` and the MD5 value of `pwd`
        """
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password


if __name__ == '__main__':
    user_1 = User()
    assert user_1.id is not None

    user_2 = User()
    assert user_1.id != user_2.id

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password is not None
    assert user_2.password is None

    user_2.password = None
    assert user_2.password is None

    user_2.password = 89
    assert user_2.password is None

    assert user_1.is_valid_password(u_pwd)
    assert not user_1.is_valid_password("Fakepwd")
    assert not user_1.is_valid_password(None)
    assert not user_1.is_valid_password(89)
    assert not user_2.is_valid_password("No pwd")
