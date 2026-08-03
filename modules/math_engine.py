import math

class MathEngine:
    """
    Comprehensive Mathematical Engine supporting standard operations (Addition, Multiplication, 
    Vectors) + JNTUK R23 LA&C methods (Echelon Rank, 2x2/3x3 Inverse, Jacobians, Directional Derivatives).
    """

    # --- STANDARD MATRIX & VECTOR OPERATIONS ---

    @staticmethod
    def matrix_add(m1, m2):
        """Adds two matrices of identical dimensions (2x2 or 3x3)."""
        rows = len(m1)
        cols = len(m1[0])
        return [[round(m1[r][c] + m2[r][c], 4) for c in range(cols)] for r in range(rows)]

    @staticmethod
    def matrix_subtract(m1, m2):
        """Subtracts m2 from m1 (2x2 or 3x3)."""
        rows = len(m1)
        cols = len(m1[0])
        return [[round(m1[r][c] - m2[r][c], 4) for c in range(cols)] for r in range(rows)]

    @staticmethod
    def matrix_multiply(m1, m2):
        """Multiplies two square matrices (2x2 or 3x3)."""
        rows = len(m1)
        cols = len(m2[0])
        inner = len(m2)
        result = [[0.0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                total = sum(m1[r][k] * m2[k][c] for k in range(inner))
                result[r][c] = round(total, 4)
        return result

    @staticmethod
    def vector_magnitude(ax, ay, az):
        """3D Vector Magnitude ||v||."""
        return round(math.sqrt(ax**2 + ay**2 + az**2), 4)

    @staticmethod
    def vector_dot_product(ax, ay, az, bx, by, bz):
        """3D Vector Dot Product (a . b)."""
        return round((ax * bx) + (ay * by) + (az * bz), 4)

    # --- JNTUK R23 ADVANCED LA&C METHODS ---

    @staticmethod
    def matrix_rank_echelon(matrix):
        """Rank of matrix using upper-triangular echelon reduction."""
        m = [row[:] for row in matrix]
        rows = len(m)
        cols = len(m[0])
        rank = cols
        
        for row in range(rank):
            if m[row][row] != 0:
                for col in range(rows):
                    if col != row:
                        multiplier = m[col][row] / m[row][row]
                        for i in range(rank):
                            m[col][i] -= multiplier * m[row][i]
            else:
                reduce_flag = True
                for i in range(row + 1, rows):
                    if m[i][row] != 0:
                        m[row], m[i] = m[i], m[row]
                        reduce_flag = False
                        break
                if reduce_flag:
                    rank -= 1
                    for i in range(rows):
                        m[i][row] = m[i][rank]
                row -= 1
        return rank

    @staticmethod
    def matrix_determinant(m):
        n = len(m)
        if n == 2:
            return round((m[0][0] * m[1][1]) - (m[0][1] * m[1][0]), 4)
        elif n == 3:
            det = (
                m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            )
            return round(det, 4)

    @staticmethod
    def matrix_inverse(m):
        det = MathEngine.matrix_determinant(m)
        if det == 0:
            raise ValueError("Inverse does not exist! Determinant is 0 (Singular Matrix).")
        n = len(m)
        if n == 2:
            inv = [
                [round(m[1][1] / det, 4), round(-m[0][1] / det, 4)],
                [round(-m[1][0] / det, 4), round(m[0][0] / det, 4)]
            ]
            return inv, det
        elif n == 3:
            adj = [
                [m[1][1]*m[2][2] - m[1][2]*m[2][1], -(m[0][1]*m[2][2] - m[0][2]*m[2][1]), m[0][1]*m[1][2] - m[0][2]*m[1][1]],
                [-(m[1][0]*m[2][2] - m[1][2]*m[2][0]), m[0][0]*m[2][2] - m[0][2]*m[2][0], -(m[0][0]*m[1][2] - m[0][2]*m[1][0])],
                [m[1][0]*m[2][1] - m[1][1]*m[2][0], -(m[0][0]*m[2][1] - m[0][1]*m[2][0]), m[0][0]*m[1][1] - m[0][1]*m[1][0]]
            ]
            inv = [[round(adj[r][c] / det, 4) for c in range(3)] for r in range(3)]
            return inv, det

    @staticmethod
    def jacobian_2x2(du_dx, du_dy, dv_dx, dv_dy):
        return round((du_dx * dv_dy) - (du_dy * dv_dx), 4)

    @staticmethod
    def directional_derivative(df_dx, df_dy, df_dz, ux, uy, uz):
        u_mag = math.sqrt(ux**2 + uy**2 + uz**2)
        if u_mag == 0:
            raise ValueError("Direction vector cannot be zero vector.")
        return round((df_dx * (ux/u_mag)) + (df_dy * (uy/u_mag)) + (df_dz * (uz/u_mag)), 4)
