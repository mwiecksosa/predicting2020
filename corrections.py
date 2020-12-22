import pandas as pd
import numpy as np

rootPath = "/home/mwiecksosa/predicting2020/"
dataPath = rootPath+"data/"


def main():

    filePath2016ExitPolls = dataPath+"2016_tweets_8e8cca7c/2016_stateExitPolls/"

    df2016exitPolls = pd.read_csv(filePath2016ExitPolls+"2016stateExitPolls.csv")
    df2016exitPolls.columns = [str(col) + '_2016exitPoll' for col in df2016exitPolls.columns]

    filePath2016WebsiteFormat = "/home/mwiecksosa/predicting2020/data/2016_tweets_8e8cca7c/2016_raceGender_politicalPreference/2016_results_41263a90/"
    df2016websiteFormat = pd.read_csv(filePath2016WebsiteFormat+"2016format.csv")
    df2016websiteFormat.columns = [str(col) + '_2016twitter' for col in df2016websiteFormat.columns]

    dfMerged2016 = pd.merge(left=df2016exitPolls, right=df2016websiteFormat, left_on='state_2016exitPoll', right_on='state_full_2016twitter')





    filePath2020ExitPolls = dataPath+"2020_tweets_d35fd9fd/2020_stateExitPolls/"
    df2020exitPolls = pd.read_csv(filePath2020ExitPolls+"2020_stateExitPolls.csv")
    df2020exitPolls.columns = [str(col) + '_2020exitPoll' for col in df2020exitPolls.columns]


    filePath2020WebsiteFormat = "/home/mwiecksosa/predicting2020/data/2020_tweets_d35fd9fd/2020_raceGender_politicalPreference/2020_results_16f22f4a/"
    df2020websiteFormat = pd.read_csv(filePath2020WebsiteFormat+"2020format.csv")
    df2020websiteFormat.columns = [str(col) + '_2020twitter' for col in df2020websiteFormat.columns]

    dfMerged2020 = pd.merge(left=df2020exitPolls, right=df2020websiteFormat, left_on='state_2020exitPoll', right_on='state_full_2020twitter')


    dfMerged = pd.merge(left=dfMerged2016,right=dfMerged2020,left_on='state_2016exitPoll',right_on='state_2020exitPoll')
    dfMerged.to_csv(dataPath+"corrections/"+"dfMerged.csv")


    # DF of predicted voter shares

    resultsDF = []
    # gender
    # men

    resultsDF.append(getMenPredictions(dfMerged))
    # women
    resultsDF.append(getWomenPredictions(dfMerged))

    # race/ethnicity
    # white
    resultsDF.append(getWhitePredictions(dfMerged))


    # black
    resultsDF.append(getBlackPredictions(dfMerged))
    # hispanic/latino
    resultsDF.append(getHispanicPredictions(dfMerged))
    # asian
    resultsDF.append(getAsianPredictions(dfMerged))
    # other - no polled "other" demographic group and no idea what group this is
    #getOtherRaceEthnicityPredictions(dfMerged)
    # voters of color - can't do this
    # because I don't know the percent of polled people for voters of color
    # in each state so no idea how to combine the different tweeters of color
    #getPOColorPredictions(dfMerged)

    # gender and race/ethnicity
    # white men
    resultsDF.append(getWhiteMenPredictions(dfMerged))
    # white women
    resultsDF.append(getWhiteWomenPredictions(dfMerged))
    # black men - can't do this because no tweets / exit poll data for black men
    resultsDF.append(getblackMenPredictions(dfMerged))
    # black women
    resultsDF.append(getblackWomenPredictions(dfMerged))
    # hispanic/latino men
    resultsDF.append(gethispanicMenPredictions(dfMerged))
    # hispanic/latino women
    resultsDF.append(gethispanicWomenPredictions(dfMerged))
    # asian men
    #resultsDF.append(getasianMenPredictions(dfMerged))
    # asian women
    #resultsDF.append(getasianWomenPredictions(dfMerged))
    # american indian alaska native - can't do this
    # other - can't do this
    # voters of color men - can't do this
    # voters of color women - can't do this



    resultsDF = pd.DataFrame(resultsDF,columns=['demographicGroup',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'absoluteErrorDemNational',
                                      'meanDemAbsoluteErrorAllStates',
                                      'percentRepubNationalPredicted',
                                      'percentRepubNationalActual',
                                      'absoluteErrorRepubNational',
                                      'meanRepubAbsoluteErrorAllStates'])


    resultsDF.to_csv(dataPath+"corrections/"+'resultsDF.csv')



def getasianWomenPredictions(dfMerged):

    dfasianWomen = dfMerged[(dfMerged['asianWomenPercentDem_2016exitPoll'] != -1) & \
                            (dfMerged['asianWomenPercentDem_2020exitPoll'] != -1) & \
                            (dfMerged['asianWomenPercentRepub_2016exitPoll'] != -1) & \
                            (dfMerged['asianWomenPercentRepub_2020exitPoll'] != -1) & \
                            (dfMerged['apiWomanPercentDemocrat_2016twitter'] != 0) & \
                            (dfMerged['apiWomanPercentRepublican_2016twitter'] != 0) & \
                            (dfMerged['apiWomanPercentDemocrat_2020twitter'] != 0) & \
                            (dfMerged['apiWomanPercentRepublican_2020twitter'] != 0) & \
                            (dfMerged['apiWomanPercentDemocrat_2016twitter'] != -1) & \
                            (dfMerged['apiWomanPercentRepublican_2016twitter'] != -1) & \
                            (dfMerged['apiWomanPercentDemocrat_2020twitter'] != -1) & \
                            (dfMerged['apiWomanPercentRepublican_2020twitter'] != -1)]

    dfasianWomen['scaleasianWomenDem'] = dfasianWomen.apply(lambda row: row['asianWomenPercentDem_2016exitPoll']/row["apiWomanPercentDemocrat_2016twitter"],axis=1)
    dfasianWomen['scaleasianWomenRep'] = dfasianWomen.apply(lambda row: row['asianWomenPercentRepub_2016exitPoll']/row["apiWomanPercentRepublican_2016twitter"],axis=1)

    dfasianWomen['asianWomenPercentDem_2020predicted'] = dfasianWomen.apply(lambda row: row["apiWomanPercentDemocrat_2020twitter"] * (row['asianWomenPercentDem_2016exitPoll']/row["apiWomanPercentDemocrat_2016twitter"]),axis=1)
    dfasianWomen['asianWomenPercentRepub_2020predicted'] = dfasianWomen.apply(lambda row: row["apiWomanPercentRepublican_2020twitter"] * (row['asianWomenPercentRepub_2016exitPoll']/row["apiWomanPercentRepublican_2016twitter"]),axis=1)

    dfasianWomen['asianWomenPercentDem_2020predicted'].values[dfasianWomen['asianWomenPercentDem_2020predicted'].values > 100] = 100
    dfasianWomen['asianWomenPercentDem_2020predicted'].values[dfasianWomen['asianWomenPercentDem_2020predicted'].values < 0] = 0
    dfasianWomen['asianWomenPercentRepub_2020predicted'].values[dfasianWomen['asianWomenPercentRepub_2020predicted'].values > 100] = 100
    dfasianWomen['asianWomenPercentRepub_2020predicted'].values[dfasianWomen['asianWomenPercentRepub_2020predicted'].values < 0] = 0

    dfasianWomen['asianWomenPercentDem_2020actual'] = dfasianWomen['asianWomenPercentDem_2020exitPoll']
    dfasianWomen['asianWomenPercentRepub_2020actual'] = dfasianWomen['asianWomenPercentRepub_2020exitPoll']

    dfasianWomen['asianWomenPercentDem_absError'] = abs(dfasianWomen['asianWomenPercentDem_2020predicted'] - dfasianWomen['asianWomenPercentDem_2020actual'])
    dfasianWomen['asianWomenPercentRepub_absError'] = abs(dfasianWomen['asianWomenPercentRepub_2020predicted'] - dfasianWomen['asianWomenPercentRepub_2020actual'])

    dfasianWomen['asianWomenPercentDem_meanAbsError'] = dfasianWomen['asianWomenPercentDem_absError'].mean()
    dfasianWomen['asianWomenPercentRepub_meanAbsError'] = dfasianWomen['asianWomenPercentRepub_absError'].mean()

    dfasianWomen['asianWomenPercentDem_meanStatesPredictedVoterShare'] = dfasianWomen['asianWomenPercentDem_2020predicted'].mean()
    dfasianWomen['asianWomenPercentRepub_meanStatesPredictedVoterShare'] = dfasianWomen['asianWomenPercentRepub_2020predicted'].mean()

    dfasianWomen['asianWomenPercentDem_meanStatesActualVoterShare'] = dfasianWomen['asianWomenPercentDem_2020actual'].mean()
    dfasianWomen['asianWomenPercentRepub_meanStatesActualVoterShare'] = dfasianWomen['asianWomenPercentRepub_2020actual'].mean()

    dfasianWomen.to_csv(dataPath+"corrections/"+'dfasianWomen.csv')

    return ['asianWomen',
            dfasianWomen.loc[0].at['asianWomenPercentDem_2020predicted'],
            dfasianWomen.loc[0].at['asianWomenPercentDem_2020actual'],
            dfasianWomen['asianWomenPercentDem_absError'].mean(),
            dfasianWomen.loc[0].at['asianWomenPercentRepub_2020predicted'],
            dfasianWomen.loc[0].at['asianWomenPercentRepub_2020actual'],
            dfasianWomen['asianWomenPercentRepub_absError'].mean()]




def getasianMenPredictions(dfMerged):

    dfasianMen = dfMerged[(dfMerged['asianMenPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['asianMenPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['asianMenPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['asianMenPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['apiManPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['apiManPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['apiManPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['apiManPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['apiManPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['apiManPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['apiManPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['apiManPercentRepublican_2020twitter'] != -1)]

    dfasianMen['scaleasianMenDem'] = dfasianMen.apply(lambda row: row['asianMenPercentDem_2016exitPoll']/row["apiManPercentDemocrat_2016twitter"],axis=1)
    dfasianMen['scaleasianMenRep'] = dfasianMen.apply(lambda row: row['asianMenPercentRepub_2016exitPoll']/row["apiManPercentRepublican_2016twitter"],axis=1)

    dfasianMen['asianMenPercentDem_2020predicted'] = dfasianMen.apply(lambda row: row["apiManPercentDemocrat_2020twitter"] * (row['asianMenPercentDem_2016exitPoll']/row["apiManPercentDemocrat_2016twitter"]),axis=1)
    dfasianMen['asianMenPercentRepub_2020predicted'] = dfasianMen.apply(lambda row: row["apiManPercentRepublican_2020twitter"] * (row['asianMenPercentRepub_2016exitPoll']/row["apiManPercentRepublican_2016twitter"]),axis=1)

    dfasianMen['asianMenPercentDem_2020predicted'].values[dfasianMen['asianMenPercentDem_2020predicted'].values > 100] = 100
    dfasianMen['asianMenPercentDem_2020predicted'].values[dfasianMen['asianMenPercentDem_2020predicted'].values < 0] = 0
    dfasianMen['asianMenPercentRepub_2020predicted'].values[dfasianMen['asianMenPercentRepub_2020predicted'].values > 100] = 100
    dfasianMen['asianMenPercentRepub_2020predicted'].values[dfasianMen['asianMenPercentRepub_2020predicted'].values < 0] = 0

    dfasianMen['asianMenPercentDem_2020actual'] = dfasianMen['asianMenPercentDem_2020exitPoll']
    dfasianMen['asianMenPercentRepub_2020actual'] = dfasianMen['asianMenPercentRepub_2020exitPoll']

    dfasianMen['asianMenPercentDem_absError'] = abs(dfasianMen['asianMenPercentDem_2020predicted'] - dfasianMen['asianMenPercentDem_2020actual'])
    dfasianMen['asianMenPercentRepub_absError'] = abs(dfasianMen['asianMenPercentRepub_2020predicted'] - dfasianMen['asianMenPercentRepub_2020actual'])

    dfasianMen['asianMenPercentDem_meanAbsError'] = dfasianMen['asianMenPercentDem_absError'].mean()
    dfasianMen['asianMenPercentRepub_meanAbsError'] = dfasianMen['asianMenPercentRepub_absError'].mean()

    dfasianMen['asianMenPercentDem_meanStatesPredictedVoterShare'] = dfasianMen['asianMenPercentDem_2020predicted'].mean()
    dfasianMen['asianMenPercentRepub_meanStatesPredictedVoterShare'] = dfasianMen['asianMenPercentRepub_2020predicted'].mean()

    dfasianMen['asianMenPercentDem_meanStatesActualVoterShare'] = dfasianMen['asianMenPercentDem_2020actual'].mean()
    dfasianMen['asianMenPercentRepub_meanStatesActualVoterShare'] = dfasianMen['asianMenPercentRepub_2020actual'].mean()


    dfasianMen.to_csv(dataPath+"corrections/"+'dfasianMen.csv')


    return ['asianMen',
            dfasianMen.loc[0].at['asianMenPercentDem_2020predicted'],
            dfasianMen.loc[0].at['asianMenPercentDem_2020actual'],
            dfasianMen['asianMenPercentDem_absError'].mean(),
            dfasianMen.loc[0].at['asianMenPercentRepub_2020predicted'],
            dfasianMen.loc[0].at['asianMenPercentRepub_2020actual'],
            dfasianMen['asianMenPercentRepub_absError'].mean()]





def gethispanicWomenPredictions(dfMerged):


    dfhispanicWomen = dfMerged[(dfMerged['latinoWomenPercentDem_2016exitPoll'] != -1) & \
                            (dfMerged['latinoWomenPercentDem_2020exitPoll'] != -1) & \
                            (dfMerged['latinoWomenPercentRepub_2016exitPoll'] != -1) & \
                            (dfMerged['latinoWomenPercentRepub_2020exitPoll'] != -1) & \
                            (dfMerged['hispanicWomanPercentDemocrat_2016twitter'] != 0) & \
                            (dfMerged['hispanicWomanPercentRepublican_2016twitter'] != 0) & \
                            (dfMerged['hispanicWomanPercentDemocrat_2020twitter'] != 0) & \
                            (dfMerged['hispanicWomanPercentRepublican_2020twitter'] != 0) & \
                            (dfMerged['hispanicWomanPercentDemocrat_2016twitter'] != -1) & \
                            (dfMerged['hispanicWomanPercentRepublican_2016twitter'] != -1) & \
                            (dfMerged['hispanicWomanPercentDemocrat_2020twitter'] != -1) & \
                            (dfMerged['hispanicWomanPercentRepublican_2020twitter'] != -1)]


    dfhispanicWomen['scalehispanicWomenDem'] = dfhispanicWomen.apply(lambda row: row['latinoWomenPercentDem_2016exitPoll']/row["hispanicWomanPercentDemocrat_2016twitter"],axis=1)
    dfhispanicWomen['scalehispanicWomenRep'] = dfhispanicWomen.apply(lambda row: row['latinoWomenPercentRepub_2016exitPoll']/row["hispanicWomanPercentRepublican_2016twitter"],axis=1)

    dfhispanicWomen['hispanicWomenPercentDem_2020predicted'] = dfhispanicWomen.apply(lambda row: row["hispanicWomanPercentDemocrat_2020twitter"] * (row['latinoWomenPercentDem_2016exitPoll']/row["hispanicWomanPercentDemocrat_2016twitter"]),axis=1)
    dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'] = dfhispanicWomen.apply(lambda row: row["hispanicWomanPercentRepublican_2020twitter"] * (row['latinoWomenPercentRepub_2016exitPoll']/row["hispanicWomanPercentRepublican_2016twitter"]),axis=1)

    dfhispanicWomen['hispanicWomenPercentDem_2020predicted'].values[dfhispanicWomen['hispanicWomenPercentDem_2020predicted'].values > 100] = 100
    dfhispanicWomen['hispanicWomenPercentDem_2020predicted'].values[dfhispanicWomen['hispanicWomenPercentDem_2020predicted'].values < 0] = 0
    dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'].values[dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'].values > 100] = 100
    dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'].values[dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'].values < 0] = 0

    dfhispanicWomen['hispanicWomenPercentDem_2020actual'] = dfhispanicWomen['latinoWomenPercentDem_2020exitPoll']
    dfhispanicWomen['hispanicWomenPercentRepub_2020actual'] = dfhispanicWomen['latinoWomenPercentRepub_2020exitPoll']

    dfhispanicWomen['hispanicWomenPercentDem_absError'] = abs(dfhispanicWomen['hispanicWomenPercentDem_2020predicted'] - dfhispanicWomen['hispanicWomenPercentDem_2020actual'])
    dfhispanicWomen['hispanicWomenPercentRepub_absError'] = abs(dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'] - dfhispanicWomen['hispanicWomenPercentRepub_2020actual'])

    dfhispanicWomen['hispanicWomenPercentDem_meanAbsError'] = dfhispanicWomen['hispanicWomenPercentDem_absError'].mean()
    dfhispanicWomen['hispanicWomenPercentRepub_meanAbsError'] = dfhispanicWomen['hispanicWomenPercentRepub_absError'].mean()

    dfhispanicWomen['hispanicWomenPercentDem_meanStatesPredictedVoterShare'] = dfhispanicWomen['hispanicWomenPercentDem_2020predicted'].mean()
    dfhispanicWomen['hispanicWomenPercentRepub_meanStatesPredictedVoterShare'] = dfhispanicWomen['hispanicWomenPercentRepub_2020predicted'].mean()

    dfhispanicWomen['hispanicWomenPercentDem_meanStatesActualVoterShare'] = dfhispanicWomen['hispanicWomenPercentDem_2020actual'].mean()
    dfhispanicWomen['hispanicWomenPercentRepub_meanStatesActualVoterShare'] = dfhispanicWomen['hispanicWomenPercentRepub_2020actual'].mean()


    dfhispanicWomen.to_csv(dataPath+"corrections/"+'dfhispanicWomen.csv')


    return ['hispanicWomen',
            dfhispanicWomen.loc[0].at['hispanicWomenPercentDem_2020predicted'],
            dfhispanicWomen.loc[0].at['hispanicWomenPercentDem_2020actual'],
            abs(dfhispanicWomen.loc[0].at['hispanicWomenPercentDem_2020predicted']-dfhispanicWomen.loc[0].at['hispanicWomenPercentDem_2020actual']),
            dfhispanicWomen['hispanicWomenPercentDem_absError'].mean(),
            dfhispanicWomen.loc[0].at['hispanicWomenPercentRepub_2020predicted'],
            dfhispanicWomen.loc[0].at['hispanicWomenPercentRepub_2020actual'],
            abs(dfhispanicWomen.loc[0].at['hispanicWomenPercentRepub_2020predicted']-dfhispanicWomen.loc[0].at['hispanicWomenPercentRepub_2020actual']),
            dfhispanicWomen['hispanicWomenPercentRepub_absError'].mean()]



def gethispanicMenPredictions(dfMerged):


    dfhispanicMen = dfMerged[(dfMerged['latinoMenPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['latinoMenPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['latinoMenPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['latinoMenPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['hispanicManPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['hispanicManPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['hispanicManPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['hispanicManPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['hispanicManPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['hispanicManPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['hispanicManPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['hispanicManPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['hispanicManPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['hispanicManPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['hispanicManPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['hispanicManPercentRepublican_2020twitter'] != -1)]

    dfhispanicMen['scalehispanicMenDem'] = dfhispanicMen.apply(lambda row: row['latinoMenPercentDem_2016exitPoll']/row["hispanicManPercentDemocrat_2016twitter"],axis=1)
    dfhispanicMen['scalehispanicMenRep'] = dfhispanicMen.apply(lambda row: row['latinoMenPercentRepub_2016exitPoll']/row["hispanicManPercentRepublican_2016twitter"],axis=1)

    dfhispanicMen['hispanicMenPercentDem_2020predicted'] = dfhispanicMen.apply(lambda row: row["hispanicManPercentDemocrat_2020twitter"] * (row['latinoMenPercentDem_2016exitPoll']/row["hispanicManPercentDemocrat_2016twitter"]),axis=1)
    dfhispanicMen['hispanicMenPercentRepub_2020predicted'] = dfhispanicMen.apply(lambda row: row["hispanicManPercentRepublican_2020twitter"] * (row['latinoMenPercentRepub_2016exitPoll']/row["hispanicManPercentRepublican_2016twitter"]),axis=1)

    dfhispanicMen['hispanicMenPercentDem_2020predicted'].values[dfhispanicMen['hispanicMenPercentDem_2020predicted'].values > 100] = 100
    dfhispanicMen['hispanicMenPercentDem_2020predicted'].values[dfhispanicMen['hispanicMenPercentDem_2020predicted'].values < 0] = 0
    dfhispanicMen['hispanicMenPercentRepub_2020predicted'].values[dfhispanicMen['hispanicMenPercentRepub_2020predicted'].values > 100] = 100
    dfhispanicMen['hispanicMenPercentRepub_2020predicted'].values[dfhispanicMen['hispanicMenPercentRepub_2020predicted'].values < 0] = 0

    dfhispanicMen['hispanicMenPercentDem_2020actual'] = dfhispanicMen['latinoMenPercentDem_2020exitPoll']
    dfhispanicMen['hispanicMenPercentRepub_2020actual'] = dfhispanicMen['latinoMenPercentRepub_2020exitPoll']

    dfhispanicMen['hispanicMenPercentDem_absError'] = abs(dfhispanicMen['hispanicMenPercentDem_2020predicted'] - dfhispanicMen['hispanicMenPercentDem_2020actual'])
    dfhispanicMen['hispanicMenPercentRepub_absError'] = abs(dfhispanicMen['hispanicMenPercentRepub_2020predicted'] - dfhispanicMen['hispanicMenPercentRepub_2020actual'])

    dfhispanicMen['hispanicMenPercentDem_meanAbsError'] = dfhispanicMen['hispanicMenPercentDem_absError'].mean()
    dfhispanicMen['hispanicMenPercentRepub_meanAbsError'] = dfhispanicMen['hispanicMenPercentRepub_absError'].mean()

    dfhispanicMen['hispanicMenPercentDem_meanStatesPredictedVoterShare'] = dfhispanicMen['hispanicMenPercentDem_2020predicted'].mean()
    dfhispanicMen['hispanicMenPercentRepub_meanStatesPredictedVoterShare'] = dfhispanicMen['hispanicMenPercentRepub_2020predicted'].mean()

    dfhispanicMen['hispanicMenPercentDem_meanStatesActualVoterShare'] = dfhispanicMen['hispanicMenPercentDem_2020actual'].mean()
    dfhispanicMen['hispanicMenPercentRepub_meanStatesActualVoterShare'] = dfhispanicMen['hispanicMenPercentRepub_2020actual'].mean()


    dfhispanicMen.to_csv(dataPath+"corrections/"+'dfhispanicMen.csv')




    return ['hispanicMen',
            dfhispanicMen.loc[0].at['hispanicMenPercentDem_2020predicted'],
            dfhispanicMen.loc[0].at['hispanicMenPercentDem_2020actual'],
            abs(dfhispanicMen.loc[0].at['hispanicMenPercentDem_2020predicted']-dfhispanicMen.loc[0].at['hispanicMenPercentDem_2020actual']),
            dfhispanicMen['hispanicMenPercentDem_absError'].mean(),
            dfhispanicMen.loc[0].at['hispanicMenPercentRepub_2020predicted'],
            dfhispanicMen.loc[0].at['hispanicMenPercentRepub_2020actual'],
            abs(dfhispanicMen.loc[0].at['hispanicMenPercentRepub_2020predicted']-dfhispanicMen.loc[0].at['hispanicMenPercentRepub_2020actual']),
            dfhispanicMen['hispanicMenPercentRepub_absError'].mean()]




def getblackWomenPredictions(dfMerged):



    dfblackWomen = dfMerged[(dfMerged['blackWomenPercentDem_2016exitPoll'] != -1) & \
                            (dfMerged['blackWomenPercentDem_2020exitPoll'] != -1) & \
                            (dfMerged['blackWomenPercentRepub_2016exitPoll'] != -1) & \
                            (dfMerged['blackWomenPercentRepub_2020exitPoll'] != -1) & \
                            (dfMerged['blackWomanPercentDemocrat_2016twitter'] != 0) & \
                            (dfMerged['blackWomanPercentRepublican_2016twitter'] != 0) & \
                            (dfMerged['blackWomanPercentDemocrat_2020twitter'] != 0) & \
                            (dfMerged['blackWomanPercentRepublican_2020twitter'] != 0) & \
                            (dfMerged['blackWomanPercentDemocrat_2016twitter'] != -1) & \
                            (dfMerged['blackWomanPercentRepublican_2016twitter'] != -1) & \
                            (dfMerged['blackWomanPercentDemocrat_2020twitter'] != -1) & \
                            (dfMerged['blackWomanPercentRepublican_2020twitter'] != -1)]

    dfblackWomen['scaleblackWomenDem'] = dfblackWomen.apply(lambda row: row['blackWomenPercentDem_2016exitPoll']/row["blackWomanPercentDemocrat_2016twitter"],axis=1)
    dfblackWomen['scaleblackWomenRep'] = dfblackWomen.apply(lambda row: row['blackWomenPercentRepub_2016exitPoll']/row["blackWomanPercentRepublican_2016twitter"],axis=1)

    dfblackWomen['blackWomenPercentDem_2020predicted'] = dfblackWomen.apply(lambda row: row["blackWomanPercentDemocrat_2020twitter"] * (row['blackWomenPercentDem_2016exitPoll']/row["blackWomanPercentDemocrat_2016twitter"]),axis=1)
    dfblackWomen['blackWomenPercentRepub_2020predicted'] = dfblackWomen.apply(lambda row: row["blackWomanPercentRepublican_2020twitter"] * (row['blackWomenPercentRepub_2016exitPoll']/row["blackWomanPercentRepublican_2016twitter"]),axis=1)

    dfblackWomen['blackWomenPercentDem_2020predicted'].values[dfblackWomen['blackWomenPercentDem_2020predicted'].values > 100] = 100
    dfblackWomen['blackWomenPercentDem_2020predicted'].values[dfblackWomen['blackWomenPercentDem_2020predicted'].values < 0] = 0
    dfblackWomen['blackWomenPercentRepub_2020predicted'].values[dfblackWomen['blackWomenPercentRepub_2020predicted'].values > 100] = 100
    dfblackWomen['blackWomenPercentRepub_2020predicted'].values[dfblackWomen['blackWomenPercentRepub_2020predicted'].values < 0] = 0

    dfblackWomen['blackWomenPercentDem_2020actual'] = dfblackWomen['blackWomenPercentDem_2020exitPoll']
    dfblackWomen['blackWomenPercentRepub_2020actual'] = dfblackWomen['blackWomenPercentRepub_2020exitPoll']

    dfblackWomen['blackWomenPercentDem_absError'] = abs(dfblackWomen['blackWomenPercentDem_2020predicted'] - dfblackWomen['blackWomenPercentDem_2020actual'])
    dfblackWomen['blackWomenPercentRepub_absError'] = abs(dfblackWomen['blackWomenPercentRepub_2020predicted'] - dfblackWomen['blackWomenPercentRepub_2020actual'])

    dfblackWomen['blackWomenPercentDem_meanAbsError'] = dfblackWomen['blackWomenPercentDem_absError'].mean()
    dfblackWomen['blackWomenPercentRepub_meanAbsError'] = dfblackWomen['blackWomenPercentRepub_absError'].mean()

    dfblackWomen['blackWomenPercentDem_meanStatesPredictedVoterShare'] = dfblackWomen['blackWomenPercentDem_2020predicted'].mean()
    dfblackWomen['blackWomenPercentRepub_meanStatesPredictedVoterShare'] = dfblackWomen['blackWomenPercentRepub_2020predicted'].mean()

    dfblackWomen['blackWomenPercentDem_meanStatesActualVoterShare'] = dfblackWomen['blackWomenPercentDem_2020actual'].mean()
    dfblackWomen['blackWomenPercentRepub_meanStatesActualVoterShare'] = dfblackWomen['blackWomenPercentRepub_2020actual'].mean()


    dfblackWomen.to_csv(dataPath+"corrections/"+'dfblackWomen.csv')



    return ['blackWomen',
            dfblackWomen.loc[0].at['blackWomenPercentDem_2020predicted'],
            dfblackWomen.loc[0].at['blackWomenPercentDem_2020actual'],
            abs(dfblackWomen.loc[0].at['blackWomenPercentDem_2020predicted']-dfblackWomen.loc[0].at['blackWomenPercentDem_2020actual']),
            dfblackWomen['blackWomenPercentDem_absError'].mean(),
            dfblackWomen.loc[0].at['blackWomenPercentRepub_2020predicted'],
            dfblackWomen.loc[0].at['blackWomenPercentRepub_2020actual'],
            abs(dfblackWomen.loc[0].at['blackWomenPercentRepub_2020predicted']-dfblackWomen.loc[0].at['blackWomenPercentRepub_2020actual']),
            dfblackWomen['blackWomenPercentRepub_absError'].mean()]



def getblackMenPredictions(dfMerged):

    dfblackMen = dfMerged[(dfMerged['blackMenPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['blackMenPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['blackMenPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['blackMenPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['blackManPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['blackManPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['blackManPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['blackManPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['blackManPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['blackManPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['blackManPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['blackManPercentRepublican_2020twitter'] != -1)]

    dfblackMen['scaleblackMenDem'] = dfblackMen.apply(lambda row: row['blackMenPercentDem_2016exitPoll']/row["blackManPercentDemocrat_2016twitter"],axis=1)
    dfblackMen['scaleblackMenRep'] = dfblackMen.apply(lambda row: row['blackMenPercentRepub_2016exitPoll']/row["blackManPercentRepublican_2016twitter"],axis=1)

    dfblackMen['blackMenPercentDem_2020predicted'] = dfblackMen.apply(lambda row: row["blackManPercentDemocrat_2020twitter"] * (row['blackMenPercentDem_2016exitPoll']/row["blackManPercentDemocrat_2016twitter"]),axis=1)
    dfblackMen['blackMenPercentRepub_2020predicted'] = dfblackMen.apply(lambda row: row["blackManPercentRepublican_2020twitter"] * (row['blackMenPercentRepub_2016exitPoll']/row["blackManPercentRepublican_2016twitter"]),axis=1)

    dfblackMen['blackMenPercentDem_2020predicted'].values[dfblackMen['blackMenPercentDem_2020predicted'].values > 100] = 100
    dfblackMen['blackMenPercentDem_2020predicted'].values[dfblackMen['blackMenPercentDem_2020predicted'].values < 0] = 0
    dfblackMen['blackMenPercentRepub_2020predicted'].values[dfblackMen['blackMenPercentRepub_2020predicted'].values > 100] = 100
    dfblackMen['blackMenPercentRepub_2020predicted'].values[dfblackMen['blackMenPercentRepub_2020predicted'].values < 0] = 0

    dfblackMen['blackMenPercentDem_2020actual'] = dfblackMen['blackMenPercentDem_2020exitPoll']
    dfblackMen['blackMenPercentRepub_2020actual'] = dfblackMen['blackMenPercentRepub_2020exitPoll']

    dfblackMen['blackMenPercentDem_absError'] = abs(dfblackMen['blackMenPercentDem_2020predicted'] - dfblackMen['blackMenPercentDem_2020actual'])
    dfblackMen['blackMenPercentRepub_absError'] = abs(dfblackMen['blackMenPercentRepub_2020predicted'] - dfblackMen['blackMenPercentRepub_2020actual'])

    dfblackMen['blackMenPercentDem_meanAbsError'] = dfblackMen['blackMenPercentDem_absError'].mean()
    dfblackMen['blackMenPercentRepub_meanAbsError'] = dfblackMen['blackMenPercentRepub_absError'].mean()

    dfblackMen['blackMenPercentDem_meanStatesPredictedVoterShare'] = dfblackMen['blackMenPercentDem_2020predicted'].mean()
    dfblackMen['blackMenPercentRepub_meanStatesPredictedVoterShare'] = dfblackMen['blackMenPercentRepub_2020predicted'].mean()

    dfblackMen['blackMenPercentDem_meanStatesActualVoterShare'] = dfblackMen['blackMenPercentDem_2020actual'].mean()
    dfblackMen['blackMenPercentRepub_meanStatesActualVoterShare'] = dfblackMen['blackMenPercentRepub_2020actual'].mean()


    dfblackMen.to_csv(dataPath+"corrections/"+'dfblackMen.csv')

    return ['blackMen',
            dfblackMen.loc[0].at['blackMenPercentDem_2020predicted'],
            dfblackMen.loc[0].at['blackMenPercentDem_2020actual'],
            abs(dfblackMen.loc[0].at['blackMenPercentDem_2020predicted']-dfblackMen.loc[0].at['blackMenPercentDem_2020actual']),
            dfblackMen['blackMenPercentDem_absError'].mean(),
            dfblackMen.loc[0].at['blackMenPercentRepub_2020predicted'],
            dfblackMen.loc[0].at['blackMenPercentRepub_2020actual'],
            abs(dfblackMen.loc[0].at['blackMenPercentRepub_2020predicted']-dfblackMen.loc[0].at['blackMenPercentRepub_2020actual']),
            dfblackMen['blackMenPercentRepub_absError'].mean()]






def getWhiteWomenPredictions(dfMerged):


    dfwhiteWomen = dfMerged[(dfMerged['whiteWomenPercentDem_2016exitPoll'] != -1) & \
                            (dfMerged['whiteWomenPercentDem_2020exitPoll'] != -1) & \
                            (dfMerged['whiteWomenPercentRepub_2016exitPoll'] != -1) & \
                            (dfMerged['whiteWomenPercentRepub_2020exitPoll'] != -1) & \
                            (dfMerged['whiteWomanPercentDemocrat_2016twitter'] != 0) & \
                            (dfMerged['whiteWomanPercentRepublican_2016twitter'] != 0) & \
                            (dfMerged['whiteWomanPercentDemocrat_2020twitter'] != 0) & \
                            (dfMerged['whiteWomanPercentRepublican_2020twitter'] != 0) & \
                            (dfMerged['whiteWomanPercentDemocrat_2016twitter'] != -1) & \
                            (dfMerged['whiteWomanPercentRepublican_2016twitter'] != -1) & \
                            (dfMerged['whiteWomanPercentDemocrat_2020twitter'] != -1) & \
                            (dfMerged['whiteWomanPercentRepublican_2020twitter'] != -1)]

    dfwhiteWomen['scalewhiteWomenDem'] = dfwhiteWomen.apply(lambda row: row['whiteWomenPercentDem_2016exitPoll']/row["whiteWomanPercentDemocrat_2016twitter"],axis=1)
    dfwhiteWomen['scalewhiteWomenRep'] = dfwhiteWomen.apply(lambda row: row['whiteWomenPercentRepub_2016exitPoll']/row["whiteWomanPercentRepublican_2016twitter"],axis=1)

    dfwhiteWomen['whiteWomenPercentDem_2020predicted'] = dfwhiteWomen.apply(lambda row: row["whiteWomanPercentDemocrat_2020twitter"] * (row['whiteWomenPercentDem_2016exitPoll']/row["whiteWomanPercentDemocrat_2016twitter"]),axis=1)
    dfwhiteWomen['whiteWomenPercentRepub_2020predicted'] = dfwhiteWomen.apply(lambda row: row["whiteWomanPercentRepublican_2020twitter"] * (row['whiteWomenPercentRepub_2016exitPoll']/row["whiteWomanPercentRepublican_2016twitter"]),axis=1)

    dfwhiteWomen['whiteWomenPercentDem_2020predicted'].values[dfwhiteWomen['whiteWomenPercentDem_2020predicted'].values > 100] = 100
    dfwhiteWomen['whiteWomenPercentDem_2020predicted'].values[dfwhiteWomen['whiteWomenPercentDem_2020predicted'].values < 0] = 0
    dfwhiteWomen['whiteWomenPercentRepub_2020predicted'].values[dfwhiteWomen['whiteWomenPercentRepub_2020predicted'].values > 100] = 100
    dfwhiteWomen['whiteWomenPercentRepub_2020predicted'].values[dfwhiteWomen['whiteWomenPercentRepub_2020predicted'].values < 0] = 0

    dfwhiteWomen['whiteWomenPercentDem_2020actual'] = dfwhiteWomen['whiteWomenPercentDem_2020exitPoll']
    dfwhiteWomen['whiteWomenPercentRepub_2020actual'] = dfwhiteWomen['whiteWomenPercentRepub_2020exitPoll']

    dfwhiteWomen['whiteWomenPercentDem_absError'] = abs(dfwhiteWomen['whiteWomenPercentDem_2020predicted'] - dfwhiteWomen['whiteWomenPercentDem_2020actual'])
    dfwhiteWomen['whiteWomenPercentRepub_absError'] = abs(dfwhiteWomen['whiteWomenPercentRepub_2020predicted'] - dfwhiteWomen['whiteWomenPercentRepub_2020actual'])

    dfwhiteWomen['whiteWomenPercentDem_meanAbsError'] = dfwhiteWomen['whiteWomenPercentDem_absError'].mean()
    dfwhiteWomen['whiteWomenPercentRepub_meanAbsError'] = dfwhiteWomen['whiteWomenPercentRepub_absError'].mean()

    dfwhiteWomen['whiteWomenPercentDem_meanStatesPredictedVoterShare'] = dfwhiteWomen['whiteWomenPercentDem_2020predicted'].mean()
    dfwhiteWomen['whiteWomenPercentRepub_meanStatesPredictedVoterShare'] = dfwhiteWomen['whiteWomenPercentRepub_2020predicted'].mean()

    dfwhiteWomen['whiteWomenPercentDem_meanStatesActualVoterShare'] = dfwhiteWomen['whiteWomenPercentDem_2020actual'].mean()
    dfwhiteWomen['whiteWomenPercentRepub_meanStatesActualVoterShare'] = dfwhiteWomen['whiteWomenPercentRepub_2020actual'].mean()


    dfwhiteWomen.to_csv(dataPath+"corrections/"+'dfwhiteWomen.csv')


    return ['whiteWomen',
            dfwhiteWomen.loc[0].at['whiteWomenPercentDem_2020predicted'],
            dfwhiteWomen.loc[0].at['whiteWomenPercentDem_2020actual'],
            abs(dfwhiteWomen.loc[0].at['whiteWomenPercentDem_2020predicted']-dfwhiteWomen.loc[0].at['whiteWomenPercentDem_2020actual']),
            dfwhiteWomen['whiteWomenPercentDem_absError'].mean(),
            dfwhiteWomen.loc[0].at['whiteWomenPercentRepub_2020predicted'],
            dfwhiteWomen.loc[0].at['whiteWomenPercentRepub_2020actual'],
            abs(dfwhiteWomen.loc[0].at['whiteWomenPercentRepub_2020predicted']-dfwhiteWomen.loc[0].at['whiteWomenPercentRepub_2020actual']),
            dfwhiteWomen['whiteWomenPercentRepub_absError'].mean()]


    resultsDF = pd.DataFrame(resultsDF,columns=['demographicGroup',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'meanDemAbsoluteErrorAllStates',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'meanRepAbsoluteErrorAllStates'])


def getWhiteMenPredictions(dfMerged):



    dfwhiteMen = dfMerged[(dfMerged['whiteMenPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['whiteMenPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['whiteMenPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['whiteMenPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['whiteManPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['whiteManPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['whiteManPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['whiteManPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['whiteManPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['whiteManPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['whiteManPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['whiteManPercentRepublican_2020twitter'] != -1)]

    dfwhiteMen['scalewhiteMenDem'] = dfwhiteMen.apply(lambda row: row['whiteMenPercentDem_2016exitPoll']/row["whiteManPercentDemocrat_2016twitter"],axis=1)
    dfwhiteMen['scalewhiteMenRep'] = dfwhiteMen.apply(lambda row: row['whiteMenPercentRepub_2016exitPoll']/row["whiteManPercentRepublican_2016twitter"],axis=1)

    dfwhiteMen['whiteMenPercentDem_2020predicted'] = dfwhiteMen.apply(lambda row: row["whiteManPercentDemocrat_2020twitter"] * (row['whiteMenPercentDem_2016exitPoll']/row["whiteManPercentDemocrat_2016twitter"]),axis=1)
    dfwhiteMen['whiteMenPercentRepub_2020predicted'] = dfwhiteMen.apply(lambda row: row["whiteManPercentRepublican_2020twitter"] * (row['whiteMenPercentRepub_2016exitPoll']/row["whiteManPercentRepublican_2016twitter"]),axis=1)

    dfwhiteMen['whiteMenPercentDem_2020predicted'].values[dfwhiteMen['whiteMenPercentDem_2020predicted'].values > 100] = 100
    dfwhiteMen['whiteMenPercentDem_2020predicted'].values[dfwhiteMen['whiteMenPercentDem_2020predicted'].values < 0] = 0
    dfwhiteMen['whiteMenPercentRepub_2020predicted'].values[dfwhiteMen['whiteMenPercentRepub_2020predicted'].values > 100] = 100
    dfwhiteMen['whiteMenPercentRepub_2020predicted'].values[dfwhiteMen['whiteMenPercentRepub_2020predicted'].values < 0] = 0

    dfwhiteMen['whiteMenPercentDem_2020actual'] = dfwhiteMen['whiteMenPercentDem_2020exitPoll']
    dfwhiteMen['whiteMenPercentRepub_2020actual'] = dfwhiteMen['whiteMenPercentRepub_2020exitPoll']

    dfwhiteMen['whiteMenPercentDem_absError'] = abs(dfwhiteMen['whiteMenPercentDem_2020predicted'] - dfwhiteMen['whiteMenPercentDem_2020actual'])
    dfwhiteMen['whiteMenPercentRepub_absError'] = abs(dfwhiteMen['whiteMenPercentRepub_2020predicted'] - dfwhiteMen['whiteMenPercentRepub_2020actual'])

    dfwhiteMen['whiteMenPercentDem_meanAbsError'] = dfwhiteMen['whiteMenPercentDem_absError'].mean()
    dfwhiteMen['whiteMenPercentRepub_meanAbsError'] = dfwhiteMen['whiteMenPercentRepub_absError'].mean()

    dfwhiteMen['whiteMenPercentDem_meanStatesPredictedVoterShare'] = dfwhiteMen['whiteMenPercentDem_2020predicted'].mean()
    dfwhiteMen['whiteMenPercentRepub_meanStatesPredictedVoterShare'] = dfwhiteMen['whiteMenPercentRepub_2020predicted'].mean()

    dfwhiteMen['whiteMenPercentDem_meanStatesActualVoterShare'] = dfwhiteMen['whiteMenPercentDem_2020actual'].mean()
    dfwhiteMen['whiteMenPercentRepub_meanStatesActualVoterShare'] = dfwhiteMen['whiteMenPercentRepub_2020actual'].mean()


    dfwhiteMen.to_csv(dataPath+"corrections/"+'dfwhiteMen.csv')



    return ['whiteMen',
            dfwhiteMen.loc[0].at['whiteMenPercentDem_2020predicted'],
            dfwhiteMen.loc[0].at['whiteMenPercentDem_2020actual'],
            abs(dfwhiteMen.loc[0].at['whiteMenPercentDem_2020predicted']-dfwhiteMen.loc[0].at['whiteMenPercentDem_2020actual']),
            dfwhiteMen['whiteMenPercentDem_absError'].mean(),
            dfwhiteMen.loc[0].at['whiteMenPercentRepub_2020predicted'],
            dfwhiteMen.loc[0].at['whiteMenPercentRepub_2020actual'],
            abs(dfwhiteMen.loc[0].at['whiteMenPercentRepub_2020predicted']-dfwhiteMen.loc[0].at['whiteMenPercentRepub_2020actual']),
            dfwhiteMen['whiteMenPercentRepub_absError'].mean()]


    resultsDF = pd.DataFrame(resultsDF,columns=['demographicGroup',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'meanDemAbsoluteErrorAllStates',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'meanRepAbsoluteErrorAllStates'])


def getHispanicPredictions(dfMerged):

    dfHispanicLatino = dfMerged[(dfMerged['latinoPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['latinoPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['latinoPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['latinoPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['hispanicPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['hispanicPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['hispanicPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['hispanicPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['hispanicPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['hispanicPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['hispanicPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['hispanicPercentRepublican_2020twitter'] != -1)]

    print(dfHispanicLatino)

    dfHispanicLatino['scalehispanicDem'] = dfHispanicLatino.apply(lambda row: row['latinoPercentDem_2016exitPoll']/row["hispanicPercentDemocrat_2016twitter"],axis=1)
    dfHispanicLatino['scalehispanicRep'] = dfHispanicLatino.apply(lambda row: row['latinoPercentRepub_2016exitPoll']/row["hispanicPercentRepublican_2016twitter"],axis=1)

    dfHispanicLatino['hispanicPercentDem_2020predicted'] = dfHispanicLatino.apply(lambda row: row["hispanicPercentDemocrat_2020twitter"] * (row['latinoPercentDem_2016exitPoll']/row["hispanicPercentDemocrat_2016twitter"]),axis=1)
    dfHispanicLatino['hispanicPercentRepub_2020predicted'] = dfHispanicLatino.apply(lambda row: row["hispanicPercentRepublican_2020twitter"] * (row['latinoPercentRepub_2016exitPoll']/row["hispanicPercentRepublican_2016twitter"]),axis=1)

    dfHispanicLatino['hispanicPercentDem_2020predicted'].values[dfHispanicLatino['hispanicPercentDem_2020predicted'].values > 100] = 100
    dfHispanicLatino['hispanicPercentDem_2020predicted'].values[dfHispanicLatino['hispanicPercentDem_2020predicted'].values < 0] = 0
    dfHispanicLatino['hispanicPercentRepub_2020predicted'].values[dfHispanicLatino['hispanicPercentRepub_2020predicted'].values > 100] = 100
    dfHispanicLatino['hispanicPercentRepub_2020predicted'].values[dfHispanicLatino['hispanicPercentRepub_2020predicted'].values < 0] = 0

    dfHispanicLatino['hispanicPercentDem_2020actual'] = dfHispanicLatino['latinoPercentDem_2020exitPoll']
    dfHispanicLatino['hispanicPercentRepub_2020actual'] = dfHispanicLatino['latinoPercentRepub_2020exitPoll']

    dfHispanicLatino['hispanicPercentDem_absError'] = abs(dfHispanicLatino['hispanicPercentDem_2020predicted'] - dfHispanicLatino['hispanicPercentDem_2020actual'])
    dfHispanicLatino['hispanicPercentRepub_absError'] = abs(dfHispanicLatino['hispanicPercentRepub_2020predicted'] - dfHispanicLatino['hispanicPercentRepub_2020actual'])

    dfHispanicLatino['hispanicPercentDem_meanAbsError'] = dfHispanicLatino['hispanicPercentDem_absError'].mean()
    dfHispanicLatino['hispanicPercentRepub_meanAbsError'] = dfHispanicLatino['hispanicPercentRepub_absError'].mean()

    dfHispanicLatino['hispanicPercentDem_meanStatesPredictedVoterShare'] = dfHispanicLatino['hispanicPercentDem_2020predicted'].mean()
    dfHispanicLatino['hispanicPercentRepub_meanStatesPredictedVoterShare'] = dfHispanicLatino['hispanicPercentRepub_2020predicted'].mean()

    dfHispanicLatino['hispanicPercentDem_meanStatesActualVoterShare'] = dfHispanicLatino['hispanicPercentDem_2020actual'].mean()
    dfHispanicLatino['hispanicPercentRepub_meanStatesActualVoterShare'] = dfHispanicLatino['hispanicPercentRepub_2020actual'].mean()



    dfHispanicLatino.to_csv(dataPath+"corrections/"+'dfHispanicLatino.csv')



    return ['hispanic',
            dfHispanicLatino.loc[0].at['hispanicPercentDem_2020predicted'],
            dfHispanicLatino.loc[0].at['hispanicPercentDem_2020actual'],
            abs(dfHispanicLatino.loc[0].at['hispanicPercentDem_2020predicted']-dfHispanicLatino.loc[0].at['hispanicPercentDem_2020actual']),
            dfHispanicLatino['hispanicPercentDem_absError'].mean(),
            dfHispanicLatino.loc[0].at['hispanicPercentRepub_2020predicted'],
            dfHispanicLatino.loc[0].at['hispanicPercentRepub_2020actual'],
            abs(dfHispanicLatino.loc[0].at['hispanicPercentRepub_2020predicted']-dfHispanicLatino.loc[0].at['hispanicPercentRepub_2020actual']),
            dfHispanicLatino['hispanicPercentRepub_absError'].mean()]


def getAsianPredictions(dfMerged):



    dfasian = dfMerged[(dfMerged['asianPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['asianPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['asianPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['asianPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['apiPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['apiPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['apiPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['apiPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['apiPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['apiPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['apiPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['apiPercentRepublican_2020twitter'] != -1)]

    print(dfasian)

    dfasian['scaleasianDem'] = dfasian.apply(lambda row: row['asianPercentDem_2016exitPoll']/row["apiPercentDemocrat_2016twitter"],axis=1)
    dfasian['scaleasianRep'] = dfasian.apply(lambda row: row['asianPercentRepub_2016exitPoll']/row["apiPercentRepublican_2016twitter"],axis=1)

    dfasian['asianPercentDem_2020predicted'] = dfasian.apply(lambda row: row["apiPercentDemocrat_2020twitter"] * (row['asianPercentDem_2016exitPoll']/row["apiPercentDemocrat_2016twitter"]),axis=1)
    dfasian['asianPercentRepub_2020predicted'] = dfasian.apply(lambda row: row["apiPercentRepublican_2020twitter"] * (row['asianPercentRepub_2016exitPoll']/row["apiPercentRepublican_2016twitter"]),axis=1)

    dfasian['asianPercentDem_2020predicted'].values[dfasian['asianPercentDem_2020predicted'].values > 100] = 100
    dfasian['asianPercentDem_2020predicted'].values[dfasian['asianPercentDem_2020predicted'].values < 0] = 0
    dfasian['asianPercentRepub_2020predicted'].values[dfasian['asianPercentRepub_2020predicted'].values > 100] = 100
    dfasian['asianPercentRepub_2020predicted'].values[dfasian['asianPercentRepub_2020predicted'].values < 0] = 0

    dfasian['asianPercentDem_2020actual'] = dfasian['asianPercentDem_2020exitPoll']
    dfasian['asianPercentRepub_2020actual'] = dfasian['asianPercentRepub_2020exitPoll']

    dfasian['asianPercentDem_absError'] = abs(dfasian['asianPercentDem_2020predicted'] - dfasian['asianPercentDem_2020actual'])
    dfasian['asianPercentRepub_absError'] = abs(dfasian['asianPercentRepub_2020predicted'] - dfasian['asianPercentRepub_2020actual'])

    dfasian['asianPercentDem_meanAbsError'] = dfasian['asianPercentDem_absError'].mean()
    dfasian['asianPercentRepub_meanAbsError'] = dfasian['asianPercentRepub_absError'].mean()

    dfasian['asianPercentDem_meanStatesPredictedVoterShare'] = dfasian['asianPercentDem_2020predicted'].mean()
    dfasian['asianPercentRepub_meanStatesPredictedVoterShare'] = dfasian['asianPercentRepub_2020predicted'].mean()

    dfasian['asianPercentDem_meanStatesActualVoterShare'] = dfasian['asianPercentDem_2020actual'].mean()
    dfasian['asianPercentRepub_meanStatesActualVoterShare'] = dfasian['asianPercentRepub_2020actual'].mean()


    dfasian.to_csv(dataPath+"corrections/"+'dfasian.csv')


    return ['asian',
            dfasian.loc[0].at['asianPercentDem_2020predicted'],
            dfasian.loc[0].at['asianPercentDem_2020actual'],
            abs(dfasian.loc[0].at['asianPercentDem_2020predicted']-dfasian.loc[0].at['asianPercentDem_2020actual']),
            dfasian['asianPercentDem_absError'].mean(),
            dfasian.loc[0].at['asianPercentRepub_2020predicted'],
            dfasian.loc[0].at['asianPercentRepub_2020actual'],
            abs(dfasian.loc[0].at['asianPercentRepub_2020predicted']-dfasian.loc[0].at['asianPercentRepub_2020actual']),
            dfasian['asianPercentRepub_absError'].mean()]


    resultsDF = pd.DataFrame(resultsDF,columns=['demographicGroup',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'meanDemAbsoluteErrorAllStates',
                                      'percentDemNationalPredicted',
                                      'percentDemNationalActual',
                                      'meanRepAbsoluteErrorAllStates'])


def getBlackPredictions(dfMerged):

    dfBlack = dfMerged[(dfMerged['blackPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['blackPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['blackPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['blackPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['blackPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['blackPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['blackPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['blackPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['blackPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['blackPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['blackPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['blackPercentRepublican_2020twitter'] != -1)]


    dfBlack['scaleblackDem'] = dfBlack.apply(lambda row: row['blackPercentDem_2016exitPoll']/row["blackPercentDemocrat_2016twitter"],axis=1)
    dfBlack['scaleblackRep'] = dfBlack.apply(lambda row: row['blackPercentRepub_2016exitPoll']/row["blackPercentRepublican_2016twitter"],axis=1)

    dfBlack['blackPercentDem_2020predicted'] = dfBlack.apply(lambda row: row["blackPercentDemocrat_2020twitter"] * (row['blackPercentDem_2016exitPoll']/row["blackPercentDemocrat_2016twitter"]),axis=1)
    dfBlack['blackPercentRepub_2020predicted'] = dfBlack.apply(lambda row: row["blackPercentRepublican_2020twitter"] * (row['blackPercentRepub_2016exitPoll']/row["blackPercentRepublican_2016twitter"]),axis=1)

    dfBlack['blackPercentDem_2020predicted'].values[dfBlack['blackPercentDem_2020predicted'].values > 100] = 100
    dfBlack['blackPercentDem_2020predicted'].values[dfBlack['blackPercentDem_2020predicted'].values < 0] = 0
    dfBlack['blackPercentRepub_2020predicted'].values[dfBlack['blackPercentRepub_2020predicted'].values > 100] = 100
    dfBlack['blackPercentRepub_2020predicted'].values[dfBlack['blackPercentRepub_2020predicted'].values < 0] = 0

    dfBlack['blackPercentDem_2020actual'] = dfBlack['blackPercentDem_2020exitPoll']
    dfBlack['blackPercentRepub_2020actual'] = dfBlack['blackPercentRepub_2020exitPoll']

    dfBlack['blackPercentDem_absError'] = abs(dfBlack['blackPercentDem_2020predicted'] - dfBlack['blackPercentDem_2020actual'])
    dfBlack['blackPercentRepub_absError'] = abs(dfBlack['blackPercentRepub_2020predicted'] - dfBlack['blackPercentRepub_2020actual'])

    dfBlack['blackPercentDem_meanAbsError'] = dfBlack['blackPercentDem_absError'].mean()
    dfBlack['blackPercentRepub_meanAbsError'] = dfBlack['blackPercentRepub_absError'].mean()

    dfBlack['blackPercentDem_meanStatesPredictedVoterShare'] = dfBlack['blackPercentDem_2020predicted'].mean()
    dfBlack['blackPercentRepub_meanStatesPredictedVoterShare'] = dfBlack['blackPercentRepub_2020predicted'].mean()

    dfBlack['blackPercentDem_meanStatesActualVoterShare'] = dfBlack['blackPercentDem_2020actual'].mean()
    dfBlack['blackPercentRepub_meanStatesActualVoterShare'] = dfBlack['blackPercentRepub_2020actual'].mean()


    dfBlack.to_csv(dataPath+"corrections/"+'dfblack.csv')


    return ['black',
            dfBlack.loc[0].at['blackPercentDem_2020predicted'],
            dfBlack.loc[0].at['blackPercentDem_2020actual'],
            abs(dfBlack.loc[0].at['blackPercentDem_2020predicted']-dfBlack.loc[0].at['blackPercentDem_2020actual']),
            dfBlack['blackPercentDem_absError'].mean(),
            dfBlack.loc[0].at['blackPercentRepub_2020predicted'],
            dfBlack.loc[0].at['blackPercentRepub_2020actual'],
            abs(dfBlack.loc[0].at['blackPercentRepub_2020predicted']-dfBlack.loc[0].at['blackPercentRepub_2020actual']),
            dfBlack['blackPercentRepub_absError'].mean()]




def getMenPredictions(dfMerged):
    print(dfMerged)

    dfMen = dfMerged[(dfMerged['menPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['menPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['menPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['menPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['manPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['manPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['manPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['manPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['manPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['manPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['manPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['manPercentRepublican_2020twitter'] != -1)]




    dfMen['scaleMenDem'] = dfMen.apply(lambda row: row['menPercentDem_2016exitPoll']/row["manPercentDemocrat_2016twitter"],axis=1)
    dfMen['scaleMenRep'] = dfMen.apply(lambda row: row['menPercentRepub_2016exitPoll']/row["manPercentRepublican_2016twitter"],axis=1)

    dfMen['menPercentDem_2020predicted'] = dfMen.apply(lambda row: row["manPercentDemocrat_2020twitter"] * (row['menPercentDem_2016exitPoll']/row["manPercentDemocrat_2016twitter"]),axis=1)
    dfMen['menPercentRepub_2020predicted'] = dfMen.apply(lambda row: row["manPercentRepublican_2020twitter"] * (row['menPercentRepub_2016exitPoll']/row["manPercentRepublican_2016twitter"]),axis=1)

    dfMen['menPercentDem_2020predicted'].values[dfMen['menPercentDem_2020predicted'].values > 100] = 100
    dfMen['menPercentDem_2020predicted'].values[dfMen['menPercentDem_2020predicted'].values < 0] = 0
    dfMen['menPercentRepub_2020predicted'].values[dfMen['menPercentRepub_2020predicted'].values > 100] = 100
    dfMen['menPercentRepub_2020predicted'].values[dfMen['menPercentRepub_2020predicted'].values < 0] = 0

    dfMen['menPercentDem_2020actual'] = dfMen['menPercentDem_2020exitPoll']
    dfMen['menPercentRepub_2020actual'] = dfMen['menPercentRepub_2020exitPoll']

    dfMen['menPercentDem_absError'] = abs(dfMen['menPercentDem_2020predicted'] - dfMen['menPercentDem_2020actual'])
    dfMen['menPercentRepub_absError'] = abs(dfMen['menPercentRepub_2020predicted'] - dfMen['menPercentRepub_2020actual'])

    dfMen['menPercentDem_meanAbsError'] = dfMen['menPercentDem_absError'].mean()
    dfMen['menPercentRepub_meanAbsError'] = dfMen['menPercentRepub_absError'].mean()

    dfMen['menPercentDem_meanStatesPredictedVoterShare'] = dfMen['menPercentDem_2020predicted'].mean()
    dfMen['menPercentRepub_meanStatesPredictedVoterShare'] = dfMen['menPercentRepub_2020predicted'].mean()

    dfMen['menPercentDem_meanStatesActualVoterShare'] = dfMen['menPercentDem_2020actual'].mean()
    dfMen['menPercentRepub_meanStatesActualVoterShare'] = dfMen['menPercentRepub_2020actual'].mean()

    dfMen.to_csv(dataPath+"corrections/"+'dfMen.csv')

    print(dfMen)

    return ['men',
            dfMen.loc[0].at['menPercentDem_2020predicted'],
            dfMen.loc[0].at['menPercentDem_2020actual'],
            abs(dfMen.loc[0].at['menPercentDem_2020predicted']-dfMen.loc[0].at['menPercentDem_2020actual']),
            dfMen['menPercentDem_absError'].mean(),
            dfMen.loc[0].at['menPercentRepub_2020predicted'],
            dfMen.loc[0].at['menPercentRepub_2020actual'],
            abs(dfMen.loc[0].at['menPercentRepub_2020predicted']-dfMen.loc[0].at['menPercentRepub_2020actual']),
            dfMen['menPercentRepub_absError'].mean()]


def getMenPredictionsDistribution(dfMerged):

    dfMen = dfMerged[(dfMerged['menPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['menPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['menPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['menPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['manPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['manPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['manPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['manPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['manPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['manPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['manPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['manPercentRepublican_2020twitter'] != -1)]


    dfMen['scaleMenDem'] = dfMen.apply(lambda row: row['menPercentDem_2016exitPoll']/row["manPercentDemocrat_2016twitter"],axis=1)
    dfMen['scaleMenRep'] = dfMen.apply(lambda row: row['menPercentRepub_2016exitPoll']/row["manPercentRepublican_2016twitter"],axis=1)


    dfMen['menPercentDem_2020predicted'] = dfMen.apply(lambda row: row["manPercentDemocrat_2020twitter"] * (row['menPercentDem_2016exitPoll']/row["manPercentDemocrat_2016twitter"]),axis=1)
    dfMen['menPercentRepub_2020predicted'] = dfMen.apply(lambda row: row["manPercentRepublican_2020twitter"] * (row['menPercentRepub_2016exitPoll']/row["manPercentRepublican_2016twitter"]),axis=1)

    dfMen['menPercentDem_2020predicted'].values[dfMen['menPercentDem_2020predicted'].values > 100] = 100
    dfMen['menPercentDem_2020predicted'].values[dfMen['menPercentDem_2020predicted'].values < 0] = 0
    dfMen['menPercentRepub_2020predicted'].values[dfMen['menPercentRepub_2020predicted'].values > 100] = 100
    dfMen['menPercentRepub_2020predicted'].values[dfMen['menPercentRepub_2020predicted'].values < 0] = 0

    dfMen['menPercentDem_2020actual'] = dfMen['menPercentDem_2020exitPoll']
    dfMen['menPercentRepub_2020actual'] = dfMen['menPercentRepub_2020exitPoll']

    dfMen['menPercentDem_absError'] = abs(dfMen['menPercentDem_2020predicted'] - dfMen['menPercentDem_2020actual'])
    dfMen['menPercentRepub_absError'] = abs(dfMen['menPercentRepub_2020predicted'] - dfMen['menPercentRepub_2020actual'])

    dfMen['menPercentDem_meanAbsError'] = dfMen['menPercentDem_absError'].mean()
    dfMen['menPercentRepub_meanAbsError'] = dfMen['menPercentRepub_absError'].mean()

    dfMen['menPercentDem_meanStatesPredictedVoterShare'] = dfMen['menPercentDem_2020predicted'].mean()
    dfMen['menPercentRepub_meanStatesPredictedVoterShare'] = dfMen['menPercentRepub_2020predicted'].mean()

    dfMen['menPercentDem_meanStatesActualVoterShare'] = dfMen['menPercentDem_2020actual'].mean()
    dfMen['menPercentRepub_meanStatesActualVoterShare'] = dfMen['menPercentRepub_2020actual'].mean()

    dfMen.to_csv(dataPath+"corrections/"+'dfMen.csv')

    print(dfMen)

    return ['men',
            dfMen.loc[0].at['menPercentDem_2020predicted'],
            dfMen.loc[0].at['menPercentDem_2020actual'],
            abs(dfMen.loc[0].at['menPercentDem_2020predicted']-dfMen.loc[0].at['menPercentDem_2020actual']),
            dfMen['menPercentDem_absError'].mean(),
            dfMen.loc[0].at['menPercentRepub_2020predicted'],
            dfMen.loc[0].at['menPercentRepub_2020actual'],
            abs(dfMen.loc[0].at['menPercentRepub_2020predicted']-dfMen.loc[0].at['menPercentRepub_2020actual']),
            dfMen['menPercentRepub_absError'].mean()]



def getWomenPredictions(dfMerged):

    dfWomen = dfMerged[(dfMerged['womenPercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['womenPercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['womenPercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['womenPercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['womanPercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['womanPercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['womanPercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['womanPercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['womanPercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['womanPercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['womanPercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['womanPercentRepublican_2020twitter'] != -1)]

    dfWomen['scaleWomenDem'] = dfWomen.apply(lambda row: row['womenPercentDem_2016exitPoll']/row["womanPercentDemocrat_2016twitter"],axis=1)
    dfWomen['scaleWomenRep'] = dfWomen.apply(lambda row: row['womenPercentRepub_2016exitPoll']/row["womanPercentRepublican_2016twitter"],axis=1)

    dfWomen['womenPercentDem_2020predicted'] = dfWomen.apply(lambda row: row["womanPercentDemocrat_2020twitter"] * (row['womenPercentDem_2016exitPoll']/row["womanPercentDemocrat_2016twitter"]),axis=1)
    dfWomen['womenPercentRepub_2020predicted'] = dfWomen.apply(lambda row: row["womanPercentRepublican_2020twitter"] * (row['womenPercentRepub_2016exitPoll']/row["womanPercentRepublican_2016twitter"]),axis=1)

    dfWomen['womenPercentDem_2020predicted'].values[dfWomen['womenPercentDem_2020predicted'].values > 100] = 100
    dfWomen['womenPercentDem_2020predicted'].values[dfWomen['womenPercentDem_2020predicted'].values < 0] = 0
    dfWomen['womenPercentRepub_2020predicted'].values[dfWomen['womenPercentRepub_2020predicted'].values > 100] = 100
    dfWomen['womenPercentRepub_2020predicted'].values[dfWomen['womenPercentRepub_2020predicted'].values < 0] = 0

    dfWomen['womenPercentDem_2020actual'] = dfWomen['womenPercentDem_2020exitPoll']
    dfWomen['womenPercentRepub_2020actual'] = dfWomen['womenPercentRepub_2020exitPoll']

    dfWomen['womenPercentDem_absError'] = abs(dfWomen['womenPercentDem_2020predicted'] - dfWomen['womenPercentDem_2020actual'])
    dfWomen['womenPercentRepub_absError'] = abs(dfWomen['womenPercentRepub_2020predicted'] - dfWomen['womenPercentRepub_2020actual'])

    dfWomen['womenPercentDem_meanAbsError'] = dfWomen['womenPercentDem_absError'].mean()
    dfWomen['womenPercentRepub_meanAbsError'] = dfWomen['womenPercentRepub_absError'].mean()

    dfWomen['womenPercentDem_meanStatesPredictedVoterShare'] = dfWomen['womenPercentDem_2020predicted'].mean()
    dfWomen['womenPercentRepub_meanStatesPredictedVoterShare'] = dfWomen['womenPercentRepub_2020predicted'].mean()

    dfWomen['womenPercentDem_meanStatesActualVoterShare'] = dfWomen['womenPercentDem_2020actual'].mean()
    dfWomen['womenPercentRepub_meanStatesActualVoterShare'] = dfWomen['womenPercentRepub_2020actual'].mean()

    dfWomen.to_csv(dataPath+"corrections/"+'dfWomen.csv')

    return ['women',
            dfWomen.loc[0].at['womenPercentDem_2020predicted'],
            dfWomen.loc[0].at['womenPercentDem_2020actual'],
            abs(dfWomen.loc[0].at['womenPercentDem_2020predicted']-dfWomen.loc[0].at['womenPercentDem_2020actual']),
            dfWomen['womenPercentDem_absError'].mean(),
            dfWomen.loc[0].at['womenPercentRepub_2020predicted'],
            dfWomen.loc[0].at['womenPercentRepub_2020actual'],
            abs(dfWomen.loc[0].at['womenPercentRepub_2020predicted']-dfWomen.loc[0].at['womenPercentRepub_2020actual']),
            dfWomen['womenPercentRepub_absError'].mean()]

def getWhitePredictions(dfMerged):

    dfWhite = dfMerged[(dfMerged['whitePercentDem_2016exitPoll'] != -1) & \
                        (dfMerged['whitePercentDem_2020exitPoll'] != -1) & \
                        (dfMerged['whitePercentRepub_2016exitPoll'] != -1) & \
                        (dfMerged['whitePercentRepub_2020exitPoll'] != -1) & \
                        (dfMerged['whitePercentDemocrat_2016twitter'] != 0) & \
                        (dfMerged['whitePercentRepublican_2016twitter'] != 0) & \
                        (dfMerged['whitePercentDemocrat_2020twitter'] != 0) & \
                        (dfMerged['whitePercentRepublican_2020twitter'] != 0) & \
                        (dfMerged['whitePercentDemocrat_2016twitter'] != -1) & \
                        (dfMerged['whitePercentRepublican_2016twitter'] != -1) & \
                        (dfMerged['whitePercentDemocrat_2020twitter'] != -1) & \
                        (dfMerged['whitePercentRepublican_2020twitter'] != -1)]


    dfWhite['scaleWhiteDem'] = dfWhite.apply(lambda row: row['whitePercentDem_2016exitPoll']/row["whitePercentDemocrat_2016twitter"],axis=1)
    dfWhite['scaleWhiteRep'] = dfWhite.apply(lambda row: row['whitePercentRepub_2016exitPoll']/row["whitePercentRepublican_2016twitter"],axis=1)

    dfWhite['whitePercentDem_2020predicted'] = dfWhite.apply(lambda row: row["whitePercentDemocrat_2020twitter"] * (row['whitePercentDem_2016exitPoll']/row["whitePercentDemocrat_2016twitter"]),axis=1)
    dfWhite['whitePercentRepub_2020predicted'] = dfWhite.apply(lambda row: row["whitePercentRepublican_2020twitter"] * (row['whitePercentRepub_2016exitPoll']/row["whitePercentRepublican_2016twitter"]),axis=1)

    dfWhite['whitePercentDem_2020predicted'].values[dfWhite['whitePercentDem_2020predicted'].values > 100] = 100
    dfWhite['whitePercentDem_2020predicted'].values[dfWhite['whitePercentDem_2020predicted'].values < 0] = 0
    dfWhite['whitePercentRepub_2020predicted'].values[dfWhite['whitePercentRepub_2020predicted'].values > 100] = 100
    dfWhite['whitePercentRepub_2020predicted'].values[dfWhite['whitePercentRepub_2020predicted'].values < 0] = 0

    dfWhite['whitePercentDem_2020actual'] = dfWhite['whitePercentDem_2020exitPoll']
    dfWhite['whitePercentRepub_2020actual'] = dfWhite['whitePercentRepub_2020exitPoll']

    dfWhite['whitePercentDem_absError'] = abs(dfWhite['whitePercentDem_2020predicted'] - dfWhite['whitePercentDem_2020actual'])
    dfWhite['whitePercentRepub_absError'] = abs(dfWhite['whitePercentRepub_2020predicted'] - dfWhite['whitePercentRepub_2020actual'])

    dfWhite['whitePercentDem_meanAbsError'] = dfWhite['whitePercentDem_absError'].mean()
    dfWhite['whitePercentRepub_meanAbsError'] = dfWhite['whitePercentRepub_absError'].mean()

    dfWhite['whitePercentDem_meanStatesPredictedVoterShare'] = dfWhite['whitePercentDem_2020predicted'].mean()
    dfWhite['whitePercentRepub_meanStatesPredictedVoterShare'] = dfWhite['whitePercentRepub_2020predicted'].mean()

    dfWhite['whitePercentDem_meanStatesActualVoterShare'] = dfWhite['whitePercentDem_2020actual'].mean()
    dfWhite['whitePercentRepub_meanStatesActualVoterShare'] = dfWhite['whitePercentRepub_2020actual'].mean()


    dfWhite.to_csv(dataPath+"corrections/"+'dfWhite.csv')

    return ['white',
            dfWhite.loc[0].at['whitePercentDem_2020predicted'],
            dfWhite.loc[0].at['whitePercentDem_2020actual'],
            abs(dfWhite.loc[0].at['whitePercentDem_2020predicted']-dfWhite.loc[0].at['whitePercentDem_2020actual']),
            dfWhite['whitePercentDem_absError'].mean(),
            dfWhite.loc[0].at['whitePercentRepub_2020predicted'],
            dfWhite.loc[0].at['whitePercentRepub_2020actual'],
            abs(dfWhite.loc[0].at['whitePercentRepub_2020predicted']-dfWhite.loc[0].at['whitePercentRepub_2020actual']),
            dfWhite['whitePercentRepub_absError'].mean()]




if __name__ == '__main__':
    main()
