# AI Chatbot de Consolidação de Problemas

Este é um chatbot desenvolvido em Python utilizando **Streamlit** e a API do **Azure OpenAI**. O objetivo do chatbot é auxiliar empresas a consolidar e resumir problemas em várias etapas, sem oferecer soluções imediatas. O chatbot interage com o usuário, coletando informações detalhadas e, ao final, fornece um resumo para confirmação.

## Sumário

- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Uso](#uso)
- [Como Funciona](#como-funciona)
- [Possíveis Melhorias](#possíveis-melhorias)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

O chatbot foi projetado para:

- **Entender o problema do usuário** através de múltiplas interações.
- **Não fornecer soluções** imediatas, focando na compreensão do problema.
- **Resumir o problema** após coletar informações suficientes.
- **Solicitar confirmação** do usuário sobre o resumo apresentado.
- **Enviar o problema resumido** para uma instituição parceira para análise posterior.

## Pré-requisitos

- **Conta no Azure** com acesso ao **Azure OpenAI Service**.
- **Chave de API** válida para o Azure OpenAI.
- **Python 3.7** ou superior instalado.
- As seguintes bibliotecas Python:
  - `streamlit`
  - `requests`
  - `python-dotenv`

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/frotaadriano/ai-chatbot.git
   cd ai-chatbot
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

```
3. Instale as dependências:
```
pip install -r requirements.txt
```
Se não houver um arquivo requirements.txt, instale manualmente:
```
pip install streamlit requests python-dotenv
```

## Configuração

1. Obtenha suas credenciais do Azure OpenAI:

AZURE_OPENAI_API_KEY: Sua chave de API do Azure OpenAI.
AZURE_OPENAI_ENDPOINT: O endpoint base do seu recurso Azure OpenAI (sem caminhos adicionais). Exemplo: https://seu-recurso.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME: O nome do deployment que você configurou no Azure OpenAI.

2. Crie um arquivo .env na raiz do projeto e adicione suas credenciais:
    
    ```
    AZURE_OPENAI_API_KEY=YOUR_API_KEY
AZURE_OPENAI_ENDPOINT=YOUR_ENDPOINT
AZURE_OPENAI_DEPLOYMENT_NAME=YOUR_DEPLOYMENT_NAME
    ```


Importante: Substitua YOUR_API_KEY, YOUR_ENDPOINT e YOUR_DEPLOYMENT_NAME pelas suas informações reais.

## Execução
Para iniciar o chatbot, execute o seguinte comando:
    
    ``` streamlit run chatbot.py
    ```
    Isso abrirá o aplicativo no seu navegador padrão.


## Uso
1. Interaja com o Chatbot:
* Digite sua mensagem no campo de entrada e clique em Enviar.
* O chatbot fará perguntas dinâmicas para entender melhor o problema.
* Após pelo menos três interações, ele fornecerá um resumo do problema e pedirá sua confirmação.
2. Confirmação do Resumo:
* Concorde com o resumo se estiver correto.
* Se não concordar, forneça mais detalhes para que o chatbot ajuste o resumo.
3. Finalização:
* Após a confirmação, o chatbot informará que o problema será enviado para uma instituição parceira para análise.
## Como Funciona
* Streamlit: Utilizado para criar a interface web interativa do chatbot.
* Azure OpenAI Service: Fornece a inteligência artificial para gerar as respostas do chatbot.
* Gerenciamento de Estado: O st.session_state do Streamlit é usado para manter o histórico da conversa e o estado da sessão.
* Integração com a API:
* As mensagens são enviadas para a API do Azure OpenAI usando a biblioteca requests.
* A API retorna a resposta do assistente, que é exibida na interface do usuário.
## Possíveis Melhorias
*  Validação de Respostas:
* * Aprimorar a lógica para identificar melhor quando o usuário concorda ou não com o resumo.
* Interface do Usuário:
* * Personalizar o design para melhorar a experiência do usuário.
* * Adicionar suporte a diferentes idiomas ou temas visuais.
* Manuseio de Erros:
* *Implementar tratamento de exceções mais robusto para lidar com falhas na API ou problemas de conectividade.
* Segurança:
* * Garantir que os dados do usuário sejam tratados de forma segura e em conformidade com as leis de proteção de dados.

## Licença
* Este projeto está licenciado sob a MIT License. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.

## Contato
Para dúvidas ou sugestões, entre em contato:

Nome: Adriano Frota
GitHub: frotaadriano 

