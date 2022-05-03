# from code import interact

import csv

# import statistics

from collections import Counter

colleges = {}

def convert_to_size(population):
    population = int(float(population))
    if population > 10000:
        return "large"
    elif population < 4000:
        return "small"
    else:
        return "medium"

def round_total_cost(cost):
    cost = int(cost/1000)
    n = round(cost, 0) * 1000
    return n

def load_data():
    """
    Load data from CSV files into colleges dictionary
    """

    # Load college stats
    with open("ForbesAmericasTopColleges2019 2.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # name = row["Name"]
            id = int(float(row["Rank"]))
            colleges[id] = {
                "Public/Private": row["Public/Private"],
                "SAT": row["SAT Lower"],
                "Cost": row["Total Annual Cost"],
                "Size": convert_to_size(row["Undergraduate Population"])
            }
    return colleges



# collect preferences from user
  #with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        #reader = csv.DictReader(f)
        #for row in reader:
            #id = int(row["id"])
            #movies[id] = {
                #"title": row["title"],
                #"year": row["year"],
                #"stars": set(),
                 #}
            


                 
# TEST CODE (small dictionary)                
# print("Get ready to get matched \U0001F60E")
# colleges = {
#   'Harvard': "medium",
#   'Yale': "small"
# }





# # function to return key for any value
# def get_key(val):
#     for key, value in colleges.items():
#          if val == value:
#              return key
#          else:
#             return "not found"
    
# finding size preferences

def ideal_size(size_pref):
    sizes_list = []
    for key, value in colleges.items():
        if size_pref == value:
            sizes_list.append(key)
    return sizes_list

# finding public vs private preferences

def ideal_type(pub_pref):
    pub_list = []
    for key, value in colleges.items():
        if pub_pref == value:
            pub_list.append(key)
    return pub_list

# finding cost preferences

def closest_price(cost_pref):
    price_list = []
    for key, value in colleges.items():
        if cost_pref >= value:
            price_list.append(key)
    return price_list


# finding SAT matches
def closest_score(score_pref):
    SAT_scores = []
    for college_name in colleges:
        SAT_score=colleges[college_name]["SAT"]
        if score_pref >= float(SAT_score):
            SAT_scores.append(college_name)
    return SAT_scores

# tally up the number of times a college is in the match list                 
# top_match = statistics.mode(matches)

# matches.pop(top_match)
                  
# second_top_match = statistics.mode(matches)
                  
# matches.pop(second_top_match)

# third_top_match = statistics.mode(matches)
                  


def main():
    print('Welcome to the COLLEGE MATCHMAKER \n Get ready to get matched! \U0001F60E')

    print('Loading colleges...')
    
    load_data()
    print(colleges)
    ### continue with rest of main statements
    while True:
        size_pref = input('Do you prefer a small, medium or large school population? ').lower()
        size_list = ['small', 'medium', 'large']

        if size_pref not in size_list:
            print('Size must be small, medium or large. Try again...')
        else:
            break


    while True:
        pub_pref = input('Do you prefer a public or private institution? ').lower()
        pub_list = ['public', 'private']

        if pub_pref not in pub_list:
            print('Your choices are public or private. Try again...')
        else:
            break


    while True:
        try:
            SAT_score = int(input('What is your SAT score? '))
        except ValueError:
            print('SAT score must be a number. Try again...')
        break

    while True:
        try:
            cost_pref = int(input('What is the most that you are willing to pay for your tuition? '))
        except ValueError:
            print('Tuition must be a whole number. Do not include currency signs. Try again...')
        break
          
    # key_list = list(colleges.keys())
    # val_list = list(colleges.values())
    matches = []
    size_match = ideal_size(size_pref)

    matches.append(size_match)

    pub_match = ideal_type(pub_pref)

    matches.append(pub_match)

    cost_match = closest_price(cost_pref)

    matches.append(cost_match)
    SAT_match = closest_score(SAT_score)

    matches.append(SAT_match)
    
    total_counts = Counter()
    for school in matches:
        total_counts[school] += 1

    top_matches = total_counts.most_common(3)

    print(f' According to our analysis, your top match is {top_matches[0]}!!')

    while True:
        see_second = input('Do you wish to see your next match? ')

        if see_second == 'yes':
            print(f' Your second top match is {top_matches[1]}!')
            see_third = input('Do you wish to see your next match? ')

            while True:

                if see_third == 'yes':
                    print(f' Your third top match is {top_matches[2]}!')
                elif see_third == 'no':
                    print('You\'re all done!')
                else:
                    print('Sorry, we didn\'t understand your response. Please respond with yes or no.')
            break
            
        elif see_second == 'no':
            print('You\'re all done!')
        else:
            print('Sorry, we didn\'t understand your response. Please respond with yes or no.')
        break
if __name__ == '__main__':
    main()
