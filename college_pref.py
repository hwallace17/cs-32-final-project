import csv

import statistics

colleges = {}

print('Welcome to the COLLEGE MATCHMAKER \n Get ready to get matched! \U0001F60E')

print('Loading colleges...')

def load_data():
    """
    Load data from CSV files into colleges dictionary
    """

    # Load college stats
    with open(f"{directory}/College_Data.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = int(row["College Name"])
            colleges[id] = {
                "F.undergrad": row["F.Undergrad"],
                "S.F.Ratio": row["S.F.Ratio"],
            }
            
# collect preferences from user

size_pref = input('Do you prefer a small, medium or large school population?').lower
size_list = ['small', 'medium', 'large']

if size_pref not in size_list:
    print('Size must be small, medium or large')
else:
    pass


                 
# TEST CODE (small dictionary)                
# print("Get ready to get matched \U0001F60E")
# colleges = {
#   'Harvard': "medium",
#   'Yale': "small"
# }

key_list = list(colleges.keys())
val_list = list(colleges.values())


matches = []

# function to return key for any value
def get_key(val):
    for key, value in colleges.items():
         if val == value:
             return key
 
    return "key doesn't exist"
    
size_match = get_key(size_pref)

matches.append(size_match)
                 
# tally up the number of times a college is in the match list                 
top_match = statistics.mode(matches)

matches.pop(top_match)
                  
second_top_match = statistics.mode(matches)
                  
matches.pop(second_top_match)

third_top_match = statistics.mode(matches)
                  
print(f' According to our analysis, your top match is {top_match.upper}!!)

see_second = input('Do you wish to see your next match? ')

if see_second == 'yes':
    print(f' Your second top match is {second_top_match.upper}!)
elif see_second == 'no':
    print('You\'re all done!)
else:
    print('Sorry, we didn\'t understand your response. Please respond with yes or no.')
          
          
see_third = input('Do you wish to see your next match? ')

if see_third == 'yes':
    print(f' Your third top match is {third_top_match.upper}!)
elif see_third == 'no':
    print('You\'re all done!)
else:
    print('Sorry, we didn\'t understand your response. Please respond with yes or no.')
    
    

