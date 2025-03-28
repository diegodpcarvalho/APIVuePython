## 🏥 API de Busca de Dados em CSV com Flask + Vue.js

## 🚀 Visão Geral  
Este projeto implementa uma **API Flask** para buscar informações em um arquivo CSV e um **frontend Vue.js** para consumir essa API. Ele inclui tratamento de acentos, normalização de texto e CORS configurado corretamente para permitir integração entre backend e frontend.  

📌 **Principais Tecnologias:**  
- 🔥 **Flask** para criar a API REST  
- 🎨 **Vue.js** para o frontend dinâmico  
- 🐍 **Pandas** para manipulação de dados CSV  
- 🌍 **Flask-CORS** para permitir requisições entre domínios diferentes  

---

## 📂 Estrutura do Projeto  

```bash
 📂 APIVuePython/            # API em Flask
│   ├── main.py           # Código principal da API
│   ├── Relatorio_cadop.csv # Base de dados usada para busca
│── 📂 front-end/           # Aplicação Vue.js
│   ├── src/
│   │   ├── components/
│   │   │   ├── BuscarDados.vue  # Componente Vue que faz a busca
│   ├── App.vue           # Componente raiz Vue
│── README.md             # Documentação do projeto
```
## ⚙️ Como Executar
1️⃣ Rodando o Backend (Flask)
Pré-requisitos: Python instalado

📌 Instale as dependências:
pip install flask flask-cors pandas

📌 Inicie a API Flask:
python main.py

📌 A API estará rodando em:
http://127.0.0.1:5000/buscar?q=santos&coluna=Cidade

2️⃣ Rodando o Frontend (Vue.js)
Pré-requisitos: Node.js instalado

📌 Instale as dependências:
cd frontend
npm install

📌 Inicie o servidor Vue:
npm run dev

📌 Acesse no navegador:
http://localhost:8080

## 🔍 Como Funciona
🌐 Backend (Flask)
O Flask lê um arquivo CSV (Relatorio_cadop.csv) e expõe uma API REST para buscar dados filtrando por diferentes colunas.

Exemplo de requisição:
GET /buscar?q=santos&coluna=Cidade

## 🎨 Frontend (Vue.js)
O frontend tem um componente Vue chamado BuscarDados.vue, que:
✅ Permite o usuário digitar um termo e escolher uma coluna
✅ Faz uma requisição fetch() para a API Flask
✅ Exibe os resultados em uma tabela interativa

## Testes Automatizados com Pytest
Para garantir o funcionamento da API, testes foram criados utilizando pytest. Para executá-los, rode o seguinte comando:
pytest tests/

## 🔧 Melhorias Implementadas
✅ CORS Configurado – O backend permite requisições de http://localhost:8080 (frontend Vue.js)
✅ Normalização de Texto – Removemos acentos para buscas mais eficazes
✅ Tratamento de Erros – Erros do usuário são exibidos corretamente
✅ Otimização no Backend – Uso de applymap() para processamento eficiente do CSV
✅ Interface Intuitiva – Frontend Vue com experiência fluída
