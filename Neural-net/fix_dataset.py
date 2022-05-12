file = open('./household_power_consumption.txt', 'r')
db = file.read().splitlines()
del db[0]

last_date = None
days = []

for line in db:
    date, time, power, _, voltage, current = line.split(';')[:6]
    if '?' in voltage:

        if last_date != date:
            print(date)
            days.append(date)
            last_date = date

to_add = []
for line in db:
    date = line.split(';')[0]
    if date not in days:
        to_add.append(line)

print(to_add)
with open('./cleaned_dataset.txt', 'w') as file2:
    file2.write('\n'.join(to_add))
