import streamlit as st

GRADE_MAP = {
    'O': 10,
    'A+': 9,
    'A-': 8,
    'B+': 7,
    'B-': 6,
    'C': 5,
    'Others': 0
}

def calculate_cgpa(subjects):
    total_credits = 0
    total_points = 0

    for subject, credit, grade in subjects:
        total_credits += credit
        total_points += credit * grade

    cgpa = total_points / total_credits
    return cgpa

def main():
    st.title("CGPA Calculator App")

    st.sidebar.header("User Input")
    
    pcgpa = st.sidebar.number_input("Enter Previous CGPA", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

    default_subjects = [
        ("APP DEVELOPMENT", 3, 'O'),
        ("DISASTER MANAGEMENT", 3, 'O'),
        ("OBJECT ORIENTED ANALYSIS AND DESIGN", 4, 'O'),
        ("COMPUTER NETWORKS", 4, 'O'),
        ("MINI PROJECT", 1, 'O'),
        ("COMPUTER NETWORKS LABORATORY", 1, 'O'),
        ("SOFTWARE PROJECT MANAGEMENT", 3, 'O'),
        ("MICROCONTROLLERS AND EMBEDDED SYSTEMS", 4, 'O'),
        ("SOFT SKILLS", 1, 'O')
    ]

    subjects = []

    st.subheader("Default Subjects:")
    for i, (subject, credit, default_grade) in enumerate(default_subjects):
        grade = st.sidebar.selectbox(f"Grade for {subject}", list(GRADE_MAP.keys()), list(GRADE_MAP.keys()).index(default_grade))
        subjects.append((subject, credit, GRADE_MAP[grade]))

    additional_subjects = st.sidebar.number_input("Number of Additional Subjects", min_value=0, value=0)

    for i in range(additional_subjects):
        subject_name = st.sidebar.text_input(f"Name of Additional Subject {i + 1}")
        credit = st.sidebar.number_input(f"Credits for {subject_name}", min_value=1, value=3)
        grade_input = st.sidebar.text_input(f"Grade for {subject_name} (Enter 'O', 'A+', 'A-', 'B+', 'B-', 'C', or 'Others')", 'O')
        grade = GRADE_MAP.get(grade_input.upper(), 0)
        subjects.append((subject_name, credit, grade))

    if st.sidebar.button("Calculate CGPA"):
        cgpa = calculate_cgpa(subjects)
        ccgpa = (cgpa + pcgpa) / 2
        st.success(f"Your CGPA is: {ccgpa:.2f}")

    st.text("Made with 🧡 by DHARANI2D")

if __name__ == "__main__":
    main()
