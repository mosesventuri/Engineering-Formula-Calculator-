import re

class RuleBasedAIEngine:
    """
    Rule-Based Natural Language Query Processing Engine
    Aligned strictly with JNTUK B.Tech R23 Regulation Syllabus:
    - Linear Algebra & Calculus (LA&C)
    - Engineering Physics
    """

    def __init__(self):
        self.rules = [
            # --- LA&C UNIT I ---
            {
                "id": "echelon_rank",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Matrix Rank (Echelon Form)",
                "keywords": ["rank", "echelon form", "row echelon", "non zero rows"],
                "formula": "Rank(A) = Number of non-zero rows in upper triangular echelon form",
                "explanation": "Perform row operations to convert matrix to upper triangular form; count rows containing at least one non-zero entry."
            },
            {
                "id": "gauss_jordan",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Gauss-Jordan Matrix Inversion",
                "keywords": ["gauss jordan", "matrix inverse", "augmented matrix", "identity matrix"],
                "formula": "[A | I]  --> [I | A^-1]",
                "explanation": "Transform augmented matrix [A | I] using elementary row operations until A becomes Identity matrix I."
            },
            {
                "id": "gauss_seidel",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Gauss-Seidel Iteration Method",
                "keywords": ["gauss seidel", "jacobi", "iteration", "system of linear equations"],
                "formula": "x_i^(k+1) = (1/a_ii) * [ b_i - sum_{j<i} a_ij*x_j^(k+1) - sum_{j>i} a_ij*x_j^(k) ]",
                "explanation": "Iterative method for linear systems where newest updated variable values are immediately plugged into the current iteration."
            },

            # --- LA&C UNIT II ---
            {
                "id": "eigenvalues",
                "category": "LA&C (Unit II: Eigenvalues)",
                "name": "Eigenvalues & Characteristic Equation",
                "keywords": ["eigenvalue", "eigenvector", "characteristic equation", "det(A-lambda I)"],
                "formula": "|A - lambda * I| = 0",
                "explanation": "Roots of the characteristic polynomial equation give the eigenvalues (lambda) of matrix A."
            },
            {
                "id": "cayley_hamilton",
                "category": "LA&C (Unit II: Eigenvalues)",
                "name": "Cayley-Hamilton Theorem",
                "keywords": ["cayley hamilton", "power of matrix", "inverse using cayley"],
                "formula": "P(A) = A^n + c_{n-1}*A^(n-1) + ... + c_0*I = 0",
                "explanation": "Every square matrix satisfies its own characteristic equation; used to find A^-1 and higher matrix powers A^n."
            },

            # --- LA&C UNIT III ---
            {
                "id": "lagrange_mvt",
                "category": "LA&C (Unit III: Calculus)",
                "name": "Lagrange's Mean Value Theorem",
                "keywords": ["lagrange", "mean value theorem", "mvt", "derivative c"],
                "formula": "f'(c) = (f(b) - f(a)) / (b - a)",
                "explanation": "If f(x) is continuous on [a,b] and differentiable on (a,b), there exists c in (a,b) where secant line slope equals tangent slope."
            },

            # --- LA&C UNIT IV ---
            {
                "id": "directional_derivative",
                "category": "LA&C (Unit IV: Multivariable Calculus)",
                "name": "Directional Derivative",
                "keywords": ["directional derivative", "gradient", "grad f", "unit vector u"],
                "formula": "D_u(f) = grad(f) . u_hat = (df/dx i + df/dy j + df/dz k) . u_hat",
                "explanation": "Rate of change of multivariable scalar function f(x,y,z) along the unit vector directional direction u_hat."
            },
            {
                "id": "jacobian",
                "category": "LA&C (Unit IV: Multivariable Calculus)",
                "name": "Jacobian Determinant",
                "keywords": ["jacobian", "functional dependence", "transformation"],
                "formula": "J = d(u,v) / d(x,y) = | [du/dx, du/dy], [dv/dx, dv/dy] |",
                "explanation": "Determinant of partial derivative matrix used in change of variables and testing functional dependence."
            },

            # --- LA&C UNIT V ---
            {
                "id": "polar_integrals",
                "category": "LA&C (Unit V: Multiple Integrals)",
                "name": "Double Integrals (Polar Coordinates)",
                "keywords": ["double integral", "polar coordinates", "area integral", "dx dy to r dr dtheta"],
                "formula": "iint f(x,y) dx dy = iint f(r cos theta, r sin theta) * r dr dtheta",
                "explanation": "Transforms Cartesian integrals into polar coordinates using substitution x = r*cos(theta), y = r*sin(theta), dx dy = r dr dtheta."
            },

            # --- PHYSICS UNIT I ---
            {
                "id": "thin_film",
                "category": "Engineering Physics (Unit I: Wave Optics)",
                "name": "Thin Film Interference",
                "keywords": ["thin film", "interference", "reflection geometry", "path difference"],
                "formula": "2 * mu * t * cos(r) = n * lambda  (Destructive),  (n + 0.5)*lambda (Constructive)",
                "explanation": "Calculates optical path difference condition for light reflected from thin transparent films."
            },
            {
                "id": "newtons_rings",
                "category": "Engineering Physics (Unit I: Wave Optics)",
                "name": "Newton's Rings (Wavelength)",
                "keywords": ["newtons rings", "refractive index", "radius of curvature", "dark ring"],
                "formula": "lambda = (D_(n+m)^2 - D_n^2) / (4 * m * R)",
                "explanation": "Calculates light wavelength using dark ring diameters D_n measured with a Plano-convex lens of radius R."
            },
            {
                "id": "bragg_law",
                "category": "Engineering Physics (Unit II: Crystallography)",
                "name": "Bragg's Law of X-Ray Diffraction",
                "keywords": ["braggs law", "x ray diffraction", "interplanar spacing", "glancing angle"],
                "formula": "2 * d * sin(theta) = n * lambda",
                "explanation": "Condition for constructive interference of X-rays scattered from crystal lattice planes separated by distance d."
            },
            {
                "id": "interplanar_d",
                "category": "Engineering Physics (Unit II: Crystallography)",
                "name": "Interplanar Spacing (d_hkl)",
                "keywords": ["miller indices", "interplanar spacing", "lattice constant a", "hkl planes"],
                "formula": "d_hkl = a / sqrt(h^2 + k^2 + l^2)",
                "explanation": "Calculates perpendicular separation distance between parallel planes defined by Miller indices (h, k, l)."
            },

            # --- PHYSICS UNIT III ---
            {
                "id": "clausius_mossotti",
                "category": "Engineering Physics (Unit III: Dielectrics)",
                "name": "Clausius-Mossotti Equation",
                "keywords": ["clausius mossotti", "dielectric constant", "polarisability", "electric susceptibility"],
                "formula": "(epsilon_r - 1) / (epsilon_r + 2) = (N * alpha) / (3 * epsilon_0)",
                "explanation": "Relates macroscopic dielectric constant (epsilon_r) to microscopic atomic polarizability (alpha)."
            },

            # --- PHYSICS UNIT IV ---
            {
                "id": "heisenberg",
                "category": "Engineering Physics (Unit IV: Quantum Mechanics)",
                "name": "Heisenberg Uncertainty Principle",
                "keywords": ["heisenberg", "uncertainty", "momentum", "position"],
                "formula": "Delta_x * Delta_p >= h / (4 * pi)",
                "explanation": "Fundamental quantum limit stating position and momentum of a particle cannot be simultaneously measured with absolute precision."
            },
            {
                "id": "particle_in_box",
                "category": "Engineering Physics (Unit IV: Quantum Mechanics)",
                "name": "Particle in 1D Potential Box Energy",
                "keywords": ["particle in box", "1d well", "quantum energy levels", "schrodinger"],
                "formula": "E_n = (n^2 * h^2) / (8 * m * L^2)",
                "explanation": "Calculates quantized energy levels for a constrained quantum particle in an infinite 1D potential well of width L."
            },

            # --- PHYSICS UNIT V ---
            {
                "id": "hall_effect",
                "category": "Engineering Physics (Unit V: Semiconductors)",
                "name": "Hall Effect & Hall Coefficient",
                "keywords": ["hall effect", "hall coefficient", "carrier density", "magnetic field"],
                "formula": "R_H = 1 / (n * e)   OR   V_H = (B * I) / (n * e * t)",
                "explanation": "Calculates Hall coefficient and voltage generated when magnetic field B is applied perpendicular to electric current I."
            }
        ]

    def process_query(self, query_text):
        if not query_text or not query_text.strip():
            return None, "Please enter a question or query term."

        clean_text = re.sub(r'[^\w\s]', '', query_text.lower())
        query_words = clean_text.split()

        scored_matches = []
        for rule in self.rules:
            score = 0
            for kw in rule["keywords"]:
                if kw in clean_text:
                    score += 3
                for word in query_words:
                    if word in kw.split():
                        score += 1
            if score > 0:
                scored_matches.append((score, rule))

        if not scored_matches:
            return None, "No exact match found in JNTUK R23 Database. Try searching terms like: 'Gauss Seidel', 'Eigenvalue', 'Directional Derivative', 'Bragg Law', or 'Hall Effect'."

        scored_matches.sort(key=lambda x: x[0], reverse=True)
        top_rule = scored_matches[0][1]
        return top_rule, f"JNTUK R23 Rule Confidence Score: {scored_matches[0][0]} pts"
