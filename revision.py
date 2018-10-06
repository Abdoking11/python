class Grand(object):
	def __init__(self , grand_name , eye_color):
		self.grand_name = grand_name
		self.eye_color = eye_color
class Parent(Grand):
	def __init__(self, grand_name , eye_color , name , baby , Age , job):
		Grand.__init__(self , grand_name ,eye_color)
		self.name = name
		self.baby = baby
		self.Age = Age
		self.job = job
father_info = Parent("Hardy" , "Blue" ,  "Vardy" , "Jamie" , 30 , "Progrmmer")

print father_info.baby + " " + father_info.name + " " + father_info.grand_name 		