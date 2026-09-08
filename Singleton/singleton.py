"""
SINGLETON PATTERN

What is Singleton?
- Singleton is a creational design pattern.
- It ensures that a class has only ONE instance.
- It provides a global access point to that instance.

Problem:
- If we create multiple ConfigManager objects,
  each object has its own settings.

    manager = ConfigManager()
    manager.set("name", "mosh")

    other = ConfigManager()
    other.get("name")       # None

- But configuration should usually be shared throughout
  the application.

Solution:
- Prevent normal creation of multiple instances.
- Store one instance inside the class.
- Provide get_instance() to access that shared instance.

In this example:

    ConfigManager.get_instance()

always returns the SAME ConfigManager object.

Key idea:

    One class → One shared instance
"""


class ConfigManager:

    # Shared class variable.
    # Stores the single ConfigManager instance.
    __instance = None

    def __init__(self):
        if ConfigManager.__instance is not None:
            raise RuntimeError(
                "ConfigManager already exists Use ConfigManager.get_instance()")

        ConfigManager.__instance = self
        self.__settings: dict[str, object] = {}

    @staticmethod
    def get_instance():
        if ConfigManager.__instance is None:
            ConfigManager()

        return ConfigManager.__instance

    def set(self, key: str, value: object):
        self.__settings[key] = value

    def get(self, key: str):
        return self.__settings.get(key)


# ==================================================
# MAIN
# ==================================================
if __name__ == "__main__":

    manager = ConfigManager()

    manager.set("name", "mosh")

    # Returns the SAME ConfigManager object.
    other = ConfigManager.get_instance()

    print(other.get("name"))

    # Prove they are the exact same object.
    print(manager is other)
