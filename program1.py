import time
Start_Time = time.time()
DataBase_File = open("DATA","r")   # Reading File
DataBase = []    # Made a List to Store Data Orgnaizedly
for i in DataBase_File:
  	i = i.split(";")
	Data = {} # Made a Dictionary for Key and Values of Attributes
	Data["ID"] = i[0]
	Data["STATUS"] = i[1]
	Data["PRICE"] = i[2]
	DataBase.append(Data) # Our List Consists of Dictionaries
DataBaseLen = len(DataBase)

# PRINTING CONTENT OD DATA FILE #

print "CONTENT OF DATA FILE\n"
for j in range(0, DataBaseLen):
	print "ID = " + DataBase[j]["ID"] + "   STATUS = " + DataBase[j]["STATUS"] + "   PRICE = " + DataBase[j]["PRICE"]
print ""

End_Time = time.time()
Total_Time_Taken = End_Time - Start_Time
print "Time Take for this Program = " + str(Total_Time_Taken)

k = 1
j = 0

# Function Defined to get Sum of Attributes

while(j != 1 and k != 0):
	print "Enter Your Attribute to get Sum"
	a = raw_input()
	if(a == "ID"):
		count = 0
		for j in range(0, DataBaseLen):
			l = int(DataBase[j]["ID"])
			count = count + l
		print count
		print "Enter 1 to Exit or 0 to Give an Attribute"
		b = raw_input()
		b = str(b)
		while(b!="0" and b!="1"):
			print "WRONG KEY ENTERED"
			print "Enter 1 to Exit or 0 to Give an Attribute"
			b = raw_input()
			b = str(b)
		if(b == "1"):
			j = 1
	elif(a == "STATUS"):
		print "ERROR! It's a String Type Attribute"
		print "Enter 1 to Exit or 0 to Give an Attribute"
		b = raw_input()
		b = str(b)
		while(b!="0" and b!="1"):
			print "WRONG KEY ENTERED"
			print "Enter 1 to Exit or 0 to Give an Attribute"
			b = raw_input()
			b = str(b)
		if(b == "1"):
			j = 1
		elif(b == "0"):
			j = 0
	elif(a == "PRICE"):
		count = 0
		for j in range(0, DataBaseLen):
			l = DataBase[j]["PRICE"]
			l=float(l)
			count = count + l
		print count
		print "Enter 1 to Exit or 0 to Give an Attribute"
		b = raw_input()
		b = str(b)
		while(b!="0" and b!="1"):
			print "WRONG KEY ENTERED"
			print "Enter 1 to Exit or 0 to Give an Attribute"
			b = raw_input()
			b = str(b)
		if(b == "1"):
			j = 1
	else:
		print "UnKnown Attribute"
		print "Enter 1 to Exit or 0 to Give an Attribute"
		b = raw_input()
		b = str(b)
		while(b!="0" and b!="1"):
			print "WRONG KEY ENTERED"
			print "Enter 1 to Exit or 0 to Give an Attribute"
			b = raw_input()
			b = str(b)	
		if(b == "1"):
			j = 1