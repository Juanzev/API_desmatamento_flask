# API de Dados de Desmatamento
Esta é uma API RESTful desenvolvida com Flask e utilizando SQLite como banco de dados, projetada para fornecer dados sobre desmatamento e queimadas no Brasil, com foco nas regiões da Amazônia e Cerrado, além de um comparativo por períodos presidenciais.

## 🚀 Como Rodar a API Localmente
Siga estes passos para configurar e executar a API no seu ambiente de desenvolvimento.

### Pré-requisitos
Certifique-se de ter o ***Python 3*** instalado em sua máquina.

### 1. Clone o Repositório (Opcional, se você já tiver os arquivos)
Se o código da sua API estiver em um repositório Git, clone-o:

Bash

```
git clone https://github.com/SeuUsuario/NomeDoSeuRepositorioDaAPI.git
cd NomeDoSeuRepositorioDaAPI
Se você já tem os arquivos localmente, navegue até a pasta raiz do projeto da API.
```

2. Crie e Ative um Ambiente Virtual (Recomendado)
É uma boa prática usar ambientes virtuais para isolar as dependências do seu projeto.

Bash

python -m venv venv
No Windows:

Bash

.\venv\Scripts\activate
No macOS/Linux:

Bash

source venv/bin/activate
3. Instale as Dependências
Com o ambiente virtual ativado, instale as bibliotecas Flask e Flask-CORS:

Bash

pip install Flask Flask-Cors
4. Execute a API
Para iniciar o servidor da sua API:

Bash

python DesmatamentoApi.py
Você verá uma mensagem no terminal indicando que a API está rodando, algo como:

 * Serving Flask app 'DesmatamentoApi'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
Isso significa que sua API está ativa e acessível localmente no endereço http://127.0.0.1:5000.

💡 Endpoints da API
A API oferece os seguintes endpoints para acesso aos dados:

GET /amazonia

Retorna dados de desmatamento na Amazônia (ano, área desmatada em km²).
Exemplo de resposta: [[1988, 21050], [1990, 13730], ...]
GET /cerrado

Retorna dados de desmatamento no Cerrado (ano, área desmatada em km²).
Exemplo de resposta: [[2001, 13500], [2005, 11580], ...]
GET /queimadas

Retorna dados de focos de queimadas (ano, número de focos).
Exemplo de resposta: [[2000, 115000], [2005, 226000], ...]
GET /presidentes

Retorna dados comparativos de desmatamento por período presidencial (nome, início, fim, taxa média anual em km²).
Exemplo de resposta: [["Sarney", 1985, 1990, 22400], ["Collor/Itamar", 1990, 1995, 17200], ...]
🛠️ Estrutura do Banco de Dados (SQLite)
A API utiliza um banco de dados SQLite (desmatamento.db) com as seguintes tabelas:

amazonia: id (INTEGER PRIMARY KEY), ano (INTEGER UNIQUE), area_desmatada (REAL)
cerrado: id (INTEGER PRIMARY KEY), ano (INTEGER UNIQUE), area_desmatada (REAL)
queimadas: id (INTEGER PRIMARY KEY), ano (INTEGER UNIQUE), focos (INTEGER)
presidentes: id (INTEGER PRIMARY KEY), nome (TEXT), inicio (INTEGER), fim (INTEGER), taxa_media_anual (REAL)
Os dados iniciais são inseridos automaticamente na primeira vez que a API é executada (função insert_initial_data()).

🔗 Integração com o Frontend
Para integrar esta API ao seu frontend (por exemplo, um site HTML/CSS/JavaScript com gráficos Chart.js), você precisará fazer requisições HTTP para os endpoints fornecidos.

No seu código JavaScript, a API_BASE_URL deve apontar para o endereço onde sua API está rodando. Se estiver localmente, será http://127.0.0.1:5000.

Exemplo de como buscar dados no JavaScript:

JavaScript

const API_BASE_URL = 'http://127.0.0.1:5000'; // Alterar para a URL de deploy se for o caso

async function getAmazoniaData() {
    try {
        const response = await fetch(`${API_BASE_URL}/amazonia`);
        const data = await response.json();
        console.log(data); // Utilize estes dados para popular seu gráfico
        return data;
    } catch (error) {
        console.error('Erro ao buscar dados da Amazônia:', error);
        return null;
    }
}

// Chame a função quando precisar dos dados
// getAmazoniaData();
☁️ Deploy (Hospedagem)
Para que a API esteja disponível publicamente e funcione sem que seu notebook esteja ligado, ela precisa ser hospedada em um servidor na internet. Plataformas como Render, Heroku ou PythonAnywhere são excelentes opções para fazer o deploy de aplicações Flask, muitas delas oferecendo planos gratuitos para projetos iniciantes.

Após o deploy, lembre-se de atualizar a API_BASE_URL no seu código JavaScript para a nova URL pública da sua API.

🤝 Contribuição (Opcional)
Se outras pessoas forem trabalhar no projeto, adicione uma seção sobre como elas podem contribuir.

Espero que este README.md seja muito útil para o seu projeto! Ele cobre os pontos mais importantes e facilita a compreensão e o uso da sua API.


Fontes





pode me mandar escrita dentro de um unico readme igual no github


Com certeza! Para ter um README.md completo, como os que vemos no GitHub, que abranja tanto o site (frontend) quanto a API (backend), o ideal é organizar as informações em seções claras.

Aqui está uma sugestão de como estruturar seu README.md principal, supondo que os arquivos do site e da API estejam em pastas separadas dentro do mesmo repositório, ou que você queira vincular os dois projetos.

Projeto Desmatamento e Queimadas no Brasil
Este projeto tem como objetivo visualizar dados de desmatamento e focos de queimadas em biomas brasileiros, principalmente Amazônia e Cerrado, além de apresentar um comparativo por períodos presidenciais. Ele é composto por um frontend (o site com os gráficos interativos) e um backend (uma API RESTful que fornece os dados).

🚀 Visão Geral e Como Rodar o Projeto
Para executar o projeto completo (site e API) em sua máquina local, siga os passos abaixo.

Pré-requisitos
Certifique-se de ter o Python 3 e o Node.js (para gerenciamento de dependências do frontend, embora não seja estritamente necessário para o seu HTML/CSS/JS simples, é uma boa prática para projetos maiores) instalados.

Estrutura do Projeto
É recomendado que seu projeto tenha uma estrutura similar a esta:

/
├── README.md              <- Este arquivo
├── site/                  <- Pasta com os arquivos do frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
└── api/                   <- Pasta com os arquivos da API
    ├── DesmatamentoApi.py
    └── desmatamento.db    <- Gerado automaticamente pela API
💻 1. Rodando a API (Backend)
Sua API Flask é responsável por servir os dados de desmatamento e queimadas.

Navegue até a Pasta da API
Abra seu terminal e vá para a pasta da API:

Bash

cd api/
Crie e Ative um Ambiente Virtual (Recomendado)
Isolar as dependências é uma boa prática.

Bash

python -m venv venv
No Windows:

Bash

.\venv\Scripts\activate
No macOS/Linux:

Bash

source venv/bin/activate
Instale as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:

Bash

pip install Flask Flask-Cors
Execute a API
Para iniciar o servidor da sua API:

Bash

python DesmatamentoApi.py
Você verá uma mensagem no terminal indicando que a API está rodando localmente em http://127.0.0.1:5000. Mantenha este terminal aberto enquanto estiver usando o site.

🌐 2. Acessando o Site (Frontend)
O site com os gráficos interativos consome os dados da API.

Localização dos Arquivos
Navegue até a pasta site/ onde estão seus arquivos index.html, style.css e script.js.

Abra o index.html no Navegador
Basta abrir o arquivo index.html diretamente no seu navegador de preferência (arrastando-o para a janela do navegador ou clicando duas vezes nele).

Se a sua API estiver rodando corretamente (passo 1), os gráficos deverão carregar automaticamente com os dados fornecidos por ela.

📊 Endpoints da API
A API Flask (http://127.0.0.1:5000) oferece os seguintes endpoints:

GET /amazonia: Dados de desmatamento na Amazônia (ano, área em km²).
GET /cerrado: Dados de desmatamento no Cerrado (ano, área em km²).
GET /queimadas: Dados de focos de queimadas (ano, número de focos).
GET /presidentes: Dados comparativos de desmatamento por período presidencial (nome, início, fim, taxa média anual em km²).
⚙️ Detalhes da Implementação
Backend (API Flask)
Tecnologias: Python, Flask, SQLite.
Banco de Dados: desmatamento.db é um arquivo SQLite. Ele é criado e populado com dados iniciais automaticamente na primeira execução do DesmatamentoApi.py.
CORS: Configurado para permitir requisições do frontend local ou de outras origens durante o desenvolvimento.
Frontend (Site)
Tecnologias: HTML, CSS, JavaScript.
Visualização de Dados: Utiliza a biblioteca Chart.js para criar os gráficos interativos de linha e barra.
Consumo da API: O JavaScript faz requisições Workspace para a API Flask (http://127.0.0.1:5000) para obter os dados dinamicamente.
🚀 Deploy (Hospedagem Online)
Para que este projeto esteja acessível 24/7 e por outras pessoas, tanto o site quanto a API precisam ser hospedados online.

Frontend (Site): Pode ser hospedado gratuitamente em serviços de hospedagem de conteúdo estático como GitHub Pages, Netlify ou Vercel.
Backend (API Flask): Requer um ambiente de execução para Python. Plataformas PaaS (Platform as a Service) como Render, Heroku ou PythonAnywhere são as mais recomendadas para iniciantes, pois simplificam bastante o processo de deploy.
Ao fazer o deploy da API, você receberá uma nova URL pública (ex: https://sua-api-desmatamento.render.com). Lembre-se de atualizar a variável API_BASE_URL no seu arquivo script.js com essa nova URL.

🤝 Contribuição
Se você quiser contribuir com este projeto, sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias.

Este README.md oferece uma visão completa do seu projeto, explicando como rodá-lo, quais são seus componentes, como eles se integram e como ele pode ser disponibilizado online.
