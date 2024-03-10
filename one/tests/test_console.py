#!/usr/bin/python3

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHelpCommand(unittest.TestCase):
    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        expected_output = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
        self.assertEqual(expected_output, f.getvalue())


class TestQuitCommand(unittest.TestCase):
    def test_do_quit(self):
        """Tests the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        expected_output = ""
        self.assertEqual(expected_output, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        self.assertEqual(expected_output, f.getvalue())


class TestEOFCommand(unittest.TestCase):
    def test_do_EOF(self):
        """Tests the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        expected_output = "\n"
        self.assertEqual(expected_output, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        self.assertEqual(expected_output, f.getvalue())


class TestEmptyLineCommand(unittest.TestCase):
    def test_do_emptyline(self):
        """Tests the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        expected_output = ""
        self.assertEqual(expected_output, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                     \n")
        self.assertEqual(expected_output, f.getvalue())


if __name__ == "__main__":
    unittest.main()