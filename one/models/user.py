#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value arguments
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
