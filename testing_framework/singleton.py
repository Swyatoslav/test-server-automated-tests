from typing import TypeVar

T = TypeVar("T")


def singleton(my_class: T) -> T:
    """decorator for a class to make a singleton out of it"""

    class_instances = {}

    def get_instance(*args, **kwargs):
        """Creating or just return the one and only class instance.
        The singleton depends on the parameters used in __init__"""

        key = (my_class, args, str(kwargs))
        if key not in class_instances:
            class_instances[key] = my_class(*args, **kwargs)
        return class_instances[key]

    return get_instance
