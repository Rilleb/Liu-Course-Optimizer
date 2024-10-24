# TODO 
# Add datastructure for schedule
import json
from dataclasses import dataclass
from ortools.linear_solver import pywraplp

@dataclass #not used
class Course:
    name: str
    hp: int
    advanced: int #1 true, 0 false
    profile_specific: int #1 true, 0 false
    mandatory: int #1 true, 0 false
    user_required: int #1 true, 0 false
    time_block: int #between 1 and 4


def main():
    course_list = []
    course_list.append(Course("Avancerad c++",6,1,0,0,0,1))
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return
    
    with open ('courses.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    course_list = data.get("courses")
    print(courses)
    x = [] # {0,1} course is taken 
    c = [] # number of credits for the course
    w = [] # {0,1} course is wanted 
    m = [] # {0,1} course is mandatory 
    a = [] # {0,1} course is advanced 

    courses = [solver.NumVar(0, 1, course[0]) for course in course_list]
    print("Number of variables =", solver.NumVariables())

    # Constraints
    constraints = []
    for i, course in enumerate(course_list):
        constraints.append(solver.Constraint())

if __name__ == "__main__":
    main()
