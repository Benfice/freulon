# modèle de données pour stocker les informations des cours
class Course:
    def __init__(self, name, link, subjects):
        self.name = name
        self.link = link
        self.subjects = subjects

# liste des cours
courses = [
    Course(
        "CS50's Introduction to Computer Science", 
        "https://www.edx.org/course/cs50s-introduction-to-computer-science", 
        "HTML - CSS - JavaScript - Python - SQL - C"),
    Course(
        "CS50's Web Programming with Python and JavaScript", 
        "https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript", 
        "HTML - CSS - JavaScript - Python - SQL - Django - Git"),
    Course(
        "La Formation Complète Python", 
        "https://www.udemy.com/course/formation-complete-python/", 
        "Python"),
    Course(
        "Python and Flask Bootcamp: Create Websites using Flask!",
        "https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/",
        "HTML - CSS - Bootstrap - Python - SQL - Flask"),
    Course(
        "Django 3 - Full Stack Websites with Python Web Development",
        "https://www.udemy.com/course/django-3-make-websites-with-python-tutorial-beginner-learn-bootstrap/",
        "Python - Django"),
    Course(
        "JavaScript : la formation ULTIME",
        "https://www.udemy.com/course/javascript-la-formation-ultime/",
        "JavaScript"),
    Course(
        "Flutter & Dart - The Complete Guide",
        "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/",
        "Dart - Flutter"
    ),
    Course(
        "The Complete Graphic Design Theory for Beginners Course",
        "https://www.udemy.com/course/graphic-design-theory-for-beginners-course/",
        "Graphic Design"),
    Course(
        "And many other courses on OpenClassRooms",
        "https://openclassrooms.com/",
        "HTML - CCS - JavaScript - Python - Java - PHP - MySQL - Git - Linux - Agile..."
    )
]

# fonction pour afficher les informations d'un cours
def display_course(course):
    return f'<tr><td><a href="{course.link}">{course.name}</a></td><td>{course.subjects}</td></tr>'

# utilisation de la fonction pour afficher chaque cours
courses_html = ''.join(display_course(course) for course in courses)