#!/usr/bin/env python2.7
import sys
import socket
import time

MAZE_SERVER = ('185.229.226.251', 80)
RECV_SIZE = 8192
conn = socket.create_connection(MAZE_SERVER)

changed = 0
changed_c_g = []
start_g = ""
dtg = ""
a = ""
directions = ""
directions_list = ""
directions_list_values = ""
corrent_point = ""
past_points = []
g = ""
loop_check = {}
count = 0

l = 10
r = 10
u = 10
d = 10

def main():
	global directions, corrent_point, g, l, r, u, d, dtg, past_points, count, a, directions_list, directions_list_values, start_g, changed_c_g, changed

	icg = ['i', 'c', 'g']
	a = ""
	count = 0

	conn.settimeout(1)
	while True:
		try:
			print "Printing"
			printing_data()
		except:
			print "Done printing"
			if icg:
				a = icg.pop(0)
				conn.send(a)
				print "message sent(", a + ")"
				placing_values(a)
			else:
				print g ##, l, u, r, d, dtg
				
				if g != start_g:	
					changed_c_g.append([corrent_point, g])
					changed += 1
					if g == "Your distance from the treasure is \xe2\x88\x9a 1":
						print (g)	

				arrange_directions_lists_left_hand()
				#print directions_list, directions_list_values
				dtg = direction_to_go()
				past_points.append(corrent_point)
				print past_points
				print g
				print changed_c_g
				print changed
				if changed == 10:
					conn.send("s")
					response = conn.recv(RECV_SIZE)
					print (response)
					a = input()
					b = input()
					conn.send("(%d,%d)" % (int(a), int(b)))
					response = conn.recv(RECV_SIZE)
					print (response)
					response = conn.recv(RECV_SIZE)
					print (response)
					return
				else:
					conn.send(dtg)
				#print "message sent(", dtg + ")"
				icg = ['i', 'c', 'g']
			conn.settimeout(0.1)


def printing_data():
	while True:
		response = conn.recv(RECV_SIZE)
		print (response)
		# print "Done"


def placing_values(a):
	global directions, corrent_point, g, start_g
	if a == 'i':
		directions = conn.recv(RECV_SIZE)[:-1]
		creating_directions(directions) # placing value in each direction
	elif a == 'c':
		corrent_point = conn.recv(RECV_SIZE)[:-1]
	elif a == 'g':
		g = conn.recv(RECV_SIZE)[:-1]
		if start_g == "":
			start_g = g


def creating_directions(directions):
	global l, r, u, d
	# print l, r, u, d
	directions = directions.split(", ")
	for i in range(len(directions)):
		directions[i] = "global " + directions[i][0] + "; " + directions[i]
		exec directions[i]
	# print l, r, u, d


def arrange_directions_lists_left_hand():
	global directions_list, directions_list_values, l, r, u, d, dtg
	if dtg == "d":
		directions_list = ["r", "d", "l", "u"]
		directions_list_values = [r, d, l, u]
	elif dtg == "l" :
		directions_list = ["d", "l", "u", "r"]
		directions_list_values = [d, l, u, r]
	elif dtg == "r":
		directions_list = ["u", "r", "d", "l"]
		directions_list_values = [u, r, d, l]
	else:
		directions_list = ["l", "u", "r", "d"]
		directions_list_values = [l, u, r, d]


def direction_to_go():
	global corrent_point, past_points, loop_check, directions_list, directions_list_values
	if corrent_point in past_points:
		if corrent_point in loop_check:
			if loop_check[corrent_point] == 4:
				print "LOOPING"
			else:
				loop_check[corrent_point] += 1
		else:
			loop_check[corrent_point] = 1
	for i in range(4):
		if directions_list_values[i] == 1:
			return directions_list[i]
		
if __name__ == '__main__':
	main()
