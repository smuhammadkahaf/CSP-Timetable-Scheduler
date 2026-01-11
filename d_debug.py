import pandas as pd
from collections import defaultdict


def check_duplicate_subjects(excel_file_path):
    """
    Check if any section has more than one class of the same subject on the same day.
    Ignores consecutive slots (labs) as they are valid.

    Args:
        excel_file_path: Path to the Excel file containing timetables

    Returns:
        Dictionary with results for each section
    """
    try:
        # Read all sheets from the Excel file
        excel_file = pd.ExcelFile(excel_file_path)

        results = {}
        issues_found = False

        print("=" * 80)
        print("TIMETABLE DUPLICATE SUBJECT CHECKER")
        print("=" * 80)
        print()

        # Process each sheet (section)
        for sheet_name in excel_file.sheet_names:
            print(f"Checking Section: {sheet_name}")
            print("-" * 80)

            # Read the sheet
            df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

            # Get the day column (usually first column)
            day_column = df.columns[0]

            section_issues = []

            # Iterate through each row (each day)
            for idx, row in df.iterrows():
                day = row[day_column]

                # Skip if day is NaN or empty
                if pd.isna(day) or str(day).strip() == '':
                    continue

                # Extract all subjects for this day with their time slot positions
                time_slots = []
                for col_idx, col in enumerate(df.columns[1:], start=1):  # Skip the day column
                    cell_value = row[col]

                    # Skip empty cells
                    if pd.isna(cell_value) or str(cell_value).strip() == '':
                        time_slots.append(None)
                        continue

                    # Extract subject name (first line of the cell)
                    cell_text = str(cell_value).strip()
                    lines = cell_text.split('\n')

                    if lines and lines[0].strip():
                        subject = lines[0].strip()
                        time_slots.append(subject)
                    else:
                        time_slots.append(None)

                # Find all occurrences of each subject
                subject_positions = defaultdict(list)
                for pos, subject in enumerate(time_slots):
                    if subject:
                        subject_positions[subject].append(pos)

                # Check for duplicates that are NOT consecutive
                for subject, positions in subject_positions.items():
                    if len(positions) > 1:
                        # Check if all occurrences are consecutive (lab slots)
                        is_consecutive = True
                        sorted_positions = sorted(positions)

                        for i in range(len(sorted_positions) - 1):
                            if sorted_positions[i + 1] - sorted_positions[i] != 1:
                                is_consecutive = False
                                break

                        if not is_consecutive:
                            # Non-consecutive duplicates found - this is an issue
                            issue = {
                                'day': day,
                                'subject': subject,
                                'count': len(positions),
                                'slots': [pos + 1 for pos in positions]  # +1 for human-readable slot numbers
                            }
                            section_issues.append(issue)
                            issues_found = True
                            slot_info = ", ".join([f"Slot {s}" for s in issue['slots']])
                            print(
                                f"  ⚠️  NON-CONSECUTIVE DUPLICATE on {day}: '{subject}' appears {len(positions)} times at {slot_info}")
                        else:
                            # Consecutive slots - this is a lab, which is valid
                            print(
                                f"  ℹ️  Lab detected on {day}: '{subject}' in {len(positions)} consecutive slots (Valid)")

            if not section_issues:
                print(f"  ✓ No problematic duplicate subjects found")

            print()

            results[sheet_name] = section_issues

        # Summary
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)

        if issues_found:
            print("⚠️  Issues found in the following sections:")
            print()
            for section, issues in results.items():
                if issues:
                    print(f"Section: {section}")
                    for issue in issues:
                        slot_info = ", ".join([f"Slot {s}" for s in issue['slots']])
                        print(f"  - Day: {issue['day']}")
                        print(f"    Subject: {issue['subject']}")
                        print(f"    Appears {issue['count']} times at: {slot_info}")
                        print(f"    Status: NON-CONSECUTIVE (Potential Issue)")
                    print()
        else:
            print("✓ No problematic duplicate subjects found in any section!")
            print("  (Consecutive duplicates detected as labs are considered valid)")

        return results

    except FileNotFoundError:
        print(f"Error: File '{excel_file_path}' not found!")
        return None
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None


# Example usage
if __name__ == "__main__":
    # Replace with your actual file path
    file_path = "generated_timetable_csp.xlsx"  # Change this to your Excel file path


    results = check_duplicate_subjects(file_path)

    if results is not None:
        print("\nCheck complete!")