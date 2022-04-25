/*Below is predicate used to add other variants to list
 Note: Before this is done, check is needed to determine if variant is already in list
 Directory was added since definition of predicate may change during execution*/

:- dynamic omicron/1.
:- dynamic cases/2.
:- dynamic tot_omicron/1.
:- dynamic tot_delta/1.
:- dynamic tot_covid/1.
:- dynamic covid_symptoms/1.
:- dynamic delta_symptoms/1.
:- dynamic omicron_symptoms/1.
:- dynamic underlying_conditions/1.
:- dynamic blood_pressure_check_required/1.
:- dynamic male_positives/1.
:- dynamic female_positives/1.
:- dynamic blood_pressure/1.
:- dynamic mild/1.
:- dynamic severe/1.

cases(24,11).
mild(2).
severe(2).
tot_omicron(4).
tot_delta(2).
tot_covid(2).
omicron_underlying(1).
male_positives(4).
female_positives(7).
blood_pressure(4).
covid_symptoms(['Dizzyness', 'Fainting', 'Dry Cough']).
delta_symptoms(['Sore Throat','Short Breath','Loss of Taste']).
omicron_symptoms(['Migraine','Nausea','Chest Pain']).
underlying_conditions(['High Blood Pressure','Low Blood Pressure', 'Heart Disease']).
blood_pressure_check_required(['Dizzyness', 'Fainting', 'Dry Cough', 'High Blood Pressure', 'Low Blood Pressure', 'Heart Disease']).

update_covid_symptoms(Sym):- nl,covid_symptoms(Oldlist),append(Oldlist,[Sym],Newlist),
                     retractall(covid_symptoms(_)),asserta(covid_symptoms(Newlist)).


update_delta_symptoms(Sym):- nl,delta_symptoms(Oldlist),append(Oldlist,[Sym],Newlist),
                     retractall(delta_symptoms(_)),asserta(delta_symptoms(Newlist)).


update_omicron_symptoms(Sym):- nl,omicron_symptoms(Oldlist),append(Oldlist,[Sym],Newlist),
                     retractall(omicron_symptoms(_)),asserta(omicron_symptoms(Newlist)).



update_conditions(Con):- nl,underlying_conditions(Oldlist),append(Oldlist,[Con],Newlist),
                     retractall(underlying_conditions(_)),asserta(underlying_conditions(Newlist)).


update_bp_required(Sym):- nl,blood_pressure_check_required(Oldlist),append(Oldlist,[Sym],Newlist),
                     retractall(blood_pressure_check_required(_)),asserta(blood_pressure_check_required(Newlist)).



