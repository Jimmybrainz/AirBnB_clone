#!/usr/bin/python3

'''Command Line Interpreter'''
import cmd
import json
import re
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, args):
        '''Usage: EOF
           Function: Exits the program
        '''
        print()
        return True

    def do_quit(self, args):
        '''Usage: quit
           Function: Exits the program
        '''
        return True

    def do_create(self, args):
        '''Usage: create <class name>
           Function: Creates an instance of the class
        '''
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        obj_instance = storage.classes()[class_name]()
        obj_instance.save()
        print(obj_instance.id)

    def do_show(self, args):
        '''Usage: show <class name> <id>
           Function: Shows the instance details of the class
        '''
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        instance_dict = storage.all()[key]
        print(instance_dict)

    def do_destroy(self, args):
        '''Usage: destroy <class name> <id>
           Function: Deletes the instance of the class
        '''
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        '''Usage: all | all <class name>
           Function: Prints the string representation of all instances
        '''
        instance_list = []

        if args:
            class_name = args.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if key.split('.')[0] == class_name:
                    instance_list.append(str(value))
        else:
            for value in storage.all().values():
                instance_list.append(str(value))

        print(instance_list)

    def do_update(self, args):
        '''Usage: update <class name> <id> <attribute> <value>
           Function: Updates the instance of the class
        '''
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        instance_dict = storage.all()[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3]
        setattr(instance_dict, attribute, value)
        instance_dict.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()