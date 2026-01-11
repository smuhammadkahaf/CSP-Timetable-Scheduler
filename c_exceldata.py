import pandas as pd
import random


def generate_database():
    """Generate improved university database with proper lab assignments"""

    # 1. ROOMS - Z103-Z120, Z203-Z220, A103-A120, A203-A220, P1-P9
    rooms_data = []

    # Building Z: Z103 to Z120
    for room_num in range(103, 121):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'Z{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building Z: Z203 to Z220
    for room_num in range(203, 221):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'Z{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building A: A103 to A120
    for room_num in range(103, 121):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'A{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building A: A203 to A220
    for room_num in range(203, 221):
        strength = random.choice([30, 40, 50, 60])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'A{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # Building P: P1 to P9
    for room_num in range(1, 10):
        strength = random.choice([40, 50, 60, 80])
        has_multimedia = random.choice([True, False])
        rooms_data.append({
            'Room_Number': f'P{room_num}',
            'Strength': strength,
            'Multimedia': has_multimedia
        })

    # 2. LABS - Specific labs with types
    labs_data = [
        {'Lab_Name': 'Computer Lab 1', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 2', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 3', 'Strength': 35, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 4', 'Strength': 30, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Computer Lab 5', 'Strength': 35, 'Lab_Type': 'Computer'},
        {'Lab_Name': 'Physics Lab', 'Strength': 25, 'Lab_Type': 'Physics'},
        {'Lab_Name': 'Power System Lab', 'Strength': 30, 'Lab_Type': 'Power'},
        {'Lab_Name': 'Machine Lab', 'Strength': 25, 'Lab_Type': 'Machine'},
        {'Lab_Name': 'DLD Lab', 'Strength': 35, 'Lab_Type': 'DLD'},
        {'Lab_Name': 'VLSI Lab', 'Strength': 30, 'Lab_Type': 'VLSI'},
        {'Lab_Name': 'Control Lab', 'Strength': 30, 'Lab_Type': 'Control'},
        {'Lab_Name': 'ELE Communication Lab', 'Strength': 35, 'Lab_Type': 'Communication'}
    ]

    # 3. TEACHERS - Pakistani names only
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
        {'Teacher_ID': 'T026', 'Teacher_Name': 'Dr. Muhammad Imran Shehzad'}
    ]

    # 4. COURSES - With proper lab type assignments
    courses_data = [
        {'Course_ID': 'CS101', 'Course_Name': 'Introduction to Programming', 'Theory_Classes_Per_Week': 2,
         'Has_Lab': True, 'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS102', 'Course_Name': 'Data Structures', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS201', 'Course_Name': 'Algorithms', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS202', 'Course_Name': 'Database Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS301', 'Course_Name': 'Operating Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS302', 'Course_Name': 'Computer Networks', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS401', 'Course_Name': 'Artificial Intelligence', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'CS402', 'Course_Name': 'Machine Learning', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'SE101', 'Course_Name': 'Software Engineering', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'SE201', 'Course_Name': 'Web Development', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Computer', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE101', 'Course_Name': 'Circuit Analysis', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE102', 'Course_Name': 'Digital Logic Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'DLD', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE201', 'Course_Name': 'Electronics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE202', 'Course_Name': 'Power Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Power', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE301', 'Course_Name': 'Control Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Control', 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
        {'Course_ID': 'EE302', 'Course_Name': 'Communication Systems', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Communication', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME101', 'Course_Name': 'Engineering Mechanics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME201', 'Course_Name': 'Thermodynamics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'ME301', 'Course_Name': 'Machine Design', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Machine', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'MA101', 'Course_Name': 'Calculus I', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'MA102', 'Course_Name': 'Linear Algebra', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'PH101', 'Course_Name': 'Physics I', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'PH201', 'Course_Name': 'Physics II', 'Theory_Classes_Per_Week': 2, 'Has_Lab': True,
         'Lab_Type': 'Physics', 'Needs_Multimedia': False, 'Is_2Hour_Special': False},
        {'Course_ID': 'BA101', 'Course_Name': 'Business Management', 'Theory_Classes_Per_Week': 1, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': True},
        {'Course_ID': 'EC101', 'Course_Name': 'Microeconomics', 'Theory_Classes_Per_Week': 2, 'Has_Lab': False,
         'Lab_Type': None, 'Needs_Multimedia': True, 'Is_2Hour_Special': False},
    ]

    # 5. SECTIONS - Simple structure
    sections_data = []
    section_names = ['CS-A', 'CS-B', 'CS-C', 'SE-A', 'SE-B', 'EE-A', 'EE-B', 'EE-C', 'ME-A', 'ME-B']

    for i, section_name in enumerate(section_names, 1):
        sections_data.append({
            'Section_ID': section_name,
            'Student_Count': random.randint(35, 55)
        })

    # 6. COURSE ASSIGNMENTS - Assign courses to sections with teachers
    course_assignments_data = []
    assignment_id = 1

    # CS-A assignments
    cs_a_courses = ['CS101', 'CS102', 'MA101', 'PH101', 'BA101', 'CS201']
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
    cs_b_courses = ['CS101', 'CS102', 'MA102', 'PH201', 'EC101', 'CS202']
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
    cs_c_courses = ['CS301', 'CS302', 'CS401', 'SE101', 'MA101', 'CS402']
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

    # SE-A assignments
    se_a_courses = ['SE101', 'SE201', 'CS101', 'CS201', 'MA101', 'BA101']
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
    se_b_courses = ['SE101', 'CS202', 'CS301', 'MA102', 'EC101']
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
    ee_b_courses = ['EE202', 'EE301', 'EE302', 'MA102', 'PH201']
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
    ee_c_courses = ['EE101', 'EE201', 'EE301', 'MA101', 'PH101']
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

    # ME-A assignments
    me_a_courses = ['ME101', 'ME201', 'MA101', 'PH101', 'BA101', 'EE101']
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
    me_b_courses = ['ME301', 'ME201', 'MA102', 'PH201', 'EC101']
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
    with pd.ExcelWriter('university_database.xlsx', engine='openpyxl') as writer:
        pd.DataFrame(rooms_data).to_excel(writer, sheet_name='Rooms', index=False)
        pd.DataFrame(labs_data).to_excel(writer, sheet_name='Labs', index=False)
        pd.DataFrame(teachers_data).to_excel(writer, sheet_name='Teachers', index=False)
        pd.DataFrame(courses_data).to_excel(writer, sheet_name='Courses', index=False)
        pd.DataFrame(sections_data).to_excel(writer, sheet_name='Sections', index=False)
        pd.DataFrame(course_assignments_data).to_excel(writer, sheet_name='Course_Assignments', index=False)
        pd.DataFrame(time_slots_data).to_excel(writer, sheet_name='Time_Slots', index=False)
        pd.DataFrame(days_data).to_excel(writer, sheet_name='Days', index=False)

    print("✓ Database generated successfully: university_database.xlsx")
    print(f"  - {len(rooms_data)} Rooms (Z103-Z120, Z203-Z220, A103-A120, A203-A220, P1-P9)")
    print(f"  - {len(labs_data)} Labs with types")
    print(f"  - {len(teachers_data)} Teachers")
    print(f"  - {len(courses_data)} Courses with lab type mappings")
    print(f"  - {len(sections_data)} Sections")
    print(f"  - {len(course_assignments_data)} Course Assignments")


if __name__ == "__main__":
    generate_database()