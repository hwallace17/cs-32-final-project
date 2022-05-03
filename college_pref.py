import csv

import statistics

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
            name = row["Name"]
            # id = int(float(row["Rank"]))
            colleges[name] = {
                "Public/Private": row["Public/Private"].lower(),
                "SAT": row["SAT Lower"],
                "Cost": row["Total Annual Cost"],
                "Size": convert_to_size(row["Undergraduate Population"])
            }
    return colleges


# collect preferences from user

# finding size preferences

def ideal_size(size_pref):
    sizes_list = []
    for college_name in colleges:
        size = colleges[college_name]["Size"]
        if size_pref == str(size):
            sizes_list.append(college_name)
    return sizes_list

# finding public vs private preferences

def ideal_type(pub_pref):
    pub_list = []
    for college_name in colleges:
        pref = colleges[college_name]["Public/Private"]
        if pub_pref == str(pref):
            pub_list.append(college_name)
    return pub_list

# finding cost preferences

def closest_price(cost_pref):
    
    price_list = []

    for college_name in colleges:
        price = colleges[college_name]["Cost"]
        
        if cost_pref >= float(price):
            price_list.append(college_name)
    
    return price_list

# finding SAT matches
def closest_score(score_pref):
    
    SAT_scores = []
    
    for college_name in colleges:
        SAT_score=colleges[college_name]["SAT"]

        if SAT_score == '':
            SAT_score = 400.0
            
        if score_pref >= float(SAT_score):
            SAT_scores.append(college_name)
            
    return SAT_scores
    

def main():
    print('Welcome to the COLLEGE MATCHMAKER \n Get ready to get matched! \U0001F60E')

    print('Loading colleges...')
    
    load_data()
   
    ### gather user input and check valid input
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
            SAT_score = float(input('What is your SAT score? '))
        except ValueError:
            print('SAT score must be a number. Try again...')
        break

    while True:
        try:
            cost_pref = float(input('What is the most that you are willing to pay for your tuition? '))
        except ValueError:
            print('Tuition must be a whole number. Do not include currency signs. Try again...')
        break
          

    matches = []

    # add all matches from preferences list to one big list
    
    size_match = ideal_size(size_pref)

    matches.extend(size_match)

    pub_match = ideal_type(pub_pref)

    matches.extend(pub_match)

    cost_match = closest_price(cost_pref)


    matches.extend(cost_match)
    
    SAT_match = closest_score(SAT_score)


    matches.extend(SAT_match)

    top_match = statistics.mode(matches)
    
 
    print(f' According to our analysis, your top match is {top_match}!!')


    def check_input(prompt):
        answers = ['yes', 'no']
        while prompt not in answers:
            prompt = input('Your response must be yes or no: ')
        return prompt
            
            
    while True:
        see_second = check_input(input('Do you wish to see your next match? '))
        
        if see_second == 'yes':
            matches.remove(top_match)
            second_top_match = statistics.mode(matches)
            print(f' Your second top match is {second_top_match}!')
           
            while True:
                see_third = check_input(input('Do you wish to see your next match? '))

                if see_third == 'yes':
                    matches.remove(second_top_match)
                    third_top_match = statistics.mode(matches)
                    print(f' Your third top match is {third_top_match}! \n You\'re all done!')
                elif see_third == 'no':
                    print('You\'re all done!')
                    break
            
        elif see_second == 'no':
            print('You\'re all done!')

        break
if __name__ == '__main__':
    main()
