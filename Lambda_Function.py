import json


def lambda_handler(event, context):
    #Input
    text = event['startingText']
    replaceList = [ 'Oracle','Oracle©','Google','Google©','Microsoft','Microsoft©','Amazon','Amazon©','Deloitte','Deloitte©','test']
    
    #prevent error if amount of items i isn't even
    if len(replaceList)%2 != 0:
        replaceList.append(replaceList[-1]) 
        
    #Replace undesired parts of the string
    for i in range(0, len(replaceList), 2):
        text = text.replace(replaceList[i],replaceList[i+1])
        
    #Output
    return {
        'statusCode': 200,
        'body': text
    }
