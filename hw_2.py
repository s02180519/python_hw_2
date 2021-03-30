class CustomMeta(type):
    def __new__(cls, custom_class_name, custom_class_parents, custom_class_attr):
        new_attributes = {}
        for name, val in custom_class_attr.items():
            if not name.startswith('__'):
                new_attributes["custom_" + name] = val
            else:
                new_attributes[name] = val
        return type(custom_class_name, custom_class_parents, new_attributes)

class CustomClass(metaclass=CustomMeta):
    x = 50

    def line(self):
        return 100
