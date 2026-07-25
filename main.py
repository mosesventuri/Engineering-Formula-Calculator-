import os
import tkinter as tk
from tkinter import ttk, messagebox

# Import modular engines
from modules.math_engine import MathEngine
from modules.physics_engine import PhysicsEngine
from modules.ai_engine import RuleBasedAIEngine

class EngineeringCalculatorApp:
    def __init__(self, root):
        """Constructor: Initializes app setup, styles, navigation, and page builds."""
        self.root = root
        
        # Instantiate AI Engine
        self.ai_engine = RuleBasedAIEngine()

        # 1. Main Window Configuration
        self.root.title("Formula Calculator for Engineering Subjects - B.Tech Project")
        self.window_width = 1024
        self.window_height = 680
        self.center_window()
        self.root.minsize(900, 600)
        self.root.configure(bg="#F1F5F9")
        
        # 2. Top Header Banner
        self.create_header()
        
        # 3. Configure Modern Tab Styling
        self.configure_styles()
        
        # 4. Create Tab Navigation System
        self.create_tabs()
        
        # 5. Populate All Content Pages
        self.build_home_tab()
        self.build_subjects_tab()
        self.build_programming_tab()
        self.build_ai_tab()
        self.build_live_demo_tab()
        self.build_about_tab()

    def center_window(self):
        """Calculates screen dimensions to center the window perfectly."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (self.window_width / 2))
        y_coordinate = int((screen_height / 2) - (self.window_height / 2))
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x_coordinate}+{y_coordinate}")

    def create_header(self):
        """Creates a styled top title banner for the app."""
        header_frame = tk.Frame(self.root, bg="#1E293B", height=75)
        header_frame.pack(side="top", fill="x")
        header_frame.pack_propagate(False)

        title_label = tk.Label(
            header_frame,
            text="ENGINEERING FORMULA CALCULATOR",
            font=("Helvetica", 17, "bold"),
            fg="#F8FAFC",
            bg="#1E293B"
        )
        title_label.pack(pady=(12, 2))

        subtitle_label = tk.Label(
            header_frame,
            text="Smart Computational & AI Formula Suggestion System | B.Tech Project",
            font=("Helvetica", 9, "italic"),
            fg="#94A3B8",
            bg="#1E293B"
        )
        subtitle_label.pack()

    def configure_styles(self):
        """Configures clean, professional theme styles for ttk widgets."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TNotebook", background="#F1F5F9", borderwidth=0)
        self.style.configure(
            "TNotebook.Tab",
            font=("Helvetica", 10, "bold"),
            padding=[14, 8],
            background="#CBD5E1",
            foreground="#334155",
            borderwidth=0
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", "#0F172A")],
            foreground=[("selected", "#FFFFFF")]
        )

    def create_tabs(self):
        """Creates the Notebook and adds all 6 project tabs."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

        self.tabs = {}
        tab_titles = [
            "Home",
            "Subjects Used",
            "Programming Used",
            "AI/ML Layer",
            "Live Demo",
            "About Project"
        ]

        for title in tab_titles:
            frame = tk.Frame(self.notebook, bg="#FFFFFF")
            self.notebook.add(frame, text=f"  {title}  ")
            self.tabs[title] = frame

    def build_home_tab(self):
        """Builds the complete layout for the Home Page."""
        home_frame = self.tabs["Home"]
        main_container = tk.Frame(home_frame, bg="#FFFFFF", padx=20, pady=20)
        main_container.pack(fill="both", expand=True)

        meta_card = tk.LabelFrame(
            main_container,
            text=" Project Overview & Academic Info ",
            font=("Helvetica", 11, "bold"),
            fg="#0F172A", bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15
        )
        meta_card.pack(fill="x", pady=(0, 15))

        info_items = [
            ("Project Title:", "Formula Calculator for Engineering Subjects"),
            ("Institution:", "Department of Computer Science & Engineering"),
            ("Course & Year:", "B.Tech II Year (Semester III / IV)"),
            ("Project Guide:", "Prof. Engineering Mentor"),
            ("Team Members:", "Student Developer 1 (Roll No: 2XX1A05XX)")
        ]

        for row_idx, (label_text, val_text) in enumerate(info_items):
            lbl = tk.Label(meta_card, text=label_text, font=("Helvetica", 10, "bold"), fg="#334155", bg="#FFFFFF", anchor="w")
            lbl.grid(row=row_idx, column=0, sticky="w", pady=4, padx=(0, 15))
            val = tk.Label(meta_card, text=val_text, font=("Helvetica", 10), fg="#0F172A", bg="#FFFFFF", anchor="w")
            val.grid(row=row_idx, column=1, sticky="w", pady=4)

        split_frame = tk.Frame(main_container, bg="#FFFFFF")
        split_frame.pack(fill="both", expand=True)

        obj_card = tk.LabelFrame(
            split_frame, text=" Key Project Objectives ",
            font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15
        )
        obj_card.pack(side="left", fill="both", expand=True, padx=(0, 10))

        objectives = [
            "• Provide quick, accurate calculations for B.Tech Engg. Math & Physics.",
            "• Reduce manual calculation errors in core formula problem solving.",
            "• Implement a Rule-Based AI Layer to suggest formulas dynamically.",
            "• Demonstrate modular software architecture using Python & Tkinter GUI.",
            "• Offer step-by-step variable input validation and clear output rendering."
        ]

        for obj in objectives:
            o_lbl = tk.Label(obj_card, text=obj, font=("Helvetica", 9), fg="#475569", bg="#FFFFFF", anchor="w", justify="left")
            o_lbl.pack(anchor="w", pady=5)

        img_card = tk.LabelFrame(
            split_frame, text=" System Blueprint ",
            font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15
        )
        img_card.pack(side="right", fill="both", expand=True, padx=(10, 0))

        canvas = tk.Canvas(img_card, bg="#F8FAFC", highlightthickness=1, highlightbackground="#CBD5E1")
        canvas.pack(fill="both", expand=True)
        canvas.create_rectangle(20, 20, 280, 140, outline="#94A3B8", width=2, dash=(4, 4))
        canvas.create_text(150, 80, text="[ Project Architecture Diagram ]\n\nPython + Tkinter + AI Rules", fill="#64748B", font=("Helvetica", 10, "bold"), justify="center")

    def build_subjects_tab(self):
        sub_frame = self.tabs["Subjects Used"]
        container = tk.Frame(sub_frame, bg="#FFFFFF", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        math_card = tk.LabelFrame(container, text=" Engineering Mathematics Curriculum ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        math_card.pack(fill="x", pady=(0, 15))

        math_topics = [
            ("1. Linear Algebra & Matrices:", "Includes 2x2 Matrix Addition, Matrix Multiplication, Determinant computation, and Matrix Inverse calculation."),
            ("2. Vector Calculus & Geometry:", "Covers 3D spatial Vector Magnitude calculation and Vector Dot Product for directional force projection.")
        ]
        for title, desc in math_topics:
            tk.Label(math_card, text=title, font=("Helvetica", 10, "bold"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(3, 0))
            tk.Label(math_card, text=desc, font=("Helvetica", 9), fg="#334155", bg="#FFFFFF", justify="left", wraplength=900).pack(anchor="w", pady=(0, 5))

        phy_card = tk.LabelFrame(container, text=" Engineering Physics Curriculum ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        phy_card.pack(fill="x")

        phy_topics = [
            ("1. Classical Mechanics & Kinematics:", "Covers Force (F=ma), Velocity (v=d/t), Acceleration, Linear Momentum (p=mv), Work (W=Fd), Power (P=W/t), and Kinetic Energy."),
            ("2. Fluid Statics & Material Science:", "Includes Hydrostatic Pressure (P=F/A) and Mass Density (rho=m/V) calculations."),
            ("3. Electromagnetism & Circuit Theory:", "Covers Ohm's Law (V=I*R) for electrical potential calculation across conductors.")
        ]
        for title, desc in phy_topics:
            tk.Label(phy_card, text=title, font=("Helvetica", 10, "bold"), fg="#166534", bg="#FFFFFF").pack(anchor="w", pady=(3, 0))
            tk.Label(phy_card, text=desc, font=("Helvetica", 9), fg="#334155", bg="#FFFFFF", justify="left", wraplength=900).pack(anchor="w", pady=(0, 5))

    def build_programming_tab(self):
        prog_frame = self.tabs["Programming Used"]
        container = tk.Frame(prog_frame, bg="#FFFFFF", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        card = tk.LabelFrame(container, text=" Programming Concepts & Technologies Implemented ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        concepts = [
            ("• Object-Oriented Programming (OOP):", "App is structured using Python Classes (`EngineeringCalculatorApp`, `MathEngine`, `PhysicsEngine`, `RuleBasedAIEngine`) ensuring encapsulated, reusable code."),
            ("• GUI Development (Tkinter & Ttk):", "Built using `ttk.Notebook` tabbed navigation, `tk.LabelFrame` cards, dynamic `ttk.Combobox` dropdowns, and responsive grid geometry management."),
            ("• Modular Software Architecture:", "Application logic is decoupled into separate module files (`math_engine.py`, `physics_engine.py`, `ai_engine.py`), preventing bloated single-file code."),
            ("• Natural Language Processing (NLP):", "Rule-based natural language parsing engine utilizing `re` (Regular Expressions) and keyword tokenization for AI formula matching."),
            ("• Robust Error & Exception Handling:", "Includes `try-except` blocks guarding against division-by-zero errors, invalid input types, and singular matrix inversion exceptions.")
        ]

        for title, desc in concepts:
            tk.Label(card, text=title, font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#FFFFFF").pack(anchor="w", pady=(4, 0))
            tk.Label(card, text=desc, font=("Helvetica", 9), fg="#475569", bg="#FFFFFF", justify="left", wraplength=880).pack(anchor="w", pady=(0, 6))

    def build_ai_tab(self):
        ai_frame = self.tabs["AI/ML Layer"]
        container = tk.Frame(ai_frame, bg="#FFFFFF", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        arch_card = tk.LabelFrame(container, text=" AI Recommendation Layer Architecture ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        arch_card.pack(fill="x", pady=(0, 15))

        arch_txt = (
            "The AI Layer uses a Rule-Based NLP Parser. It extracts semantic keywords from natural language "
            "engineering questions and maps them to appropriate mathematical or physical formulas with high precision.\n"
            "Future Roadmap: Modular design allows seamlessly hooking an external LLM API (e.g., Llama 3 / OpenAI) for complex problem breakdown."
        )
        tk.Label(arch_card, text=arch_txt, font=("Helvetica", 9), fg="#334155", bg="#FFFFFF", justify="left", wraplength=900).pack(anchor="w")

        query_card = tk.LabelFrame(container, text=" Ask the AI Formula Assistant ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        query_card.pack(fill="both", expand=True)

        input_box_frame = tk.Frame(query_card, bg="#FFFFFF")
        input_box_frame.pack(fill="x", pady=(0, 15))

        tk.Label(input_box_frame, text="Type your question or variables:", font=("Helvetica", 10, "bold"), bg="#FFFFFF", fg="#0F172A").pack(anchor="w", pady=(0, 5))

        self.ai_query_entry = ttk.Entry(input_box_frame, font=("Helvetica", 11), width=60)
        self.ai_query_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.ai_query_entry.insert(0, "How do I calculate kinetic energy with mass and velocity?")

        tk.Button(
            input_box_frame, text="Ask AI Assistant", bg="#2563EB", fg="#FFFFFF", font=("Helvetica", 10, "bold"),
            padx=15, pady=5, command=self.handle_ai_query, cursor="hand2"
        ).pack(side="left")

        self.ai_res_card = tk.Frame(query_card, bg="#F8FAFC", bd=1, relief="solid", padx=15, pady=15)
        self.ai_res_card.pack(fill="both", expand=True)

        self.ai_title_lbl = tk.Label(self.ai_res_card, text="AI Recommendation Output", font=("Helvetica", 12, "bold"), fg="#0F172A", bg="#F8FAFC")
        self.ai_title_lbl.pack(anchor="w", pady=(0, 5))

        self.ai_formula_lbl = tk.Label(self.ai_res_card, text="Recommended Formula: --", font=("Helvetica", 11, "bold"), fg="#2563EB", bg="#F8FAFC")
        self.ai_formula_lbl.pack(anchor="w", pady=(0, 5))

        self.ai_desc_lbl = tk.Label(self.ai_res_card, text="Enter a question above and click 'Ask AI Assistant' to see rule-based reasoning.", font=("Helvetica", 10), fg="#475569", bg="#F8FAFC", justify="left")
        self.ai_desc_lbl.pack(anchor="w")

    def handle_ai_query(self):
        query = self.ai_query_entry.get()
        matched_rule, msg = self.ai_engine.process_query(query)

        if matched_rule:
            self.ai_title_lbl.config(text=f"AI Suggestion: {matched_rule['name']} ({matched_rule['category']})", fg="#166534")
            self.ai_formula_lbl.config(text=f"Formula: {matched_rule['formula']}")
            self.ai_desc_lbl.config(text=f"{matched_rule['explanation']}\n\n[{msg}]")
        else:
            self.ai_title_lbl.config(text="No Match Found", fg="#991B1B")
            self.ai_formula_lbl.config(text="Formula: None")
            self.ai_desc_lbl.config(text=msg)

    # --- LIVE DEMO TAB BUILDER ---
    def build_live_demo_tab(self):
        demo_frame = self.tabs["Live Demo"]
        self.demo_notebook = ttk.Notebook(demo_frame)
        self.demo_notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.math_demo_frame = tk.Frame(self.demo_notebook, bg="#FFFFFF")
        self.physics_demo_frame = tk.Frame(self.demo_notebook, bg="#FFFFFF")

        self.demo_notebook.add(self.math_demo_frame, text="  Engineering Mathematics  ")
        self.demo_notebook.add(self.physics_demo_frame, text="  Engineering Physics  ")

        self.build_math_calculators()
        self.build_physics_calculators()

    # --- MATH CALCULATORS SECTION ---
    def build_math_calculators(self):
        container = tk.Frame(self.math_demo_frame, bg="#FFFFFF", padx=20, pady=15)
        container.pack(fill="both", expand=True)

        select_frame = tk.Frame(container, bg="#F1F5F9", padx=10, pady=10, bd=1, relief="solid")
        select_frame.pack(fill="x", pady=(0, 15))

        tk.Label(select_frame, text="Select Mathematics Calculator:", font=("Helvetica", 10, "bold"), bg="#F1F5F9", fg="#0F172A").pack(side="left", padx=(0, 10))

        math_options = [
            "Matrix Addition",
            "Matrix Multiplication",
            "Determinant (2x2)",
            "Inverse Matrix (2x2)",
            "Vector Magnitude (3D)",
            "Dot Product (3D)"
        ]

        self.math_choice = ttk.Combobox(select_frame, values=math_options, state="readonly", width=30, font=("Helvetica", 10))
        self.math_choice.pack(side="left")
        self.math_choice.current(0)
        self.math_choice.bind("<<ComboboxSelected>>", self.render_selected_math_calc)

        self.math_work_panel = tk.Frame(container, bg="#FFFFFF")
        self.math_work_panel.pack(fill="both", expand=True)

        self.render_selected_math_calc()

    def render_selected_math_calc(self, event=None):
        for widget in self.math_work_panel.winfo_children():
            widget.destroy()

        selected = self.math_choice.get()

        if selected in ["Matrix Addition", "Matrix Multiplication"]:
            self.render_matrix_two_input_ui(selected)
        elif selected in ["Determinant (2x2)", "Inverse Matrix (2x2)"]:
            self.render_matrix_single_input_ui(selected)
        elif selected == "Vector Magnitude (3D)":
            self.render_vector_single_ui()
        elif selected == "Dot Product (3D)":
            self.render_vector_double_ui()

    def render_matrix_two_input_ui(self, calc_name):
        card = tk.LabelFrame(self.math_work_panel, text=f" {calc_name} ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        formula_str = "Formula: [A] + [B] = [C]" if calc_name == "Matrix Addition" else "Formula: [C]_{ij} = sum(A_{ik} * B_{kj})"
        tk.Label(card, text=formula_str, font=("Helvetica", 10, "italic"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(0, 10))

        matrices_frame = tk.Frame(card, bg="#FFFFFF")
        matrices_frame.pack(fill="x", pady=10)

        mA_box = tk.LabelFrame(matrices_frame, text=" Matrix A (2x2) ", bg="#FFFFFF", fg="#334155")
        mA_box.grid(row=0, column=0, padx=10)
        self.a_entries = [[ttk.Entry(mA_box, width=5) for _ in range(2)] for _ in range(2)]
        for r in range(2):
            for c in range(2):
                self.a_entries[r][c].grid(row=r, column=c, padx=5, pady=5)
                self.a_entries[r][c].insert(0, "0")

        mB_box = tk.LabelFrame(matrices_frame, text=" Matrix B (2x2) ", bg="#FFFFFF", fg="#334155")
        mB_box.grid(row=0, column=1, padx=10)
        self.b_entries = [[ttk.Entry(mB_box, width=5) for _ in range(2)] for _ in range(2)]
        for r in range(2):
            for c in range(2):
                self.b_entries[r][c].grid(row=r, column=c, padx=5, pady=5)
                self.b_entries[r][c].insert(0, "0")

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Calculate", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=lambda: self.process_matrix_two_op(calc_name), cursor="hand2").pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Clear", bg="#E2E8F0", fg="#0F172A", font=("Helvetica", 10), padx=15, pady=5, command=self.render_selected_math_calc, cursor="hand2").pack(side="left")

        self.res_label = tk.Label(card, text="Result: Click Calculate to view output.", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_matrix_two_op(self, calc_name):
        try:
            mA = [[float(self.a_entries[r][c].get().strip()) for c in range(2)] for r in range(2)]
            mB = [[float(self.b_entries[r][c].get().strip()) for c in range(2)] for r in range(2)]

            if calc_name == "Matrix Addition":
                res = MathEngine.matrix_add(mA, mB)
            else:
                res = MathEngine.matrix_multiply(mA, mB)

            out_text = f"Result Matrix:\n[ {res[0][0]},  {res[0][1]} ]\n[ {res[1][0]},  {res[1][1]} ]"
            self.res_label.config(text=out_text, fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric numbers into all matrix cells.")

    def render_matrix_single_input_ui(self, calc_name):
        card = tk.LabelFrame(self.math_work_panel, text=f" {calc_name} ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        formula_str = "Formula: det(A) = ad - bc" if "Determinant" in calc_name else "Formula: A^-1 = (1/det(A)) * [[d, -b], [-c, a]]"
        tk.Label(card, text=formula_str, font=("Helvetica", 10, "italic"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(0, 10))

        mA_box = tk.LabelFrame(card, text=" Matrix A (2x2) ", bg="#FFFFFF", fg="#334155")
        mA_box.pack(anchor="w", pady=10)

        self.a_entries = [[ttk.Entry(mA_box, width=5) for _ in range(2)] for _ in range(2)]
        for r in range(2):
            for c in range(2):
                self.a_entries[r][c].grid(row=r, column=c, padx=5, pady=5)
                self.a_entries[r][c].insert(0, "0")

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Calculate", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=lambda: self.process_matrix_single_op(calc_name), cursor="hand2").pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Clear", bg="#E2E8F0", fg="#0F172A", font=("Helvetica", 10), padx=15, pady=5, command=self.render_selected_math_calc, cursor="hand2").pack(side="left")

        self.res_label = tk.Label(card, text="Result: Click Calculate to view output.", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_matrix_single_op(self, calc_name):
        try:
            mA = [[float(self.a_entries[r][c].get().strip()) for c in range(2)] for r in range(2)]

            if "Determinant" in calc_name:
                det = MathEngine.matrix_determinant(mA)
                self.res_label.config(text=f"Determinant det(A) = {det}", fg="#166534")
            else:
                inv, det = MathEngine.matrix_inverse(mA)
                out_text = f"Determinant = {det}\nInverse Matrix A^-1:\n[ {inv[0][0]},  {inv[0][1]} ]\n[ {inv[1][0]},  {inv[1][1]} ]"
                self.res_label.config(text=out_text, fg="#166534")
        except ValueError as e:
            messagebox.showerror("Calculation Error", str(e))

    def render_vector_single_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" Vector Magnitude (3D) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        tk.Label(card, text="Formula: ||v|| = sqrt(ax^2 + ay^2 + az^2)", font=("Helvetica", 10, "italic"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(0, 10))

        v_frame = tk.Frame(card, bg="#FFFFFF")
        v_frame.pack(anchor="w", pady=10)

        tk.Label(v_frame, text="Vector Components (ax, ay, az):", font=("Helvetica", 10), bg="#FFFFFF").grid(row=0, column=0, columnspan=6, sticky="w", pady=(0, 5))

        self.ax_entry = ttk.Entry(v_frame, width=6)
        self.ax_entry.grid(row=1, column=0, padx=2)
        tk.Label(v_frame, text="i + ", bg="#FFFFFF").grid(row=1, column=1)

        self.ay_entry = ttk.Entry(v_frame, width=6)
        self.ay_entry.grid(row=1, column=2, padx=2)
        tk.Label(v_frame, text="j + ", bg="#FFFFFF").grid(row=1, column=3)

        self.az_entry = ttk.Entry(v_frame, width=6)
        self.az_entry.grid(row=1, column=4, padx=2)
        tk.Label(v_frame, text="k", bg="#FFFFFF").grid(row=1, column=5)

        for entry in [self.ax_entry, self.ay_entry, self.az_entry]:
            entry.insert(0, "0")

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Calculate", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_vector_mag, cursor="hand2").pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Clear", bg="#E2E8F0", fg="#0F172A", font=("Helvetica", 10), padx=15, pady=5, command=self.render_selected_math_calc, cursor="hand2").pack(side="left")

        self.res_label = tk.Label(card, text="Result: Click Calculate to view output.", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_vector_mag(self):
        try:
            ax = float(self.ax_entry.get().strip())
            ay = float(self.ay_entry.get().strip())
            az = float(self.az_entry.get().strip())
            mag = MathEngine.vector_magnitude(ax, ay, az)
            self.res_label.config(text=f"Vector Magnitude ||v|| = {mag}", fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric values for vector components.")

    def render_vector_double_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" Dot Product (3D Vectors) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        tk.Label(card, text="Formula: a . b = (ax*bx) + (ay*by) + (az*bz)", font=("Helvetica", 10, "italic"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(0, 10))

        v_frame = tk.Frame(card, bg="#FFFFFF")
        v_frame.pack(anchor="w", pady=10)

        tk.Label(v_frame, text="Vector A (ax, ay, az):", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=0, column=0, columnspan=6, sticky="w")
        self.ax_entry = ttk.Entry(v_frame, width=6)
        self.ax_entry.grid(row=1, column=0, padx=2)
        tk.Label(v_frame, text="i + ", bg="#FFFFFF").grid(row=1, column=1)
        self.ay_entry = ttk.Entry(v_frame, width=6)
        self.ay_entry.grid(row=1, column=2, padx=2)
        tk.Label(v_frame, text="j + ", bg="#FFFFFF").grid(row=1, column=3)
        self.az_entry = ttk.Entry(v_frame, width=6)
        self.az_entry.grid(row=1, column=4, padx=2)
        tk.Label(v_frame, text="k", bg="#FFFFFF").grid(row=1, column=5)

        tk.Label(v_frame, text="Vector B (bx, by, bz):", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=2, column=0, columnspan=6, sticky="w", pady=(10, 0))
        self.bx_entry = ttk.Entry(v_frame, width=6)
        self.bx_entry.grid(row=3, column=0, padx=2)
        tk.Label(v_frame, text="i + ", bg="#FFFFFF").grid(row=3, column=1)
        self.by_entry = ttk.Entry(v_frame, width=6)
        self.by_entry.grid(row=3, column=2, padx=2)
        tk.Label(v_frame, text="j + ", bg="#FFFFFF").grid(row=3, column=3)
        self.bz_entry = ttk.Entry(v_frame, width=6)
        self.bz_entry.grid(row=3, column=4, padx=2)
        tk.Label(v_frame, text="k", bg="#FFFFFF").grid(row=3, column=5)

        for entry in [self.ax_entry, self.ay_entry, self.az_entry, self.bx_entry, self.by_entry, self.bz_entry]:
            entry.insert(0, "0")

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Calculate", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_vector_dot, cursor="hand2").pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Clear", bg="#E2E8F0", fg="#0F172A", font=("Helvetica", 10), padx=15, pady=5, command=self.render_selected_math_calc, cursor="hand2").pack(side="left")

        self.res_label = tk.Label(card, text="Result: Click Calculate to view output.", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_vector_dot(self):
        try:
            ax, ay, az = float(self.ax_entry.get().strip()), float(self.ay_entry.get().strip()), float(self.az_entry.get().strip())
            bx, by, bz = float(self.bx_entry.get().strip()), float(self.by_entry.get().strip()), float(self.bz_entry.get().strip())
            dot = MathEngine.vector_dot_product(ax, ay, az, bx, by, bz)
            self.res_label.config(text=f"Dot Product (a . b) = {dot}", fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric values for all vector components.")

    # --- PHYSICS CALCULATORS SECTION ---
    def build_physics_calculators(self):
        container = tk.Frame(self.physics_demo_frame, bg="#FFFFFF", padx=20, pady=15)
        container.pack(fill="both", expand=True)

        select_frame = tk.Frame(container, bg="#F1F5F9", padx=10, pady=10, bd=1, relief="solid")
        select_frame.pack(fill="x", pady=(0, 15))

        tk.Label(select_frame, text="Select Physics Calculator:", font=("Helvetica", 10, "bold"), bg="#F1F5F9", fg="#0F172A").pack(side="left", padx=(0, 10))

        physics_options = [
            "Force (F = m * a)",
            "Velocity (v = d / t)",
            "Acceleration (a = (vf - vi) / t)",
            "Momentum (p = m * v)",
            "Work (W = F * d)",
            "Power (P = W / t)",
            "Kinetic Energy (KE = 0.5 * m * v^2)",
            "Pressure (P = F / A)",
            "Density (rho = m / V)",
            "Ohm's Law (V = I * R)"
        ]

        self.physics_choice = ttk.Combobox(select_frame, values=physics_options, state="readonly", width=35, font=("Helvetica", 10))
        self.physics_choice.pack(side="left")
        self.physics_choice.current(0)
        self.physics_choice.bind("<<ComboboxSelected>>", self.render_selected_physics_calc)

        self.physics_work_panel = tk.Frame(container, bg="#FFFFFF")
        self.physics_work_panel.pack(fill="both", expand=True)

        self.render_selected_physics_calc()

    def render_selected_physics_calc(self, event=None):
        for widget in self.physics_work_panel.winfo_children():
            widget.destroy()

        choice = self.physics_choice.get()

        configs = {
            "Force (F = m * a)": ("Force Calculator", "Formula: Force F = m * a", [("Mass (m):", "kg"), ("Acceleration (a):", "m/s^2")], "N", PhysicsEngine.calculate_force),
            "Velocity (v = d / t)": ("Velocity Calculator", "Formula: Velocity v = d / t", [("Displacement (d):", "m"), ("Time (t):", "s")], "m/s", PhysicsEngine.calculate_velocity),
            "Acceleration (a = (vf - vi) / t)": ("Acceleration Calculator", "Formula: Acceleration a = (vf - vi) / t", [("Final Velocity (vf):", "m/s"), ("Initial Velocity (vi):", "m/s"), ("Time (t):", "s")], "m/s^2", PhysicsEngine.calculate_acceleration),
            "Momentum (p = m * v)": ("Momentum Calculator", "Formula: Momentum p = m * v", [("Mass (m):", "kg"), ("Velocity (v):", "m/s")], "kg·m/s", PhysicsEngine.calculate_momentum),
            "Work (W = F * d)": ("Work Calculator", "Formula: Work W = F * d", [("Force (F):", "N"), ("Distance (d):", "m")], "J", PhysicsEngine.calculate_work),
            "Power (P = W / t)": ("Power Calculator", "Formula: Power P = W / t", [("Work (W):", "J"), ("Time (t):", "s")], "W", PhysicsEngine.calculate_power),
            "Kinetic Energy (KE = 0.5 * m * v^2)": ("Kinetic Energy Calculator", "Formula: KE = 0.5 * m * v^2", [("Mass (m):", "kg"), ("Velocity (v):", "m/s")], "J", PhysicsEngine.calculate_kinetic_energy),
            "Pressure (P = F / A)": ("Pressure Calculator", "Formula: Pressure P = F / A", [("Force (F):", "N"), ("Area (A):", "m^2")], "Pa", PhysicsEngine.calculate_pressure),
            "Density (rho = m / V)": ("Density Calculator", "Formula: Density rho = m / V", [("Mass (m):", "kg"), ("Volume (V):", "m^3")], "kg/m^3", PhysicsEngine.calculate_density),
            "Ohm's Law (V = I * R)": ("Ohm's Law Calculator", "Formula: Voltage V = I * R", [("Current (I):", "A"), ("Resistance (R):", "Ohm")], "V", PhysicsEngine.calculate_ohms_law)
        }

        title, formula, inputs, unit, func = configs[choice]

        card = tk.LabelFrame(self.physics_work_panel, text=f" {title} ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        tk.Label(card, text=formula, font=("Helvetica", 10, "italic"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(0, 10))

        form_frame = tk.Frame(card, bg="#FFFFFF")
        form_frame.pack(anchor="w", pady=10)

        self.physics_entries = []
        for idx, (label_txt, unit_txt) in enumerate(inputs):
            tk.Label(form_frame, text=label_txt, font=("Helvetica", 10), bg="#FFFFFF").grid(row=idx, column=0, sticky="w", pady=5)
            ent = ttk.Entry(form_frame, width=12)
            ent.grid(row=idx, column=1, padx=10, pady=5)
            ent.insert(0, "0")
            tk.Label(form_frame, text=unit_txt, font=("Helvetica", 9, "bold"), fg="#64748B", bg="#FFFFFF").grid(row=idx, column=2, sticky="w")
            self.physics_entries.append(ent)

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Calculate", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=lambda: self.process_physics_calc(func, unit), cursor="hand2").pack(side="left", padx=(0, 10))
        tk.Button(btn_frame, text="Clear", bg="#E2E8F0", fg="#0F172A", font=("Helvetica", 10), padx=15, pady=5, command=self.render_selected_physics_calc, cursor="hand2").pack(side="left")

        self.phy_res_label = tk.Label(card, text="Result: Click Calculate to view output.", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.phy_res_label.pack(fill="x", pady=10)

    def process_physics_calc(self, func, unit):
        try:
            vals = [float(ent.get().strip()) for ent in self.physics_entries]
            res = func(*vals)
            self.phy_res_label.config(text=f"Calculated Output = {res} {unit}", fg="#166534")
        except ValueError as e:
            err_msg = str(e) if str(e) else "Please enter valid numerical numbers."
            messagebox.showwarning("Input Alert", err_msg)

    def build_about_tab(self):
        """Builds the layout for the About Project Page."""
        about_frame = self.tabs["About Project"]
        container = tk.Frame(about_frame, bg="#FFFFFF", padx=25, pady=25)
        container.pack(fill="both", expand=True)

        title = tk.Label(container, text="About 'Engineering Formula Calculator'", font=("Helvetica", 15, "bold"), fg="#0F172A", bg="#FFFFFF")
        title.pack(anchor="w", pady=(0, 10))

        desc_text = (
            "This software is designed as a B.Tech Mini Project to assist first and second-year "
            "engineering students in mastering core mathematical and physical computations.\n\n"
            "Key Engineering Modules Covered:\n"
            "1. Engineering Mathematics: Linear Algebra, Matrix Transformations, and Vector Calculus.\n"
            "2. Engineering Physics: Classical Mechanics, Kinematics, Dynamics, Thermodynamics, and Electromagnetism.\n"
            "3. AI Assistance: Dynamic rule-based query parser that automatically maps keywords to the right engineering equation."
        )

        desc = tk.Label(container, text=desc_text, font=("Helvetica", 10), fg="#334155", bg="#FFFFFF", justify="left", wraplength=850)
        desc.pack(anchor="w", pady=(0, 20))

        tech_frame = tk.LabelFrame(container, text=" Technical Environment Specifications ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15)
        tech_frame.pack(fill="x")

        specs = [
            ("Application Version:", "v1.0.0 (Mini Project Build)"),
            ("Programming Language:", "Python 3.x"),
            ("GUI Framework:", "Tkinter (Ttk Engine)"),
            ("IDE Used:", "Visual Studio Code (VS Code)"),
            ("Math Engine:", "Python Native Math & Matrix Processing Routines"),
            ("AI Recommendation:", "Rule-Based Natural Language Keyword Parser")
        ]

        for idx, (spec_k, spec_v) in enumerate(specs):
            k_lbl = tk.Label(tech_frame, text=spec_k, font=("Helvetica", 9, "bold"), fg="#475569", bg="#FFFFFF")
            k_lbl.grid(row=idx, column=0, sticky="w", pady=3, padx=(0, 20))
            v_lbl = tk.Label(tech_frame, text=spec_v, font=("Helvetica", 9), fg="#0F172A", bg="#FFFFFF")
            v_lbl.grid(row=idx, column=1, sticky="w", pady=3)

# --- Application Launch Point ---
if __name__ == "__main__":
    main_window = tk.Tk()
    app = EngineeringCalculatorApp(main_window)
    main_window.mainloop()