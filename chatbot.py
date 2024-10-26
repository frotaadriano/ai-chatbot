import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  # Exemplo: 'https://seu-recurso.openai.azure.com/'
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")  # Nome do seu deployment, por exemplo, 'gpt-4o'
API_VERSION = "2023-08-01-preview"  # Atualize para a versão apropriada

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

def main():
    st.title("Chatbot de Consolidação de Problemas")

    # Inicializa o histórico da conversa
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Você é um assistente que ajuda empresas a consolidar e resumir problemas. "
                            "Faça perguntas para entender o problema em detalhes, mas nunca forneça soluções. "
                            "Construa o entendimento do problema em várias etapas e, ao final, forneça um resumo "
                            "e pergunte se o usuário concorda. Se o usuário não fornecer detalhes suficientes, "
                            "solicite mais informações. Certifique-se de que a interação tenha pelo menos três trocas "
                            "antes de fornecer o resumo."
                        )
                    }
                ]
            }
        ]
        st.session_state.interaction_count = 0
        st.session_state.summary_provided = False

    # Exibe o histórico da conversa
    for message in st.session_state.messages[1:]:
        if message["role"] == "user":
            st.markdown(f"**Usuário:** {message['content'][0]['text']}")
        else:
            st.markdown(f"**Assistente:** {message['content'][0]['text']}")

    # Formulário para entrada do usuário
    with st.form(key='input_form', clear_on_submit=True):
        user_input = st.text_input("Digite sua mensagem:")
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        if user_input.strip():
            # Adiciona a mensagem do usuário ao histórico
            st.session_state.messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input.strip()
                    }
                ]
            })
            st.session_state.interaction_count += 1

            # Verifica se é hora de fornecer o resumo
            if st.session_state.interaction_count >= 3 and not st.session_state.summary_provided:
                # Adiciona instrução para fornecer o resumo
                st.session_state.messages.append({
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Agora, forneça um resumo do problema com base na conversa até agora. "
                                "Pergunte ao usuário se ele concorda com esse resumo. "
                                "Lembre-se de não oferecer soluções."
                            )
                        }
                    ]
                })
                st.session_state.summary_provided = True

            # Prepara o payload
            payload = {
                "messages": st.session_state.messages,
                "temperature": 0.7,
                "top_p": 0.95,
                "max_tokens": 800
            }

            # Monta a URL do endpoint
            url = f"{ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version={API_VERSION}"

            print(f'\n\n===================================================')
            print('Envia a solicitação para a API do Azure OpenAI')
            print('Sua mensagem foi: ', payload.get('messages'))
            try:
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()
                response_json = response.json()

                assistant_message = response_json['choices'][0]['message']['content']
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": assistant_message
                        }
                    ]
                })

                # Exibe a mensagem do assistente
                st.markdown(f"**Assistente:** {assistant_message}")
                print(f'\n===================================================')
                print(f'\nResposta: ', assistant_message)
            except requests.exceptions.RequestException as e:
                st.error(f"Erro ao chamar a API: {e}")

            # O campo de entrada será limpo automaticamente devido a clear_on_submit=True

        else:
            st.warning("Por favor, digite uma mensagem.")

if __name__ == "__main__":
    main()
