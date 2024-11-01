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


profile_specific_requirements = {
    "hp": 120,
    "advanced":90,
    #"mandatory": "...." #implement same course name later
}


def main():
    course_list = []
    course_list.append(Course("Avancerad c++",6,1,0,0,0,1))
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return
    
    with open ('courses.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    course_list = data.get("courses")
    print(course_list)

    x = [solver.NumVar(0, 1, "x"+str(i)) for i in range(0,len(course_list))]
    print("Number of variables =", solver.NumVariables())

    # Constraints
    # Read exactly 120 credits
    solver.Add(sum(course_list[i]["hp"]*x[i] for i in range (0, len(course_list))) == 120)
    # Atleast 90 credits advanced
    solver.Add(sum(course_list[i]["hp"]*course_list[i]["advanced"]*x[i] for i in range (0, len(course_list))) >= 90)

   

if __name__ == "__main__":
    main()
