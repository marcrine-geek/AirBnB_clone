#!/usr/bin/python3
"""the Hbnb console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
