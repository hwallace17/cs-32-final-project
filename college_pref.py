import csv

colleges = {}

def load_data(directory='small'):
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

pop_pref = input('Do you prefer a small, medium or large school population?").lower
pop_size_list = ['small', 'medium', 'large']

if pop_pref not in pop_size_list:
    print('Size must be small, medium or large')
else:
    break

matches = []
                 
x = colleges.get(pop_pref)

matches.append(x)

