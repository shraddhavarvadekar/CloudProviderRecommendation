import csv
import math


def mining_model():


	"""
	Array for storing data for different services

	"""
	a1 = [ 4*[0] for i in range(200) ]
	a2 = [ 4*[0] for i in range(200) ]
	a3 = [ 4*[0] for i in range(200) ]
	a4 = [ 4*[0] for i in range(200) ]
	a5 = [ 4*[0] for i in range(200) ]

	"""
	Array for storing price

	"""
	p1 = []
	p2 = []
	p3 = []
	p4 = []
	p5 = []
	"""
	counter for each category

	"""
	s1 = 0
	s2 = 0
	s3 = 0
	s4 = 0
	s5 = 0

	def roundup(x):
	    return int(math.ceil(x / 10.0)) * 10

	with open('csvfile.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	     	if(row[2] == "TRUE"):
	     		a1[s1][0] = row[0]
	     		a1[s1][1] = row[1]
	     		a1[s1][2] = row[7]
	     		a1[s1][3] = row[2]
	     		p1.append(int(row[0]))
	     		s1 =  s1 + 1

	with open('csvfile.csv', 'rb') as f:
	    reader = csv.reader(f)     		
	    for row in reader:
	     	if(row[3] == "TRUE"):
	     		a2[s2][0] = row[0]
	     		a2[s2][1] = row[1]
	     		a2[s2][2] = row[7]
	     		a2[s2][3] = row[2]	
	     		p2.append(int(row[0]))
	     		s2 = s2 + 1		
	with open('csvfile.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	     	if(row[4] == "TRUE"):
	     		a3[s3][0] = row[0]
	     		a3[s3][1] = row[1]
	     		a3[s3][2] = row[7]	
	     		a3[s3][3] = row[2]
	     		p3.append(int(row[0]))	
	     		s3 = s3 + 1

	with open('csvfile.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	     	if(row[5] == "TRUE"):
	     		a4[s4][0] = row[0]
	     		a4[s4][1] = row[1]
	     		a4[s4][2] = row[7]	
	     		a4[s4][3] = row[2]
	     		p4.append(int(row[0]))
	     		s4 = s4 + 1

	with open('csvfile.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:     		
	     	if(row[6] == "TRUE"):
	     		a5[s5][0] = row[0]
	     		a5[s5][1] = row[1]
	     		a5[s5][2] = row[7]	
	     		a5[s5][3] = row[2]
	     		p5.append(int(row[0]))
	     		s5 = s5 + 1

# to delete extra index for each service

	del a1[s1:200]
	del a2[s2:200]
	del a3[s3:200]
	del a4[s4:200]
	del a5[s5:200]

	"""
	price min and max array for each category

	"""
	pr1 = {}
	pr2 = {}
	pr3 = {}
	pr4 = {}
	pr5 = {}


	# print len(p1)
	# print len(a1)
	# print s1

	# print len(p2)
	# print len(a2)
	# print s2

	# print len(p3)
	# print len(a3)
	# print s3

	# print len(p4)
	# print len(a4)
	# print s4

	# print len(p5)
	# print len(a5)
	# print s5

	pr1["min"] = min(p1)
	pr1["max"] = max(p1)

	pr2["min"] = min(p2)
	pr2["max"] = max(p2)

	pr3["min"] = min(p3)
	pr3["max"] = max(p3)

	pr4["min"] = min(p4)
	pr4["max"] = max(p4)

	pr5["min"] = min(p5)
	pr5["max"] = max(p5)




	# for i in range(len(a1)):
	# 	print a1[i]

	# print "Gee"
	# for i in range(len(a2)):
	# 	print a2[i]	

	# print pr1
	# print pr2
	# print pr3
	# print pr4
	# print pr5

	"""
	Array for storing range

	"""
	p1 = {}
	p2 = {}
	p3 = {}
	p4 = {}
	p5 = {}

	int1 = (pr1['max'] - pr1['min']) / 5
	int2 = (pr2['max'] - pr2['min']) / 5
	int3 = (pr3['max'] - pr3['min']) / 5
	int4 = (pr4['max'] - pr4['min']) / 5
	int5 = (pr5['max'] - pr5['min']) / 5		

	model = []

	"""Service 1"""
	
	provider = []
	mindata = pr1['min']
	for i in range(5):
		p1[i] = {}
		data = {}
		data['start'] = mindata
		data['end'] = mindata + int1
		pricelist = []
		mindata = mindata + int1
		for j in range(len(a1)):
			if(int(a1[j][0])>= int(data['start']) and int(a1[j][0])<= int(data['end'])):
				pricelist.append(a1[j][2])
				provider.append(a1[j][1])
		data['provider'] = provider[pricelist.index(min(pricelist))]	
		data['price'] = min(pricelist)
		p1[i] = data


	"""Service 2"""

	provider = []
	mindata = pr2['min']
	for i in range(5):
		p2[i] = {}
		data = {}
		data['start'] = mindata
		data['end'] = mindata + int2
		pricelist = []
		mindata = mindata + int2
		for j in range(len(a2)):
			if(int(a2[j][0])>= int(data['start']) and int(a2[j][0])<= int(data['end'])):
				pricelist.append(a2[j][2])
				provider.append(a2[j][1])
		data['provider'] = provider[pricelist.index(min(pricelist))]	
		data['price'] = min(pricelist)
		p2[i] = data


	"""Service 3"""

	provider = []
	mindata = pr3['min']
	for i in range(5):
		p3[i] = {}
		data = {}
		data['start'] = mindata
		data['end'] = mindata + int3
		pricelist = []
		mindata = mindata + int3
		for j in range(len(a3)):
			if(int(a3[j][0])>= int(data['start']) and int(a3[j][0])<= int(data['end'])):
				pricelist.append(a3[j][2])
				provider.append(a3[j][1])
		data['provider'] = provider[pricelist.index(min(pricelist))]	
		data['price'] = min(pricelist)		
		p3[i] = data


	"""Service 4"""

	provider = []
	mindata = pr4['min']
	for i in range(5):
		p4[i] = {}
		data = {}
		data['start'] = mindata
		data['end'] = mindata + int4
		pricelist = []
		mindata = mindata + int4
		for j in range(len(a4)):
			if(int(a4[j][0])>= int(data['start']) and int(a4[j][0])<= int(data['end'])):
				pricelist.append(a4[j][2])
				provider.append(a4[j][1])
		data['provider'] = provider[pricelist.index(min(pricelist))]	
		data['price'] = min(pricelist)		
		p4[i] = data		


	"""Service 5"""

	provider = []
	mindata = pr5['min']
	for i in range(5):
		p5[i] = {}
		data = {}
		data['start'] = mindata
		data['end'] = mindata + int5
		pricelist = []
		mindata = mindata + int5
		for j in range(len(a5)):
			if(int(a5[j][0])>= int(data['start']) and int(a5[j][0])<= int(data['end'])):
				pricelist.append(a5[j][2])
				provider.append(a5[j][1])
		data['provider'] = provider[pricelist.index(min(pricelist))]	
		data['price'] = min(pricelist)			
		p5[i] = data		

# conbine rabge for each service and store range
	model.append(p1)
	model.append(p2)
	model.append(p3)
	model.append(p4)
	model.append(p5)			
	return model



def user_screen():
	model = mining_model()
	revenue = input("Enter your revenue : ")
	s = []
	s1 = input("Do you want service 1 : ")
	s.append(s1)
	s2 = input("Do you want service 2 : ")
	s.append(s2)
	s3 = input("Do you want service 3 : ")
	s.append(s3)
	s4 = input("Do you want service 4 : ")
	s.append(s4)
	s5 = input("Do you want service 5 : ")
	s.append(s5)
	result = mining_process(model,revenue,s)
	print "Your recommended Provider is : " + result


def mining_process(model,revenue,s):
	predict_price = []
	predict_provider = []
	for i in range(len(model)):
		if(s[i]==1):
			for  j in range(len(model[i])):
				if(j==0 and revenue<=model[i][j]['end']):
					predict_price.append(int(model[i][j]['price']))
					predict_provider.append(model[i][j]['provider'])
				elif(j==len(model[i])-1 and revenue>=model[i][j]['start']):
					predict_price.append(int(model[i][j]['price']))
					predict_provider.append(model[i][j]['provider'])
				elif(revenue>model[i][j]['start'] and revenue<model[i][j]['end']):
					predict_price.append(int(model[i][j]['price']))
					predict_provider.append(model[i][j]['provider'])
	# print predict_price
	# print predict_provider
	return predict_provider[predict_price.index(min(predict_price))]

user_screen()

