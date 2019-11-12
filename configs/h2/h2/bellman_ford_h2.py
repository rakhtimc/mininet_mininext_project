import os
cost_map = {}
f1=open("r4.txt","r")
lines1=f1.readlines()
result1=[]

f2=open("h2.txt","a+")
lines2=f2.readlines()
result2=[]

List = []

for x in lines1:
    k=-1
    for y in lines2:
        cost_map.update( {y.split(' ')[0] : y.split(' ')[2]} )
        k = k+1
        if(k not in List):
            if(x.split(' ')[0] == y.split(' ')[0] and x.split(' ')[0] != "h2"):
                if(int(x.split(' ')[2]) + int(cost_map.get("r4")) < int(y.split(' ')[2])):
                    newEntry = x.split(' ')[0] + " " + "r4" +" " + str(int(x.split(' ')[2]) + int(cost_map.get("r4")))
                    List.append(k)
                    cost_map.update( {x.split(' ')[0] : str(int(x.split(' ')[2]) + int(cost_map.get("r4")))} )
                    f2.write(newEntry+"\n")

    if(x.split(' ')[0] not in cost_map and x.split(' ')[0] != "h2"):
                    newEntry = x.split(' ')[0] + " " + "r4" +" " + str(int(x.split(' ')[2]) + int(cost_map.get("r4")))
                    cost_map.update( {x.split(' ')[0] : str(int(x.split(' ')[2]) + int(cost_map.get("r4")))} )
                    f2.write(newEntry+"\n")

f1.close()
f2.close()

f2=open("h2.txt","a+")
lines2=f2.readlines()

f3=open("new_file.txt","a")
#lines3=f3.readlines()
counter = -1
for y in lines2:
	counter = counter + 1
	if(counter not in List):
		f3.write(y)

f2.close
os.remove('h2.txt')
os.rename('new_file.txt','h2.txt') 	
f3.close()


