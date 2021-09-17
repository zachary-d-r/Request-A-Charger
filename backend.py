import Student
import Verification

#student = Student.student('output.txt')
#print(f'{student.studentID} {student.email} {student.name}')

test = Verification.verification('jfdg', 'dfvsd')
test.getVerificationCode()
print(test.verification)

# Verification stuff: