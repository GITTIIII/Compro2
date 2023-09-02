club = []
diamond = []
heart = []
spade = []
deck = [club,diamond,heart,spade]
card = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for x in (deck):
    for n in (card):
        if x == club:
            x.append(n+"\u2663")
        if x == diamond:
            x.append(n+"\u2666")
        if x == heart:
            x.append(n+"\u2665")
        if x == spade:
            x.append(n+"\u2660")

deck = []
deck = club+diamond+heart+spade

print("Club =",club)
print("Diamond =",diamond)
print("Heart =",heart)
print("Spade =",spade)
print("Deck =",deck)
print("Total card in one deck =",len(deck))