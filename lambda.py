import json
import boto3
# Cliente SNS
sns = boto3.client('sns')
# Constantes
SNS_ARN = "arn:aws:sns:us-east-1:610575052461:NotificacionesBackups_Lambda"
def lambda_handler(event, context):
# Imprimir evento a log
print(event)
# Crear payload
subject = "Prueba Newrelc Backup Notification"
messageDic = {}
    try:
        messageDic["Account"] = event["account"]
        messageDic["CreationDate"] = event["detail"]["creationDate"]
        messageDic["ResourceType"] = event["detail"]["resourceType"]
        messageDic["ResourceARN"] = event["detai"]["resourceArn"]
        messageDic["State"] = event["detail"]["state"]
    try:
        messageDic["BackupSize"] = (int(event["detail"]["backupSizeInBytes"])/1024)/1024
    except:
        messageDic["BackupSize"] = 0
        messageDic["ComplatationDate"] = event["detail"]["completionDate"]
    except:
        messageDic = event
        message = json.dumps(messageDic)
# Enviar mensaje a SNS
response = sns.publish(
    TargetArn=SNS_ARN,
    Message=message,
    Subject=subject
)
# Responder
return {
    'statusCode': 200,
    'body': json.dumps(event)
}