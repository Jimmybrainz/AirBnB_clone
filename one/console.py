#!/usr/bin/python3

import cmd
import json
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, args):
        '''Exits the program'''
        print()
        return True

    def do_quit(self, args):
        '''Exits the program'''
        return True

    def do_create(self, args):
        '''Creates an instance of the class'''
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
        '''Shows the instance details of the class'''
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
        '''Deletes the instance of the class'''
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
        '''Prints the string representation of all instances'''
        instance_list = []

        if args:
            class_name = args.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if class_name == key.split('.')[0]:
                    instance_list.append(str(value))
        else:
            for value in storage.all().values():
                instance_list.append(str(value))

        print(instance_list)

    def do_update(self, args):
        '''Updates the instance of the class'''
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
        storage.save()

    def do_count(self, args):
        '''Retrieves the number of instances of a class'''
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        instance_count = sum(1 for key in storage.all() if key.split('.')[0] == class_name)
        print(instance_count)

    def do_get(self, args):
        '''Retrieves an instance based on its ID'''
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

    def do_update_dict(self, args):
        '''Updates theinstance with a dictionary representation'''
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
            print("** dictionary missing **")
            return

        try:
            dictionary = json.loads(args[2].replace("'", "\""))
        except Exception:
            print("** invalid dictionary **")
            return

        for k, v in dictionary.items():
            setattr(instance_dict, k, v)

        storage.save()

    def emptyline(self):
        '''Called when an empty line is entered in response to the prompt'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()