import os 

class PluginI(object):
    def execute(self):
        raise NotImplementedError("You must implement this method") 
    
class ConvertPluginI(PluginI):
    def execute(self):
        raise NotImplementedError("You must implement this method in ConvertPlugin")
    
class ParsePluginI(PluginI):
    def execute(self):
        raise NotImplementedError("You must implement this method in ParsePlugin")
    
    