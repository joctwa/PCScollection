from procyclingstats import Race, Stage
import csv

with open('Races.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['RaceID','Race','Year','StartDate','EndDate','Stages'])

    primaryString = "race/tour-de-france/"
    baseYear = 1903

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages()
            writer.writerow([raceString,race.name(),race.year(),race.startdate(),race.enddate(),len(stages)])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished TDF')
    
    primaryString = "race/vuelta-a-espana/"
    baseYear = 1903

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages()
            writer.writerow([raceString,race.name(),race.year(),race.startdate(),race.enddate(),len(stages)])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished vuelta')
    
    primaryString = "race/giro-d-italia/"
    baseYear = 1903

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages()
            writer.writerow([raceString,race.name(),race.year(),race.startdate(),race.enddate(),len(stages)])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished giro')

print('done')
