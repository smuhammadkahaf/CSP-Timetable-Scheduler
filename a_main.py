import  time
from b_CSPTimetableScheduler import CSPTimetableScheduler
# ==================== MAIN PROGRAM ====================

def main():
    """Main entry point for the timetable scheduler."""
    print("\n" + "=" * 80)
    print("CSP-BASED TIMETABLE SCHEDULER")
    print("=" * 80)

    # Create scheduler instance
    scheduler = CSPTimetableScheduler('university_database.xlsx')

    # Generate timetable
    start_time = time.time()
    success_count, failed_assignments = scheduler.generate_timetable()
    end_time = time.time()

    # Export to Excel
    scheduler.export_to_excel()

    # Print statistics
    scheduler.print_statistics()

    # Show failed assignments if any
    if failed_assignments:
        print("=" * 80)
        print("FAILED ASSIGNMENTS (Need Manual Review)")
        print("=" * 80)
        for assignment in failed_assignments:
            course_name = scheduler.course_dict[assignment['Course_ID']]['Course_Name']
            print(f"  ✗ {assignment['Section_ID']}: {assignment['Course_ID']} ({course_name})")
        print("=" * 80 + "\n")

    print("✓ TIMETABLE GENERATION COMPLETE!\n")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()