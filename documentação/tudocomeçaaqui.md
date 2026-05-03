# 🏃‍♂️ KoraJá

**KoraJá** é uma plataforma para descoberta, registro e recomendação de rotas de corrida, combinando experiência do usuário com engenharia de dados.

> Explore. Corra. Evolua.

---

## 🚀 Visão do Produto

O KoraJá permite que corredores encontrem novos percursos com base em:
- 📍 Localização
- 📏 Distância
- ⛰️ Elevação
- 🔥 Popularidade

Além disso, a plataforma evolui para recomendações inteligentes baseadas em dados.

---

## 🧭 Funcionalidades

### ✅ MVP
- Visualização de rotas em mapa
- Cadastro de novas rotas
- Listagem de rotas

### 🔜 Próximas versões
- Filtro por distância e dificuldade
- Rotas próximas do usuário
- Ranking de rotas
- Sistema de recomendação
- Integração com informações de clima

---

## 🏗️ Arquitetura

```mermaid
graph LR
  FE[Frontend\nReact / Next.js] --> API[API Gateway]
  API --> BE[Backend\nFastAPI / AWS Lambda]
  BE --> DB[PostgreSQL + PostGIS]
  BE --> S3[S3\n(Data Lake)]
  S3 --> ETL[AWS Glue / Spark\n(ETL)]
  ETL --> CUR[Camada de\nDados Curados]
  CUR --> RECO[Recomendações /\nAnalytics]
  DB --> RECO
```

> Se o seu visualizador de Markdown não renderizar Mermaid, use o fluxograma textual abaixo como fallback:

Frontend (React / Next.js) -> API Gateway -> Backend (FastAPI / AWS Lambda) -> PostgreSQL + PostGIS

Backend -> S3 (Data Lake) -> AWS Glue / Spark (ETL) -> Camada de Dados Curados -> Recomendações / Analytics

---

## 🔧 Stack Tecnológica

### 🖥️ Frontend
- React / Next.js
- Mapbox ou Google Maps

### ⚙️ Backend
- Python
- FastAPI
- AWS Lambda (opcional)

### 🗄️ Banco de Dados
- PostgreSQL
- PostGIS (dados geoespaciais)

### ☁️ Dados & Engenharia
- AWS S3 (Data Lake)
- AWS Glue / PySpark
- Athena / Query Engine

### 🛠️ Infraestrutura
- Terraform (Infrastructure as Code)

---

## 🧠 Diferenciais Técnicos

- Modelagem geoespacial com PostGIS
- Pipeline de dados para enriquecimento de rotas
- Arquitetura orientada a dados
- Base preparada para recomendações inteligentes

---

## 📊 Exemplo de Caso de Uso

**Recomendação de rotas:**

1. Usuário informa localização
2. Sistema busca rotas próximas (PostGIS)
3. Aplica ranking baseado em:
   - Popularidade
   - Distância
   - Dificuldade
4. Retorna melhores opções

---

## 📁 Estrutura de Repositórios
- koraja-app — Frontend
- koraja-api — Backend (FastAPI)
- koraja-data — Pipelines de dados (Glue/Spark)
- koraja-infra — Infraestrutura (Terraform)

---

## 📌 Exemplo de Modelo de Dados

```sql
CREATE TABLE routes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  distance_km FLOAT,
  elevation_gain FLOAT,
  geometry GEOMETRY(LINESTRING, 4326),
  city VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ Como rodar o backend (instruções rápidas)

Siga os passos abaixo para executar o backend (exemplo para o repositório `koraja-api`). Ajuste o repositório remoto conforme o seu projeto.

1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/koraja-api
cd koraja-api
```

2. Crie e ative um ambiente virtual

- Linux / macOS (bash/zsh):

```bash
python3 -m venv venv
source venv/bin/activate
```

- Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- Windows (cmd.exe):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Execute a aplicação (exemplo usando uvicorn)

```bash
uvicorn app.main:app --reload
```

Observações:
- Se estiver usando PowerShell e receber uma mensagem de execução de scripts bloqueada, execute (como Administrador) o comando: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` e depois ative novamente o venv.
- Ajuste a referência do módulo (`app.main:app`) para o caminho correto do seu projeto, caso seja diferente.

---

## 🧪 Próximos Passos
- Implementar endpoints de rotas
- Integrar com PostGIS
- Criar pipeline de dados (Glue/Spark)
- Implementar recomendação básica
- Fazer deploy na AWS

---

## 💡 Visão de Evolução

O KoraJá pode evoluir para:

- Rede social de corredores
- Análise de performance
- Sugestões personalizadas com machine learning
- Integração com wearables

---

## 👨‍💻 Autor

Desenvolvido por Tuck
Engenharia de Dados | Backend | Cloud

---

## 📄 Licença

Este projeto está licenciado como MIT.

---

## 🔥 Próximo nível (se quiser melhorar ainda mais)
Posso ajudar a evoluir o projeto com:
- README com badges (build, versão, etc.)
- Prints / mockups do app
- Pitch de 1 minuto para apresentar o projeto
- Código inicial do FastAPI com endpoints e estrutura profissional

Quer que eu gere o backend base (endpoints + estrutura)?
