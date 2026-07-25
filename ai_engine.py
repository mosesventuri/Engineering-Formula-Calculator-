import re

class RuleBasedAIEngine:
    """
    Rule-Based Natural Language Query Processing Engine for Engineering Formulas.
    Matches natural user input against structured intent rules.
    """

    def __init__(self):
        # Knowledge Base mapping intent keywords to engineering formulas
        self.rules = [
            {
                "id": "force",
                "category": "Engineering Physics",
                "name": "Force (Newton's 2nd Law)",
                "keywords": ["force", "push", "pull", "mass", "acceleration", "f=ma", "newton"],
                "formula": "F = m * a",
                "explanation": "Calculates the net force applied on an object given its mass (kg) and acceleration (m/s²)."
            },
            {
                "id": "velocity",
                "category": "Engineering Physics",
                "name": "Velocity",
                "keywords": ["velocity", "speed", "displacement", "distance", "time", "v=d/t"],
                "formula": "v = d / t",
                "explanation": "Calculates the rate of change of displacement over time."
            },
            {
                "id": "acceleration",
                "category": "Engineering Physics",
                "name": "Acceleration",
                "keywords": ["acceleration", "speed up", "change in velocity", "final velocity", "initial velocity"],
                "formula": "a = (v_final - v_initial) / t",
                "explanation": "Calculates the rate of change of velocity over time."
            },
            {
                "id": "momentum",
                "category": "Engineering Physics",
                "name": "Momentum",
                "keywords": ["momentum", "linear momentum", "mass in motion", "p=mv"],
                "formula": "p = m * v",
                "explanation": "Calculates linear momentum as the product of mass and velocity."
            },
            {
                "id": "work",
                "category": "Engineering Physics",
                "name": "Work Done",
                "keywords": ["work", "joules", "force over distance", "w=fd"],
                "formula": "W = F * d",
                "explanation": "Calculates energy transferred when a force moves an object across a displacement."
            },
            {
                "id": "power",
                "category": "Engineering Physics",
                "name": "Power",
                "keywords": ["power", "watt", "rate of work", "work done per second", "p=w/t"],
                "formula": "P = W / t",
                "explanation": "Calculates the rate at which work is done or energy is converted."
            },
            {
                "id": "kinetic_energy",
                "category": "Engineering Physics",
                "name": "Kinetic Energy",
                "keywords": ["kinetic", "energy", "moving body", "ke", "1/2 mv^2"],
                "formula": "KE = 0.5 * m * v^2",
                "explanation": "Calculates the mechanical energy possessed by an object due to its motion."
            },
            {
                "id": "pressure",
                "category": "Engineering Physics",
                "name": "Pressure",
                "keywords": ["pressure", "pascal", "force per unit area", "p=f/a"],
                "formula": "P = F / A",
                "explanation": "Calculates normal force distributed over a unit surface area."
            },
            {
                "id": "density",
                "category": "Engineering Physics",
                "name": "Density",
                "keywords": ["density", "mass per volume", "rho", "volumetric mass"],
                "formula": "rho = m / V",
                "explanation": "Calculates mass per unit volume of a substance."
            },
            {
                "id": "ohms_law",
                "category": "Engineering Physics",
                "name": "Ohm's Law (Voltage)",
                "keywords": ["ohms law", "ohm", "voltage", "current", "resistance", "v=ir", "circuit"],
                "formula": "V = I * R",
                "explanation": "Calculates electrical potential difference across a conductor."
            },
            {
                "id": "matrix_add",
                "category": "Engineering Mathematics",
                "name": "Matrix Addition",
                "keywords": ["matrix add", "matrix sum", "add matrices", "2x2 matrix addition"],
                "formula": "[A] + [B] = [C]",
                "explanation": "Performs component-wise addition of two matrices of equal dimensions."
            },
            {
                "id": "matrix_mult",
                "category": "Engineering Mathematics",
                "name": "Matrix Multiplication",
                "keywords": ["matrix multiply", "matrix product", "dot product of matrix", "multiply matrices"],
                "formula": "[C] = [A] x [B]",
                "explanation": "Calculates matrix row-by-column linear transformation."
            },
            {
                "id": "determinant",
                "category": "Engineering Mathematics",
                "name": "Matrix Determinant",
                "keywords": ["determinant", "det", "ad-bc", "singular matrix"],
                "formula": "det(A) = ad - bc",
                "explanation": "Calculates the scalar determinant of a 2x2 matrix."
            },
            {
                "id": "inverse",
                "category": "Engineering Mathematics",
                "name": "Inverse Matrix",
                "keywords": ["inverse", "matrix inverse", "invertible", "a^-1"],
                "formula": "A^-1 = (1/det(A)) * adj(A)",
                "explanation": "Calculates the multiplicative inverse matrix."
            },
            {
                "id": "vector_mag",
                "category": "Engineering Mathematics",
                "name": "Vector Magnitude",
                "keywords": ["vector magnitude", "vector length", "norm", "3d vector magnitude"],
                "formula": "||v|| = sqrt(ax^2 + ay^2 + az^2)",
                "explanation": "Calculates Euclidean length of a 3D vector."
            },
            {
                "id": "dot_product",
                "category": "Engineering Mathematics",
                "name": "Vector Dot Product",
                "keywords": ["dot product", "scalar product", "vector dot", "inner product"],
                "formula": "a . b = ax*bx + ay*by + az*bz",
                "explanation": "Calculates scalar dot product of two 3D spatial vectors."
            }
        ]

    def process_query(self, query_text):
        """
        Parses user query, normalizes input, ranks matching rules,
        and returns best matching formula details.
        """
        if not query_text or not query_text.strip():
            return None, "Please type a question or natural language search prompt."

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
            return None, (
                "No direct formula match found.\n"
                "Try keywords like: 'force', 'voltage', 'kinetic energy', 'determinant', 'dot product'."
            )

        scored_matches.sort(key=lambda x: x[0], reverse=True)
        top_rule = scored_matches[0][1]

        return top_rule, f"Rule Match Confidence: High ({scored_matches[0][0]} point score)"