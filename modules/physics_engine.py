import math

class PhysicsEngine:
    """
    Physics Computation Engine supporting Classical Mechanics & Circuits + 
    JNTUK R23 Engineering Physics (Optics, Crystallography, Quantum, Semiconductors).
    """

    # --- CLASSICAL MECHANICS & BASIC PHYSICS ---

    @staticmethod
    def calculate_force(mass, acceleration):
        return round(mass * acceleration, 4)

    @staticmethod
    def calculate_velocity(displacement, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        return round(displacement / time, 4)

    @staticmethod
    def calculate_acceleration(v_final, v_initial, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        return round((v_final - v_initial) / time, 4)

    @staticmethod
    def calculate_momentum(mass, velocity):
        return round(mass * velocity, 4)

    @staticmethod
    def calculate_work(force, distance):
        return round(force * distance, 4)

    @staticmethod
    def calculate_power(work, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        return round(work / time, 4)

    @staticmethod
    def calculate_kinetic_energy(mass, velocity):
        return round(0.5 * mass * (velocity ** 2), 4)

    @staticmethod
    def calculate_pressure(force, area):
        if area == 0:
            raise ValueError("Area cannot be zero!")
        return round(force / area, 4)

    @staticmethod
    def calculate_density(mass, volume):
        if volume == 0:
            raise ValueError("Volume cannot be zero!")
        return round(mass / volume, 4)

    @staticmethod
    def calculate_ohms_law(current, resistance):
        return round(current * resistance, 4)

    # --- JNTUK R23 ENGINEERING PHYSICS METHODS ---

    @staticmethod
    def thin_film_refractive_index(lambda_nm, t_nm, n_order):
        if t_nm <= 0:
            raise ValueError("Film thickness must be positive.")
        return round((n_order * lambda_nm) / (2 * t_nm), 4)

    @staticmethod
    def newtons_rings_radius_curvature(D_n_plus_m, D_n, m_rings, lambda_nm):
        if m_rings <= 0 or lambda_nm <= 0:
            raise ValueError("Rings count m and wavelength must be greater than zero.")
        lam_m = lambda_nm * 1e-9
        D2 = (D_n_plus_m * 1e-2)**2
        D1 = (D_n * 1e-2)**2
        return round((D2 - D1) / (4 * m_rings * lam_m), 4)

    @staticmethod
    def interplanar_spacing(a_angstrom, h, k, l):
        denom = math.sqrt(h**2 + k**2 + l**2)
        if denom == 0:
            raise ValueError("Miller indices (h,k,l) cannot all be zero.")
        return round(a_angstrom / denom, 4)

    @staticmethod
    def bragg_law_wavelength(d_angstrom, theta_deg, n_order=1):
        theta_rad = math.radians(theta_deg)
        return round((2 * d_angstrom * math.sin(theta_rad)) / n_order, 4)

    @staticmethod
    def quantum_particle_box_energy(n_quantum, L_nm):
        if L_nm <= 0:
            raise ValueError("Box width L must be greater than 0.")
        h, m_e = 6.626e-34, 9.109e-31
        L_m = L_nm * 1e-9
        E_joules = (n_quantum**2 * h**2) / (8 * m_e * L_m**2)
        return round(E_joules / 1.602e-19, 4)

    @staticmethod
    def hall_coefficient(carrier_density_m3):
        if carrier_density_m3 <= 0:
            raise ValueError("Carrier density must be positive.")
        return 1.0 / (carrier_density_m3 * 1.602e-19)
