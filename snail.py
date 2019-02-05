n=int(input())
z=int(input())
matrix=[[0 for x in range(n)] for y in range(n)] 
dir=1
rem=2 
dx=0
dy=0
x=1
count=-1
try:
	for i in range(1, n*n+1):
		matrix[n//2+dx][n//2+dy]=i
		
		if i == n*n:
			break
		rem=rem-1
		if rem==0:
			dir=dir+1
			count=count+1
			if count%2==1:
				x=x+1 #prob
			rem+=x
		if dir>4:
			dir=1
		if dir==1: #up
			dx=dx-1
			matrix[n//2+dx][n//2+dy]=i
		elif dir==2: #Right
			dy=dy+1
			matrix[n//2+dx][n//2+dy]=i
		elif dir==3: #down
			dx=dx+1
			matrix[n//2+dx][n//2+dy]=i
		else: #left
			dy=dy-1
			matrix[n//2+dx][n//2+dy]=i

except:
	pass
	
for r in matrix:
	for c in r:
		print( c,"" , end = "" )
	print()
	
for q in range (0, n): #use double for loop to find the two n values :D 
		for w in range (0, n):
			if matrix[q][w]==z:
				print(q+1, w+1)
