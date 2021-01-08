class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Books(self.pages + other.pages )

    def __str__(self):
        return str(self.pages)

    def __sub__(self, other):
        return self.pages - other.pages

ob1 = Books(100)
ob2 = Books(200)
ob3 = Books(300)
print(ob1 + ob2 + ob3)
print(ob1 - ob2)
