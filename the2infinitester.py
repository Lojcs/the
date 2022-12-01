import os, sys, subprocess, random, math, numpy

def intersect(seg1, seg2):
	if seg1[1][0] + seg1[2][0] != seg2[1][0] + seg2[2][0] or seg1[1][1] + seg1[2][1] != seg2[1][1] + seg2[2][1] and seg1[1][0] - seg1[2][0] != seg2[1][0] + seg2[2][0] or seg1[1][1] - seg1[2][1] != seg2[1][1] + seg2[2][1] and seg1[1][0] + seg1[2][0] != seg2[1][0] - seg2[2][0] or seg1[1][1] + seg1[2][1] != seg2[1][1] - seg2[2][1] and seg1[1][0] - seg1[2][0] != seg2[1][0] - seg2[2][0] or seg1[1][1] - seg1[2][1] != seg2[1][1] - seg2[2][1]:
		if seg2[1][0]-seg2[2][0] <= seg1[1][0]-seg1[2][0] <= seg2[1][0]+seg2[2][0] or seg2[1][0]-seg2[2][0] <= seg1[1][0]+seg1[2][0] <= seg2[1][0]+seg2[2][0] or seg1[1][0]-seg1[2][0] <= seg2[1][0]-seg2[2][0] <= seg1[1][0]+seg1[2][0] or seg1[1][0]-seg1[2][0] <= seg2[1][0]+seg2[2][0] <= seg1[1][0]+seg1[2][0] and seg2[1][1]-seg2[2][1] <= seg1[1][1]-seg1[2][1] <= seg2[1][1]+seg2[2][1] or seg2[1][1]-seg2[2][1] <= seg1[1][1]+seg1[2][1] <= seg2[1][1]+seg2[2][1] or seg1[1][1]-seg1[2][1] <= seg2[1][1]-seg2[2][1] <= seg1[1][1]+seg1[2][1] or seg1[1][1]-seg1[2][1] <= seg2[1][1]+seg2[2][1] <= seg1[1][1]+seg1[2][1]:
			if len(seg1[0]) == 1 or len(seg2[0]) == 1:
				return True
			c = int(seg1[0][2])-int(seg2[0][2])
			a = int(seg1[0][0])/int(seg2[0][0])
			c = c/int(seg2[0][0])
			c = a*int(seg1[0][1]) - c - int(seg2[0][1])
			a -= 1
			x = c/a
			if seg1[1][0]-seg1[2][0] < x < seg1[1][0]+seg1[2][0] or seg2[1][0]-seg2[2][0] < x < seg2[1][0]+seg2[2][0]: # TODO VERY IMPORTANT: Test for presicion loss
				y = seg1[0][0]*(x-seg1[0][1]) + seg1[0][2]
				if seg1[1][1]-seg1[2][1] < y < seg1[1][1]+seg1[2][1] or seg2[1][1]-seg2[2][1] < y < seg2[1][1]+seg2[2][1]:
					return True
	return False
			
def gencord(poly, i):
	cord = random.randrange(1000)/2
	same = 0
	for corner in poly:
		if corner[i] == cord:
			same += 1
			if same == 2:
				return gencord(poly, i)
	return cord
def genpoly(n=4, selfinterceting=0, convex=0):
	poly = []
	for i in range(n):
		poly.append((gencord(poly, 0), gencord(poly, 1)))
	if selfinterceting == 0:
		sides = []
		intersecting = -1
		for i in range(n):
			sides.append(([((poly[i][1]-poly[(i+1)%n][1]) / (poly[i][0]-poly[(i+1)%n][0])), poly[i][0], poly[i][1]] if (poly[i][0]-poly[(i+1)%n][0]) != 0 else [poly[i][0]], ((poly[i][0]+(poly[(i+1)%n][0]))/2, (poly[i][1]+(poly[(i+1)%n][1]))/2), (poly[i][0]-(poly[(i+1)%n][0])/2, poly[i][1]-(poly[(i+1)%n][1]))/2))
		for i in range(n):
			for otherside in sides:
				if sides[i] != otherside and intersect(sides[i], otherside):
					intersecting = i
		if intersecting != -1:
			newpoly = poly[:]
			newpoly[i%2] = poly[(i%2-1)%n]
			newpoly[(i%2-1)%n] = poly[i%2]
		if convex == 1: # Ik, don't shame me # TODO: Finish this
			for i in range(n):
				m1 = sides[i][0][0]
				m2 = sides[(i+1)%n][0][0]
	return poly
	

def areaunderpoly(poly):
	sides = []
	left, right = (poly.index(x) for x in sorted(poly, lambda x: x[0])[::len(poly)-1])
	poly = poly[right:] + poly[:left+1] if right > left else poly[right, left+1]
	if len(poly) > 2:
		for i in range(len(poly)):
			sides.append((str((poly[i][1]-poly[(i+1)%len(poly)][1]) / (poly[i][0]-poly[(i+1)%len(poly)][0])) + "*({x} -  " + str(poly[i][0]) + ") + " + str(poly[i][1]), ((poly[i][0]+(poly[(i+1)%len(poly)][0]))/2, (poly[i][1]+(poly[(i+1)%len(poly)][1]))/2), (abs(poly[i][0]-(poly[(i+1)%len(poly)][0]))/2, abs(poly[i][1]-(poly[(i+1)%len(poly)][1]))/2)))
		
		

poly = genpoly(4)
if os.path.isfile("the2.py"):
	sample = subprocess.run(f"{sys.executable} the2.py", input=f"{poly}", stdout=subprocess.PIPE).stdout
else:
	raise FileNotFoundError("Please put the2.py in the same folder.")
	
	