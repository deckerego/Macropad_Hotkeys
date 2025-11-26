import os

NAME_DEFAULT = ''
ORDER_DEFAULT = 0
TIMEOUT_DEFAULT = 300
LAUNCH_DEFUALT = None
MACROS_DEFAULT = []

class App:
    def __init__(self, appdata):
        self.name    = appdata['name']    if 'name'    in appdata else NAME_DEFAULT
        self.order   = appdata['order']   if 'order'   in appdata else ORDER_DEFAULT
        self.launch  = appdata['launch']  if 'launch'  in appdata else LAUNCH_DEFUALT
        self.timeout = appdata['timeout'] if 'timeout' in appdata else TIMEOUT_DEFAULT
        self.macros  = appdata['macros']  if 'macros'  in appdata else MACROS_DEFAULT

    @staticmethod
    def load_all(dir):
        apps = []

        try:
            files = os.listdir(dir)
        except OSError as err:
            print(err)
            return apps

        for filename in files:
            if filename.endswith('.py'):
                try:
                    module = __import__(dir + '/' + filename[:-3])
                    apps.append(App(module.app))
                except (SyntaxError, ImportError, AttributeError, KeyError, NameError, IndexError, TypeError) as err:
                    print("Macro Error: ", err)
                    pass

        apps.sort(key=lambda m:m.order)
        return apps
