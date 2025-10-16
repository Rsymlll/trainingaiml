
class InvalidMarks(Exception):
    pass
def validate_marks(marks):
    if marks<0 or marks>50:
        raise InvalidMarks("Marks should be between 0 and 50")
    else:
        print (f"Valid marks!!! Your {marks} is accepted")