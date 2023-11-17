class Person:
    """Class Person for test autodocstring
    :param name str: Name of person, defaults to \"Jhon\"
    :param name str: Age of person, defaults to 15
    """
    def __init__(self, name="Jhon", age=15):
        self.name = name
        self.age = age
    
    def greet(self):
        """Just say hello
        """
        print("Hello my name is " + self.name)
    
    def run(self, distance):
        """Set a distance and returns if he is tired or not
        :param distance int: Distance in meters
        :return: If tired or not, see also :class:`.Wine`
        :rtype: str
        """
        return "Tired" if distance>20 else "OK"