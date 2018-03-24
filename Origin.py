from origin import oparser


class OriginError(Exception):
    pass


class CLI(object):
    def __init__(self, name, prompt, version):
        self.name = name
        self.prompt = prompt
        self.version = version
        self.custom_intro = False
        self.cintro = ""
        self.commands = {}
        self.command_help = {}
        self.add_command("help", self.get_help)
        self.add_help("help", "Displays help about command. If no argument is specified, print all.")
        self.add_command("exit",lambda code: exit(code))
        self.add_help("exit", "Exits the program with code <CODE>")

    def parse(self, command, arg):
        parsed_command = oparser.parse(command, self)
        if parsed_command != 'err':
            parsed_command(arg)
        else:
            print("Command Not Recognized")

    def add_command(self, name, func):
        setattr(self, name, func)
        self.commands[name] = True

    def del_command(self, name):
        delattr(self, name)
        self.commands[name] = None

    def add_help(self, name, help):
        self.command_help[name] = help

    def get_help(self,arg):
        if arg == "":
            for cmd in self.commands:
                print(cmd)
        else:
            try:
                print(self.command_help[arg])
            except KeyError:
                print("help not found!")

    def intro(self, intro):
        self.custom_intro = True
        self.cintro = intro

    def loop(self):
        if not self.custom_intro:
            print("{n} V{v}".format(n=self.name, v=self.version))
        else:
            print(self.cintro)
        done = False
        while not done:
            user_input = input(self.prompt)
            nui = user_input.split()
            cmd = nui[0]
            nui.pop(0)
            arg = " ".join(nui)
            try:
                self.parse(cmd, arg)
            except IndexError:
                self.parse(nui[0], "")


def create(name, prompt, version):
    return CLI(name, prompt, version)
