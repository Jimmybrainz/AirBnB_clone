#!/usr/bin/python3

'''Command Line Interpreter'''
import cmd
import json
import re
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, *args):
        '''Usage: EOF
           Function: Exits the program
        '''
        print()
        return True

    def do_quit(self, *args):
        '''Usage: quit
           Function: Exits the program
        '''
        # quit()
        return True

    def do_create(self, line):
        '''Usage: 1. create <class name> | 2. <class name>.create()
           Function: Creates an instance of the class
        '''
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                # create an instance of the given class
                obj_instance = storage.classes()[line]()
                obj_instance.save()
                print(obj_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        '''Usage: 1. show <class name> <id> | 2. <class name>.show(<id>)
           Function: Shows the instance details of the class
        '''
        # check if class name and instance id were provided
        if line == "" or line is None:
            print("** class name missing **")

        else:
            # get all the arguments passed via the command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict)

                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        '''Usage: 1. destroy <class name> <id> | 2. <class name>.delete(<id>)
           Function: Deletes the instance of the class
        '''
        # check if class name and instance id were provided
        if line == "" or line is None:
            print("** class name missing **")

        else:
            # get all the arguments passed via the command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        # delete this instance and save to json
                        del storage.all()[key]
                        storage.save()
                        return

                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        '''Usage: 1. all | 2. all <class name> | 3. <class name>.all()
           Function: Prints the string representation of all instances
        '''
        instance_list = []

        if line == "" or line is None:
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)

        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    class_name, instance_id = key.split(".")
                    if line == class_name:
                        instance_list.append(str(value))
                print(instance_list)

    def do_update(self, line):
        '''Usage: 1. update <class name> <id> <attribute> <value> | \
           2. <class name>.update(<id> <attribute> <value>) \
           3. update <class name> <id> <dictionary> \
           4. <class name>.update(<id> <dictionary>) \
           Function: Updates the instance of the class
        '''
        checks = re.search(r"^(\w+)\s([\S]+?)\s({.+?})$", line)
        if checks:
            # it is a dictionary
            class_name = checks.group(1)
            instance_id = checks.group(2)
            update_dict = checks.group(3)

            if class_name is None:
                print("** class name missing **")
            elif instance_id is None:
                print("**class name missing **")
            elif class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                # update the instance with the dictionary
                key = f"{class_name}.{instance_id}"
                if key in storage.all():
                    instance_dict = storage.all()[key]
                    # convert the dictionary string to a dictionary object
                    update_dict = json.loads(update_dict)
                    for attribute, value in update_dict.items():
                        setattr(instance_dict, attribute, value)
                    instance_dict.save()
                else:
                    print("** no instance found **")

        else:
            # it is not a dictionary
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        if len(class_info) < 3:
                            print("** attribute name missing **")
                        elif len(class_info) < 4:
                            print("** value missing **")
                        else:
                            attribute = class_info[2]
                            value = class_info[3]
                            setattr(instance_dict, attribute, value)
                            instance_dict.save()
                else:
                    print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()