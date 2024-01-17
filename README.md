# Bandejão Twitter Bot

Este é um script Python que consulta o cardápio do bandejão da universidade e publica no Twitter. O script lê o cardápio semanal do arquivo 'cardapioSemana.txt' e, com base na data e hora atual, identifica se é hora do almoço ou jantar. Em seguida, ele cria um tweet informando o cardápio correspondente.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python (versão 3.x)
- Pacotes Python: `tweepy`, `google-cloud-secret-manager`

## Configuração

O script utiliza o Google Cloud Secret Manager para armazenar as chaves de API do Twitter. Você deve configurar quatro segredos:

- `twitter_consumer_key`: Chave de Consumidor do Twitter
- `twitter_consumer_secret`: Segredo de Consumidor do Twitter
- `btoken`: Token do Portador do Twitter
- `twitter_acess_token`: Token de Acesso do Twitter
- `twitter_acess_secret`: Segredo de Acesso do Twitter

Certifique-se de ter configurado corretamente o Google Cloud SDK e autenticado a conta.

## Instalação de Dependências

```bash
pip install tweepy google-cloud-secret-manager

Observação: Este script pode precisar de ajustes adicionais com base em mudanças futuras no formato do cardápio ou na API do Twitter. Certifique-se de verificar regularmente se há atualizações ou modificações necessárias.
    Lembre-se de substituir `nome_do_script.py` pelo nome real do seu script, se for diferente.
