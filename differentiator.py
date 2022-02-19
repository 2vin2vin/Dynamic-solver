# Need to add cross multiply function
# Need to add mass identifier function

def frame(visualisation=None):
	###Frames are done
	#Getting the total number of frames
	a=int(input('Enter number of frames:'))

	#Show data if visualisation is 'y'
	visualisation='y'

	#Generating the frames
	FRAMES=[]
	for i in range(1,a+1):
		frames=[]
		for j in range(1,4):
			frames.append('a'+str(i)+str(j)+'^')
		FRAMES.append(frames)
	if visualisation=='y':
		print(FRAMES)

	#Modifying the frames
	modify=0
	while modify==0:
		a=int(input('Enter the frame to be modified(only numbers):'))
		b=int(input('Enter the value to be replaced in the above frame(only numbers):'))
		FRAMES[int(a/10)-1][a%10-1]=FRAMES[int(b/10)-1][b%10-1]
		print(FRAMES)
		print('Do you want to modify')
		print('Press 0')
		print('Else')
		modify=int(input('Press 1:'))
	return FRAMES
	###Frames are done
'''
#cross multiply function
def cross_multiply(eqn,diff_fr,fr_lo):
	a=eqn
	b=a[1:3]
	c=diff_fr[b[0]
	#b x c => a11^ x (l1 x a21^)
	d=1
	while d>0:
		d=c.find('a')
		e=c[d+1:d+2]
	return eqn
'''
#completely generalised cross function
def cross(eqn1,eqn2,fr_lo):
	fin_eqn='('
	#eqn1=l1 x a11^ + l2 x a21^
	#eqn2=l3 x a31^ + l2 x a21^
	if visualisation!=None:
		print("CROSS MULTIPLY")
		print("eqn1:",eqn1)
		print("eqn2:",eqn2)
	a=eqn1
	b=1
	while b>0:
		#b=8
		b=a.find('^')
		if b==0:
			break
		#c=a11^
		if len(a)<4:
			break
		c=a[b-3:b+1]
		#fin_eqn=(l1 x 
		fin_eqn=fin_eqn+a[:b-3]
		
		e=1
		d=eqn2
		while e>0:
			#e=8
			e=d.find('^')
			if visualisation!=None:
				print('d:',d)
				print('e 8:',e)
			if e==0:
				break
			#f=a31^
			if len(d)<4:
				break
			f=d[e-3:e+1]
			if visualisation!=None:
				print('f a31^:',f)
			#fin_eqn=(l1 x l3 x 
			fin_eqn=fin_eqn+d[:e-3]
			if visualisation!=None:
				print('fin_eqn=(l1 x l3 x:',fin_eqn)
			no_con=0
			for i in fr_lo:
				if visualisation!=None:
					print('i:',i,c,f)
				if i[1:5]==c and i[8:12]==f:
					print('i.split:',i.split(' ')[-1])
					#fin_eqn=(l1 x l3 x (a11^ x a31^
					fin_eqn=fin_eqn+i.split(' ')[-1]+') + '
					no_con=1
					break
			if no_con==0:
				fin_eqn=fin_eqn+'('+c+' x '+f+') + '
			
			d=d[e+1:]
		a=a[b+1:]
	if visualisation!=None:
		print("final equation:",fin_eqn[:-3])
	return fin_eqn[:-3]

###Frame logic
def frame_logic(frames):
	fr_lo=[]
	for i,j,k in frames:
		fr_lo.append('('+i+' x '+j+' = '+k+')')
		fr_lo.append('('+j+' x '+k+' = '+i+')')
		fr_lo.append('('+k+' x '+i+' = '+j+')')
		fr_lo.append('('+j+' x '+i+' = '+'-'+k+')')
		fr_lo.append('('+k+' x '+j+' = '+'-'+i+')')
		fr_lo.append('('+i+' x '+k+' = '+'-'+j+')')
	return fr_lo

def check_eqn(eqn,frames):
	#verification that all frames are present
	for i,j,k in frames:
		a=eqn.count(i)
		b=eqn.count(j)
		c=eqn.count(k)
#		print(a,b,c)
		if a+b+c<1:
			print("The equation doesn't have all the required vectors")
			return None
	return 1

def frame_differential(total_frames):
	diff_fr=[]
	for i in range(0,total_frames-1):
		a=str(input('Enter change of frame '+str(i)+' w.r.t frame '+str(i+1)+':'))
		diff_fr.append('('+a+')')
	return diff_fr

def differentiator(eqn,diff_fr,fr_lo,visualisation=None):
	##Equation split
	a=eqn.split('+')
	b=[]
	for i in a:
		b.append(i)
		b.append('+')
	a=b[:-1]
	if visualisation!=None:
		print('a ln 131:',a)

	d,c=[],[]
	for i in a:
		b=i.split('-')
		if visualisation!=None:
			print('b ln 137:',b)
		if len(b)==1:
			if visualisation!=None:
				print('d ln 140:',i)
			d.append(i)
			continue
		c=[]
		for j in b:
			if visualisation!=None:
				print('c ln 146:',j)
			c.append(j)
			c.append('-')
	c=c[:-1]
	for i in c:
		d.append(i)
	if visualisation!=None:
		print('d ln 153;',d)	
	##Equation split done

	##Now differentiate starts
	
	#storing in f
	e=[]
	for i in d:
		a=i.split(' ')
		if len(a)==1:
			continue
		a=a[1:-1]
		if visualisation!=None:
			print('a ln 166:',a)
		j=0
		b='('
		while j<len(a):
			
			#Addressed the x term
			if a[j]=='x':
				j+=1
				continue
	
			k=0
			##check here for vector dot
			if visualisation!=None:
				print('a[j] ln 179:',a[j])
				print('j ln 180:',j)
			if a[j].find('^')>0:
				c=cross(a[j],diff_fr[int(a[j][1])-2],fr_lo)+' '
				##add cross multiply function
			else:
				c=a[j]+'_dot'+' '
				if visualisation!=None:
					print("ln 189 c:",c)
			while k<len(a):
				k+=1
				if k==j+1:
					b=b+c
					continue
				b=b+a[k-1]+' '

			b=b[:-1]+')'
					
			j+=1
			b=b+' + ('
			if j==len(a):
				e.append(b[:-4])
			if visualisation!=None:
				print('ln 204 b:',b)
	if visualisation!=None:
		print('e:',e)
	f='('
	j=0
	for i in range(0,len(d)):
		if len(d[i])>1:
			f=f+'('+e[j]+')'+' '
			j+=1
		else:
			f=f+d[i]+' '
	f=f[:-1]+')'
	return f
	
print('start')	
visualisation=None	
FRAMES=frame()
for i in FRAMES:
	print(i)

logic=frame_logic(FRAMES)
diff_fr=frame_differential(len(FRAMES))
print(' ')
print('#########RULES')
print('# 1. First and last characters in the equation should be spaces')
print('# 2. All the vectors should be the same as mentioned in the frames')
print('# 3. There should be space between every variable')
print('# Ex: " l1 x t1^ + l2 x s1^ - l3 x r1^ "')

eqn=input('Equation:')
check=check_eqn(eqn,FRAMES)

if check==None:
	print('Equation ERROR')
else:
	eqn=differentiator(eqn,diff_fr,logic,None)
	print('gen:',eqn)
#########RULES
# 1. First and last characters in the equation should be spaces
# 2. All the vectors should be the same as mentioned in the frames
# 3. There should be space between every variable
# Ex: ' l1 x t1^ + l2 x s1^ - l3 x r1^ '
# 4. Vectors should be the same as in the mentioned frames
