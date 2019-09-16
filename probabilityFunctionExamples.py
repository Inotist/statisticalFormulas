from independentEvents import probability

print(probability(['white', 'white', 'white'], {'red': 8, 'white': 3, 'blue': 9})*100 == 0.08771929824561402)
print(probability({'white': 3}, {'red': 8, 'white': 3, 'blue': 9})*100 == 0.08771929824561402)
print(probability({'blue': 0, 'red': 0, 'other': 3}, {'red': 8, 'white': 3, 'blue': 9})*100 == 0.08771929824561402)
print()

print(probability(['red', 'white', 'red'], {'red': 8, 'white': 3, 'blue': 9})*100 == 7.36842105263158)
print(probability({'red': 2, 'white': 1}, {'red': 8, 'white': 3, 'blue': 9})*100 == 7.368421052631578)
print(probability({'red': 2, 'other': 1, 'blue': 0}, {'red': 8, 'white': 3, 'blue': 9})*100 == 7.368421052631578)
print(probability({'other': 2, 'white': 1, 'blue': 0}, {'red': 8, 'white': 3, 'blue': 9})*100 == 7.368421052631578)
print()
                        # EVENTS MUST HAPPEN IN THE SEQUENCE SPECIFIED BY THE LIST HERE
print(probability(['red', 'white', 'blue'], {'red': 8, 'white': 3, 'blue': 9}, ordered=True)*100 == 3.1578947368421053)
print()

print((probability({'white': 1, 'other': 2}, {'red': 8, 'white': 3, 'blue': 9})+\
      probability({'white': 2, 'other': 1}, {'red': 8, 'white': 3, 'blue': 9})+\
      probability({'white': 3}, {'red': 8, 'white': 3, 'blue': 9}))*100 == 40.35087719298245)

print(probability({'white': 0, 'other': 3}, {'red': 8, 'white': 3, 'blue': 9}, negated=True)*100 == 40.35087719298246)
print()

print((1-(probability({'red': 3}, {'red': 8, 'white': 3, 'blue': 9})+\
      probability({'red': 2, 'blue': 1}, {'red': 8, 'white': 3, 'blue': 9})+\
      probability({'blue': 2, 'red': 1}, {'red': 8, 'white': 3, 'blue': 9})+\
      probability({'blue': 3}, {'red': 8, 'white': 3, 'blue': 9})))*100 == 40.35087719298246)


print(probability(['red', 'white', 'blue'], {'red': 8, 'white': 3, 'blue': 9})*100 == 18.947368421052634)
print(probability(['red', 'white', 'other'], {'red': 8, 'white': 3, 'blue': 9})*100 == 18.947368421052634)
print(probability(['red', 'other', 'blue'], {'red': 8, 'white': 3, 'blue': 9})*100 == 18.947368421052634)
print(probability(['other', 'white', 'blue'], {'red': 8, 'white': 3, 'blue': 9})*100 == 18.947368421052634)
print()

print(probability({'blue': 2, 'green': 1}, {'red': 8, 'white': 3, 'blue': 9})*100 == 0)
print(probability({'white': 4}, {'red': 8, 'white': 3, 'blue': 9})*100 == 0)
print(probability({'other': 21}, {'red': 8, 'white': 3, 'blue': 9})*100 == 0)
print(probability({'red': 1, 'other': 13}, {'red': 8, 'white': 3, 'blue': 9})*100 == 0)
print()

print(round(probability({'white': 3, 'other': 17}, {'red': 8, 'white': 3, 'blue': 9})*100) == 100)
print(probability({'other': 20}, {'red': 8, 'white': 3, 'blue': 9})*100 == 100)
print(round(probability({'red': 8, 'other': 12}, {'red': 8, 'white': 3, 'blue': 9})*100) == 100)