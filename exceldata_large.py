import pandas as pd
import random


def generate_large_database():
    """Generate expanded university database with more rooms, labs, teachers, courses, and sections"""

    # 1. ROOMS - Expanded: Z103-Z140, Z203-Z240, A103-A140, A203-A240, B103-B140, P1-P20
    rooms_data = []

    # Building Z: Z103 to Z140
    for room_num in range(103, 141):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'Z{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building Z: Z203 to Z240
    for room_num in range(203, 241):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'Z{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building A: A103 to A140
    for room_num in range(103, 141):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'A{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building A: A203 to A240
    for room_num in range(203, 241):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'A{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building B: B103 to B140
    for room_num in range(103, 141):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'B{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building P: P1 to P20
    for room_num in range(1, 21):
        strength = random.choice([40, 50, 60, 80])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'P{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # 2. LABS - Expanded with more labs of each type
    labs_data = [
        # Computer Labs (7 total)
        {'Lab_Name': 'Computer Lab 1', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 2', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 3', 'Strength': 35, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 4', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 5', 'Strength': 35, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 6', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 7', 'Strength': 35, 'Lab_Type': 'Computer'},
        # Physics Labs (4 total)
        {'Lab_Name': 'Physics Lab 1', 'Strength': 25, 'Lab_Type': 'Physics'},
        {'Lab_Name': 'Physics Lab 2', 'Strength': 30, 'Lab_Type': 'Physics'},
        {'Lab_Name': 'Physics Lab 3', 'Strength': 25, 'Lab_Type': 'Physics'},
        {'Lab_Name': 'Physics Lab 4', 'Strength': 30, 'Lab_Type': 'Physics'},
        # Power System Labs (3 total)
        {'Lab_Name': 'Power System Lab 1', 'Strength': 30, 'Lab_Type': 'Power'},
        {'Lab_Name': 'Power System Lab 2', 'Strength': 30, 'Lab_Type': 'Power'},
        {'Lab_Name': 'Power System Lab 3', 'Strength': 25, 'Lab_Type': 'Power'},
        # Machine Labs (3 total)
        {'Lab_Name': 'Machine Lab 1', 'Strength': 25, 'Lab_Type': 'Machine'},
        {'Lab_Name': 'Machine Lab 2', 'Strength': 25, 'Lab_Type': 'Machine'},
        {'Lab_Name': 'Machine Lab 3', 'Strength': 30, 'Lab_Type': 'Machine'},
        # DLD Labs (3 total)
        {'Lab_Name': 'DLD Lab 1', 'Strength': 35, 'Lab_Type': 'DLD'},
        {'Lab_Name': 'DLD Lab 2', 'Strength': 35, 'Lab_Type': 'DLD'},
        {'Lab_Name': 'DLD Lab 3', 'Strength': 30, 'Lab_Type': 'DLD'},
        # VLSI Labs (3 total)
        {'Lab_Name': 'VLSI Lab 1', 'Strength': 30, 'Lab_Type': 'VLSI'},
        {'Lab_Name': 'VLSI Lab 2', 'Strength': 30, 'Lab_Type': 'VLSI'},
        {'Lab_Name': 'VLSI Lab 3', 'Strength': 25, 'Lab_Type': 'VLSI'},
        # Control Labs (3 total)
        {'Lab_Name': 'Control Lab 1', 'Strength': 30, 'Lab_Type': 'Control'},
        {'Lab_Name': 'Control Lab 2', 'Strength': 30, 'Lab_Type': 'Control'},
        {'Lab_Name': 'Control Lab 3', 'Strength': 25, 'Lab_Type': 'Control'},
        # Communication Labs (3 total)
        {'Lab_Name': 'ELE Communication Lab 1', 'Strength': 35, 'Lab_Type': 'Communication'},
        {'Lab_Name': 'ELE Communication Lab 2', 'Strength': 35, 'Lab_Type': 'Communication'},
        {'Lab_Name': 'ELE Communication Lab 3', 'Strength': 30, 'Lab_Type': 'Communication'},
    ]

    # 3. TEACHERS - Expanded to 60 teachers with Pakistani names
    teachers_data = [
        {'Teacher_ID': 'T001', 'Teacher_Name': 'Dr. Aamir Shahzad'},
        {'Teacher_ID': 'T002', 'Teacher_Name': 'Dr. Faisal Mehmood'},
        {'Teacher_ID': 'T003', 'Teacher_Name': 'Nouman Khan Tareen'},
        {'Teacher_ID': 'T004', 'Teacher_Name': 'Asad Ullah'},
        {'Teacher_ID': 'T005', 'Teacher_Name': 'Dr. S Shahid Mustafa'},
        {'Teacher_ID': 'T006', 'Teacher_Name': 'Usman Khalid'},
        {'Teacher_ID': 'T007', 'Teacher_Name': 'Sohail Muzzamil'},
        {'Teacher_ID': 'T008', 'Teacher_Name': 'Dr. Shahid Nawaz Khan'},
        {'Teacher_ID': 'T009', 'Teacher_Name': 'Nasir Khan'},
        {'Teacher_ID': 'T010', 'Teacher_Name': 'Dr. Shohaib Khalid'},
        {'Teacher_ID': 'T011', 'Teacher_Name': 'Dr. Shohaib Azmat'},
        {'Teacher_ID': 'T012', 'Teacher_Name': 'Dr. Zahid Jehangiri'},
        {'Teacher_ID': 'T013', 'Teacher_Name': 'Bakhtash Ali Jehangir'},
        {'Teacher_ID': 'T014', 'Teacher_Name': 'Syed Mashood Murtaza'},
        {'Teacher_ID': 'T015', 'Teacher_Name': 'Dr. Aftab Ahmad Khan'},
        {'Teacher_ID': 'T016', 'Teacher_Name': 'Dr. Ahmad Fayyaz'},
        {'Teacher_ID': 'T017', 'Teacher_Name': 'Dr. Sajid Aqeel'},
        {'Teacher_ID': 'T018', 'Teacher_Name': 'Sahibzada Aasim'},
        {'Teacher_ID': 'T019', 'Teacher_Name': 'Dr. Syed Wajahat Ali'},
        {'Teacher_ID': 'T020', 'Teacher_Name': 'Dr. Ch. Arshad Mehmood'},
        {'Teacher_ID': 'T021', 'Teacher_Name': 'Dr. Ali Zahir'},
        {'Teacher_ID': 'T022', 'Teacher_Name': 'Muhammad Naveed Shaikh'},
        {'Teacher_ID': 'T023', 'Teacher_Name': 'Atiq ul Anam'},
        {'Teacher_ID': 'T024', 'Teacher_Name': 'Dr. Sardar Muhammad Gulfam'},
        {'Teacher_ID': 'T025', 'Teacher_Name': 'Dr. Ali Ahmad Farooq'},
        {'Teacher_ID': 'T026', 'Teacher_Name': 'Dr. Muhammad Imran Shehzad'},
        {'Teacher_ID': 'T027', 'Teacher_Name': 'Prof. Wasiq Ahmed'},
        {'Teacher_ID': 'T028', 'Teacher_Name': 'Dr. Hassan Khalid'},
        {'Teacher_ID': 'T029', 'Teacher_Name': 'Fatima Noor Khan'},
        {'Teacher_ID': 'T030', 'Teacher_Name': 'Dr. Bilal Ahmed'},
        {'Teacher_ID': 'T031', 'Teacher_Name': 'Ms. Ayesha Malik'},
        {'Teacher_ID': 'T032', 'Teacher_Name': 'Dr. Rashid Hussain'},
        {'Teacher_ID': 'T033', 'Teacher_Name': 'Muhammad Saeed'},
        {'Teacher_ID': 'T034', 'Teacher_Name': 'Dr. Sana Iqbal'},
        {'Teacher_ID': 'T035', 'Teacher_Name': 'Dr. Tahir Abbas'},
        {'Teacher_ID': 'T036', 'Teacher_Name': 'Karim Uddin'},
        {'Teacher_ID': 'T037', 'Teacher_Name': 'Dr. Amina Ahmed'},
        {'Teacher_ID': 'T038', 'Teacher_Name': 'Habib ur Rehman'},
        {'Teacher_ID': 'T039', 'Teacher_Name': 'Dr. Rizwan Khan'},
        {'Teacher_ID': 'T040', 'Teacher_Name': 'Saira Javaid'},
        {'Teacher_ID': 'T041', 'Teacher_Name': 'Dr. Farooq Ahmed'},
        {'Teacher_ID': 'T042', 'Teacher_Name': 'Muhammad Hasan'},
        {'Teacher_ID': 'T043', 'Teacher_Name': 'Dr. Nadia Khan'},
        {'Teacher_ID': 'T044', 'Teacher_Name': 'Anwar Husain'},
        {'Teacher_ID': 'T045', 'Teacher_Name': 'Dr. Mariam Akhtar'},
        {'Teacher_ID': 'T046', 'Teacher_Name': 'Akbar Ali Khan'},
        {'Teacher_ID': 'T047', 'Teacher_Name': 'Dr. Samina Hassan'},
        {'Teacher_ID': 'T048', 'Teacher_Name': 'Tariq Mahmood'},
        {'Teacher_ID': 'T049', 'Teacher_Name': 'Dr. Hina Malik'},
        {'Teacher_ID': 'T050', 'Teacher_Name': 'Qadir Abbas'},
        {'Teacher_ID': 'T051', 'Teacher_Name': 'Dr. Rabia Khan'},
        {'Teacher_ID': 'T052', 'Teacher_Name': 'Nasim Uddin'},
        {'Teacher_ID': 'T053', 'Teacher_Name': 'Dr. Fozia Ahmed'},
        {'Teacher_ID': 'T054', 'Teacher_Name': 'Saleem Ahmad'},
        {'Teacher_ID': 'T055', 'Teacher_Name': 'Dr. Neha Fatima'},
        {'Teacher_ID': 'T056', 'Teacher_Name': 'Waqar Khan'},
        {'Teacher_ID': 'T057', 'Teacher_Name': 'Dr. Sameena Noor'},
        {'Teacher_ID': 'T058', 'Teacher_Name': 'Yousaf Ali'},
        {'Teacher_ID': 'T059', 'Teacher_Name': 'Dr. Zara Khan'},
        {'Teacher_ID': 'T060', 'Teacher_Name': 'Zahid Hussain'}
    ]

    # 4. COURSES - Expanded to 50 courses
    courses_data = [
        # Computer Science Courses
        {'Course_ID': 'CS101', 'Course_Name': 'Introduction to Programming', 'Theory_Classes_Per_Week': 2,
         'Has_Lab': True, 'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS102', 'Course_Name': 'Data Structures', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS103', 'Course_Name': 'Object Oriented Programming', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS201', 'Course_Name': 'Algorithms', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS202', 'Course_Name': 'Database Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS301', 'Course_Name': 'Operating Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS302', 'Course_Name': 'Computer Networks', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS303', 'Course_Name': 'Compiler Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS401', 'Course_Name': 'Artificial Intelligence', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS402', 'Course_Name': 'Machine Learning', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS403', 'Course_Name': 'Web Programming', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS404', 'Course_Name': 'Mobile App Development', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        # Software Engineering Courses
        {'Course_ID': 'SE101', 'Course_Name': 'Software Engineering', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'SE102', 'Course_Name': 'Fundamentals of Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'SE201', 'Course_Name': 'Web Development', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'SE202', 'Course_Name': 'Software Testing', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'SE301', 'Course_Name': 'Cloud Computing', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        # Electrical Engineering Courses
        {'Course_ID': 'EE101', 'Course_Name': 'Circuit Analysis', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE102', 'Course_Name': 'Digital Logic Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'DLD', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE103', 'Course_Name': 'Electromagnetic Theory', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE201', 'Course_Name': 'Electronics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE202', 'Course_Name': 'Power Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Power', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE203', 'Course_Name': 'Microprocessors', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE301', 'Course_Name': 'Control Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Control', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE302', 'Course_Name': 'Communication Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Communication', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE303', 'Course_Name': 'VLSI Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'VLSI', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE304', 'Course_Name': 'Power Electronics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Power', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        # Mechanical Engineering Courses
        {'Course_ID': 'ME101', 'Course_Name': 'Engineering Mechanics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME102', 'Course_Name': 'Engineering Drawing', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME201', 'Course_Name': 'Thermodynamics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME202', 'Course_Name': 'Fluid Mechanics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME301', 'Course_Name': 'Machine Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Machine', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME302', 'Course_Name': 'Manufacturing Processes', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Machine', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME303', 'Course_Name': 'Heat Transfer', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        # Mathematics Courses
        {'Course_ID': 'MA101', 'Course_Name': 'Calculus I', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'MA102', 'Course_Name': 'Linear Algebra', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'MA201', 'Course_Name': 'Calculus II', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'MA202', 'Course_Name': 'Differential Equations', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'MA301', 'Course_Name': 'Numerical Analysis', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        # Physics Courses
        {'Course_ID': 'PH101', 'Course_Name': 'Physics I', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'PH201', 'Course_Name': 'Physics II', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'PH202', 'Course_Name': 'Modern Physics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        # Business & Economics Courses
        {'Course_ID': 'BA101', 'Course_Name': 'Business Management', 'Theory_Classes_Per_Week': 1, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': True},
        {'Course_ID': 'BA102', 'Course_Name': 'Entrepreneurship', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'BA201', 'Course_Name': 'Financial Management', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EC101', 'Course_Name': 'Microeconomics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EC102', 'Course_Name': 'Macroeconomics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EC201', 'Course_Name': 'International Economics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
    ]

    # 5. SECTIONS - Expanded to 25 sections covering more departments and shifts
    sections_data = []
    section_names = [
        # Computer Science (5 sections)
        'CS-A', 'CS-B', 'CS-C', 'CS-D', 'CS-E',
        # Software Engineering (4 sections)
        'SE-A', 'SE-B', 'SE-C', 'SE-D',
        # Electrical Engineering (5 sections)
        'EE-A', 'EE-B', 'EE-C', 'EE-D', 'EE-E',
        # Mechanical Engineering (4 sections)
        'ME-A', 'ME-B', 'ME-C', 'ME-D',
        # Business Administration (3 sections)
        'BBA-A', 'BBA-B', 'BBA-C',
        # Economics (2 sections)
        'ECO-A', 'ECO-B',
        # General Science (2 sections)
        'GS-A', 'GS-B'
    ]

    for i, section_name in enumerate(section_names, 1):
        sections_data.append({
            'Section_ID': section_name,
            'Student_Count': random.randint(35, 55)
        })

    # 6. COURSE ASSIGNMENTS - Assign courses to sections with teachers
    course_assignments_data = []
    assignment_id = 1

    # CS-A assignments
    cs_a_courses = ['CS101', 'CS102', 'CS103', 'MA101', 'PH101', 'BA101', 'CS201']
    for course_id in cs_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'CS-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 45
        })
        assignment_id += 1

    # CS-B assignments
    cs_b_courses = ['CS101', 'CS102', 'MA102', 'PH201', 'EC101', 'CS202', 'CS301']
    for course_id in cs_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'CS-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 50
        })
        assignment_id += 1

    # CS-C assignments
    cs_c_courses = ['CS301', 'CS302', 'CS401', 'SE101', 'MA101', 'CS402', 'CS403']
    for course_id in cs_c_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'CS-C',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 40
        })
        assignment_id += 1

    # CS-D assignments
    cs_d_courses = ['CS102', 'CS201', 'CS302', 'MA201', 'PH101', 'CS404']
    for course_id in cs_d_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'CS-D',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 48
        })
        assignment_id += 1

    # CS-E assignments
    cs_e_courses = ['CS101', 'CS103', 'CS201', 'MA102', 'PH201', 'CS302']
    for course_id in cs_e_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'CS-E',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 42
        })
        assignment_id += 1

    # SE-A assignments
    se_a_courses = ['SE101', 'SE102', 'CS101', 'CS201', 'MA101', 'BA101']
    for course_id in se_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'SE-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 42
        })
        assignment_id += 1

    # SE-B assignments
    se_b_courses = ['SE101', 'CS202', 'CS301', 'MA102', 'EC101', 'SE201']
    for course_id in se_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'SE-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 48
        })
        assignment_id += 1

    # SE-C assignments
    se_c_courses = ['SE102', 'SE201', 'CS102', 'MA101', 'PH101', 'SE202']
    for course_id in se_c_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'SE-C',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 45
        })
        assignment_id += 1

    # SE-D assignments
    se_d_courses = ['SE201', 'CS202', 'MA102', 'PH201', 'SE301']
    for course_id in se_d_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'SE-D',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 44
        })
        assignment_id += 1

    # EE-A assignments
    ee_a_courses = ['EE101', 'EE102', 'EE201', 'MA101', 'PH101', 'BA101']
    for course_id in ee_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'EE-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 38
        })
        assignment_id += 1

    # EE-B assignments
    ee_b_courses = ['EE202', 'EE301', 'EE302', 'MA102', 'PH201', 'EE103']
    for course_id in ee_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'EE-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 44
        })
        assignment_id += 1

    # EE-C assignments
    ee_c_courses = ['EE101', 'EE201', 'EE301', 'MA101', 'PH101', 'EE203']
    for course_id in ee_c_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'EE-C',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 41
        })
        assignment_id += 1

    # EE-D assignments
    ee_d_courses = ['EE102', 'EE202', 'EE303', 'MA201', 'PH201', 'EE304']
    for course_id in ee_d_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'EE-D',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 40
        })
        assignment_id += 1

    # EE-E assignments
    ee_e_courses = ['EE101', 'EE301', 'EE202', 'MA102', 'PH101', 'EE302']
    for course_id in ee_e_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'EE-E',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 39
        })
        assignment_id += 1

    # ME-A assignments
    me_a_courses = ['ME101', 'ME102', 'ME201', 'MA101', 'PH101', 'BA101']
    for course_id in me_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'ME-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 46
        })
        assignment_id += 1

    # ME-B assignments
    me_b_courses = ['ME301', 'ME201', 'MA102', 'PH201', 'EC101', 'ME202']
    for course_id in me_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'ME-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 43
        })
        assignment_id += 1

    # ME-C assignments
    me_c_courses = ['ME102', 'ME202', 'ME302', 'MA101', 'PH101', 'ME303']
    for course_id in me_c_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'ME-C',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 45
        })
        assignment_id += 1

    # ME-D assignments
    me_d_courses = ['ME101', 'ME201', 'ME302', 'MA201', 'PH201', 'ME303']
    for course_id in me_d_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'ME-D',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 41
        })
        assignment_id += 1

    # BBA-A assignments
    bba_a_courses = ['BA101', 'BA102', 'EC101', 'MA101', 'CS101']
    for course_id in bba_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'BBA-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 55
        })
        assignment_id += 1

    # BBA-B assignments
    bba_b_courses = ['BA102', 'BA201', 'EC102', 'MA101', 'CS101']
    for course_id in bba_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'BBA-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 52
        })
        assignment_id += 1

    # BBA-C assignments
    bba_c_courses = ['BA101', 'BA201', 'EC101', 'MA102', 'CS102']
    for course_id in bba_c_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'BBA-C',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 50
        })
        assignment_id += 1

    # ECO-A assignments
    eco_a_courses = ['EC101', 'EC102', 'MA101', 'BA101', 'CS101']
    for course_id in eco_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'ECO-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 48
        })
        assignment_id += 1

    # ECO-B assignments
    eco_b_courses = ['EC102', 'EC201', 'MA102', 'BA102', 'CS101']
    for course_id in eco_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'ECO-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 46
        })
        assignment_id += 1

    # GS-A assignments
    gs_a_courses = ['PH101', 'CS101', 'MA101', 'BA101', 'EC101']
    for course_id in gs_a_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'GS-A',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 50
        })
        assignment_id += 1

    # GS-B assignments
    gs_b_courses = ['PH201', 'CS102', 'MA102', 'BA102', 'EC102']
    for course_id in gs_b_courses:
        teacher = random.choice(teachers_data)
        course_assignments_data.append({
            'Assignment_ID': f'A{assignment_id:04d}',
            'Section_ID': 'GS-B',
            'Course_ID': course_id,
            'Teacher_ID': teacher['Teacher_ID'],
            'Student_Count': 48
        })
        assignment_id += 1

    # 7. TIME SLOTS
    time_slots_data = [
        {'Slot_ID': 'S1', 'Start_Time': '08:00', 'End_Time': '09:30', 'Duration_Minutes': 90},
        {'Slot_ID': 'S2', 'Start_Time': '09:40', 'End_Time': '11:10', 'Duration_Minutes': 90},
        {'Slot_ID': 'S3', 'Start_Time': '11:20', 'End_Time': '12:50', 'Duration_Minutes': 90},
        {'Slot_ID': 'S4', 'Start_Time': '13:00', 'End_Time': '15:00', 'Duration_Minutes': 120},
        {'Slot_ID': 'S5', 'Start_Time': '15:10', 'End_Time': '16:40', 'Duration_Minutes': 90},
        {'Slot_ID': 'S6', 'Start_Time': '16:45', 'End_Time': '18:15', 'Duration_Minutes': 90},
        {'Slot_ID': 'S7', 'Start_Time': '18:15', 'End_Time': '19:45', 'Duration_Minutes': 90},
        {'Slot_ID': 'S8', 'Start_Time': '19:45', 'End_Time': '21:15', 'Duration_Minutes': 90}
    ]

    # 8. DAYS
    days_data = [
        {'Day_ID': 'MON', 'Day_Name': 'Monday', 'Order': 1},
        {'Day_ID': 'TUE', 'Day_Name': 'Tuesday', 'Order': 2},
        {'Day_ID': 'WED', 'Day_Name': 'Wednesday', 'Order': 3},
        {'Day_ID': 'THU', 'Day_Name': 'Thursday', 'Order': 4},
        {'Day_ID': 'FRI', 'Day_Name': 'Friday', 'Order': 5}
    ]

    # Create Excel file with multiple sheets
    with pd.ExcelWriter('university_database_large.xlsx', engine='openpyxl') as writer:
        pd.DataFrame(rooms_data).to_excel(writer, sheet_name='Rooms', index=False)
        pd.DataFrame(labs_data).to_excel(writer, sheet_name='Labs', index=False)
        pd.DataFrame(teachers_data).to_excel(writer, sheet_name='Teachers', index=False)
        pd.DataFrame(courses_data).to_excel(writer, sheet_name='Courses', index=False)
        pd.DataFrame(sections_data).to_excel(writer, sheet_name='Sections', index=False)
        pd.DataFrame(course_assignments_data).to_excel(writer, sheet_name='Course_Assignments', index=False)
        pd.DataFrame(time_slots_data).to_excel(writer, sheet_name='Time_Slots', index=False)
        pd.DataFrame(days_data).to_excel(writer, sheet_name='Days', index=False)

    print("✓ Large database generated successfully: university_database_large.xlsx")
    print(f"  - {len(rooms_data)} Rooms (Buildings Z, A, B, and P with expanded ranges)")
    print(f"  - {len(labs_data)} Labs (28 labs across 7 types)")
    print(f"  - {len(teachers_data)} Teachers")
    print(f"  - {len(courses_data)} Courses")
    print(f"  - {len(sections_data)} Sections (25 sections covering 8 departments)")
    print(f"  - {len(course_assignments_data)} Course Assignments")
    print(f"  - 8 Time Slots")
    print(f"  - 5 Days per week")


if __name__ == "__main__":
    generate_large_database()
