from procyclingstats import Race, Stage
import csv

with open('Stages.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['RaceID','StageID', 'RiderURL','RiderTime', 'RiderStageResult','BreakawayKMs'])

    primaryString = "race/tour-de-france/"
    baseYear = 2025

    while baseYear < 2026:
        try:
            raceString = str(primaryString + str(baseYear))
            race = Race(raceString)
            stages = race.stages('stage_url')
            
            for x in stages:
                for y in x.values():
                    stage = Stage(y)

                    
                    results = stage.results('rider_url','rank','time','breakaway_kms')
                    for a in results:
                        for b in a.values():
                            print(b)

                            if a.values(
                
                    
                    #writer.writerow([raceString, y, stage.date(), stage.vertical_meters(), stage.distance()])
            baseYear += 1
        except:
            baseYear += 1
            pass
    print('finished TDF')
##    
##    primaryString = "race/vuelta-a-espana/"
##    baseYear = 1980
##
##    while baseYear < 2026:
##        try:
##            raceString = str(primaryString + str(baseYear))
##            race = Race(raceString)
##            stages = race.stages('stage_url')
##            
##            for x in stages:
##                for y in x.values():
##                    stage = Stage(y)
##                    writer.writerow([raceString, y, stage.date(), stage.vertical_meters(), stage.distance()])
##            baseYear += 1
##        except:
##            baseYear += 1
##            pass
##    print('finished vuelta')
##    
##    primaryString = "race/giro-d-italia/"
##    baseYear = 1980
##
##    while baseYear < 2026:
##        try:
##            raceString = str(primaryString + str(baseYear))
##            race = Race(raceString)
##            stages = race.stages('stage_url')
##            
##            for x in stages:
##                for y in x.values():
##                    stage = Stage(y)
##                    writer.writerow([raceString, y, stage.date(), stage.vertical_meters(), stage.distance()])
##            baseYear += 1
##        except:
##            baseYear += 1
##            pass
##    print('finished giro')
##
##print('done')
##
