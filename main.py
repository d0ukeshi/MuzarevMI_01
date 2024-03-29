#!/usr/bin/env python3

# add cycles of length 1
def prepare(g, n):
	control = [str(i) for i in range(1, n+1)]
	for cycle in g:
		for el in cycle:
			control.remove(el)
	for el in control:
		t = []
		# avoid this case list('15') = ['1', '5']
		t.append(el)
		g.append(t)
	g.sort()
	return g

def search(g, hidden_next):
	for i, cycle in enumerate(g):
		for j, el in enumerate(cycle):
			if el == hidden_next:
				#return position
				return i, (j+1)%len(cycle)

def multiple(g1, g2, n):
	g1 = prepare(g1, n)
	g2 = prepare(g2, n)
	g3 = []	
	possible_start = [str(i) for i in range(1, n+1)]

	# tmp arr for 1 cycle
	tmp = []
	for k in range(n):
		# append new element to empty array
		if not tmp:
			start_el = possible_start[0]
			possible_start.remove(start_el)
			tmp.append(start_el)

		# get hidden el
		i, j = search(g1, tmp[-1])
		hidden_next = g1[i][j]

		# get new el
		i, j = search(g2, hidden_next)
		new_el = g2[i][j]
		
		#check end cycle
		if new_el == tmp[0]:
			g3.append(tmp)
			tmp = []
		else:
			tmp.append(new_el)
			# for avoid repeat
			possible_start.remove(new_el)

	return g3

def create_table(g1, g2, n):
	epsilon = [list(str(x)) for x in range(1, n+1)]
	table = [epsilon, g1, g2]

	for i, x in enumerate(table):
		# print("\\\\")
		for j, y in enumerate(table):
			res = multiple(x, y, n)
			res.sort()
			if res not in table:
				table.append(res)

			pos = table.index(res)

			print(f"g{i}*g{j}=g{pos}: {res}")
			# Output for tex, except first line.
			# if pos == 0:
			# 	print("$\\varepsilon$ & ", end = '')
			# else:
			# 	print("$g_"+"{"+str(pos)+"}$ & ", end = '')

	print("\n\nВсе итоговые перестановки:")
	for i,x in enumerate(table):
		print(f"g{i}: {x}")

if __name__ == '__main__':
	print("""
Циклы разделяются между собой пробелом!
Важно указать степень группы подстановок n!

Вводить подстановки необходимо таким образом:
Если g1=(123)(456), то ввести нужно  g1: 1,2,3 4,5,6
Если g2=(11 35 17 23), то аналогично g2: 11,35,17,23
""")

	n = int(input("Введите степень подстановки n: "))
	g1 = input("Введите подстановку g1: ").split(" ")
	g2 = input("Введите подстановку g2: ").split(" ")

	g1 = [ x.split(",") for x in g1]
	g2 = [ x.split(",") for x in g2]

	# Uncomment this line for simple multiplication
	# print(multiple(g1, g2, n))
	# print(multiple(g2, g1, n))

	# Create table for task
	create_table(g1, g2, n)
