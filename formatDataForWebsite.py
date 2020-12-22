import numpy as np
import pandas as pd
import uuid
import os

rootPath = "/home/mwiecksosa/predicting2020/"

tweet2020Extension = "2020_tweets_d35fd9fd/"
tweet2016Extension = "2016_tweets_8e8cca7c/"

dataPath = rootPath+"data/"+tweet2020Extension

filePath = dataPath+"2020_raceGender_politicalPreference/"

def main():

    filePath2016 = "/home/mwiecksosa/predicting2020/data/2016_tweets_8e8cca7c/2016_raceGender_politicalPreference/raceGender_PoliticalPreference-2016-all.csv"
    filePath2020 = "/home/mwiecksosa/predicting2020/data/2020_tweets_d35fd9fd/2020_raceGender_politicalPreference/raceGender_PoliticalPreference-2020-all.csv"
    df = pd.read_csv(filePath2020)

    electionYear="2020"
    savedir = filePath+electionYear+"_results_"+str(uuid.uuid4())[:8]+"/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)


    states_short = ["National","AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


    states_full = ["National","Alabama", "Alaska", "Arizona", "Arkansas",
                   "California", "Colorado", "Connecticut",
                   "District of Columbia","Delaware","Florida","Georgia",
                   "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                   "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
                   "Michigan", "Minnesota", "Mississippi", "Missouri",
                   "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                   "New Mexico", "New York", "North Carolina", "North Dakota",
                   "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                   "Rhode Island", "South Carolina",
                   "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                   "Virginia","Washington", "West Virginia","Wisconsin",
                   "Wyoming"]


    result = pd.DataFrame()

    for state_short,state_full in zip(states_short,states_full):

        print(state_full)

        totalCounter = 0

        republicanCounter = 0
        democratCounter = 0
        neutralCounter = 0
        unknownPoliticsCounter = 0

        manRepublicanCounter = 0
        manDemocratCounter = 0
        manUnknownCounter = 0
        manNeutralCounter = 0
        womanRepublicanCounter = 0
        womanDemocratCounter = 0
        womanUnknownPoliticsCounter = 0
        womanNeutralCounter = 0
        unknownGenderRepublicanCounter = 0
        unknownGenderDemocratCounter = 0
        unknownGenderUnknownPoliticsCounter = 0
        unknownGenderNeutralCounter = 0


        whiteRepublicanCounter = 0
        whiteDemocratCounter = 0
        whiteUnknownPoliticsCounter = 0
        whiteNeutralCounter = 0
        hispanicRepublicanCounter = 0
        hispanicDemocratCounter = 0
        hispanicUnknownPoliticsCounter = 0
        hispanicNeutralCounter = 0
        apiRepublicanCounter = 0
        apiDemocratCounter = 0
        apiUnknownPoliticsCounter = 0
        apiNeutralCounter = 0
        blackRepublicanCounter = 0
        blackDemocratCounter = 0
        blackUnknownPoliticsCounter = 0
        blackNeutralCounter = 0
        aianRepublicanCounter = 0
        aianDemocratCounter = 0
        aianUnknownPoliticsCounter = 0
        aianNeutralCounter = 0
        unknownRaceEthnicityRepublicanCounter = 0
        unknownRaceEthnicityDemocratCounter = 0
        unknownRaceEthnicityUnknownPoliticsCounter = 0
        unknownRaceEthnicityNeutralCounter = 0

        whiteManRepublicanCounter = 0
        whiteManDemocratCounter = 0
        whiteManUnknownPoliticsCounter = 0
        whiteManNeutralCounter = 0
        whiteWomanRepublicanCounter = 0
        whiteWomanDemocratCounter = 0
        whiteWomanUnknownPoliticsCounter = 0
        whiteWomanNeutralCounter = 0

        hispanicManRepublicanCounter = 0
        hispanicManDemocratCounter = 0
        hispanicManUnknownPoliticsCounter = 0
        hispanicManNeutralCounter = 0
        hispanicWomanRepublicanCounter = 0
        hispanicWomanDemocratCounter = 0
        hispanicWomanUnknownPoliticsCounter = 0
        hispanicWomanNeutralCounter = 0

        apiManRepublicanCounter = 0
        apiManDemocratCounter = 0
        apiManUnknownPoliticsCounter = 0
        apiManNeutralCounter = 0
        apiWomanRepublicanCounter = 0
        apiWomanDemocratCounter = 0
        apiWomanUnknownPoliticsCounter = 0
        apiWomanNeutralCounter = 0

        blackManRepublicanCounter = 0
        blackManDemocratCounter = 0
        blackManUnknownPoliticsCounter = 0
        blackManNeutralCounter = 0
        blackWomanRepublicanCounter = 0
        blackWomanDemocratCounter = 0
        blackWomanUnknownPoliticsCounter = 0
        blackWomanNeutralCounter = 0

        aianManRepublicanCounter = 0
        aianManDemocratCounter = 0
        aianManUnknownPoliticsCounter = 0
        aianManNeutralCounter = 0
        aianWomanRepublicanCounter = 0
        aianWomanDemocratCounter = 0
        aianWomanUnknownPoliticsCounter = 0
        aianWomanNeutralCounter = 0


        whiteUnknownGenderRepublicanCounter = 0
        whiteUnknownGenderDemocratCounter = 0
        whiteUnknownGenderUnknownPoliticsCounter = 0
        whiteUnknownGenderNeutralCounter = 0

        hispanicUnknownGenderRepublicanCounter = 0
        hispanicUnknownGenderDemocratCounter = 0
        hispanicUnknownGenderUnknownPoliticsCounter = 0
        hispanicUnknownGenderNeutralCounter = 0

        apiUnknownGenderRepublicanCounter = 0
        apiUnknownGenderDemocratCounter = 0
        apiUnknownGenderUnknownPoliticsCounter = 0
        apiUnknownGenderNeutralCounter = 0

        blackUnknownGenderRepublicanCounter = 0
        blackUnknownGenderDemocratCounter = 0
        blackUnknownGenderUnknownPoliticsCounter = 0
        blackUnknownGenderNeutralCounter = 0

        aianUnknownGenderRepublicanCounter = 0
        aianUnknownGenderDemocratCounter = 0
        aianUnknownGenderUnknownPoliticsCounter = 0
        aianUnknownGenderNeutralCounter = 0

        unknownRaceEthnicityUnknownGenderRepublicanCounter = 0
        unknownRaceEthnicityUnknownGenderDemocratCounter = 0
        unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter = 0
        unknownRaceEthnicityUnknownGenderNeutralCounter = 0

        unknownRaceEthnicityManRepublicanCounter = 0
        unknownRaceEthnicityManDemocratCounter = 0
        unknownRaceEthnicityManUnknownPoliticsCounter = 0
        unknownRaceEthnicityManNeutralCounter = 0
        unknownRaceEthnicityWomanRepublicanCounter = 0
        unknownRaceEthnicityWomanDemocratCounter = 0
        unknownRaceEthnicityWomanUnknownPoliticsCounter = 0
        unknownRaceEthnicityWomanNeutralCounter = 0

        for i,row in df.iterrows():
            if type(row['near']) != str:
                continue
            elif state_full == "National" or state_short == row['near'][-len(state_short):] or state_full == row['near'][-len(state_full):]:
                print(row['near'])
                totalCounter += 1
                if row['race/ethnicity'] == 'white':
                    if row['gender'] == 'M':
                        if row['pp'] == 0.: # neutral
                            whiteManNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            whiteManRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            whiteManDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            whiteManUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    elif row['gender'] == 'F':
                        if row['pp'] == 0.: # neutral
                            whiteWomanNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            whiteWomanRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            whiteWomanDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            whiteWomanUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    else: # UnknownGender
                        if row['pp'] == 0.: # neutral
                            whiteUnknownGenderNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            whiteUnknownGenderRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            whiteUnknownGenderDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            whiteUnknownGenderUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1

                elif row['race/ethnicity'] == 'hispanic':
                    if row['gender'] == 'M':
                        if row['pp'] == 0.: # neutral
                            hispanicManNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            hispanicManRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            hispanicManDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            hispanicManUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    elif row['gender'] == 'F':
                        if row['pp'] == 0.: # neutral
                            hispanicWomanNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            hispanicWomanRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            hispanicWomanDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            hispanicWomanUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    else: # UnknownGender
                        if row['pp'] == 0.: # neutral
                            hispanicUnknownGenderNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            hispanicUnknownGenderRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            hispanicUnknownGenderDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            hispanicUnknownGenderUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1

                elif row['race/ethnicity'] == 'api':
                    if row['gender'] == 'M':
                        if row['pp'] == 0.: # neutral
                            apiManNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            apiManRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            apiManDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            apiManUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1

                    elif row['gender'] == 'F':
                        if row['pp'] == 0.: # neutral
                            apiWomanNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            apiWomanRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            apiWomanDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            apiWomanUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    else: # UnknownGender
                        if row['pp'] == 0.: # neutral
                            apiUnknownGenderNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            apiUnknownGenderRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            apiUnknownGenderDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            apiUnknownGenderUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                elif row['race/ethnicity'] == 'black':
                    if row['gender'] == 'M':
                        if row['pp'] == 0.: # neutral
                            blackManNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            blackManRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            blackManDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            blackManUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    elif row['gender'] == 'F':
                        if row['pp'] == 0.: # neutral
                            blackWomanNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            blackWomanRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            blackWomanDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            blackWomanUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    else: # UnknownGender
                        if row['pp'] == 0.: # neutral
                            blackUnknownGenderNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            blackUnknownGenderRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            blackUnknownGenderDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            blackUnknownGenderUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1

                elif row['race/ethnicity'] == 'aian':
                    if row['gender'] == 'M':
                        if row['pp'] == 0.: # neutral
                            aianManNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            aianManRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            aianManDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            aianManUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    elif row['gender'] == 'F':
                        if row['pp'] == 0.: # neutral
                            aianWomanNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            aianWomanRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            aianWomanDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            aianWomanUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    else: # UnknownGender
                        if row['pp'] == 0.: # neutral
                            aianUnknownGenderNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            aianUnknownGenderRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            aianUnknownGenderDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            aianUnknownGenderUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1

                else: # unknownRaceEthnicity
                    if row['gender'] == 'M':
                        if row['pp'] == 0.: # neutral
                            unknownRaceEthnicityManNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            unknownRaceEthnicityManRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            unknownRaceEthnicityManDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            unknownRaceEthnicityManUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    elif row['gender'] == 'F':
                        if row['pp'] == 0.: # neutral
                            unknownRaceEthnicityWomanNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            unknownRaceEthnicityWomanRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            unknownRaceEthnicityWomanDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            unknownRaceEthnicityWomanUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1
                    else: # UnknownGender
                        if row['pp'] == 0.: # neutral
                            unknownRaceEthnicityUnknownGenderNeutralCounter += 1
                            neutralCounter += 1
                        elif row['pp'] == 1.: # republican
                            unknownRaceEthnicityUnknownGenderRepublicanCounter += 1
                            republicanCounter += 1
                        elif row['pp'] == 2.: # democrat
                            unknownRaceEthnicityUnknownGenderDemocratCounter += 1
                            democratCounter += 1
                        else: # UnknownPolitics
                            unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter += 1
                            unknownPoliticsCounter += 1



        ### RACE/ETHNICITY + PARTY ###
        whiteRepublicanCounter = whiteManRepublicanCounter + whiteWomanRepublicanCounter + whiteUnknownGenderRepublicanCounter
        whiteDemocratCounter = whiteManDemocratCounter + whiteWomanDemocratCounter + whiteUnknownGenderDemocratCounter
        whiteNeutralCounter = whiteManNeutralCounter + whiteWomanNeutralCounter + whiteUnknownGenderNeutralCounter
        whiteUnknownPoliticsCounter = whiteManUnknownPoliticsCounter + whiteWomanUnknownPoliticsCounter + whiteUnknownGenderUnknownPoliticsCounter

        hispanicRepublicanCounter = hispanicManRepublicanCounter + hispanicWomanRepublicanCounter + hispanicUnknownGenderRepublicanCounter
        hispanicDemocratCounter = hispanicManDemocratCounter + hispanicWomanDemocratCounter + hispanicUnknownGenderDemocratCounter
        hispanicNeutralCounter = hispanicManNeutralCounter + hispanicWomanNeutralCounter + hispanicUnknownGenderNeutralCounter
        hispanicUnknownPoliticsCounter = hispanicManUnknownPoliticsCounter + hispanicWomanUnknownPoliticsCounter + hispanicUnknownGenderUnknownPoliticsCounter

        apiRepublicanCounter = apiManRepublicanCounter + apiWomanRepublicanCounter + apiUnknownGenderRepublicanCounter
        apiDemocratCounter = apiManDemocratCounter + apiWomanDemocratCounter + apiUnknownGenderDemocratCounter
        apiNeutralCounter = apiManNeutralCounter + apiWomanNeutralCounter + apiUnknownGenderNeutralCounter
        apiUnknownPoliticsCounter = apiManUnknownPoliticsCounter + apiWomanUnknownPoliticsCounter + apiUnknownGenderUnknownPoliticsCounter

        blackRepublicanCounter = blackManRepublicanCounter + blackWomanRepublicanCounter + blackUnknownGenderRepublicanCounter
        blackDemocratCounter = blackManDemocratCounter + blackWomanDemocratCounter + blackUnknownGenderDemocratCounter
        blackNeutralCounter = blackManNeutralCounter + blackWomanNeutralCounter + blackUnknownGenderNeutralCounter
        blackUnknownPoliticsCounter = blackManUnknownPoliticsCounter + blackWomanUnknownPoliticsCounter + blackUnknownGenderUnknownPoliticsCounter

        aianRepublicanCounter = aianManRepublicanCounter + aianWomanRepublicanCounter + aianUnknownGenderRepublicanCounter
        aianDemocratCounter = aianManDemocratCounter + aianWomanDemocratCounter + aianUnknownGenderDemocratCounter
        aianNeutralCounter = aianManNeutralCounter + aianWomanNeutralCounter + aianUnknownGenderNeutralCounter
        aianUnknownPoliticsCounter = aianManUnknownPoliticsCounter + aianWomanUnknownPoliticsCounter + aianUnknownGenderUnknownPoliticsCounter

        unknownRaceEthnicityRepublicanCounter = unknownRaceEthnicityManRepublicanCounter + unknownRaceEthnicityWomanRepublicanCounter + unknownRaceEthnicityUnknownGenderRepublicanCounter
        unknownRaceEthnicityDemocratCounter = unknownRaceEthnicityManDemocratCounter + unknownRaceEthnicityWomanDemocratCounter + unknownRaceEthnicityUnknownGenderDemocratCounter
        unknownRaceEthnicityNeutralCounter = unknownRaceEthnicityManNeutralCounter + unknownRaceEthnicityWomanNeutralCounter + unknownRaceEthnicityUnknownGenderNeutralCounter
        unknownRaceEthnicityUnknownPoliticsCounter = unknownRaceEthnicityManUnknownPoliticsCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter


        ### GENDER + PARTY ###
        manRepublicanCounter = whiteManRepublicanCounter + hispanicManRepublicanCounter + apiManRepublicanCounter + blackManRepublicanCounter + aianManRepublicanCounter + unknownRaceEthnicityManRepublicanCounter
        womanRepublicanCounter = whiteWomanRepublicanCounter + hispanicWomanRepublicanCounter + apiWomanRepublicanCounter + blackWomanRepublicanCounter + aianWomanRepublicanCounter + unknownRaceEthnicityWomanRepublicanCounter
        unknownGenderRepublicanCounter = whiteUnknownGenderRepublicanCounter + hispanicUnknownGenderRepublicanCounter + apiUnknownGenderRepublicanCounter + blackUnknownGenderRepublicanCounter + aianUnknownGenderRepublicanCounter + unknownRaceEthnicityUnknownGenderRepublicanCounter

        manDemocratCounter = whiteManDemocratCounter + hispanicManDemocratCounter + apiManDemocratCounter + blackManDemocratCounter + aianManDemocratCounter + unknownRaceEthnicityManDemocratCounter
        womanDemocratCounter = whiteWomanDemocratCounter + hispanicWomanDemocratCounter + apiWomanDemocratCounter + blackWomanDemocratCounter + aianWomanDemocratCounter + unknownRaceEthnicityWomanDemocratCounter
        unknownGenderDemocratCounter = whiteUnknownGenderDemocratCounter + hispanicUnknownGenderDemocratCounter + apiUnknownGenderDemocratCounter + blackUnknownGenderDemocratCounter + aianUnknownGenderDemocratCounter + unknownRaceEthnicityUnknownGenderDemocratCounter

        manNeutralCounter = whiteManNeutralCounter + hispanicManNeutralCounter + apiManNeutralCounter + blackManNeutralCounter + aianManNeutralCounter + unknownRaceEthnicityManNeutralCounter
        womanNeutralCounter = whiteWomanNeutralCounter + hispanicWomanNeutralCounter + apiWomanNeutralCounter + blackWomanNeutralCounter + aianWomanNeutralCounter + unknownRaceEthnicityWomanNeutralCounter
        unknownGenderNeutralCounter = whiteUnknownGenderNeutralCounter + hispanicUnknownGenderNeutralCounter + apiUnknownGenderNeutralCounter + blackUnknownGenderNeutralCounter + aianUnknownGenderNeutralCounter + unknownRaceEthnicityUnknownGenderNeutralCounter

        manUnknownPoliticsCounter = whiteManUnknownPoliticsCounter + hispanicManUnknownPoliticsCounter + apiManUnknownPoliticsCounter + blackManUnknownPoliticsCounter + aianManUnknownPoliticsCounter + unknownRaceEthnicityManUnknownPoliticsCounter
        womanUnknownPoliticsCounter = whiteWomanUnknownPoliticsCounter + hispanicWomanUnknownPoliticsCounter + apiWomanUnknownPoliticsCounter + blackWomanUnknownPoliticsCounter + aianWomanUnknownPoliticsCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter
        unknownGenderUnknownPoliticsCounter = whiteUnknownGenderUnknownPoliticsCounter + hispanicUnknownGenderUnknownPoliticsCounter + apiUnknownGenderUnknownPoliticsCounter + blackUnknownGenderUnknownPoliticsCounter + aianUnknownGenderUnknownPoliticsCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter


        ### PARTY ###
        # SHOULD BE EQUAL TO republicanCounter
        republicanCounterByAddingAcrossRaceEthnicity = whiteRepublicanCounter + hispanicRepublicanCounter + apiRepublicanCounter +blackRepublicanCounter + aianRepublicanCounter + unknownRaceEthnicityRepublicanCounter
        republicanCounterByAddingAcrossGender = manRepublicanCounter + womanRepublicanCounter + unknownGenderRepublicanCounter

        # SHOULD BE EQUAL TO democratCounter
        democratCounterByAddingAcrossRaceEthnicity = whiteDemocratCounter + hispanicDemocratCounter + apiDemocratCounter +blackDemocratCounter + aianDemocratCounter + unknownRaceEthnicityDemocratCounter
        democratCounterByAddingAcrossGender = manDemocratCounter + womanDemocratCounter + unknownGenderDemocratCounter

        # SHOULD BE EQUAL TO neutralCounter
        neutralCounterByAddingAcrossRaceEthnicity = whiteNeutralCounter + hispanicNeutralCounter + apiNeutralCounter +blackNeutralCounter + aianNeutralCounter + unknownRaceEthnicityNeutralCounter
        neutralCounterByAddingAcrossGender = manNeutralCounter + womanNeutralCounter + unknownGenderNeutralCounter

        # SHOULD BE EQUAL TO unknownPoliticsCounter
        unknownPoliticsCounterByAddingAcrossRaceEthnicity = whiteUnknownPoliticsCounter + hispanicUnknownPoliticsCounter + apiUnknownPoliticsCounter +blackUnknownPoliticsCounter + aianUnknownPoliticsCounter + unknownRaceEthnicityUnknownPoliticsCounter
        unknownPoliticsCounterByAddingAcrossGender = manUnknownPoliticsCounter + womanUnknownPoliticsCounter + unknownGenderUnknownPoliticsCounter



        ### PERCENTS ###
        # RACE/ETHNICITY + GENDER + PARTY PERCENT
        if (whiteManRepublicanCounter + whiteManDemocratCounter + whiteManNeutralCounter + whiteManUnknownPoliticsCounter) != 0:
            whiteManPercentRepublican = whiteManRepublicanCounter / (whiteManRepublicanCounter + whiteManDemocratCounter + whiteManNeutralCounter + whiteManUnknownPoliticsCounter)
            whiteManPercentDemocrat = whiteManDemocratCounter / (whiteManRepublicanCounter + whiteManDemocratCounter + whiteManNeutralCounter + whiteManUnknownPoliticsCounter)
            whiteManPercentNeutral = whiteManNeutralCounter / (whiteManRepublicanCounter + whiteManDemocratCounter + whiteManNeutralCounter + whiteManUnknownPoliticsCounter)
            whiteManPercentUnknownPolitics = whiteManUnknownPoliticsCounter / (whiteManRepublicanCounter + whiteManDemocratCounter + whiteManNeutralCounter + whiteManUnknownPoliticsCounter)
        else:
            whiteManPercentRepublican = -1
            whiteManPercentDemocrat = -1
            whiteManPercentNeutral = -1
            whiteManPercentUnknownPolitics = -1

        if (whiteWomanRepublicanCounter + whiteWomanDemocratCounter + whiteWomanNeutralCounter + whiteWomanUnknownPoliticsCounter) != 0:
            whiteWomanPercentRepublican = whiteWomanRepublicanCounter / (whiteWomanRepublicanCounter + whiteWomanDemocratCounter + whiteWomanNeutralCounter + whiteWomanUnknownPoliticsCounter)
            whiteWomanPercentDemocrat = whiteWomanDemocratCounter / (whiteWomanRepublicanCounter + whiteWomanDemocratCounter + whiteWomanNeutralCounter + whiteWomanUnknownPoliticsCounter)
            whiteWomanPercentNeutral = whiteWomanNeutralCounter / (whiteWomanRepublicanCounter + whiteWomanDemocratCounter + whiteWomanNeutralCounter + whiteWomanUnknownPoliticsCounter)
            whiteWomanPercentUnknownPolitics = whiteWomanUnknownPoliticsCounter / (whiteWomanRepublicanCounter + whiteWomanDemocratCounter + whiteWomanNeutralCounter + whiteWomanUnknownPoliticsCounter)
        else:
            whiteWomanPercentRepublican = -1
            whiteWomanPercentDemocrat = -1
            whiteWomanPercentNeutral = -1
            whiteWomanPercentUnknownPolitics = -1

        if (whiteUnknownGenderRepublicanCounter + whiteUnknownGenderDemocratCounter + whiteUnknownGenderNeutralCounter + whiteUnknownGenderUnknownPoliticsCounter) != 0:
            whiteUnknownGenderPercentRepublican = whiteUnknownGenderRepublicanCounter / (whiteUnknownGenderRepublicanCounter + whiteUnknownGenderDemocratCounter + whiteUnknownGenderNeutralCounter + whiteUnknownGenderUnknownPoliticsCounter)
            whiteUnknownGenderPercentDemocrat = whiteUnknownGenderDemocratCounter / (whiteUnknownGenderRepublicanCounter + whiteUnknownGenderDemocratCounter + whiteUnknownGenderNeutralCounter + whiteUnknownGenderUnknownPoliticsCounter)
            whiteUnknownGenderPercentNeutral = whiteUnknownGenderNeutralCounter / (whiteUnknownGenderRepublicanCounter + whiteUnknownGenderDemocratCounter + whiteUnknownGenderNeutralCounter + whiteUnknownGenderUnknownPoliticsCounter)
            whiteUnknownGenderPercentUnknownPolitics = whiteUnknownGenderUnknownPoliticsCounter / (whiteUnknownGenderRepublicanCounter + whiteUnknownGenderDemocratCounter + whiteUnknownGenderNeutralCounter + whiteUnknownGenderUnknownPoliticsCounter)
        else:
            whiteUnknownGenderPercentRepublican = -1
            whiteUnknownGenderPercentDemocrat = -1
            whiteUnknownGenderPercentNeutral = -1
            whiteUnknownGenderPercentUnknownPolitics = -1

        if (hispanicManRepublicanCounter + hispanicManDemocratCounter + hispanicManNeutralCounter + hispanicManUnknownPoliticsCounter) != 0:
            hispanicManPercentRepublican = hispanicManRepublicanCounter / (hispanicManRepublicanCounter + hispanicManDemocratCounter + hispanicManNeutralCounter + hispanicManUnknownPoliticsCounter)
            hispanicManPercentDemocrat = hispanicManDemocratCounter / (hispanicManRepublicanCounter + hispanicManDemocratCounter + hispanicManNeutralCounter + hispanicManUnknownPoliticsCounter)
            hispanicManPercentNeutral = hispanicManNeutralCounter / (hispanicManRepublicanCounter + hispanicManDemocratCounter + hispanicManNeutralCounter + hispanicManUnknownPoliticsCounter)
            hispanicManPercentUnknownPolitics = hispanicManUnknownPoliticsCounter / (hispanicManRepublicanCounter + hispanicManDemocratCounter + hispanicManNeutralCounter + hispanicManUnknownPoliticsCounter)
        else:
            hispanicManPercentRepublican = -1
            hispanicManPercentDemocrat = -1
            hispanicManPercentNeutral = -1
            hispanicManPercentUnknownPolitics = -1

        if (hispanicWomanRepublicanCounter + hispanicWomanDemocratCounter + hispanicWomanNeutralCounter + hispanicWomanUnknownPoliticsCounter) != 0:
            hispanicWomanPercentRepublican = hispanicWomanRepublicanCounter / (hispanicWomanRepublicanCounter + hispanicWomanDemocratCounter + hispanicWomanNeutralCounter + hispanicWomanUnknownPoliticsCounter)
            hispanicWomanPercentDemocrat = hispanicWomanDemocratCounter / (hispanicWomanRepublicanCounter + hispanicWomanDemocratCounter + hispanicWomanNeutralCounter + hispanicWomanUnknownPoliticsCounter)
            hispanicWomanPercentNeutral = hispanicWomanNeutralCounter / (hispanicWomanRepublicanCounter + hispanicWomanDemocratCounter + hispanicWomanNeutralCounter + hispanicWomanUnknownPoliticsCounter)
            hispanicWomanPercentUnknownPolitics = hispanicWomanUnknownPoliticsCounter / (hispanicWomanRepublicanCounter + hispanicWomanDemocratCounter + hispanicWomanNeutralCounter + hispanicWomanUnknownPoliticsCounter)
        else:
            hispanicWomanPercentRepublican = -1
            hispanicWomanPercentDemocrat = -1
            hispanicWomanPercentNeutral = -1
            hispanicWomanPercentUnknownPolitics = -1

        if (hispanicUnknownGenderRepublicanCounter + hispanicUnknownGenderDemocratCounter + hispanicUnknownGenderNeutralCounter + hispanicUnknownGenderUnknownPoliticsCounter) != 0:
            hispanicUnknownGenderPercentRepublican = hispanicUnknownGenderRepublicanCounter / (hispanicUnknownGenderRepublicanCounter + hispanicUnknownGenderDemocratCounter + hispanicUnknownGenderNeutralCounter + hispanicUnknownGenderUnknownPoliticsCounter)
            hispanicUnknownGenderPercentDemocrat = hispanicUnknownGenderDemocratCounter / (hispanicUnknownGenderRepublicanCounter + hispanicUnknownGenderDemocratCounter + hispanicUnknownGenderNeutralCounter + hispanicUnknownGenderUnknownPoliticsCounter)
            hispanicUnknownGenderPercentNeutral = hispanicUnknownGenderNeutralCounter / (hispanicUnknownGenderRepublicanCounter + hispanicUnknownGenderDemocratCounter + hispanicUnknownGenderNeutralCounter + hispanicUnknownGenderUnknownPoliticsCounter)
            hispanicUnknownGenderPercentUnknownPolitics = hispanicUnknownGenderUnknownPoliticsCounter / (hispanicUnknownGenderRepublicanCounter + hispanicUnknownGenderDemocratCounter + hispanicUnknownGenderNeutralCounter + hispanicUnknownGenderUnknownPoliticsCounter)
        else:
            hispanicUnknownGenderPercentRepublican = -1
            hispanicUnknownGenderPercentDemocrat = -1
            hispanicUnknownGenderPercentNeutral = -1
            hispanicUnknownGenderPercentUnknownPolitics = -1

        if (apiManRepublicanCounter + apiManDemocratCounter + apiManNeutralCounter + apiManUnknownPoliticsCounter) != 0:
            apiManPercentRepublican = apiManRepublicanCounter / (apiManRepublicanCounter + apiManDemocratCounter + apiManNeutralCounter + apiManUnknownPoliticsCounter)
            apiManPercentDemocrat = apiManDemocratCounter / (apiManRepublicanCounter + apiManDemocratCounter + apiManNeutralCounter + apiManUnknownPoliticsCounter)
            apiManPercentNeutral = apiManNeutralCounter / (apiManRepublicanCounter + apiManDemocratCounter + apiManNeutralCounter + apiManUnknownPoliticsCounter)
            apiManPercentUnknownPolitics = apiManUnknownPoliticsCounter / (apiManRepublicanCounter + apiManDemocratCounter + apiManNeutralCounter + apiManUnknownPoliticsCounter)
        else:
            apiManPercentRepublican = -1
            apiManPercentDemocrat = -1
            apiManPercentNeutral = -1
            apiManPercentUnknownPolitics = -1

        if (apiWomanRepublicanCounter + apiWomanDemocratCounter + apiWomanNeutralCounter + apiWomanUnknownPoliticsCounter) != 0:
            apiWomanPercentRepublican = apiWomanRepublicanCounter / (apiWomanRepublicanCounter + apiWomanDemocratCounter + apiWomanNeutralCounter + apiWomanUnknownPoliticsCounter)
            apiWomanPercentDemocrat = apiWomanDemocratCounter / (apiWomanRepublicanCounter + apiWomanDemocratCounter + apiWomanNeutralCounter + apiWomanUnknownPoliticsCounter)
            apiWomanPercentNeutral = apiWomanNeutralCounter / (apiWomanRepublicanCounter + apiWomanDemocratCounter + apiWomanNeutralCounter + apiWomanUnknownPoliticsCounter)
            apiWomanPercentUnknownPolitics = apiWomanUnknownPoliticsCounter / (apiWomanRepublicanCounter + apiWomanDemocratCounter + apiWomanNeutralCounter + apiWomanUnknownPoliticsCounter)
        else:
            apiWomanPercentRepublican = -1
            apiWomanPercentDemocrat = -1
            apiWomanPercentNeutral = -1
            apiWomanPercentUnknownPolitics = -1


        if (apiUnknownGenderRepublicanCounter + apiUnknownGenderDemocratCounter + apiUnknownGenderNeutralCounter + apiUnknownGenderUnknownPoliticsCounter):
            apiUnknownGenderPercentRepublican = apiUnknownGenderRepublicanCounter / (apiUnknownGenderRepublicanCounter + apiUnknownGenderDemocratCounter + apiUnknownGenderNeutralCounter + apiUnknownGenderUnknownPoliticsCounter)
            apiUnknownGenderPercentDemocrat = apiUnknownGenderDemocratCounter / (apiUnknownGenderRepublicanCounter + apiUnknownGenderDemocratCounter + apiUnknownGenderNeutralCounter + apiUnknownGenderUnknownPoliticsCounter)
            apiUnknownGenderPercentNeutral = apiUnknownGenderNeutralCounter / (apiUnknownGenderRepublicanCounter + apiUnknownGenderDemocratCounter + apiUnknownGenderNeutralCounter + apiUnknownGenderUnknownPoliticsCounter)
            apiUnknownGenderPercentUnknownPolitics = apiUnknownGenderUnknownPoliticsCounter / (apiUnknownGenderRepublicanCounter + apiUnknownGenderDemocratCounter + apiUnknownGenderNeutralCounter + apiUnknownGenderUnknownPoliticsCounter)
        else:
            apiUnknownGenderPercentRepublican = -1
            apiUnknownGenderPercentDemocrat = -1
            apiUnknownGenderPercentNeutral = -1
            apiUnknownGenderPercentUnknownPolitics = -1


        if (blackManRepublicanCounter + blackManDemocratCounter + blackManNeutralCounter + blackManUnknownPoliticsCounter) != 0:
            blackManPercentRepublican = blackManRepublicanCounter / (blackManRepublicanCounter + blackManDemocratCounter + blackManNeutralCounter + blackManUnknownPoliticsCounter)
            blackManPercentDemocrat = blackManDemocratCounter / (blackManRepublicanCounter + blackManDemocratCounter + blackManNeutralCounter + blackManUnknownPoliticsCounter)
            blackManPercentNeutral = blackManNeutralCounter / (blackManRepublicanCounter + blackManDemocratCounter + blackManNeutralCounter + blackManUnknownPoliticsCounter)
            blackManPercentUnknownPolitics = blackManUnknownPoliticsCounter / (blackManRepublicanCounter + blackManDemocratCounter + blackManNeutralCounter + blackManUnknownPoliticsCounter)
        else:
            blackManPercentRepublican = -1
            blackManPercentDemocrat = -1
            blackManPercentNeutral = -1
            blackManPercentUnknownPolitics = -1

        if (blackWomanRepublicanCounter + blackWomanDemocratCounter + blackWomanNeutralCounter + blackWomanUnknownPoliticsCounter) != 0:
            blackWomanPercentRepublican = blackWomanRepublicanCounter / (blackWomanRepublicanCounter + blackWomanDemocratCounter + blackWomanNeutralCounter + blackWomanUnknownPoliticsCounter)
            blackWomanPercentDemocrat = blackWomanDemocratCounter / (blackWomanRepublicanCounter + blackWomanDemocratCounter + blackWomanNeutralCounter + blackWomanUnknownPoliticsCounter)
            blackWomanPercentNeutral = blackWomanNeutralCounter / (blackWomanRepublicanCounter + blackWomanDemocratCounter + blackWomanNeutralCounter + blackWomanUnknownPoliticsCounter)
            blackWomanPercentUnknownPolitics = blackWomanUnknownPoliticsCounter / (blackWomanRepublicanCounter + blackWomanDemocratCounter + blackWomanNeutralCounter + blackWomanUnknownPoliticsCounter)
        else:
            blackWomanPercentRepublican = -1
            blackWomanPercentDemocrat = -1
            blackWomanPercentNeutral = -1
            blackWomanPercentUnknownPolitics = -1


        if (blackUnknownGenderRepublicanCounter + blackUnknownGenderDemocratCounter + blackUnknownGenderNeutralCounter + blackUnknownGenderUnknownPoliticsCounter) != 0:
            blackUnknownGenderPercentRepublican = blackUnknownGenderRepublicanCounter / (blackUnknownGenderRepublicanCounter + blackUnknownGenderDemocratCounter + blackUnknownGenderNeutralCounter + blackUnknownGenderUnknownPoliticsCounter)
            blackUnknownGenderPercentDemocrat = blackUnknownGenderDemocratCounter / (blackUnknownGenderRepublicanCounter + blackUnknownGenderDemocratCounter + blackUnknownGenderNeutralCounter + blackUnknownGenderUnknownPoliticsCounter)
            blackUnknownGenderPercentNeutral = blackUnknownGenderNeutralCounter / (blackUnknownGenderRepublicanCounter + blackUnknownGenderDemocratCounter + blackUnknownGenderNeutralCounter + blackUnknownGenderUnknownPoliticsCounter)
            blackUnknownGenderPercentUnknownPolitics = blackUnknownGenderUnknownPoliticsCounter / (blackUnknownGenderRepublicanCounter + blackUnknownGenderDemocratCounter + blackUnknownGenderNeutralCounter + blackUnknownGenderUnknownPoliticsCounter)
        else:
            blackUnknownGenderPercentRepublican = -1
            blackUnknownGenderPercentDemocrat = -1
            blackUnknownGenderPercentNeutral = -1
            blackUnknownGenderPercentUnknownPolitics = -1

        if (aianManRepublicanCounter + aianManDemocratCounter + aianManNeutralCounter + aianManUnknownPoliticsCounter) != 0:
            aianManPercentRepublican = aianManRepublicanCounter / (aianManRepublicanCounter + aianManDemocratCounter + aianManNeutralCounter + aianManUnknownPoliticsCounter)
            aianManPercentDemocrat = aianManDemocratCounter / (aianManRepublicanCounter + aianManDemocratCounter + aianManNeutralCounter + aianManUnknownPoliticsCounter)
            aianManPercentNeutral = aianManNeutralCounter / (aianManRepublicanCounter + aianManDemocratCounter + aianManNeutralCounter + aianManUnknownPoliticsCounter)
            aianManPercentUnknownPolitics = aianManUnknownPoliticsCounter / (aianManRepublicanCounter + aianManDemocratCounter + aianManNeutralCounter + aianManUnknownPoliticsCounter)
        else:
            aianManPercentRepublican = -1
            aianManPercentDemocrat = -1
            aianManPercentNeutral = -1
            aianManPercentUnknownPolitics = -1

        if (aianWomanRepublicanCounter + aianWomanDemocratCounter + aianWomanNeutralCounter + aianWomanUnknownPoliticsCounter) != 0:
            aianWomanPercentRepublican = aianWomanRepublicanCounter / (aianWomanRepublicanCounter + aianWomanDemocratCounter + aianWomanNeutralCounter + aianWomanUnknownPoliticsCounter)
            aianWomanPercentDemocrat = aianWomanDemocratCounter / (aianWomanRepublicanCounter + aianWomanDemocratCounter + aianWomanNeutralCounter + aianWomanUnknownPoliticsCounter)
            aianWomanPercentNeutral = aianWomanNeutralCounter / (aianWomanRepublicanCounter + aianWomanDemocratCounter + aianWomanNeutralCounter + aianWomanUnknownPoliticsCounter)
            aianWomanPercentUnknownPolitics = aianWomanUnknownPoliticsCounter / (aianWomanRepublicanCounter + aianWomanDemocratCounter + aianWomanNeutralCounter + aianWomanUnknownPoliticsCounter)
        else:
            aianWomanPercentRepublican = -1
            aianWomanPercentDemocrat = -1
            aianWomanPercentNeutral = -1
            aianWomanPercentUnknownPolitics = -1


        if (aianUnknownGenderRepublicanCounter + aianUnknownGenderDemocratCounter + aianUnknownGenderNeutralCounter + aianUnknownGenderUnknownPoliticsCounter) != 0:
            aianUnknownGenderPercentRepublican = aianUnknownGenderRepublicanCounter / (aianUnknownGenderRepublicanCounter + aianUnknownGenderDemocratCounter + aianUnknownGenderNeutralCounter + aianUnknownGenderUnknownPoliticsCounter)
            aianUnknownGenderPercentDemocrat = aianUnknownGenderDemocratCounter / (aianUnknownGenderRepublicanCounter + aianUnknownGenderDemocratCounter + aianUnknownGenderNeutralCounter + aianUnknownGenderUnknownPoliticsCounter)
            aianUnknownGenderPercentNeutral = aianUnknownGenderNeutralCounter / (aianUnknownGenderRepublicanCounter + aianUnknownGenderDemocratCounter + aianUnknownGenderNeutralCounter + aianUnknownGenderUnknownPoliticsCounter)
            aianUnknownGenderPercentUnknownPolitics = aianUnknownGenderUnknownPoliticsCounter / (aianUnknownGenderRepublicanCounter + aianUnknownGenderDemocratCounter + aianUnknownGenderNeutralCounter + aianUnknownGenderUnknownPoliticsCounter)
        else:
            aianUnknownGenderPercentRepublican = -1
            aianUnknownGenderPercentDemocrat = -1
            aianUnknownGenderPercentNeutral = -1
            aianUnknownGenderPercentUnknownPolitics = -1


        if (unknownRaceEthnicityManRepublicanCounter + unknownRaceEthnicityManDemocratCounter + unknownRaceEthnicityManNeutralCounter + unknownRaceEthnicityManUnknownPoliticsCounter):
            unknownRaceEthnicityManPercentRepublican = unknownRaceEthnicityManRepublicanCounter / (unknownRaceEthnicityManRepublicanCounter + unknownRaceEthnicityManDemocratCounter + unknownRaceEthnicityManNeutralCounter + unknownRaceEthnicityManUnknownPoliticsCounter)
            unknownRaceEthnicityManPercentDemocrat = unknownRaceEthnicityManDemocratCounter / (unknownRaceEthnicityManRepublicanCounter + unknownRaceEthnicityManDemocratCounter + unknownRaceEthnicityManNeutralCounter + unknownRaceEthnicityManUnknownPoliticsCounter)
            unknownRaceEthnicityManPercentNeutral = unknownRaceEthnicityManNeutralCounter / (unknownRaceEthnicityManRepublicanCounter + unknownRaceEthnicityManDemocratCounter + unknownRaceEthnicityManNeutralCounter + unknownRaceEthnicityManUnknownPoliticsCounter)
            unknownRaceEthnicityManPercentUnknownPolitics = unknownRaceEthnicityManUnknownPoliticsCounter / (unknownRaceEthnicityManRepublicanCounter + unknownRaceEthnicityManDemocratCounter + unknownRaceEthnicityManNeutralCounter + unknownRaceEthnicityManUnknownPoliticsCounter)
        else:
            unknownRaceEthnicityManPercentRepublican = -1
            unknownRaceEthnicityManPercentDemocrat = -1
            unknownRaceEthnicityManPercentNeutral = -1
            unknownRaceEthnicityManPercentUnknownPolitics = -1


        if (unknownRaceEthnicityWomanRepublicanCounter + unknownRaceEthnicityWomanDemocratCounter + unknownRaceEthnicityWomanNeutralCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter) != 0:
            unknownRaceEthnicityWomanPercentRepublican = unknownRaceEthnicityWomanRepublicanCounter / (unknownRaceEthnicityWomanRepublicanCounter + unknownRaceEthnicityWomanDemocratCounter + unknownRaceEthnicityWomanNeutralCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter)
            unknownRaceEthnicityWomanPercentDemocrat = unknownRaceEthnicityWomanDemocratCounter / (unknownRaceEthnicityWomanRepublicanCounter + unknownRaceEthnicityWomanDemocratCounter + unknownRaceEthnicityWomanNeutralCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter)
            unknownRaceEthnicityWomanPercentNeutral = unknownRaceEthnicityWomanNeutralCounter / (unknownRaceEthnicityWomanRepublicanCounter + unknownRaceEthnicityWomanDemocratCounter + unknownRaceEthnicityWomanNeutralCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter)
            unknownRaceEthnicityWomanPercentUnknownPolitics = unknownRaceEthnicityWomanUnknownPoliticsCounter / (unknownRaceEthnicityWomanRepublicanCounter + unknownRaceEthnicityWomanDemocratCounter + unknownRaceEthnicityWomanNeutralCounter + unknownRaceEthnicityWomanUnknownPoliticsCounter)
        else:
            unknownRaceEthnicityWomanPercentRepublican = -1
            unknownRaceEthnicityWomanPercentDemocrat = -1
            unknownRaceEthnicityWomanPercentNeutral = -1
            unknownRaceEthnicityWomanPercentUnknownPolitics = -1

        if (unknownRaceEthnicityUnknownGenderRepublicanCounter + unknownRaceEthnicityUnknownGenderDemocratCounter + unknownRaceEthnicityUnknownGenderNeutralCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter) != 0:
            unknownRaceEthnicityUnknownGenderPercentRepublican = unknownRaceEthnicityUnknownGenderRepublicanCounter / (unknownRaceEthnicityUnknownGenderRepublicanCounter + unknownRaceEthnicityUnknownGenderDemocratCounter + unknownRaceEthnicityUnknownGenderNeutralCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter)
            unknownRaceEthnicityUnknownGenderPercentDemocrat = unknownRaceEthnicityUnknownGenderDemocratCounter / (unknownRaceEthnicityUnknownGenderRepublicanCounter + unknownRaceEthnicityUnknownGenderDemocratCounter + unknownRaceEthnicityUnknownGenderNeutralCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter)
            unknownRaceEthnicityUnknownGenderPercentNeutral = unknownRaceEthnicityUnknownGenderNeutralCounter / (unknownRaceEthnicityUnknownGenderRepublicanCounter + unknownRaceEthnicityUnknownGenderDemocratCounter + unknownRaceEthnicityUnknownGenderNeutralCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter)
            unknownRaceEthnicityUnknownGenderPercentUnknownPolitics = unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter / (unknownRaceEthnicityUnknownGenderRepublicanCounter + unknownRaceEthnicityUnknownGenderDemocratCounter + unknownRaceEthnicityUnknownGenderNeutralCounter + unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter)
        else:
            unknownRaceEthnicityUnknownGenderPercentRepublican = -1
            unknownRaceEthnicityUnknownGenderPercentDemocrat = -1
            unknownRaceEthnicityUnknownGenderPercentNeutral = -1
            unknownRaceEthnicityUnknownGenderPercentUnknownPolitics = -1


        # RACE/ETHNICITY + PARTY PERCENT
        if (whiteRepublicanCounter + whiteDemocratCounter + whiteNeutralCounter + whiteUnknownPoliticsCounter) != 0:
            whitePercentRepublican = whiteRepublicanCounter / (whiteRepublicanCounter + whiteDemocratCounter + whiteNeutralCounter + whiteUnknownPoliticsCounter)
            whitePercentDemocrat = whiteDemocratCounter / (whiteRepublicanCounter + whiteDemocratCounter + whiteNeutralCounter + whiteUnknownPoliticsCounter)
            whitePercentNeutral = whiteNeutralCounter / (whiteRepublicanCounter + whiteDemocratCounter + whiteNeutralCounter + whiteUnknownPoliticsCounter)
            whitePercentUnknownPolitics = whiteUnknownPoliticsCounter / (whiteRepublicanCounter + whiteDemocratCounter + whiteNeutralCounter + whiteUnknownPoliticsCounter)
        else:
            whitePercentRepublican = -1
            whitePercentDemocrat = -1
            whitePercentNeutral = -1
            whitePercentUnknownPolitics = -1

        if (hispanicRepublicanCounter + hispanicDemocratCounter + hispanicNeutralCounter + hispanicUnknownPoliticsCounter) != 0:
            hispanicPercentRepublican = hispanicRepublicanCounter / (hispanicRepublicanCounter + hispanicDemocratCounter + hispanicNeutralCounter + hispanicUnknownPoliticsCounter)
            hispanicPercentDemocrat = hispanicDemocratCounter / (hispanicRepublicanCounter + hispanicDemocratCounter + hispanicNeutralCounter + hispanicUnknownPoliticsCounter)
            hispanicPercentNeutral = hispanicNeutralCounter / (hispanicRepublicanCounter + hispanicDemocratCounter + hispanicNeutralCounter + hispanicUnknownPoliticsCounter)
            hispanicPercentUnknownPolitics = hispanicUnknownPoliticsCounter / (hispanicRepublicanCounter + hispanicDemocratCounter + hispanicNeutralCounter + hispanicUnknownPoliticsCounter)
        else:
            hispanicPercentRepublican = -1
            hispanicPercentDemocrat = -1
            hispanicPercentNeutral = -1
            hispanicPercentUnknownPolitics = -1

        if (apiRepublicanCounter + apiDemocratCounter + apiNeutralCounter + apiUnknownPoliticsCounter) != 0:
            apiPercentRepublican = apiRepublicanCounter / (apiRepublicanCounter + apiDemocratCounter + apiNeutralCounter + apiUnknownPoliticsCounter)
            apiPercentDemocrat = apiDemocratCounter / (apiRepublicanCounter + apiDemocratCounter + apiNeutralCounter + apiUnknownPoliticsCounter)
            apiPercentNeutral = apiNeutralCounter / (apiRepublicanCounter + apiDemocratCounter + apiNeutralCounter + apiUnknownPoliticsCounter)
            apiPercentUnknownPolitics = apiUnknownPoliticsCounter / (apiRepublicanCounter + apiDemocratCounter + apiNeutralCounter + apiUnknownPoliticsCounter)
        else:
            apiPercentRepublican = -1
            apiPercentDemocrat = -1
            apiPercentNeutral = -1
            apiPercentUnknownPolitics = -1

        if (blackRepublicanCounter + blackDemocratCounter + blackNeutralCounter + blackUnknownPoliticsCounter) != 0:
            blackPercentRepublican = blackRepublicanCounter / (blackRepublicanCounter + blackDemocratCounter + blackNeutralCounter + blackUnknownPoliticsCounter)
            blackPercentDemocrat = blackDemocratCounter / (blackRepublicanCounter + blackDemocratCounter + blackNeutralCounter + blackUnknownPoliticsCounter)
            blackPercentNeutral = blackNeutralCounter / (blackRepublicanCounter + blackDemocratCounter + blackNeutralCounter + blackUnknownPoliticsCounter)
            blackPercentUnknownPolitics = blackUnknownPoliticsCounter / (blackRepublicanCounter + blackDemocratCounter + blackNeutralCounter + blackUnknownPoliticsCounter)
        else:
            blackPercentRepublican = -1
            blackPercentDemocrat = -1
            blackPercentNeutral = -1
            blackPercentUnknownPolitics = -1

        if (aianRepublicanCounter + aianDemocratCounter + aianNeutralCounter + aianUnknownPoliticsCounter) != 0:
            aianPercentRepublican = aianRepublicanCounter / (aianRepublicanCounter + aianDemocratCounter + aianNeutralCounter + aianUnknownPoliticsCounter)
            aianPercentDemocrat = aianDemocratCounter / (aianRepublicanCounter + aianDemocratCounter + aianNeutralCounter + aianUnknownPoliticsCounter)
            aianPercentNeutral = aianNeutralCounter / (aianRepublicanCounter + aianDemocratCounter + aianNeutralCounter + aianUnknownPoliticsCounter)
            aianPercentUnknownPolitics = aianUnknownPoliticsCounter / (aianRepublicanCounter + aianDemocratCounter + aianNeutralCounter + aianUnknownPoliticsCounter)
        else:
            aianPercentRepublican = -1
            aianPercentDemocrat = -1
            aianPercentNeutral = -1
            aianPercentUnknownPolitics = -1

        if (unknownRaceEthnicityRepublicanCounter + unknownRaceEthnicityDemocratCounter + unknownRaceEthnicityNeutralCounter + unknownRaceEthnicityUnknownPoliticsCounter) != 0:
            unknownRaceEthnicityPercentRepublican = unknownRaceEthnicityRepublicanCounter / (unknownRaceEthnicityRepublicanCounter + unknownRaceEthnicityDemocratCounter + unknownRaceEthnicityNeutralCounter + unknownRaceEthnicityUnknownPoliticsCounter)
            unknownRaceEthnicityPercentDemocrat = unknownRaceEthnicityDemocratCounter / (unknownRaceEthnicityRepublicanCounter + unknownRaceEthnicityDemocratCounter + unknownRaceEthnicityNeutralCounter + unknownRaceEthnicityUnknownPoliticsCounter)
            unknownRaceEthnicityPercentNeutral = unknownRaceEthnicityNeutralCounter / (unknownRaceEthnicityRepublicanCounter + unknownRaceEthnicityDemocratCounter + unknownRaceEthnicityNeutralCounter + unknownRaceEthnicityUnknownPoliticsCounter)
            unknownRaceEthnicityPercentUnknownPolitics = unknownRaceEthnicityUnknownPoliticsCounter / (unknownRaceEthnicityRepublicanCounter + unknownRaceEthnicityDemocratCounter + unknownRaceEthnicityNeutralCounter + unknownRaceEthnicityUnknownPoliticsCounter)

        else:
            unknownRaceEthnicityPercentRepublican = -1
            unknownRaceEthnicityPercentDemocrat = -1
            unknownRaceEthnicityPercentNeutral = -1
            unknownRaceEthnicityPercentUnknownPolitics = -1

        # GENDER + PARTY PERCENT
        if (manRepublicanCounter + womanRepublicanCounter + unknownGenderRepublicanCounter) != 0:
            manPercentRepublican = manRepublicanCounter / (manRepublicanCounter + womanRepublicanCounter + unknownGenderRepublicanCounter)
            womanPercentRepublican = womanRepublicanCounter / (manRepublicanCounter + womanRepublicanCounter + unknownGenderRepublicanCounter)
            unknownGenderRepublicanCounter = unknownGenderRepublicanCounter / (manRepublicanCounter + womanRepublicanCounter + unknownGenderRepublicanCounter)
        else:
            manPercentRepublican = -1
            womanPercentRepublican = -1
            unknownGenderRepublicanCounter = -1

        if (manDemocratCounter + womanDemocratCounter + unknownGenderDemocratCounter) != 0:
            manPercentDemocrat = manDemocratCounter / (manDemocratCounter + womanDemocratCounter + unknownGenderDemocratCounter)
            womanPercentDemocrat = womanDemocratCounter / (manDemocratCounter + womanDemocratCounter + unknownGenderDemocratCounter)
            unknownGenderDemocratCounter = unknownGenderDemocratCounter / (manDemocratCounter + womanDemocratCounter + unknownGenderDemocratCounter)
        else:
            manPercentDemocrat = -1
            womanPercentDemocrat = -1
            unknownGenderDemocratCounter = -1

        if (manNeutralCounter + womanNeutralCounter + unknownGenderNeutralCounter) != 0:
            manPercentNeutral = manNeutralCounter / (manNeutralCounter + womanNeutralCounter + unknownGenderNeutralCounter)
            womanPercentNeutral = womanNeutralCounter / (manNeutralCounter + womanNeutralCounter + unknownGenderNeutralCounter)
            unknownGenderNeutralCounter = unknownGenderNeutralCounter / (manNeutralCounter + womanNeutralCounter + unknownGenderNeutralCounter)
        else:
            manPercentNeutral = -1
            womanPercentNeutral = -1
            unknownGenderNeutralCounter = -1

        if (manUnknownPoliticsCounter + womanUnknownPoliticsCounter + unknownGenderUnknownPoliticsCounter) != 0:
            manPercentUnknownPolitics = manUnknownPoliticsCounter / (manUnknownPoliticsCounter + womanUnknownPoliticsCounter + unknownGenderUnknownPoliticsCounter)
            womanPercentUnknownPolitics = womanUnknownPoliticsCounter / (manUnknownPoliticsCounter + womanUnknownPoliticsCounter + unknownGenderUnknownPoliticsCounter)
            unknownGenderUnknownPoliticsCounter = unknownGenderUnknownPoliticsCounter / (manUnknownPoliticsCounter + womanUnknownPoliticsCounter + unknownGenderUnknownPoliticsCounter)
        else:
            manPercentUnknownPolitics = -1
            womanPercentUnknownPolitics = -1
            unknownGenderUnknownPoliticsCounter = -1

        # PARTY
        if (republicanCounter + democratCounter + neutralCounter + unknownPoliticsCounter) != 0:
            percentRepublican = republicanCounter / (republicanCounter + democratCounter + neutralCounter + unknownPoliticsCounter)
            percentDemocrat = democratCounter / (republicanCounter + democratCounter + neutralCounter + unknownPoliticsCounter)
            percentNeutral = neutralCounter / (republicanCounter + democratCounter + neutralCounter + unknownPoliticsCounter)
            percentUnknownPolitics = unknownPoliticsCounter / (republicanCounter + democratCounter + neutralCounter + unknownPoliticsCounter)
        else:
            percentRepublican = -1
            percentDemocrat = -1
            percentNeutral = -1
            percentUnknownPolitics = -1


        resultDict = {'state_full':state_full,
                      'state_short':state_short,
                      'percentRepublican':percentRepublican,
                      'percentDemocrat':percentDemocrat,
                      'percentNeutral':percentNeutral,
                      'percentUnknownPolitics':percentUnknownPolitics,
                      'manPercentRepublican':manPercentRepublican,
                      'womanPercentRepublican':womanPercentRepublican,
                      'unknownGenderRepublicanCounter':unknownGenderRepublicanCounter,
                      'manPercentDemocrat':manPercentDemocrat,
                      'womanPercentDemocrat':womanPercentDemocrat,
                      'unknownGenderNeutralCounter':unknownGenderNeutralCounter,
                      'manPercentUnknownPolitics':manPercentUnknownPolitics,
                      'womanPercentUnknownPolitics':womanPercentUnknownPolitics,
                      'unknownGenderUnknownPoliticsCounter':unknownGenderUnknownPoliticsCounter,
                      'whitePercentRepublican':whitePercentRepublican,
                      'whitePercentDemocrat':whitePercentDemocrat,
                      'whitePercentNeutral':whitePercentNeutral,
                      'whitePercentUnknownPolitics':whitePercentUnknownPolitics,
                      'hispanicPercentRepublican':hispanicPercentRepublican,
                      'hispanicPercentDemocrat':hispanicPercentDemocrat,
                      'hispanicPercentNeutral':hispanicPercentNeutral,
                      'hispanicPercentUnknownPolitics':hispanicPercentUnknownPolitics,
                      'apiPercentRepublican':apiPercentRepublican,
                      'apiPercentDemocrat':apiPercentDemocrat,
                      'apiPercentNeutral':apiPercentNeutral,
                      'apiPercentUnknownPolitics':apiPercentUnknownPolitics,
                      'blackPercentRepublican':blackPercentRepublican,
                      'blackPercentDemocrat':blackPercentDemocrat,
                      'blackPercentNeutral':blackPercentNeutral,
                      'blackPercentUnknownPolitics':blackPercentUnknownPolitics,
                      'aianPercentRepublican':aianPercentRepublican,
                      'aianPercentDemocrat':aianPercentDemocrat,
                      'aianPercentNeutral':aianPercentNeutral,
                      'aianPercentUnknownPolitics':aianPercentUnknownPolitics,
                      'unknownRaceEthnicityPercentRepublican':unknownRaceEthnicityPercentRepublican,
                      'unknownRaceEthnicityPercentDemocrat':unknownRaceEthnicityPercentDemocrat,
                      'unknownRaceEthnicityPercentNeutral':unknownRaceEthnicityPercentNeutral,
                      'unknownRaceEthnicityPercentUnknownPolitics':unknownRaceEthnicityPercentUnknownPolitics,
                      'whiteManPercentRepublican':whiteManPercentRepublican,
                      'whiteManPercentDemocrat':whiteManPercentDemocrat,
                      'whiteManPercentNeutral':whiteManPercentNeutral,
                      'whiteManPercentUnknownPolitics':whiteManPercentUnknownPolitics,
                      'whiteWomanPercentRepublican':whiteWomanPercentRepublican,
                      'whiteWomanPercentDemocrat':whiteWomanPercentDemocrat,
                      'whiteWomanPercentNeutral':whiteWomanPercentNeutral,
                      'whiteWomanPercentUnknownPolitics':whiteWomanPercentUnknownPolitics,
                      'whiteUnknownGenderPercentRepublican':whiteUnknownGenderPercentRepublican,
                      'whiteUnknownGenderPercentDemocrat':whiteUnknownGenderPercentDemocrat,
                      'whiteUnknownGenderPercentNeutral':whiteUnknownGenderPercentNeutral,
                      'whiteUnknownGenderPercentUnknownPolitics':whiteUnknownGenderPercentUnknownPolitics,
                      'hispanicManPercentRepublican':hispanicManPercentRepublican,
                      'hispanicManPercentDemocrat':hispanicManPercentDemocrat,
                      'hispanicManPercentNeutral':hispanicManPercentNeutral,
                      'hispanicManPercentUnknownPolitics':hispanicManPercentUnknownPolitics,
                      'hispanicWomanPercentRepublican':hispanicWomanPercentRepublican,
                      'hispanicWomanPercentDemocrat':hispanicWomanPercentDemocrat,
                      'hispanicWomanPercentDemocrat':hispanicWomanPercentDemocrat,
                      'hispanicWomanPercentNeutral':hispanicWomanPercentNeutral,
                      'hispanicUnknownGenderPercentRepublican':hispanicUnknownGenderPercentRepublican,
                      'hispanicUnknownGenderPercentDemocrat':hispanicUnknownGenderPercentDemocrat,
                      'hispanicUnknownGenderPercentDemocrat':hispanicUnknownGenderPercentDemocrat,
                      'hispanicUnknownGenderPercentNeutral':hispanicUnknownGenderPercentNeutral,
                      'apiManPercentRepublican':apiManPercentRepublican,
                      'apiManPercentDemocrat':apiManPercentDemocrat,
                      'apiManPercentNeutral':apiManPercentNeutral,
                      'apiManPercentUnknownPolitics':apiManPercentUnknownPolitics,
                      'apiWomanPercentRepublican':apiWomanPercentRepublican,
                      'apiWomanPercentDemocrat':apiWomanPercentDemocrat,
                      'apiWomanPercentNeutral':apiWomanPercentNeutral,
                      'apiWomanPercentUnknownPolitics':apiWomanPercentUnknownPolitics,
                      'apiUnknownGenderPercentRepublican':apiUnknownGenderPercentRepublican,
                      'apiUnknownGenderPercentDemocrat':apiUnknownGenderPercentDemocrat,
                      'apiUnknownGenderPercentNeutral':apiUnknownGenderPercentNeutral,
                      'apiUnknownGenderPercentUnknownPolitics':apiUnknownGenderPercentUnknownPolitics,
                      'blackManPercentRepublican':blackManPercentRepublican,
                      'blackManPercentDemocrat':blackManPercentDemocrat,
                      'blackManPercentNeutral':blackManPercentNeutral,
                      'blackManPercentUnknownPolitics':blackManPercentUnknownPolitics,
                      'blackWomanPercentRepublican':blackWomanPercentRepublican,
                      'blackWomanPercentDemocrat':blackWomanPercentDemocrat,
                      'blackWomanPercentNeutral':blackWomanPercentNeutral,
                      'blackWomanPercentUnknownPolitics':blackWomanPercentUnknownPolitics,
                      'blackUnknownGenderPercentRepublican':blackUnknownGenderPercentRepublican,
                      'blackUnknownGenderPercentDemocrat':blackUnknownGenderPercentDemocrat,
                      'blackUnknownGenderPercentNeutral':blackUnknownGenderPercentNeutral,
                      'blackUnknownGenderPercentUnknownPolitics':blackUnknownGenderPercentUnknownPolitics,
                      'aianManPercentRepublican':aianManPercentRepublican,
                      'aianManPercentDemocrat':aianManPercentDemocrat,
                      'aianManPercentNeutral':aianManPercentNeutral,
                      'aianManPercentUnknownPolitics':aianManPercentUnknownPolitics,
                      'aianWomanPercentRepublican':aianWomanPercentRepublican,
                      'aianWomanPercentDemocrat':aianWomanPercentDemocrat,
                      'aianWomanPercentNeutral':aianWomanPercentNeutral,
                      'aianWomanPercentUnknownPolitics':aianWomanPercentUnknownPolitics,
                      'aianUnknownGenderPercentRepublican':aianUnknownGenderPercentRepublican,
                      'aianUnknownGenderPercentDemocrat':aianUnknownGenderPercentDemocrat,
                      'aianUnknownGenderPercentNeutral':aianUnknownGenderPercentNeutral,
                      'aianUnknownGenderPercentUnknownPolitics':aianUnknownGenderPercentUnknownPolitics,
                      'unknownRaceEthnicityManPercentRepublican':unknownRaceEthnicityManPercentRepublican,
                      'unknownRaceEthnicityManPercentDemocrat':unknownRaceEthnicityManPercentDemocrat,
                      'unknownRaceEthnicityManPercentNeutral':unknownRaceEthnicityManPercentNeutral,
                      'unknownRaceEthnicityManPercentUnknownPolitics':unknownRaceEthnicityManPercentUnknownPolitics,
                      'unknownRaceEthnicityWomanPercentRepublican':unknownRaceEthnicityWomanPercentRepublican,
                      'unknownRaceEthnicityWomanPercentDemocrat':unknownRaceEthnicityWomanPercentDemocrat,
                      'unknownRaceEthnicityWomanPercentNeutral':unknownRaceEthnicityWomanPercentNeutral,
                      'unknownRaceEthnicityWomanPercentNeutral':unknownRaceEthnicityWomanPercentNeutral,
                      'unknownRaceEthnicityWomanPercentUnknownPolitics':unknownRaceEthnicityWomanPercentUnknownPolitics,
                      'unknownRaceEthnicityUnknownGenderPercentRepublican':unknownRaceEthnicityUnknownGenderPercentRepublican,
                      'unknownRaceEthnicityUnknownGenderPercentDemocrat':unknownRaceEthnicityUnknownGenderPercentDemocrat,
                      'unknownRaceEthnicityUnknownGenderPercentNeutral':unknownRaceEthnicityUnknownGenderPercentNeutral,
                      'unknownRaceEthnicityUnknownGenderPercentNeutral':unknownRaceEthnicityUnknownGenderPercentNeutral,
                      'unknownRaceEthnicityUnknownGenderPercentUnknownPolitics':unknownRaceEthnicityUnknownGenderPercentUnknownPolitics,
                      'totalCounter':totalCounter,
                      'republicanCounter':republicanCounter,
                      'democratCounter':democratCounter,
                      'neutralCounter':neutralCounter,
                      'unknownPoliticsCounter':unknownPoliticsCounter,
                      'manRepublicanCounter':manRepublicanCounter,
                      'manDemocratCounter':manDemocratCounter,
                      'manUnknownCounter':manUnknownCounter,
                      'manNeutralCounter':manNeutralCounter,
                      'womanRepublicanCounter':womanRepublicanCounter,
                      'womanDemocratCounter':womanDemocratCounter,
                      'womanUnknownPoliticsCounter':womanUnknownPoliticsCounter,
                      'womanNeutralCounter':womanNeutralCounter,
                      'unknownGenderRepublicanCounter':unknownGenderRepublicanCounter,
                      'unknownGenderDemocratCounter':unknownGenderDemocratCounter,
                      'unknownGenderUnknownPoliticsCounter':unknownGenderUnknownPoliticsCounter,
                      'unknownGenderNeutralCounter':unknownGenderNeutralCounter,
                      'whiteRepublicanCounter':whiteRepublicanCounter,
                      'whiteDemocratCounter':whiteDemocratCounter,
                      'whiteUnknownPoliticsCounter':whiteUnknownPoliticsCounter,
                      'whiteNeutralCounter':whiteNeutralCounter,
                      'hispanicRepublicanCounter':hispanicRepublicanCounter,
                      'hispanicDemocratCounter':hispanicDemocratCounter,
                      'hispanicUnknownPoliticsCounter':hispanicUnknownPoliticsCounter,
                      'hispanicNeutralCounter':hispanicNeutralCounter,
                      'apiRepublicanCounter':apiRepublicanCounter,
                      'apiDemocratCounter':apiDemocratCounter,
                      'apiUnknownPoliticsCounter':apiUnknownPoliticsCounter,
                      'apiNeutralCounter':apiNeutralCounter,
                      'blackRepublicanCounter':blackRepublicanCounter,
                      'blackDemocratCounter':blackDemocratCounter,
                      'blackUnknownPoliticsCounter':blackUnknownPoliticsCounter,
                      'blackNeutralCounter':blackNeutralCounter,
                      'aianRepublicanCounter':aianRepublicanCounter,
                      'aianDemocratCounter':aianDemocratCounter,
                      'aianUnknownPoliticsCounter':aianUnknownPoliticsCounter,
                      'aianNeutralCounter':aianNeutralCounter,
                      'unknownRaceEthnicityRepublicanCounter':unknownRaceEthnicityRepublicanCounter,
                      'unknownRaceEthnicityDemocratCounter':unknownRaceEthnicityDemocratCounter,
                      'unknownRaceEthnicityUnknownPoliticsCounter':unknownRaceEthnicityUnknownPoliticsCounter,
                      'unknownRaceEthnicityNeutralCounter':unknownRaceEthnicityNeutralCounter,
                      'whiteManRepublicanCounter':whiteManRepublicanCounter,
                      'whiteManDemocratCounter':whiteManDemocratCounter,
                      'whiteManUnknownPoliticsCounter':whiteManUnknownPoliticsCounter,
                      'whiteManNeutralCounter':whiteManNeutralCounter,
                      'whiteWomanRepublicanCounter':whiteWomanRepublicanCounter,
                      'whiteWomanDemocratCounter':whiteWomanDemocratCounter,
                      'whiteWomanUnknownPoliticsCounter':whiteWomanUnknownPoliticsCounter,
                      'whiteWomanNeutralCounter':whiteWomanNeutralCounter,
                      'hispanicManRepublicanCounter':hispanicManRepublicanCounter,
                      'hispanicManDemocratCounter':hispanicManDemocratCounter,
                      'hispanicManUnknownPoliticsCounter':hispanicManUnknownPoliticsCounter,
                      'hispanicManNeutralCounter':hispanicManNeutralCounter,
                      'hispanicWomanRepublicanCounter':hispanicWomanRepublicanCounter,
                      'hispanicWomanDemocratCounter':hispanicWomanDemocratCounter,
                      'hispanicWomanUnknownPoliticsCounter':hispanicWomanUnknownPoliticsCounter,
                      'hispanicWomanNeutralCounter':hispanicWomanNeutralCounter,
                      'apiManRepublicanCounter':apiManRepublicanCounter,
                      'apiManDemocratCounter':apiManDemocratCounter,
                      'apiManUnknownPoliticsCounter':apiManUnknownPoliticsCounter,
                      'apiManNeutralCounter':apiManNeutralCounter,
                      'apiWomanRepublicanCounter':apiWomanRepublicanCounter,
                      'apiWomanDemocratCounter':apiWomanDemocratCounter,
                      'apiWomanUnknownPoliticsCounter':apiWomanUnknownPoliticsCounter,
                      'apiWomanNeutralCounter':apiWomanNeutralCounter,
                      'blackManRepublicanCounter':blackManRepublicanCounter,
                      'blackManDemocratCounter':blackManDemocratCounter,
                      'blackManUnknownPoliticsCounter':blackManUnknownPoliticsCounter,
                      'blackManNeutralCounter':blackManNeutralCounter,
                      'blackWomanRepublicanCounter':blackWomanRepublicanCounter,
                      'blackWomanDemocratCounter':blackWomanDemocratCounter,
                      'blackWomanUnknownPoliticsCounter':blackWomanUnknownPoliticsCounter,
                      'blackWomanNeutralCounter':blackWomanNeutralCounter,
                      'aianManRepublicanCounter':aianManRepublicanCounter,
                      'aianManDemocratCounter':aianManDemocratCounter,
                      'aianManUnknownPoliticsCounter':aianManUnknownPoliticsCounter,
                      'aianManNeutralCounter':aianManNeutralCounter,
                      'aianWomanRepublicanCounter':aianWomanRepublicanCounter,
                      'aianWomanDemocratCounter':aianWomanDemocratCounter,
                      'aianWomanUnknownPoliticsCounter':aianWomanUnknownPoliticsCounter,
                      'aianWomanNeutralCounter':aianWomanNeutralCounter,
                      'whiteUnknownGenderRepublicanCounter':whiteUnknownGenderRepublicanCounter,
                      'whiteUnknownGenderDemocratCounter':whiteUnknownGenderDemocratCounter,
                      'whiteUnknownGenderUnknownPoliticsCounter':whiteUnknownGenderUnknownPoliticsCounter,
                      'whiteUnknownGenderNeutralCounter':whiteUnknownGenderNeutralCounter,
                      'hispanicUnknownGenderRepublicanCounter':hispanicUnknownGenderRepublicanCounter,
                      'hispanicUnknownGenderDemocratCounter':hispanicUnknownGenderDemocratCounter,
                      'hispanicUnknownGenderUnknownPoliticsCounter':hispanicUnknownGenderUnknownPoliticsCounter,
                      'hispanicUnknownGenderNeutralCounter':hispanicUnknownGenderNeutralCounter,
                      'apiUnknownGenderRepublicanCounter':apiUnknownGenderRepublicanCounter,
                      'apiUnknownGenderDemocratCounter':apiUnknownGenderDemocratCounter,
                      'apiUnknownGenderUnknownPoliticsCounter':apiUnknownGenderUnknownPoliticsCounter,
                      'apiUnknownGenderNeutralCounter':apiUnknownGenderNeutralCounter,
                      'blackUnknownGenderRepublicanCounter':blackUnknownGenderRepublicanCounter,
                      'blackUnknownGenderDemocratCounter':blackUnknownGenderDemocratCounter,
                      'blackUnknownGenderUnknownPoliticsCounter':blackUnknownGenderUnknownPoliticsCounter,
                      'blackUnknownGenderNeutralCounter':blackUnknownGenderNeutralCounter,
                      'aianUnknownGenderRepublicanCounter':aianUnknownGenderRepublicanCounter,
                      'aianUnknownGenderDemocratCounter':aianUnknownGenderDemocratCounter,
                      'aianUnknownGenderUnknownPoliticsCounter':aianUnknownGenderUnknownPoliticsCounter,
                      'aianUnknownGenderNeutralCounter':aianUnknownGenderNeutralCounter,
                      'unknownRaceEthnicityUnknownGenderRepublicanCounter':unknownRaceEthnicityUnknownGenderRepublicanCounter,
                      'unknownRaceEthnicityUnknownGenderDemocratCounter':unknownRaceEthnicityUnknownGenderDemocratCounter,
                      'unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter':unknownRaceEthnicityUnknownGenderUnknownPoliticsCounter,
                      'unknownRaceEthnicityUnknownGenderNeutralCounter':unknownRaceEthnicityUnknownGenderNeutralCounter,
                      'unknownRaceEthnicityManRepublicanCounter':unknownRaceEthnicityManRepublicanCounter,
                      'unknownRaceEthnicityManDemocratCounter':unknownRaceEthnicityManDemocratCounter,
                      'unknownRaceEthnicityManUnknownPoliticsCounter':unknownRaceEthnicityManUnknownPoliticsCounter,
                      'unknownRaceEthnicityManNeutralCounter':unknownRaceEthnicityManNeutralCounter,
                      'unknownRaceEthnicityWomanRepublicanCounter':unknownRaceEthnicityWomanRepublicanCounter,
                      'unknownRaceEthnicityWomanDemocratCounter':unknownRaceEthnicityWomanDemocratCounter,
                      'unknownRaceEthnicityWomanUnknownPoliticsCounter':unknownRaceEthnicityWomanUnknownPoliticsCounter,
                      'unknownRaceEthnicityWomanNeutralCounter':unknownRaceEthnicityWomanNeutralCounter}



        result = result.append(resultDict,ignore_index=True)
        result.to_csv(savedir+state_full+"_data_websiteFormat.csv")


    result.to_csv(savedir+electionYear+"format.csv")





if __name__ == '__main__':
    main()
