class Student:
      grade= 9
      name="Maisha"
      print("Hello I am a student")
      def intro(self):
            print("My name is", self.name)
      def detail(self):
            print("I am in Grade", self.grade)
obj=Student()
obj.intro()
obj.detail()