
# Challange 3 : Implement the complete student class by completing some task...
    # 1. make the class's properties (private),
    # 2. using get & set method to those private properties,
    # 3. implement this class according to the rules of encapsulation,
    # 4. not use the initializers to initialize the properties. 





class student:
    def setStudents_name(self, name):              # using set method
        self.__name = name                        # Implimenting the following properties as private

    def getStudents_name(self):                   # using get method
        return self.__name

    def setRoll_nmbr(self, roll):
        self.__roll = roll

    def getRoll_nmbr(self):
        return self.__roll


sayan = student()                                      # calling the student class into a object



sayan.setStudents_name(name=str(input("type ur name...: ")))
                                                                         # displaying the output And took input from user
sayan.setRoll_nmbr(roll = int(input("type a number..: ")))

print("name is...",sayan.getStudents_name())
print("roll_no is...",sayan.getRoll_nmbr())




