from student import Student
from student import Project

# class MBAStudent(Student):

# 	def __init__(self, name, ID, ca, csug, nywe):
# 		# Initially just calling superclass init, 
# 		# but has room for adding new attributes
# 		# specific to an MBA student. 
# 		super(MBAStudent, self).__init__(name, ID, ca, csug, nywe)

# Random test cases for proper use of inheritance / getters and setters. 
if __name__ == "__main__":

 # 	def __init__ (self, name, ID, degree_pursuing, cod_abil, cs_ug, num_yrs_work_exp):

 	# NOTE: This is going to error. Not imperative to fix this -- just a random test.
 	lst = range(28, 39)
 	ranks_lst = map(lambda x: x * 65, lst)
	a = Student("Ameyayayaya", 2886650, 1, 0, 3, 6, ranks_lst)
	
	# print a.name
	# print a.ID
	# print a.degree_pursuing
	# print a.coding_ability
	# print a.was_cs_ug
	# print a.work_experience
	# print a.project_rankings