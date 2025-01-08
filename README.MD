# Crypto Bot

Este projeto é um bot que obtém os valores atuais de criptomoedas (Bitcoin, Ethereum, Cardano) em BRL (Reais) usando a API CoinGecko e envia esses valores formatados como uma mensagem de texto.

## Estrutura do Projeto

- `app.py`: Contém a lógica principal do bot, incluindo funções para obter valores de criptomoedas, formatar esses valores e enviar mensagens de texto.

## Como Usar

### Pré-requisitos

- Python 3.x
- Bibliotecas `requests` e `json`

### Instalação

1. Clone este repositório para sua máquina local.
2. Instale as dependências necessárias:
    ```bash
    pip install requests
    ```

### Configuração

- Certifique-se de ter uma chave de API válida para a API CoinGecko.
- Configure os parâmetros necessários no arquivo `app.py` ou passe-os via evento Lambda.

### Executando o Bot

Para executar o bot, você pode usar o AWS Lambda ou executar o script localmente.

#### Executando Localmente

1. Execute o script `app.py`:
    ```bash
    python app.py
    ```

#### Executando no AWS Lambda

1. Crie uma função Lambda no AWS.
2. Faça o upload do arquivo `app.py` e das dependências necessárias.
3. Configure o evento para chamar a função `lambda_handler`.

### Funções Principais

- `valoresCripto()`: Obtém os valores atuais das criptomoedas.
- `formatarValores(valores)`: Formata os valores das criptomoedas para uma string legível.
- `enviar_mensagem(message, instance, instance_key, sender_number)`: Envia a mensagem formatada para um número de telefone especificado.
- `lambda_handler(event, context)`: Função de entrada para o AWS Lambda.

### Exemplo de Evento Lambda

```json
{
    "instancia": "sua_instancia",
    "apikey": "sua_chave_de_api",
    "sender_number": "numero_do_destinatario"
}
```
