class Cone:
	def __init__(foo,Radius,Height):
		foo.Radius = Radius
		foo.Height = Height
		
	def Volume(foo):
		r=foo.Radius
		h=foo.Height
		vol = 3.14*(r**2)*(h/3)
		print( "Volume : ",vol)
		return "Done !"
		
		
	def Surface_area(foo):
		x=foo.Radius
		y=foo.Height
		base=3.14*(x**2)
		side=3.14*(x**2)*(((x**2)+(y**2))**(1/2))
		print("Base : ",base,"  Side : ",side)
		return "Done !"
		
h=int(input("Enter your radius : "))
j=int(input("Enter your height : "))
p1 = Cone(h,j)
print(p1.Volume())
print(p1.Surface_area())