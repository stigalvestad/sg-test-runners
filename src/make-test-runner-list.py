

import csv
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Course:
    num: int
    name: str
    difficulty: int


@dataclass
class TestRunner:
    name: str
    max_course: int
    max_difficulty: int
    sorting: float
    day: str


courses = [
    Course(1, "A - H21", 1),
    Course(2, "A - AL-åpen", 1),
    Course(3, "A - H17-20, H35-", 1),
    Course(4, "A - D21-, H40-", 1),
    Course(5, "A - D17-20, D35-, H45-", 1),
    Course(6, "A - D40-, D45-, H50-", 1),
    Course(7, "A - AM-åpen", 1),
    Course(8, "A - H15-16", 1),
    Course(9, "A - D50-, H55-, H60-", 1),
    Course(10, "A - D15-16", 1),
    Course(11, "A - D55-, D60-, H65-, H70-", 1),
    Course(12, "A - AK-åpen", 1),
    Course(13, "B - D13-14, H13-14", 2),
    Course(14, "B - B-åpen 10-16, B-åpen 17-", 2),
    Course(15, "A - D65-, D70-, D75-, D80-, H75-, H80-, H85-, D85-", 1),
    Course(16, "C - C-åpen 17-", 3),
    Course(17, "C - C-åpen 10-16", 3),
    Course(18, "C - D11-12, H11-12", 3),
    Course(19, "N - N2-åpen 17-", 4),
    Course(20, "N - N2-åpen 9-16, D9-10, H9-10", 4),
    Course(21, "N - N1-åpen", 4),
]

THURSDAY = "Torsdag"
FRIDAY = "Fredag"
SATURDAY = "Lørdag"
SUNDAY = "Søndag"

def find_match(course: Course, day: str, runners: List[TestRunner]) -> Optional[TestRunner]:
    for runner in runners:
        if runner.day == day and runner.max_difficulty <= course.difficulty and runner.max_course <= course.num:
            return runner
    return None


def difficulty_to_int(difficulty: str):
    if difficulty == "A":
        return 1
    if difficulty == "B":
        return 2
    if difficulty == "C":
        return 3
    return 4


def print_test_runners(day, runners: List[TestRunner]):
    print(f"------=========------")
    print(f"------{day}------")

    sorted_runners = sorted(runners, key=lambda x: x.sorting)
    c_copy = courses.copy()

    for course in c_copy:
        matching_runner = find_match(course, day, sorted_runners)
        print(f"{course.num} ({course.name}):\t{matching_runner.name if matching_runner else '--MANGLER--'}")
        if matching_runner:
            sorted_runners.remove(matching_runner)
        if course.num in {8, 10, 13}:
            # copy of the stuff above
            matching_runner = find_match(course, day, sorted_runners)
            print(f"{course.num} ({course.name}):\t{matching_runner.name if matching_runner else '--MANGLER--'}")
            if matching_runner:
                sorted_runners.remove(matching_runner)

    print(f"- - - reserveliste - - -")
    has_reserves = False
    for runner_left_over in sorted_runners:
        if runner_left_over.day == day:
            has_reserves = True
            print(f"{runner_left_over.name}")
    if not has_reserves:
        print(f"ingen reserver")


with open("input.csv", "r", encoding="utf8") as test_runners_file:
    tsv_reader = csv.DictReader(test_runners_file, delimiter="\t")

    runners = []
    for row in tsv_reader:
        name = row["Navn"]
        max_course = int(row["MaxCourse"])
        max_difficulty = difficulty_to_int(row["MaxDifficulty"])
        sorting = float(row["Sorting"])

        thursday = True if row[THURSDAY].strip() else False
        friday = True if row[FRIDAY].strip() else False
        saturday = True if row[SATURDAY].strip() else False
        sunday = True if row[SUNDAY].strip() else False
        if thursday:
            runners.append(TestRunner(name=name,
                                      max_course=max_course,
                                      max_difficulty=max_difficulty,
                                      sorting=sorting,
                                      day=THURSDAY))
        if friday:
            runners.append(TestRunner(name=name,
                                      max_course=max_course,
                                      max_difficulty=max_difficulty,
                                      sorting=sorting,
                                      day=FRIDAY))
        if saturday:
            runners.append(TestRunner(name=name,
                                      max_course=max_course,
                                      max_difficulty=max_difficulty,
                                      sorting=sorting,
                                      day=SATURDAY))
        if sunday:
            runners.append(TestRunner(name=name,
                                      max_course=max_course,
                                      max_difficulty=max_difficulty,
                                      sorting=sorting,
                                      day=SUNDAY))

    print_test_runners(THURSDAY, runners)
    print("")
    print_test_runners(FRIDAY, runners)
    print("")
    print_test_runners(SATURDAY, runners)
    print("")
    print_test_runners(SUNDAY, runners)

    # for row in tsv_reader:
    #     name = row["Navn"]
    #     ranking = row["Klubb"]
    #     print(f"{name} is rank {ranking}")

