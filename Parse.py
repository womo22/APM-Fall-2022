import os

DATADIR = ""
DATAFILE = "PA_singlestate_timeseries.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")  #Read first line into list
        count = 0

        # Loop through remaining lines in file object f
        for line in f:
            if count == 501:
                break
            fields = line.split(",") #Split line into list
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry) 
            count += 1
    return data
def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    seventhLine = {'date': '2020-03-08', 'state': 'PA', 'actuals.cases': '6', 'actuals.deaths': '0', 'actuals.newCases': '2', 'actuals.newDeaths': '0', 'metrics.vaccinationsInitiatedRatio': '-', 'metrics.vaccinationsCompletedRatio': '-', 'metrics.caseDensity': '0'}
    fiveHundrethLine = {'date': '2020-06-25', 'state': 'PA', 'actuals.cases': '1215735', 'actuals.deaths': '27675', 'actuals.newCases': '361', 'actuals.newDeaths': 'Platinum', 'metrics.vaccinationsInitiatedRatio': '0.622', 'metrics.vaccinationsCompletedRatio': '0.489', 'metrics.caseDensity': '1.5' }

    assert d[6] == seventhLine
    assert d[499] ==  fiveHundrethLine

    
test()