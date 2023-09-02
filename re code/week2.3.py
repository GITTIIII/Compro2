club = []
diamond = []
heart = []
spade = []
deck = [club,diamond,heart,spade]
card = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for x in deck:
    for y in card:
        if x==club:
            club.append(y+"\u2663")
        if x==diamond:
            diamond.append(y+"\u2666")
        if x==heart:
            heart.append(y+"\u2665")
        if x==spade:
            spade.append(y+"\u2660")

deck = []
deck = club+diamond+heart+spade
print("Club =",club)
print("Diamond =",diamond)
print("Heart =",heart)
print("Spade =",spade)
print("Decl =",deck)
print("Total card in one decl = %d"%len(deck))