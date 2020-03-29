import pandas as pd
import os
import csv
#Get CSV
csv_path = "Resources/election_data_test.csv"
poll_df = pd.read_csv(csv_path, encoding="utf-8")
#Print to view it
print("polldf", poll_df.head())
#Group by Candidate count uniques
group_df = poll_df.groupby("Candidate")['Voter ID'].nunique()
#check that the right values are resulted
print(group_df)
#put in new dataframe with column "Votes"
vote_df = pd.DataFrame({"Votes":group_df})
vote_df = vote_df.sort_values("Votes", ascending = False)
#get the sum of all votes
sum_df = vote_df.sum()
#Putin new dataframe and compute %
pct = round(100* vote_df / sum_df,2)
pct_df = pd.merge(vote_df,pct, on="Candidate")
print("pct", pct)
#pct_df=pd.DataFrame({"Votes": group_df, "pct":pct})
print("votes",vote_df.head())
print("sum",sum_df.head())
print("pct%",pct_df.head())
df = pct_df.rename({"Votes_x": "Votes","Votes_y":"%pop vote"}, axis = 'columns')
print(df)
