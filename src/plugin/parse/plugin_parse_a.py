from plugin.base import ParsePluginI

class ParseB(ParsePluginI):
    def execute(self):
        print("Parse B executed")
        
        
class ParseA(ParsePluginI):
    def execute(self):
        print("Parse A executed")