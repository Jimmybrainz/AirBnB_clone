#!/usr/bin/python3

"""Unittest for state.py"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.state import State
from datetime import datetime
from time import sleep


class TestStateClass(unittest.TestCase):
    """Test suite for the State class"""

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))


class TestStateInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the State class"""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_states_different_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_states_different_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        state_str = state.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + dt_repr, state_str)
        self.assertIn("'updated_at': " + dt_repr, state_str)

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSave(unittest.TestCase):
    """Unit tests for testing save method of the State class"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_two_saves(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        state.save()
        self.assertLess(second_updated_at, state.updated_at)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_updates_file(self):
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


class TestStateToDict(unittest.TestCase):
    """Unit tests for testing to_dict method of the State class"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_to_dict_contains_added_attributes(self):
        state = State()
        state.middle_name = "Jimoh"
        state.my_number = 98
        self.assertEqual("Jimoh", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == '__main__':
    unittest.main()