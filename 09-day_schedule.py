# Pewien program liczy czas tylko w sekundach i resetuje się każdego dnia. Spróbuj zapisać w
# klasycznej formie czas podany w formie sekund

import datetime
from beautifultable import BeautifulTable

wakeup = 23400
lunch = 43200
sleep = 81000

wakeup = str(datetime.timedelta(seconds=wakeup))
lunch = str(datetime.timedelta(seconds=lunch))
sleep = str(datetime.timedelta(seconds=sleep))

table = BeautifulTable()
table.columns.header = ["Plan dnia", "Godzina"]
table.rows.append(["Pobudka", wakeup])
table.rows.append(["Obiad", lunch])
table.rows.append(["Pora spania", sleep])
table.rows.header = ["1", "2", "3"]
print(table)

legend = BeautifulTable()
legend.rows.append(["Pobudka jest o godzinie " + wakeup +
                   "\nObiad będzie gotowy o " + lunch +
                   "\n Pora spania przypada na " + sleep])

print(legend)

# print(f' Pobudka jest o godzinie {wakeup}')
# print(f' Obiad będzie gotowy o {lunch}')
# print(f' Pora spania przypada na {sleep}')
