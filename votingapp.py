import streamlit as st

#App Title
st.title("🗳️ Simple Voting App")

#Instructions
st.markdown("""
Welcome to the voting app!  
1. Enter the names of **two nominees** below.  
2. Click **Lock Nominees** to start voting.  
3. Voters will enter their ID (1–10) and cast their vote.  
""")

#Nominee Setup
if "nominee_1" not in st.session_state:
    st.session_state.nominee_1 = ""
if "nominee_2" not in st.session_state:
    st.session_state.nominee_2 = ""
if "nominees_locked" not in st.session_state:
    st.session_state.nominees_locked = False

if not st.session_state.nominees_locked:
    n1 = st.text_input("Enter Nominee 1's Name")
    n2 = st.text_input("Enter Nominee 2's Name")

    if st.button("Lock Nominees", key="lock_nominees"):
        if n1.strip() != "" and n2.strip() != "":
            st.session_state.nominee_1 = n1
            st.session_state.nominee_2 = n2
            st.session_state.nominees_locked = True
            st.success(f"✅ Nominees locked: {n1} vs {n2}. Voting can begin!")
        else:
            st.error("⚠️ Please enter names for both nominees.")

else:
    st.info(f"Nominees are locked: **{st.session_state.nominee_1}** vs **{st.session_state.nominee_2}**")

#Initialize Vote Data
if "votes_id" not in st.session_state:
    st.session_state.votes_id = [1,2,3,4,5,6,7,8,9,10]
if "nom_1_votes" not in st.session_state:
    st.session_state.nom_1_votes = 0
if "nom_2_votes" not in st.session_state:
    st.session_state.nom_2_votes = 0
if "voter_valid" not in st.session_state:
    st.session_state.voter_valid = False
if "current_voter" not in st.session_state:
    st.session_state.current_voter = None

#Voting Section
if st.session_state.nominees_locked:
    voter = st.number_input("Enter your Voter ID:", min_value=1, max_value=10, step=1)

    if st.button("Submit Voter ID", key="submit_id"):
        if voter in st.session_state.votes_id:
            st.session_state.voter_valid = True
            st.session_state.current_voter = voter
            st.success("You are a valid voter ✅")
        else:
            st.error("You are not a voter or already voted ❌")

    if st.session_state.voter_valid:
        st.subheader("Cast Your Vote")
        if st.button(f"Vote for {st.session_state.nominee_1}", key="vote_nom1"):
            st.session_state.nom_1_votes += 1
            st.session_state.votes_id.remove(st.session_state.current_voter)
            st.session_state.voter_valid = False
            st.success(f"Thank you for voting for {st.session_state.nominee_1}")

        if st.button(f"Vote for {st.session_state.nominee_2}", key="vote_nom2"):
            st.session_state.nom_2_votes += 1
            st.session_state.votes_id.remove(st.session_state.current_voter)
            st.session_state.voter_valid = False
            st.success(f"Thank you for voting for {st.session_state.nominee_2}")

    #Show Results
    st.subheader("📊 Live Results")
    st.write(f"{st.session_state.nominee_1}: {st.session_state.nom_1_votes} votes")
    st.write(f"{st.session_state.nominee_2}: {st.session_state.nom_2_votes} votes")
    st.write(f"Voters remaining: {len(st.session_state.votes_id)}")

    #End of Voting
    if len(st.session_state.votes_id) == 0:
        st.subheader("🏆 Final Result")
        total_voters = 10
        if st.session_state.nom_1_votes > st.session_state.nom_2_votes:
            percent = (st.session_state.nom_1_votes / total_voters) * 100
            st.success(f"{st.session_state.nominee_1} has won with {percent:.2f}% votes 🎉")
        elif st.session_state.nom_2_votes > st.session_state.nom_1_votes:
            percent = (st.session_state.nom_2_votes / total_voters) * 100
            st.success(f"{st.session_state.nominee_2} has won with {percent:.2f}% votes 🎉")
        else:
            st.info("It’s a tie! 🤝")
