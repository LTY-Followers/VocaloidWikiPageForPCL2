import importlib

def start():
    accessapi = importlib.import_module(".accessapi")
    pagebuilder =importlib.import_module(".pagebuilder")
    RequestImage = importlib.import_module(".RequestImage")