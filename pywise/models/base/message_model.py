class GenericMessageModel(dict):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value