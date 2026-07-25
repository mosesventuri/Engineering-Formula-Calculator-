class PhysicsEngine:
    """
    Pure Python Physics Engine for Engineering Physics Calculations.
    Includes zero-division safety and standard rounding.
    """

    @staticmethod
    def calculate_force(mass, accel):
        return round(mass * accel, 4)

    @staticmethod
    def calculate_velocity(disp, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        return round(disp / time, 4)

    @staticmethod
    def calculate_acceleration(v_final, v_initial, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        return round((v_final - v_initial) / time, 4)

    @staticmethod
    def calculate_momentum(mass, vel):
        return round(mass * vel, 4)

    @staticmethod
    def calculate_work(force, dist):
        return round(force * dist, 4)

    @staticmethod
    def calculate_power(work, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        return round(work / time, 4)

    @staticmethod
    def calculate_kinetic_energy(mass, vel):
        return round(0.5 * mass * (vel ** 2), 4)

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