import json

def lambda_handler(event, context):
    text = event['startingText']
    replaceList = ['Oracle','Oracle©','Google','Google©','Microsoft','Microsoft©','Amazon','Amazon©','Deloitte','Deloitte©']

    for i in range(0, len(replaceList), 2):
        text = text.replace(replaceList[i],replaceList[i +1])
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }
