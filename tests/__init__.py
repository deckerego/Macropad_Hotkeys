import sys
import commands

sys.path.insert(0,'./lib')

# backwards compatibility for the 2.x series:
sys.modules['keyboard'] = commands
sys.modules['mouse'] = commands
sys.modules['pause'] = commands
sys.modules['sleep'] = commands
sys.modules['midi'] = commands
sys.modules['consumer'] = commands
