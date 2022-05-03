# cs-32-final-project

''' PROJECT: COLLEGE MATCHMAKER

Project Overview: Our final project “College Matchmaker” is an algorithm designed to shorten the tedious college search and match process for its users. It can be broadly divided into two pieces, first being the data collection and editing and the second.

The first part of this project involved data collection. We found a public csv file that contained data points for 650 colleges, including average SAT score, tuition cost, etc. We then created a function in Python that allowed us to load this data into an empty dictionary called ‘colleges’. This dictionary mapped the name of each of the colleges (thus the key) to a sequence of chosen data, such as the aforementioned SAT score, tuition cost, etc (these were the values). 

Once we had the dictionary running, we were able to move on to the algorithm design. We had two main types of algorithms. The first was on the client side, asking the user to input their preferences for factors related to their dream college — we chose to ask for size (small, medium, or large) and whether it was public or private. We also had the algorithm ask the user questions that asked for price range and SAT scores. We then developed four separate algorithms that essentially ran through the dictionary and found the name of each college that matched the user’s preferences and appended this to a list. For the cost and SAT criteria, we considered any college with the same or lower cost/score to be a match. For the size and public/private criteria, we only added in exact matches (but for sizes, we defined what we considered to be small, medium, or large). We then stored the lists as pkl files to increase the speed of the program. Essentially, what we did was ask whether or not a file already existed of the matches and then if not we created a new file and stored it outside the program. Then, we called upon those lists later and merged them into a new list called matches. The advantage of doing this rather than making a new list each time is that the computer only has to calculate the list once, making it easier to load later on. While you can’t really see the effects of this on the speed of our program right now since there are only 650 colleges, we anticipate that if we expand the college list it would have a serious impact on the run time. 

Once we had the matches list, we used a mode function to calculate the most frequently occurring match, which would be the user's top match. Then we removed that from the list and recalculated the top match to give the second match, and so on for the third. 

The next step for the project is simply to expand upon what we already have. Right now we have a great framework and base to increase the complexity of our program, so all we’d have to do is increase the number of colleges, the number of criteria and create some new algorithms to find matches for those criteria. This would give the user more personalized results and thus make our program more useful. 


''' 
