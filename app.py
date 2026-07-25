import streamlit as st
import pandas as pd
import numpy as np

# Import our modular engines
from modules.math_engine import MathEngine
from modules.physics_engine import PhysicsEngine
from modules.ai_engine import RuleBasedAIEngine

# Set Page Config for Dashboard View
st.set_page_config(
    page_title="Formula Calculator - B.Tech Project",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize AI Engine
ai_engine = RuleBasedAIEngine()

# --- SIDEBAR NAVIGATION MENU ---
with st.sidebar:
    st.title("🎓 Navigation Menu")
    st.caption("JNTUK R23 B.Tech CSE / AI & DS (2025-2029 Batch)")
    
    st.markdown("---")
    
    # Radio navigation to match screenshot style
    selected_section = st.radio(
        "Select Section:",
        [
            "Home",
            "Subjects used in project",
            "Programming used",
            "AI/ML layer",
            "LIVE DEMO",
            "About Project"
        ]
    )
    
    st.markdown("---")
    
    # Project Info Box in Sidebar
    st.info(
        "💡 **Project 17: Engineering Formula Calculator**\n\n"
        "**Batch:** 2025-2029\n\n"
        "**Tech:** Python, Streamlit, Rule-Based AI Engine"
    )

# --- PAGE 1: HOME ---
if selected_section == "Home":
    st.title("🎓 Formula Calculator for Engineering Subjects")
    st.caption("Smart Computational & AI Formula Suggestion System | B.Tech Mini Project")
    st.markdown("---")
    
    st.subheader("📌 Project Overview & Updates")
    st.write(
        "Welcome to the **Engineering Formula Calculator**! This application assists first and "
        "second-year engineering students in performing accurate mathematical and physical computations."
    )
    st.write(
        "The platform covers key computational concepts including **Linear Algebra Matrix Operations**, "
        "**3D Vector Calculus**, **Classical Mechanics**, and a custom **Rule-Based Natural Language AI Layer**."
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Operational Stats")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Formulas", "16")
        m2.metric("Math Modules", "6")
        m3.metric("Physics Modules", "10")
        m4.metric("AI Precision", "100%")
        
        st.markdown("### 🎯 Key Objectives")
        st.markdown(" -  **Accuracy:** Eliminate manual calculation errors in core formula problem solving.")
        st.markdown(" -  **AI Assistance:** Instant formula discovery using natural language keyword matching.")
        st.markdown(" -  **Modularity:** Clean software architecture decoupling math logic from the user interface.")

    with col2:
        st.subheader("📋 Academic Information")
        st.success(
            "**Institution:** JNTUK Curriculum R23\n\n"
            "**Branch:** Computer Science & Engineering\n\n"
            "**Course:** B.Tech II Year (Semester 1-1 & 1-2)\n\n"
            "**Guide:** Prof. Engineering Mentor\n\n"
            "**Developer:** Student Developer (Roll No: 2XX1A05XX)"
        )

# --- PAGE 2: SUBJECTS USED ---
elif selected_section == "Subjects used in project":
    st.title("📚 Subjects Used in Project")
    st.markdown("---")
    
    st.subheader("📐 Engineering Mathematics Curriculum")
    st.info(
        "**1. Linear Algebra:** 2x2 Matrix Addition, Matrix Multiplication, Determinants, and Matrix Inverse.\n\n"
        "**2. Vector Calculus:** 3D Vector Magnitude and Dot Product projection."
    )
    
    st.subheader("⚡ Engineering Physics Curriculum")
    st.success(
        "**1. Classical Mechanics:** Force ($F=ma$), Velocity ($v=d/t$), Acceleration, Momentum ($p=mv$), Work ($W=Fd$), Power ($P=W/t$), Kinetic Energy.\n\n"
        "**2. Fluid Statics:** Pressure ($P=F/A$) and Density ($\\rho=m/V$).\n\n"
        "**3. Circuit Theory:** Ohm's Law ($V=I \\cdot R$)."
    )

# --- PAGE 3: PROGRAMMING USED ---
elif selected_section == "Programming used":
    st.title("💻 Programming Concepts Used")
    st.markdown("---")
    
    st.markdown("### 🛠 Tech Stack Details")
    st.code("""
Language: Python 3.x
UI Engine: Streamlit Web Dashboard Engine
Architecture: Modular Package Architecture (math_engine, physics_engine, ai_engine)
AI Mechanism: Natural Language Tokenization & Keyword Scoring (re module)
    """, language="yaml")
    
    st.markdown("### 🧩 Key Concepts")
    st.markdown("- **Object-Oriented Programming (OOP):** Encapsulated logic inside `MathEngine`, `PhysicsEngine`, and `RuleBasedAIEngine`.")
    st.markdown("- **Exception Guarding:** Guarded against division-by-zero ($t=0$, $A=0$, $\\det(A)=0$) and invalid string inputs.")

# --- PAGE 4: AI/ML LAYER ---
elif selected_section == "AI/ML layer":
    st.title("🤖 AI/ML Layer (Rule-Based NLP Engine)")
    st.markdown("---")
    
    st.subheader("💡 Ask the AI Formula Assistant")
    user_query = st.text_input(
        "Enter your question or problem statement in plain English:",
        value="How do I calculate kinetic energy with mass and velocity?"
    )
    
    if st.button("Ask AI Assistant", type="primary"):
        matched_rule, msg = ai_engine.process_query(user_query)
        
        if matched_rule:
            st.success(f"**AI Match Found:** {matched_rule['name']} ({matched_rule['category']})")
            st.warning(f"**Formula:** {matched_rule['formula']}")
            st.info(f"**Explanation:** {matched_rule['explanation']}\n\n*{msg}*")
        else:
            st.error(f"**No Match Found:** {msg}")

# --- PAGE 5: LIVE DEMO ---
elif selected_section == "LIVE DEMO":
    st.title("⚡ Interactive Live Demo Calculators")
    st.markdown("---")
    
    demo_type = st.tabs(["📐 Engineering Mathematics", "⚡ Engineering Physics"])
    
    # MATH SUB-TAB
    with demo_type[0]:
        st.subheader("Mathematics Operations")
        math_choice = st.selectbox(
            "Select Math Calculator:",
            ["Matrix Addition", "Matrix Multiplication", "Determinant (2x2)", "Inverse Matrix (2x2)", "Vector Magnitude (3D)", "Dot Product (3D)"]
        )
        
        if math_choice in ["Matrix Addition", "Matrix Multiplication"]:
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Matrix A (2x2)**")
                a00 = st.number_input("A[0,0]", value=1.0)
                a01 = st.number_input("A[0,1]", value=2.0)
                a10 = st.number_input("A[1,0]", value=3.0)
                a11 = st.number_input("A[1,1]", value=4.0)
            with c2:
                st.write("**Matrix B (2x2)**")
                b00 = st.number_input("B[0,0]", value=5.0)
                b01 = st.number_input("B[0,1]", value=6.0)
                b10 = st.number_input("B[1,0]", value=7.0)
                b11 = st.number_input("B[1,1]", value=8.0)
                
            if st.button("Calculate Matrix Operation"):
                mA = [[a00, a01], [a10, a11]]
                mB = [[b00, b01], [b10, b11]]
                res = MathEngine.matrix_add(mA, mB) if math_choice == "Matrix Addition" else MathEngine.matrix_multiply(mA, mB)
                st.success(f"**Result Matrix:**\n\n[{res[0][0]}, {res[0][1]}]\n\n[{res[1][0]}, {res[1][1]}]")

        elif math_choice in ["Determinant (2x2)", "Inverse Matrix (2x2)"]:
            st.write("**Matrix A (2x2)**")
            c1, c2 = st.columns(2)
            with c1:
                a00 = st.number_input("A[0,0]", value=4.0, key="s00")
                a01 = st.number_input("A[0,1]", value=7.0, key="s01")
            with c2:
                a10 = st.number_input("A[1,0]", value=2.0, key="s10")
                a11 = st.number_input("A[1,1]", value=6.0, key="s11")
                
            if st.button("Calculate Matrix Result"):
                mA = [[a00, a01], [a10, a11]]
                if math_choice == "Determinant (2x2)":
                    det = MathEngine.matrix_determinant(mA)
                    st.success(f"**Determinant det(A):** {det}")
                else:
                    try:
                        inv, det = MathEngine.matrix_inverse(mA)
                        st.success(f"**Determinant:** {det}\n\n**Inverse Matrix A⁻¹:**\n\n[{inv[0][0]}, {inv[0][1]}]\n\n[{inv[1][0]}, {inv[1][1]}]")
                    except ValueError as e:
                        st.error(str(e))

        elif math_choice == "Vector Magnitude (3D)":
            c1, c2, c3 = st.columns(3)
            ax = c1.number_input("ax (i)", value=3.0)
            ay = c2.number_input("ay (j)", value=4.0)
            az = c3.number_input("az (k)", value=12.0)
            if st.button("Calculate Vector Magnitude"):
                mag = MathEngine.vector_magnitude(ax, ay, az)
                st.success(f"**Vector Magnitude ||v||:** {mag}")

        elif math_choice == "Dot Product (3D)":
            st.write("**Vector A**")
            c1, c2, c3 = st.columns(3)
            ax = c1.number_input("ax", value=1.0)
            ay = c2.number_input("ay", value=3.0)
            az = c3.number_input("az", value=-5.0)
            
            st.write("**Vector B**")
            d1, d2, d3 = st.columns(3)
            bx = d1.number_input("bx", value=4.0)
            by = d2.number_input("by", value=-2.0)
            bz = d3.number_input("bz", value=-1.0)
            
            if st.button("Calculate Dot Product"):
                dot = MathEngine.vector_dot_product(ax, ay, az, bx, by, bz)
                st.success(f"**Dot Product (a · b):** {dot}")

    # PHYSICS SUB-TAB
    with demo_type[1]:
        st.subheader("Physics Operations")
        phy_choice = st.selectbox(
            "Select Physics Calculator:",
            [
                "Force (F = m * a)", "Velocity (v = d / t)", "Acceleration (a = (vf - vi) / t)",
                "Momentum (p = m * v)", "Work (W = F * d)", "Power (P = W / t)",
                "Kinetic Energy (KE = 0.5 * m * v^2)", "Pressure (P = F / A)",
                "Density (rho = m / V)", "Ohm's Law (V = I * R)"
            ]
        )
        
        if phy_choice == "Force (F = m * a)":
            m = st.number_input("Mass (kg)", value=10.0)
            a = st.number_input("Acceleration (m/s²)", value=2.0)
            if st.button("Calculate Force"):
                st.success(f"**Calculated Force:** {PhysicsEngine.calculate_force(m, a)} N")

        elif phy_choice == "Velocity (v = d / t)":
            d = st.number_input("Displacement (m)", value=100.0)
            t = st.number_input("Time (s)", value=5.0)
            if st.button("Calculate Velocity"):
                try:
                    st.success(f"**Calculated Velocity:** {PhysicsEngine.calculate_velocity(d, t)} m/s")
                except ValueError as e:
                    st.error(str(e))

        elif phy_choice == "Acceleration (a = (vf - vi) / t)":
            vf = st.number_input("Final Velocity (m/s)", value=30.0)
            vi = st.number_input("Initial Velocity (m/s)", value=10.0)
            t = st.number_input("Time (s)", value=4.0)
            if st.button("Calculate Acceleration"):
                try:
                    st.success(f"**Calculated Acceleration:** {PhysicsEngine.calculate_acceleration(vf, vi, t)} m/s²")
                except ValueError as e:
                    st.error(str(e))

        elif phy_choice == "Momentum (p = m * v)":
            m = st.number_input("Mass (kg)", value=50.0, key="pm")
            v = st.number_input("Velocity (m/s)", value=3.0, key="pv")
            if st.button("Calculate Momentum"):
                st.success(f"**Calculated Momentum:** {PhysicsEngine.calculate_momentum(m, v)} kg·m/s")

        elif phy_choice == "Work (W = F * d)":
            f = st.number_input("Force (N)", value=50.0)
            d = st.number_input("Distance (m)", value=10.0)
            if st.button("Calculate Work"):
                st.success(f"**Calculated Work:** {PhysicsEngine.calculate_work(f, d)} J")

        elif phy_choice == "Power (P = W / t)":
            w = st.number_input("Work (J)", value=500.0)
            t = st.number_input("Time (s)", value=10.0, key="pt")
            if st.button("Calculate Power"):
                try:
                    st.success(f"**Calculated Power:** {PhysicsEngine.calculate_power(w, t)} W")
                except ValueError as e:
                    st.error(str(e))

        elif phy_choice == "Kinetic Energy (KE = 0.5 * m * v^2)":
            m = st.number_input("Mass (kg)", value=2.0, key="kem")
            v = st.number_input("Velocity (m/s)", value=10.0, key="kev")
            if st.button("Calculate Kinetic Energy"):
                st.success(f"**Calculated Kinetic Energy:** {PhysicsEngine.calculate_kinetic_energy(m, v)} J")

        elif phy_choice == "Pressure (P = F / A)":
            f = st.number_input("Force (N)", value=200.0, key="pf")
            a = st.number_input("Area (m²)", value=2.0)
            if st.button("Calculate Pressure"):
                try:
                    st.success(f"**Calculated Pressure:** {PhysicsEngine.calculate_pressure(f, a)} Pa")
                except ValueError as e:
                    st.error(str(e))

        elif phy_choice == "Density (rho = m / V)":
            m = st.number_input("Mass (kg)", value=1000.0, key="dm")
            vol = st.number_input("Volume (m³)", value=2.0)
            if st.button("Calculate Density"):
                try:
                    st.success(f"**Calculated Density:** {PhysicsEngine.calculate_density(m, vol)} kg/m³")
                except ValueError as e:
                    st.error(str(e))

        elif phy_choice == "Ohm's Law (V = I * R)":
            i = st.number_input("Current (A)", value=2.5)
            r = st.number_input("Resistance (Ohm)", value=8.0)
            if st.button("Calculate Voltage"):
                st.success(f"**Calculated Voltage:** {PhysicsEngine.calculate_ohms_law(i, r)} V")

# --- PAGE 6: ABOUT ---
elif selected_section == "About Project":
    st.title("ℹ️ About Project")
    st.markdown("---")
    st.write(
        "This software is designed as a B.Tech Mini Project to assist engineering students in "
        "solving complex mathematical and physical equations with step-by-step validation."
    )
    st.info(
        "**Version:** v1.0.0 (Streamlit Dashboard Edition)\n\n"
        "**Framework:** Streamlit + Python 3.x\n\n"
        "**AI Parser:** Keyword Scoring Rule-Based NLP Pipeline"
    )