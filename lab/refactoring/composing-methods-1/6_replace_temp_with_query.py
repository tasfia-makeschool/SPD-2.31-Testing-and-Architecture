# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    
    def get_and_process_passed_students(self):
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5  # minimum acceptable GPA
        passed_students = []
        print('*** Student who graduated *** ')
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
                # print(s.name)  # print student's name who graduated.
                s.send_congrat_email()
        print('****************************')
        return passed_students

    def get_top_10_percent(self, passed_students):
        # Find the top 10% of students
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        return passed_students[index:]
    
    def send_contact_to_employer(self, top_10_percent):
        # Send top 10% of students their contact to the top employers
        top_employers = [Employer('Microsoft'), Employer(
            'Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

    def process_graduation(self):
        passed_students = self.get_and_process_passed_students()
        top_10_percent = self.get_top_10_percent(passed_students)
        self.send_contact_to_employer(top_10_percent)
        
        
students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'), 
            Student(3.9, 'naruto'), Student(3.2,'kami'), Student(3,'guts')]
school  = School(students)
school.process_graduation()
