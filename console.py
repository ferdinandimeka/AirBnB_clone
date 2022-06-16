#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """Interpreter for AirBnB clone"""

    prompt = '(hbnb) '
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review}

    def do_quit(self, line):
        "Quit command to exit the program"

        return True

    def emptyline(self):
        """Skips the line if nothing is entered"""

        pass

    def do_EOF(self, line):
        """Exits the program
        Args:
            line - the user inputted string
        """

        print()
        return True

    def find_class(self, the_class):
        """ Return True if the class is found in the list """
        list_class = ["BaseModel", "User", "Place",
                      "State", "City", "Amenity", "Review"]
        if the_class in list_class:
            return True
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Args:
            line - user input
        """

        if not line:
            print('** class name missing **')
            return
        args = line.split()
        try:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id
        Args:
            line - user input
        """

        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if len(args) == 2:
            if args[0] in self.classes:
                key = args[0] + '.' + args[1]
                rec_of_instances = storage.all()
                if key not in rec_of_instances:
                    print("** no instance found **")
                    return
                else:
                    print(rec_of_instances[key])
                    return
            else:
                print("** class doesn't exist **")
                return
        elif len(args) == 1:
            print("** instance id missing **")
            return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Args:
            line - user input
        """

        rec_of_instances = storage.all()
        if not line or line == "":
            print('** class name missing **')

        args = line.split()
        if len(args) == 2:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
                return
            else:
                del rec_of_instances[key]
                storage.save()

        elif len(args) == 1:
            print('** instance id missing **')
            return

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Args:
            line - user input
        """

        rec_of_instances = storage.all()
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
            else:
                a3 = args[3].strip('\"')
                if hasattr(key, args[2]) is True:
                    attr_type = type(getattr(key, args[2]))
                    if attr_type == int:
                        setattr(rec_of_instances[key], args[2], int(a3))
                        storage.save()
                    elif attr_type == float:
                        setattr(rec_of_instances[key], args[2], float(a3))
                        storage.save()
                else:
                    setattr(rec_of_instances[key], args[2], a3)
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        Args:
            line - user input
        """
        key_list = []
        instances = storage.all()
        if len(line) == 0:
            for v in instances.values():
                key_list.append(v.__str__())
            print(key_list)
            return
        line_list = line.split()
        if line_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for v in instances.values():
            if line_list[0] == v.__class__.__name__:
                key_list.append(v.__str__())
        print(key_list)

    def do_count(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        Args:
            line - user input
        """
        count = 0
        key_list = []
        instances = storage.all()
        if len(line) == 0:
            for v in instances.values():
                count += 1
            print(count)
            return
        line_list = line.split()
        if line_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for v in instances.values():
            if line_list[0] == v.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """
            Handles the case where the the command has no equivlaent
            do_ method
        """
        do_braces_split = False
        line_list = line.split(".")
        check_class = self.find_class(line_list[0])
        if check_class is True:
            if line_list[1] == "all()":
                return self.do_all(line_list[0])
            elif line_list[1] == "count()":
                return self.do_count(line_list[0])
            function = line_list[1].replace(
                "(", " ").replace(")", " ").replace(",", "")
            func_args = shlex.split(function)
            # concatenamos Class_name, espacio, id
            classN_id = line_list[0] + " " + func_args[1]
            if func_args[0] == "show":
                return self.do_show(classN_id)

            elif func_args[0] == "destroy":
                return self.do_destroy(classN_id)

            if func_args[0] == "update":
                if "{" in line_list[1] and "}" in line_list[1]:
                    do_braces_split = True
                if do_braces_split is False:
                    if "{" not in line_list[1] and "}" not in line_list[1]:
                        classN_id_args = classN_id + " " + \
                            "\"" + func_args[2] + "\"" + " " + \
                            "\"" + func_args[3] + "\""
                        print(classN_id_args)
                        return self.do_update(classN_id_args)

                elif do_braces_split:
                    try:
                        func = line_list[1].split("(")[0]
                        idargs = re.compile(
                            "\\(([^)]*)\\)").split(line_list[1])[1]
                        dic_args = re.compile("\\{([^}]*)\\}").split(idargs)[1]
                        dic_ = "{" + dic_args + "}"
                        try:
                            s = eval(dic_)
                            if (type(s) is dict):
                                dic_ = dic_args.replace(
                                    ":", "").replace(",", "")
                                dic_args = shlex.split(dic_)
                                quo = "\""
                                es = " "
                                j = 0
                                for i in range(int(len(dic_args) / 2)):
                                    inp = classN_id + " " + quo + \
                                        dic_args[j] + quo + " " + \
                                        quo + dic_args[j+1] + quo
                                    j = j + 2
                                    print(inp)
                                    self.do_update(inp)
                                return
                        except NameError:
                            Exception("*** Unknown syntax: {}".format(args))
                            return
                    except NameError:
                        Exception("*** Unknown syntax: {}".format(args))
                        return

        print('default({})'.format(line))
        return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
