# TODO 
# Implement solution for same course being able to be taken in different periods or going over two continuous periods.
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
    # Atleast 30 HP within main area (ex computer science)
    solver.Add(sum(course_list[i]["hp"]*course_list[i]["main_area"]*x[i] for i in range (0, len(course_list))) >= 90)

    # Max 18 hp per period (6 periods) and no overlapping time-blocks (4 time-blocks in each period)
    for j in  range (1,7):
        same_period_courses = [x.index() for x in course_list if course_list[x]["period"] == j] #indexes of all courses going in period j
        solver.Add(sum(course_list[i]["hp"]*x[i] for i in same_period_courses) <= 18)
        for k in range (1,5):
            same_time_block_courses = [x for x in same_period_courses if course_list[x]["time_block"] == k] #indexes of all courses going in period j and time-block k
            solver.Add(sum(x[i] for i in same_time_block_courses) <= 1)




   

if __name__ == "__main__":
    main()
