# CSP Timetable Scheduler

A Python-based constraint satisfaction problem (CSP) solver for automated timetable scheduling. This project uses constraint satisfaction techniques to efficiently generate conflict-free schedules while respecting various constraints and preferences.

## Overview
The scheduler reads timetable data from Excel files and uses CSP algorithms to find valid schedule assignments. It handles multiple constraints such as room availability, instructor schedules, student course selections, and time slot conflicts.

## Author
smuhammadkahaf

## Project Structure

### a_main.py
Main entry point of the application. Initializes the scheduler, generates the timetable by calling the CSP solver, exports results to Excel, and displays statistics and any failed assignments requiring manual review.

### b_CSPTimetableScheduler.py
Core CSP scheduler implementation. Loads university data (rooms, labs, teachers, courses, sections) from Excel. Implements the backtracking algorithm with constraint satisfaction to assign classes to suitable time slots and rooms while respecting all scheduling constraints.

### c_exceldata.py
Database generation utility. Creates and exports sample university data including rooms, labs, teachers, courses, sections, and course assignments to an Excel file (`university_database.xlsx`). Used for testing the scheduler with realistic data.

### d_debug.py
Debug and validation utility. Checks generated timetables for duplicate subjects (same course appearing multiple times on the same day for a section). Helps verify the quality and validity of generated schedules.

## Setup
Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the main script:
```bash
python a_main.py
```
