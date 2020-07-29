import json

def lambda_handler(event, context):
    text = event['startingText']
    replaceList = [ 'Oracle','Oracle©','Google','Google©','Microsoft','Microsoft©','Amazon','Amazon©','Deloitte','Deloitte©','test']
    
    #prevent error if amount of items i uneven
    if len(replaceList)%2 != 0:
        replaceList.append(replaceList[-1]) 
        
    for i in range(0, len(replaceList), 2):
        text = text.replace(replaceList[i],replaceList[i +1])
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }
