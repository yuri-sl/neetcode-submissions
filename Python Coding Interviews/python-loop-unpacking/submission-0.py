from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    save_student = ''
    save_grade = 0
    for score in scores:
        student,grade = score[0],score[1]
        if grade > save_grade:
            save_grade = grade
            save_student = student
    return save_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
