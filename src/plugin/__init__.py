import os
import sys
import importlib.util

PLUGIN_DIR = os.path.dirname(__file__)

# 添加插件目录到 sys.path
sys.path.insert(0, PLUGIN_DIR)

class Plugins:
    pass

def initialize_plugins():
    for dir_name in os.listdir(PLUGIN_DIR):
        submodule_path = os.path.join(PLUGIN_DIR, dir_name)
        if os.path.isdir(submodule_path):
            submodule = type(dir_name, (object,), {})()
            setattr(Plugins, dir_name, submodule)
            for file in os.listdir(submodule_path):
                if file.endswith('.py') and file.startswith('plugin_'):
                    module_name = f"{dir_name}.{os.path.splitext(file)[0]}"
                    module_path = os.path.join(submodule_path, file)
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for name in dir(module):
                        if not name.startswith('_'):
                            attr = getattr(module, name)
                            if isinstance(attr, type):  # Check if it's a class
                                setattr(submodule, name, attr)

# 在应用初始化时调用 initialize_plugins 方法
initialize_plugins()
