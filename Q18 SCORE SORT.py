
players = {
    "Rohit Sharma": 597,
    "Rachin Ravindra": 578,
    "Quinton de Kock": 594,
    "Virat Kohli": 765,
    "Shreyas Iyer": 530,
    "KL Rahul": 512
}

sorted_players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))
for player, score in sorted_players.items():
    print(f"{player}: {score}")