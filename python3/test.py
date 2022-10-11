x = 14
for i in range(0,50):
	z = (x * i)/26
	r = (z - int(z))*26
	if round(r)<=1 :
		print ("the number :" +str(i) , str(r))
