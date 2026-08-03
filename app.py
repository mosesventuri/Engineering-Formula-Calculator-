import sys
import os
import streamlit as st
import math

# Add current directory to path so imports always work smoothly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.math_engine import MathEngine
from modules.physics_engine import PhysicsEngine
from modules.ai_engine import RuleBasedAIEngine
st.set_page_config(
    page_title="Formula Calculator for Engineering Subjects - B.Tech Project",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

ai_engine = RuleBasedAIEngine()

# --- SIDEBAR MENU WITH ORIGINAL TITLE ---
with st.sidebar:
    st.title("🎓 Formula Calculator")
    st.caption("Smart Computational & AI Formula Suggestion System | B.Tech Project")
    st.markdown("---")
    
    selected_section = st.radio(
        "Select Section:",
        [
            "Home",
            "Subjects Used",
            "Programming Used",
            "AI/ML Layer",
            "Live Demo",
            "About Project"
        ]
    )
    st.markdown("---")
    st.info("💡 **Project: Engineering Formula Calculator**\n\n**Subjects:** LA&C & Engineering Physics\n\n**Regulation:** JNTUK R23")

# --- HOME WITH ORIGINAL TITLE ---
if selected_section == "Home":
    st.title("🎓 ENGINEERING FORMULA CALCULATOR")
    st.caption("Smart Computational & AI Formula Suggestion System | B.Tech Project")
    st.markdown("---")
    
    st.subheader("📌 Project Overview")
    st.write(
        "Welcome to the **Engineering Formula Calculator**! This application assists engineering students in "
        "performing accurate mathematical and physical computations directly according to the JNTUK R23 curriculum."
    )
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("LA&C Syllabus", "5 Units")
    m2.metric("Physics Syllabus", "5 Units")
    m3.metric("Total Solvers", "25+ Calculators")
    m4.metric("Regulation", "JNTUK R23")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.success("**Linear Algebra & Calculus (LA&C):**\n- Matrix Addition & Multiplication (2x2 / 3x3)\n- Echelon Rank, Gauss-Jordan Inverse\n- Jacobians & Directional Derivatives\n- Multiple Integrals & Polar Transformations")
    with c2:
        st.info("**Engineering Physics:**\n- Classical Mechanics (Force, Work, Power, KE)\n- Wave Optics (Thin Film, Newton's Rings)\n- Crystallography (d_hkl, Bragg's Law)\n- Quantum Box Energy & Hall Effect")

# --- SUBJECTS USED ---
elif selected_section == "Subjects Used":
    st.title("📚 Subjects Used")
    st.markdown("---")
    st.subheader("Linear Algebra & Calculus (LA&C - JNTUK R23)")
    st.write("• **Matrix Operations:** Addition, Multiplication, Echelon Rank, Inverse.\n• **Calculus:** Mean Value Theorems, Jacobians, Directional Derivatives.")
    st.subheader("Engineering Physics")
    st.write("• **Mechanics & Optics:** Force, Work, Power, Thin Film, Newton's Rings, Bragg's Law, Hall Effect.")

# --- PROGRAMMING USED ---
elif selected_section == "Programming Used":
    st.title("💻 Programming Used")
    st.markdown("---")
    st.code("Language: Python 3.x\nFrameworks: Streamlit + Tkinter Desktop\nModular Design: math_engine, physics_engine, ai_engine", language="text")

# --- AI/ML LAYER ---
elif selected_section == "AI/ML Layer":
    st.title("🤖 AI/ML Layer")
    st.markdown("---")
    query = st.text_input("Type any topic or query (e.g., 'Matrix Multiplication', 'Force', 'Bragg Law', 'Jacobian'):")
    if st.button("Search AI Engine", type="primary"):
        matched, msg = ai_engine.process_query(query)
        if matched:
            st.success(f"**Method:** {matched['name']} | **Category:** {matched['category']}")
            st.warning(f"**Formula:** {matched['formula']}")
            st.info(f"**Explanation:** {matched['explanation']}\n\n*{msg}*")
        else:
            st.error(msg)

# --- LIVE DEMO CALCULATORS ---
elif selected_section == "Live Demo":
    st.title("⚡ Live Demo Calculators")
    st.markdown("---")
    
    tabs = st.tabs(["📐 Engineering Mathematics", "⚡ Engineering Physics"])
    
    # MATH TAB
    with tabs[0]:
        math_choice = st.selectbox(
            "Select Mathematics Calculator:",
            [
                "Matrix Addition", "Matrix Multiplication", "2x2 / 3x3 Matrix Inverse & Det", 
                "Matrix Rank (Echelon Form)", "3D Vector Magnitude", "3D Vector Dot Product", 
                "Jacobian Determinant (2x2)", "Directional Derivative"
            ]
        )
        
        if math_choice in ["Matrix Addition", "Matrix Multiplication"]:
            dim = st.radio("Matrix Dimension:", ["2x2", "3x3"], horizontal=True)
            n = 2 if dim == "2x2" else 3
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"**Matrix A ({dim})**")
                mA = [[st.number_input(f"A[{r},{c}]", value=1.0 if r==c else 0.0, key=f"a_{r}_{c}") for c in range(n)] for r in range(n)]
            with c2:
                st.write(f"**Matrix B ({dim})**")
                mB = [[st.number_input(f"B[{r},{c}]", value=2.0 if r==c else 1.0, key=f"b_{r}_{c}") for c in range(n)] for r in range(n)]
                
            if st.button("Calculate"):
                res = MathEngine.matrix_add(mA, mB) if math_choice == "Matrix Addition" else MathEngine.matrix_multiply(mA, mB)
                st.write("**Result Matrix:**")
                res_cols = st.columns(n)
                for r in range(n):
                    for c in range(n):
                        res_cols[c].success(f"{res[r][c]}")

        elif math_choice == "2x2 / 3x3 Matrix Inverse & Det":
            dim = st.radio("Matrix Dimension:", ["2x2", "3x3"], horizontal=True, key="inv_dim")
            n = 2 if dim == "2x2" else 3
            mA = [[st.number_input(f"A[{r},{c}]", value=1.0 if r==c else 2.0, key=f"i_{r}_{c}") for c in range(n)] for r in range(n)]
            if st.button("Calculate Inverse & Determinant"):
                try:
                    inv, det = MathEngine.matrix_inverse(mA)
                    st.success(f"**Determinant:** {det}")
                    st.write("**Inverse Matrix A⁻¹:**")
                    res_cols = st.columns(n)
                    for r in range(n):
                        for c in range(n):
                            res_cols[c].info(f"{inv[r][c]}")
                except ValueError as e:
                    st.error(str(e))

        elif math_choice == "Matrix Rank (Echelon Form)":
            dim = st.radio("Matrix Dimension:", ["2x2", "3x3"], horizontal=True, key="rk_dim")
            n = 2 if dim == "2x2" else 3
            mA = [[st.number_input(f"A[{r},{c}]", value=1.0 if r==c else 0.0, key=f"rk_{r}_{c}") for c in range(n)] for r in range(n)]
            if st.button("Calculate Rank"):
                st.success(f"**Matrix Rank:** {MathEngine.matrix_rank_echelon(mA)}")

        elif math_choice == "3D Vector Magnitude":
            c1, c2, c3 = st.columns(3)
            ax, ay, az = c1.number_input("ax", value=3.0), c2.number_input("ay", value=4.0), c3.number_input("az", value=12.0)
            if st.button("Calculate Magnitude"):
                st.success(f"**Vector Magnitude ||v||:** {MathEngine.vector_magnitude(ax, ay, az)}")

        elif math_choice == "3D Vector Dot Product":
            c1, c2, c3 = st.columns(3)
            ax, ay, az = c1.number_input("ax", value=1.0), c2.number_input("ay", value=3.0), c3.number_input("az", value=-5.0)
            d1, d2, d3 = st.columns(3)
            bx, by, bz = d1.number_input("bx", value=4.0), d2.number_input("by", value=-2.0), d3.number_input("bz", value=-1.0)
            if st.button("Calculate Dot Product"):
                st.success(f"**Dot Product (a · b):** {MathEngine.vector_dot_product(ax, ay, az, bx, by, bz)}")

        elif math_choice == "Jacobian Determinant (2x2)":
            c1, c2 = st.columns(2)
            du_dx, du_dy = c1.number_input("du/dx", value=2.0), c2.number_input("du/dy", value=3.0)
            dv_dx, dv_dy = c1.number_input("dv/dx", value=1.0), c2.number_input("dv/dy", value=4.0)
            if st.button("Calculate Jacobian"):
                st.success(f"**Jacobian J:** {MathEngine.jacobian_2x2(du_dx, du_dy, dv_dx, dv_dy)}")

        elif math_choice == "Directional Derivative":
            c1, c2, c3 = st.columns(3)
            df_dx, df_dy, df_dz = c1.number_input("df/dx", value=2.0), c2.number_input("df/dy", value=-1.0), c3.number_input("df/dz", value=4.0)
            d1, d2, d3 = st.columns(3)
            ux, uy, uz = d1.number_input("ux", value=1.0), d2.number_input("uy", value=2.0), d3.number_input("uz", value=2.0)
            if st.button("Calculate Directional Derivative"):
                st.success(f"**Directional Derivative D_u f:** {MathEngine.directional_derivative(df_dx, df_dy, df_dz, ux, uy, uz)}")

    # PHYSICS TAB
    with tabs[1]:
        phy_choice = st.selectbox(
            "Select Physics Calculator:",
            [
                "Force (F = m * a)", "Work (W = F * d)", "Power (P = W / t)", "Kinetic Energy (KE = 0.5 * m * v^2)",
                "Interplanar Spacing d_hkl", "Bragg's Law Wavelength", "Newton's Rings Lens Radius R", 
                "Quantum Particle in 1D Box", "Hall Coefficient R_H"
            ]
        )
        
        if phy_choice == "Force (F = m * a)":
            m, a = st.number_input("Mass (kg)", value=10.0), st.number_input("Acceleration (m/s²)", value=2.0)
            if st.button("Calculate Force"):
                st.success(f"**Force:** {PhysicsEngine.calculate_force(m, a)} N")

        elif phy_choice == "Work (W = F * d)":
            f, d = st.number_input("Force (N)", value=50.0), st.number_input("Distance (m)", value=10.0)
            if st.button("Calculate Work"):
                st.success(f"**Work:** {PhysicsEngine.calculate_work(f, d)} J")

        elif phy_choice == "Power (P = W / t)":
            w, t = st.number_input("Work (J)", value=500.0), st.number_input("Time (s)", value=10.0)
            if st.button("Calculate Power"):
                st.success(f"**Power:** {PhysicsEngine.calculate_power(w, t)} W")

        elif phy_choice == "Kinetic Energy (KE = 0.5 * m * v^2)":
            m, v = st.number_input("Mass (kg)", value=2.0), st.number_input("Velocity (m/s)", value=10.0)
            if st.button("Calculate Kinetic Energy"):
                st.success(f"**Kinetic Energy:** {PhysicsEngine.calculate_kinetic_energy(m, v)} J")

        elif phy_choice == "Interplanar Spacing d_hkl":
            a_ang = st.number_input("Lattice Constant a (Å)", value=4.0)
            c1, c2, c3 = st.columns(3)
            h, k, l = c1.number_input("h", value=1), c2.number_input("k", value=1), c3.number_input("l", value=1)
            if st.button("Calculate d_hkl"):
                st.success(f"**d_hkl:** {PhysicsEngine.interplanar_spacing(a_ang, h, k, l)} Å")

        elif phy_choice == "Bragg's Law Wavelength":
            d_space, theta_deg = st.number_input("d (Å)", value=2.82), st.number_input("theta (degrees)", value=30.0)
            if st.button("Calculate Wavelength"):
                st.success(f"**Lambda:** {PhysicsEngine.bragg_law_wavelength(d_space, theta_deg)} Å")

        elif phy_choice == "Newton's Rings Lens Radius R":
            d2, d1 = st.number_input("D_(n+m) (cm)", value=0.7), st.number_input("D_n (cm)", value=0.4)
            m_rings, lam_nm = st.number_input("m rings", value=5), st.number_input("lambda (nm)", value=589.3)
            if st.button("Calculate Radius R"):
                st.success(f"**Radius R:** {PhysicsEngine.newtons_rings_radius_curvature(d2, d1, m_rings, lam_nm)} m")

        elif phy_choice == "Quantum Particle in 1D Box":
            n_state, L_nm = st.number_input("n state", value=1), st.number_input("L (nm)", value=1.0)
            if st.button("Calculate Energy Level"):
                st.success(f"**Energy:** {PhysicsEngine.quantum_particle_box_energy(n_state, L_nm)} eV")

        elif phy_choice == "Hall Coefficient R_H":
            n_density = st.number_input("Carrier Density n (m^-3)", value=1e22)
            if st.button("Calculate Hall Coefficient"):
                st.success(f"**R_H:** {PhysicsEngine.hall_coefficient(n_density):.4e} m³/C")

# --- ABOUT ---
elif selected_section == "About Project":
    st.title("ℹ️ About Project")
    st.markdown("---")
    st.success("Engineering Formula Calculator for B.Tech Students.")
