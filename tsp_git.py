import tsp
import requests
import json

print("starting program")

n=int(input("enter the number of cities "))

cityList=[]

for i in range (n):
  cityname=input("enter city " + str(i+1)+"-> ")
  cityList.append(cityname)



startCity=input("Enter start city ->")

for i in range(n):
  if(cityList[i]==startCity):
    temp=cityList[0]
    cityList[0]=cityList[i]
    cityList[i]=temp

 

# initialiing matrix with 0
mat=[]



for i in range(n) :
  for j in range(n): 
    temp_r=requests.get('https://www.distance24.org/route.json?stops='+cityList[i]+'|'+cityList[j]) 
    temp_x = temp_r.json() 
    temp_distance=int(temp_x['distance'] )
    mat.append(temp_distance)    
 


matrix=[]
c=0
for i in range(n):
  mat_row=[]
  for j in range(n):    
    mat_row.append(mat[c])
    c=c+1
  matrix.append(mat_row)

  

print("Adjacecy matrix")
print(matrix)    

print("tsp part in given cities is ")
r = range(len(matrix))
print(r)
# Dictionary of distance
dist = {(i, j): matrix[i][j] for i in r for j in r}
#print(tsp.tsp(r, dist))
city_order_list=tsp.tsp(r, dist)[1]
print("total distance ->",end=" ")
print(tsp.tsp(r, dist)[0])

print("tsp order ",end=" ")
print(tsp.tsp(r, dist)[1])


#printing the cities
for i in range(n):
  print(cityList[city_order_list[i]],end=" -> ")
print(cityList[city_order_list[0]])





