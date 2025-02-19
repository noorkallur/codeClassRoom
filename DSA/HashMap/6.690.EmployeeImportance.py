# https://leetcode.com/problems/employee-importance/?envType=problem-list-v2&envId=breadth-first-search

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

def getImportance(self, employees, id: int) -> int:
    def getImportance_helper(id, subordinates):
        imp_sum = id_imp[id]
        for sub_id in subordinates:
            imp_sum += getImportance_helper(sub_id, id_sub[sub_id])
        return imp_sum

    id_imp = {}
    id_sub = {}
    imp_sum = 0
    for emp in employees:
        id_imp[emp.id] = emp.importance
        id_sub[emp.id] = emp.subordinates
    
    return getImportance_helper(id, id_sub[id])


# using anothe techniqe similar to BFS
def getImportance(self, employees, id: int) -> int:
    id_emp_obj = {}

    for emp in employees:
        id_emp_obj[emp.id] = emp

    emp_stk = [id]
    imp_sum = 0
    while emp_stk:
        emp =id_emp_obj[emp_stk.pop()]
        imp_sum += emp.importance
        emp_stk.extend(emp.subordinates)
    
    return imp_sum