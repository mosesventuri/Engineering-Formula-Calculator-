import math

class MathEngine:
    """
    Pure Python Mathematical Engine for Engineering Math Calculations.
    Handles input validation and error checking (e.g., division by zero).
    """

    @staticmethod
    def matrix_add(m1, m2):
        """
        Adds two 2x2 matrices.
        m1, m2: lists of lists, e.g., [[a, b], [c, d]]
        """
        result = [
            [m1[0][0] + m2[0][0], m1[0][1] + m2[0][1]],
            [m1[1][0] + m2[1][0], m1[1][1] + m2[1][1]]
        ]
        return result

    @staticmethod
    def matrix_multiply(m1, m2):
        """
        Multiplies two 2x2 matrices.
        """
        res_00 = (m1[0][0] * m2[0][0]) + (m1[0][1] * m2[1][0])
        res_01 = (m1[0][0] * m2[0][1]) + (m1[0][1] * m2[1][1])
        res_10 = (m1[1][0] * m2[0][0]) + (m1[1][1] * m2[1][0])
        res_11 = (m1[1][0] * m2[0][1]) + (m1[1][1] * m2[1][1])
        return [[res_00, res_01], [res_10, res_11]]

    @staticmethod
    def matrix_determinant(m):
        """
        Calculates determinant of a 2x2 matrix: ad - bc.
        """
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return det

    @staticmethod
    def matrix_inverse(m):
        """
        Calculates inverse of a 2x2 matrix.
        Raises ValueError if determinant is zero.
        """
        det = MathEngine.matrix_determinant(m)
        if det == 0:
            raise ValueError("Inverse does not exist! Determinant is 0 (Singular Matrix).")
        
        # Formula: (1/det) * [[d, -b], [-c, a]]
        inv = [
            [round(m[1][1] / det, 4), round(-m[0][1] / det, 4)],
            [round(-m[1][0] / det, 4), round(m[0][0] / det, 4)]
        ]
        return inv, det

    @staticmethod
    def vector_magnitude(ax, ay, az):
        """
        Calculates 3D vector magnitude: sqrt(ax^2 + ay^2 + az^2).
        """
        mag = math.sqrt(ax**2 + ay**2 + az**2)
        return round(mag, 4)

    @staticmethod
    def vector_dot_product(ax, ay, az, bx, by, bz):
        """
        Calculates dot product of two 3D vectors.
        """
        dot = (ax * bx) + (ay * by) + (az * bz)
        return dot