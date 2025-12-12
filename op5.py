class Matrix2x2:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __repr__(self):
        return f"Matrix2x2([{self.a11}, {self.a12}]\n          [{self.a21}, {self.a22. Lets do math!!!!}])"

    def __add__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(
                self.a11 + other.a11,
                self.a12 + other.a12,
                self.a21 + other.a21,
                self.a22 + other.a22
            )
        else:
            raise TypeError("This is not a matrix object, cant perform multiplication with it .")


    def __sub__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(
                self.a11 - other.a11,
                self.a12 - other.a12,
                self.a21 - other.a21,
                self.a22 - other.a22
            )
        else:
            raise TypeError("Can't do that. Not matrix objects.")


    def __mul__(self, other):
        if isinstance(other, Matrix2x2):


           
            return Matrix2x2(
                self.a11 * other.a11 + self.a12 * other.a21,
                self.a11 * other.a12 + self.a12 * other.a22,
                self.a21 * other.a11 + self.a22 * other.a21,
                self.a21 * other.a12 + self.a22 * other.a22
            )
        elif isinstance(other, (int, float)):
            return Matrix2x2(
                self.a11 * other,
                self.a12 * other,
                self.a21 * other,
                self.a22 * other
            )
        else:
            raise TypeError("Only int or float!!!!!!!")


    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("it's a zero, bro. i can't do anything with it.")
            return Matrix2x2(
                self.a11 / scalar,
                self.a12 / scalar,
                self.a21 / scalar,
                self.a22 / scalar
            )
        else:
            raise TypeError("int or float.")

    def determinant(self):
        return self.a11 * self.a22 - self.a12 * self.a21

    def transpose(self):
        return Matrix2x2(
            self.a11,
            self.a21,
            self.a12,
            self.a22
        )


