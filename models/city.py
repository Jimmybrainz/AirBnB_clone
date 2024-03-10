#!/usr/bin/python3
"""This module creates a City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value arguments
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
