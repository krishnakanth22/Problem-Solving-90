class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        no_food = 0
        
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                no_food = 0  
            else:
                students.append(students.pop(0))
                no_food += 1

            if no_food == len(students):
                return no_food
                
        return no_food
