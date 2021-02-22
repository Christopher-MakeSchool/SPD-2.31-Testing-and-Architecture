# By Kamran Bigdely Nov. 2020
# Replace temp variable with query


class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were received by", self.name + '.')


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa


class School:
    def __init__(self, students) -> None:
        self.students = students
        self.passed_students = []
        self.failed_students = []

    def process_graduation(self, min_gpa):
        # Find the students in the school who have successfully graduated.
        for s in self.students:
            they_passed = s.get_gpa() > min_gpa
            if they_passed:
                self.passed_students.append(s)
            else:
                self.failed_students.append(s)

        self.all_graduates_message()
        self.graduation_emails()
        self.find_employers_for_top10_students()

    def all_graduates_message(self):
        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in self.passed_students:
            print(s.name)
        print('****************************\n')

    def graduation_emails(self):
        # Send congrats emails to them.
        print('*** Send congrats emails to them *** ')
        for s in self.passed_students:
            print("Congrats", s.name + ". You graduated successfully!")
        print('****************************\n')

    def find_employers_for_top10_students(self):
        # Find the top 10% of them and send their contact to the top employers
        print('*** Send their info to employers *** ')
        self.passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(self.passed_students))
        top_10_percent = self.passed_students[index:]
        top_employers = [
            Employer('Microsoft'),
            Employer('Free Software Foundation'),
            Employer('Google')
        ]
        for e in top_employers:
            e.send(top_10_percent)
        print('****************************\n')


if __name__ == "__main__":
    students = [
        Student(2.1, 'Pinocchio'),
        Student(2.3, 'goku'),
        Student(2.7, 'toro'),
        Student(3.9, 'naruto'),
        Student(3.2, 'kami'),
        Student(3, 'guts')
    ]

    school = School(students)
    school.process_graduation(min_gpa=2.5)
