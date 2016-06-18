import json
import copy
import random

"""
dictionary: key is staff member name, value is days available

"""
weeks = 3
days = 7
max_days = 21/4 + 1
print max_days
days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
list_of_names = []
constraints_dict = {}
calendar = [[0 for x in range(days)] for y in range(weeks)]
print calendar

def assign():
	create_constraints()
	for week in range(weeks):
		print week
		for day in range(days):
			print day
			staff_member = random.choice(list_of_names)
			while not is_satisfied(week,day,staff_member):
				staff_member = random.choice(list_of_names)
			calendar[week][day] = staff_member
			constraints_dict[staff_member]['OD_count'] += 1
			print 'assigned!'

	print calendar


def create_constraints():
	with open("days_off.json") as json_file:
	    staf_data = json.load(json_file)
	for staff in staf_data:
		constraints_dict[staff['name']] = {"available_days" : available_days(staff['day_off']), "OD_count" : 0}
		list_of_names.append(staff['name'])

def available_days(day_off):
	available_days = copy.deepcopy(days_of_the_week)
	index = available_days.index(day_off)
	if index == 0:
		available_days.remove('sunday')
	elif index == 6:
		available_days.remove('monday')
	else:
		available_days.pop(index-1)
	available_days.remove(day_off)

	return available_days

def is_satisfied(week,day,name):

	if days_of_the_week[day] not in constraints_dict[name]['available_days']:
		return False
	if constraints_dict[name]['OD_count'] >= max_days:
		print constraints_dict[name]['OD_count']
		return False
	return True

assign()








