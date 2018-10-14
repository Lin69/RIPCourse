from lab_python_oop.Rectangle import Rect
from lab_python_oop.Squar import Squar
from lab_python_oop.Circle import Circle

if __name__ == "__main__":
    myrect = Rect(2,3, "Blue")
    mysquere = Squar(5, "Red")
    mycircle = Circle(5, "Green")

    print(myrect.repr())
    print(mysquere.repr())
    print(mycircle.repr())