import streamlit as st




nominee_1=input("Enter the nominee 1's name:")
nominee_2=input("Enter the nominee 2's name:")

nom_2_votes=0
nom_1_votes=0

votes_id=[1,2,3,4,5,6,7,8,9,10]

num_of_voter=len(votes_id)

while True:
	if votes_id==[]:
		print("voting session is over!")
		if nom_1_votes>nom_2_votes:
			percent=(nom_1_votes/num_of_voter)*100
			print(nominee_1,"has won with", percent, "%  votes")
			break
		elif nom_2_votes>nom_1_votes:
			percent=(nom_2_votes/num_of_voter)*100
			print(nominee_2,"has won with", percent ,"%  votes")
			break

	else:	
		voter=int(input("Enter your voter id number:"))
		if voter in votes_id:
			print("You are a voter ")
			votes_id.remove(voter)
			print("................................")
			print("To give vote to",nominee_1,"press 1")
			print("To give vote to",nominee_2,"press 2")
			print("................................")
			vote = int(input("Enter your vote"))
			if vote==1:
				nom_1_votes+=1
				print("Thank you for voting for me")
			elif vote==2:
				nom_2_votes+=1
				print("Thank you for voting for me")
		else:
			print("You are not a voter or you have already voted")		



