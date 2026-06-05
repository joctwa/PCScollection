from procyclingstats import Race, Stage
import csv

with open('Stages.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['RaceID','StageID', 'StageDate','VerticalMeters','Distance'])

    primaryString = "race/tour-de-france/"
    baseYear = 1980

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages('stage_url')
            
            for x in stages:
                for y in x.values():
                    stage = Stage(y)
                    writer.writerow([raceString, y, stage.date(), stage.vertical_meters(), stage.distance()])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished TDF')
    
    primaryString = "race/vuelta-a-espana/"
    baseYear = 1980

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages('stage_url')
            
            for x in stages:
                for y in x.values():
                    stage = Stage(y)
                    writer.writerow([raceString, y, stage.date(), stage.vertical_meters(), stage.distance()])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished vuelta')
    
    primaryString = "race/giro-d-italia/"
    baseYear = 1980

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages('stage_url')
            
            for x in stages:
                for y in x.values():
                    stage = Stage(y)
                    writer.writerow([raceString, y, stage.date(), stage.vertical_meters(), stage.distance()])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished giro')

print('done')
