import os

class App:
    def __init__(self, appdata):
        self.name = appdata['name']
        self.order = appdata['order']
        self.macros = appdata['macros']

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
                    print(err)
                    pass

        apps.sort(key=lambda m:m.order)
        return apps
