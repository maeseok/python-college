import sys
input = sys.stdin.readline
res={'P':13,'K':13,'H':13,'T':13}
card=input().strip()
card=[card[i:i+3] for i in range(0, len(card), 3)]
for i in card:
    if card.count(i)>=2:
        print("GRESKA")
        quit()
    res[i[0]]-=1
ans=list(res.values())
print(*ans)