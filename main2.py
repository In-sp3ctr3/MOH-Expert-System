from pyswip import Prolog
prolog = Prolog()
prolog.consult("prolog.pl")


symptoms = list(prolog.query("covid_symptoms(X)"))
symptoms.extend((list(prolog.query("delta_symptoms(X)"))))
symptoms.extend((list(prolog.query("omicron_symptoms(X)"))))

list1 = ['Chest Pain', 'Migraine', 'Nausea']
list2 = ['Chest Pain', 'Dizzyness', 'Dry Cough', 'Fainting', 'Loss of Taste', 'Migraine', 'Nausea', 'Short Breath', 'Sore Throat']

thing = "raa ass asas asa"
print(thing)
print(list(prolog.query(f"update_covid_symptoms('{thing}')")))
print(list(prolog.query("covid_symptoms(X)")))

"""if(all(x in list2 for x in list1)):
	print('Matches')"""

#x = list(prolog.query("covid(X)"))
#tot_covid = x[0]['X']
#print(x)

"""for i in range(len(symptoms)):
	for s in symptoms[i]['X']:
		print(s)
"""


"""prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")

print(list(prolog.query("symptoms(X)")))

li = ['water','fire']

x = list(prolog.query("cases(X,Y)"))

print(x[0]['X'])
print(x[0]['Y'])

for i in x[0]['X']:
	print(i)

prolog.retractall("variant(_)")
print(list(prolog.query(f"update_variant({li})")))
print(list(prolog.query("variant(X)")))"""