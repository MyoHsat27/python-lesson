students = [
    {
        "name": "Aung Aung",
        "subjects": [
            {"name": "Myanmar", "marks": 60},
            {"name": "English", "marks": 70},
            {"name": "Math", "marks": 80}
        ],
        "status": "student"
     },
    {
        "name": "Hla Hla",
        "subjects": [
            {"name": "Myanmar", "marks": 45},
            {"name": "English", "marks": 90},
            {"name": "Math", "marks": 68}
        ],
        "status": "student"
     },
    {
        "name": "Aung Aung",
        "subjects": [
            {"name": "Myanmar", "marks": 14},
            {"name": "English", "marks": 43},
            {"name": "Math", "marks": 36}
        ],
        "status": "student"
     },
]




student_info = [
    {
        "name": "Aung Aung",
        "mark": 60,
        "status": "student"
     },
    {
        "name": "Myo Myo",
        "mark": 80,
        "status": "student"
    },
    {
        "name": "Hla Hla",
        "mark": 20,
        "status": "student"
     },
]

for student in student_info:
    for info in student:  # {'name': 'Aung Aung', 'mark': 60, 'status': 'student'}
        if info == "mark" and student[info] > 40:
            student['status'] = "graduate"

print(student_info)