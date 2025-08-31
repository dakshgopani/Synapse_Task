n=[
[1,0,0,0,1],
[1,0,1,1,1],
[1,1,0,1,1],
[1,0,1,1,0],
[0,1,0,1,1]
]

def count_ones(i, j):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if n[x][y] == 1:
                count += 1
    return count

m = 3
result = 0
blast_radius = None

for i in range(1, len(n)-1):    
    for j in range(1, len(n[i])-1):
        if n[i][j] == 0:
            continue
        else:
            m = count_ones(i, j)
            if m > result:  
                result = m
                blast_radius = (i, j)

if blast_radius:
    print(f"Blast at {blast_radius} with damage {result} to the island")
else:
    print("No land to blast")