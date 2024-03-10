#!/usr/bin/python3
"""This module creates a State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class for managing state objects"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value arguments
        """
        super().__init__(*args, **kwargs)
