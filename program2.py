import time
MetaData_File = open("META_DATA.txt","r")
Attributes = []
for i in MetaData_File:
	i = i.split(";")
	Attribute_Properties={}
	Attribute_Properties["Attribute_Name"] = i[0]
	Attribute_Properties["Attribute_Type"] = i[1]
	Attribute_Properties["Attribute_Size"] = i[2]
	Attributes.append(Attribute_Properties)
NoOfAttributes = len(Attributes)

print "Please Provide Input File in Double_Quotes"
a = input()
DataBase_File = open(a,"r")   # Reading File
DataBase = []    # Made a List to Store Data Orgnaizedly
for i in DataBase_File:
  	i = i.split(";")
	Data = {} # Made a Dictionary for Key and Values of Attributes
	for j in range(0,NoOfAttributes):
		if(len(i[j])<int(Attributes[j]["Attribute_Size"])):
			Data[Attributes[j]["Attribute_Name"]]=i[j]
		else:
			k = str(i[j])
			l = int(Attributes[j]["Attribute_Size"])
			Data[Attributes[j]["Attribute_Name"]]=k[:l]
	DataBase.append(Data) # Our List Consists of Dictionaries

DataBaseLen = len(DataBase)
DataLen = len(Data)
print DataLen
# PRINTING CONTENT OD DATA FILE #
Start_Time = time.time()
print "CONTENT OF DATA FILE\n"
for j in range(0, DataBaseLen):
	#print "ID = " + DataBase[j]["ID"] + "   STATUS = " + DataBase[j]["STATUS"] + "   PRICE = " + DataBase[j]["PRICE"]
	temp = ""
	for k in range(0, DataLen):
		temp = temp + Attributes[k]["Attribute_Name"]
		temp = temp + " = "
		temp = temp + DataBase[j][Attributes[k]["Attribute_Name"]]
		temp = temp + "     "
	print temp
print ""
End_Time = time.time()
Total_Time_Taken = End_Time - Start_Time
print "Time Take for Printing the Content = " + str(Total_Time_Taken)
k = 1
j = 0
# Function Defined to get Sum of Attributes

while(j != 1 and k != 0):
	print "Enter Your Attribute to get Sum"
	a = raw_input()
	c = ""
	m = 0
	for m in range(0,len(Attributes)):
		if(a == Attributes[m]["Attribute_Name"]):
			c = Attributes[m]["Attribute_Type"]
			break
	if(c == "I"):
		count = 0
		for j in range(0, DataBaseLen):
			l = int(DataBase[j][Attributes[m]["Attribute_Name"]])
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
	elif(c == "F"):
		count = 0
		for j in range(0, DataBaseLen):
			l = float(DataBase[j][Attributes[m]["Attribute_Name"]])
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
	elif(c == "C"):
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