#Import Modules
import os
import csv

#Read CSV
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #Total Number of Votes
    vote = list(csvreader)
    total_votes = len(vote)
    print(f'There were a total of {total_votes} in this election!')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    candidates = []
    for row in csvreader:
        candidates.append(row[2])

candidates = sorted((set(candidates)))
print('######################################################################')
print(f'The candidates in this election are: {candidates}')
cand0 = candidates[0]
cand1 = candidates[1]
cand2 = candidates[2]
cand3 = candidates[3]
print('######################################################################')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    Correy = 0
    Khan = 0
    Li = 0
    Tooley = 0
    for row in csvreader:
        if row[2] == cand0:
            Correy = Correy + 1
        elif row[2] == cand1:
            Khan = Khan + 1
        elif row[2] == cand2:
            Li = Li + 1
        elif row[2] == cand3:
            Tooley = Tooley + 1

Correy_per = "{:.2%}".format(Correy/total_votes)
Khan_per = "{:.2%}".format(Khan/total_votes)
Li_per = "{:.2%}".format(Li/total_votes)
Tooley_per = "{:.2%}".format(Tooley/total_votes)

print(f'Correy has {Correy} votes or {Correy_per} of the total vote')
print(f'Khan has {Khan} votes or {Khan_per} of the total vote')
print(f'Li has {Li} votes or {Li_per} of the total vote')
print(f'Tooley has {Tooley} votes or {Tooley_per} of the total vote')
print('######################################################################')

Vote_Number = [Correy, Khan, Li, Tooley]

Election_summary = zip(Vote_Number, candidates)
most_votes = sorted(Election_summary, reverse=True)
winner = most_votes[0]

print(f"The winner of this election is...........{winner[1]}!!!")

perc_fig = [Correy_per, Khan_per, Li_per, Tooley_per]
Vote_figs = zip(candidates, Vote_Number, perc_fig)

output_path = os.path.join("Analysis", "output_file.csv")
with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(Vote_figs)