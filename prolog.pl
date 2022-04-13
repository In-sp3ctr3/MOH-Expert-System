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

cases(23,10).
mild(2).
severe(1).
tot_omicron(4).
tot_delta(2).
tot_covid(1).
omicron_underlying(1).
male_positives(3).
female_positives(7).
blood_pressure(4).
covid_symptoms(['Dizzyness', 'Fainting', 'Dry Cough', 'Sneeze', 'Sneeze']).
delta_symptoms(['Sore Throat','Short Breath','Loss of Taste']).
omicron_symptoms(['Migraine','Nausea','Chest Pain']).
underlying_conditions(['High Blood Pressure','Low Blood Pressure', 'Heart Disease']).
blood_pressure_check_required(['Dizzyness', 'Fainting', 'Dry Cough', 'High Blood Pressure', 'Low Blood Pressure', 'Heart Disease', 'Sneeze', 'Sneeze']).

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



%Below is predicate used to display list of variants
display_variants:- variant(X),write(X).

%Below is a list of symptoms
symptoms(['Dizziness','Fainting','Blurred Vision','Fever','Cough','Difficulty breathing']).

/*Below is the predicate that accepts new symptom and updates 'symptoms' list.
Note: Before updating 'symptoms' list, check to see if symptom is already in list

Directory was added since definition of predicate may change during execution*/

:- dynamic symptoms/1.

update_symptoms(Sym):-nl, symptoms(Oldlist),append(Oldlist,[Sym],Newlist),
                     retractall(symptoms(_)),assert(symptoms(Newlist)),symptoms(X),
                     write(X),nl,    %test to display if symptom was added successfully
                     write('Symptom Added Successfully').



/*


%(Predicte not in use)



% Below is predicate example that was created to prompt user with information to update 'symptoms' list



% Also uses recursion.



:- dynamic symptoms/1.



update_symptoms:- nl,write('New symptom: '),

                  nl,read(Sym),nl,



                     symptoms(Oldlist),append(Oldlist,[Sym],Newlist),



                     retractall(symptoms(_)),assert(symptoms(Newlist)),symptoms(X),



                     write(X),nl,



                     write('Symptom Added Successfully'),nl,



                     write('Do you want to add another? (y/n)'),nl,read(Ans),



                     (Ans=='y'->update_symptoms;nl,write('All Symptoms added.')).



*/



%Below is a predicate that displays all symptoms in the knowledge base



display_symptoms:- symptoms(X),write(X).


%Below holds a list of all underlying conditions



underlying('Covid',['Obesity','Heart Disease','Cancer','High Blood Pressure','Kidney Disease']).


%Underlying conditions specific to omicron



underlying('Omicron', ['Cancer','Kidney Disease']).



%Underlying conditions specific to delta



underlying('Delta', ['Obesity','Heart Disease']).


/*Below is the predicate that accepts new underlying condition and updates list.



  Note: Before updating list, check to see if condition is already in list



  Directory was added since definition of predicate may change during execution*/



:- dynamic underlying/2.



update_underlying(Cond):- underlying('Covid',Oldlist),append(Oldlist,[Cond],Newlist),



                          retractall(underlying('Covid',_)),assert(underlying('Covid',Newlist)),underlying('Covid',X),



                          write(X),nl, %Test to display if condition was added successfully



                          write('Condition Added Successfully').



%Displays list of all underlying conditions



disp_underlying:- underlying('Covid', X), write(X).



/*Rule to determine whether individual has (Regular) Covid.



  This was determined by the temperature and any two possible symptoms of covid



  Accepts the converted temperature (°F)*/



%****



% has_covid(Temp,Sym1, Sym2):-



%---------------------------



/*



has_delta:-



has_omicron:-



*/


%---------------------------

/*



%(Not in use)



%Checks to see if condition is already in list (using 'member')


:- dynamic lists:member/1.



lists:member(Cond,[Cond|_]).



lists:member(Cond,[_|T]):- lists:member(Cond|T).


*/


%---------------------------


/*


%(Not in use)



%holds the number of mild and severe symptoms.


stats('Mild',0).



stats('Severe', 0).



*/

