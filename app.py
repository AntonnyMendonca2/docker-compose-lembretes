import json
import requests

def valoresCripto():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,cardano",
        "vs_currencies": "brl",
        "x-cg-demo-api-key": "CG-YoqU79JUNUDXLaJdQ3dJkXsq"
    }
    response = requests.get(url, params=params)
    return response.json()

def formatarValores(valores):
    """
    bitcoin: R$1.00
    cardano: R$1.00
    ethereum: R$1.00
    """
    output = ""
    for criptomoeda, value in valores.items():
        brl = value.get("brl")
        if brl is not None:
            output += f"{criptomoeda}: R${brl:,.0f}\n"
    return output

def enviar_mensagem(message, instance, instance_key, sender_number):
    url = f"http://35.175.198.164:8080/message/sendText/{instance}"
    payload = {
        "number": sender_number,
        "text": message,
        "delay": 2000,
    }
    headers = {
        "apikey": instance_key,
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response

def lambda_handler(event, context):
    valores = valoresCripto()
    valores_formatado = formatarValores(valores)
    try:
        enviar_mensagem(valores_formatado, event['instancia'], event['apikey'], event['sender_number'])
        return {
            'statusCode': 200,
            'body': json.dumps('Mensagem enviada com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao enviar mensagem: {str(e)}')
        }
    