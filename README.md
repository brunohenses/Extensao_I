# Sistema de Divulgação de Eventos Culturais Locais (Python + Flask)

## Descrição do Projeto

Este repositório contém o código-fonte de um sistema web desenvolvido em Python utilizando o framework Flask, com o objetivo de cadastrar, gerenciar e divulgar eventos culturais locais. O sistema foi pensado para atender a pequenas cidades e instituições culturais (como centros culturais e fundações comunitárias) que necessitam de uma plataforma simples e intuitiva para promover feiras, shows, exposições e outras atividades culturais.

---

## Tema e Justificativa

### Tema

Plataforma digital para divulgação de eventos culturais em pequenas cidades.

### Justificativa

Em muitas localidades de porte reduzido, a carência de ferramentas acessíveis para a divulgação de ações culturais limita o alcance e a visibilidade de eventos que poderiam fortalecer a identidade local. Ao digitalizar o processo de cadastro e promoção de eventos, pretendemos:

- Facilitar o acesso da comunidade a informações atualizadas sobre cultura e lazer.
- Aumentar a participação do público em iniciativas locais.
- Conectar produtores culturais a apoiadores, patrocinadores e ao próprio público.

### Alinhamento com os Objetivos de Desenvolvimento Sustentável (ODS)

- **ODS 11.4 – Proteção do patrimônio cultural:**  
  O sistema contribui para a preservação e valorização do patrimônio cultural imaterial ao documentar, divulgar e arquivar eventos que refletem tradições e práticas culturais locais.

- **ODS 4.7 – Educação para a valorização da cultura:**  
  A plataforma oferece um espaço educativo, permitindo que escolas, universidades e a sociedade em geral conheçam e participem de atividades culturais, promovendo a aprendizagem e o respeito à diversidade cultural.

### Soft Skills Envolvidas

Durante o desenvolvimento deste projeto, as seguintes competências foram estimuladas:

- **Resolução de problemas:** identificação de requisitos, depuração de erros e otimização de fluxos de usuário.
- **Comunicação e trabalho em equipe:** redação de documentação clara, discussões de código e integração de sugestões.
- **Gerenciamento de tempo e prioridades:** estabelecimento de cronogramas para recursos, entregas e testes.

---

## Funcionalidades Principais

- Cadastro de eventos (título, data, local, descrição, imagem)
- Listagem e busca de eventos por data e categoria
- Edição e remoção de eventos
- Dashboard administrativo para gestão rápida
- Página pública para divulgação e acesso ao público geral

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Flask**
- **Jinja2** (templates)
- **SQLite** (banco de dados leve)
- **Git/GitHub** (controle de versão e hospedagem de código)
- **HTML5, CSS3 e Bootstrap** (front-end básico)

---

## Pré-requisitos

- Python 3 instalado
- Git instalado
- Ambiente virtual configurado (venv)

---

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows (Git Bash)
   # ou source venv/bin/activate # Linux/macOS
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure variáveis de ambiente (se necessário):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

---

## Como Executar

No terminal (com ambiente ativo):
```bash
flask run
```
Acesse `http://127.0.0.1:5000` no navegador.

---

## Estrutura do Projeto

```
Projeto-Eventos/
├── app.py
├── requirements.txt
├── venv/              # Ambiente virtual
├── templates/         # Templates HTML
│   ├── adicionar.html
│   ├── buscar.html
│   ├── editar.html
│   ├── index.html
│   ├── login.html
│   ├── registro.html
│   └── remover.html
├── static/            # Arquivos estáticos (CSS, imagens)
│   ├── img/
│       └── background.png
├── instance/
│   └── eventos.db
└── README.md          # Documentação do projeto
```

---

## Contribuição

Contribuições são sempre bem-vindas! Siga estes passos:

1. Fork deste repositório
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Faça commit das mudanças: `git commit -m "Descrição da feature"`
4. Envie para o branch original: `git push origin minha-feature`
5. Abra um Pull Request aqui no GitHub

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Bruno Henses – brunohenses@exemplo.com

Link do Projeto: https://github.com/brunohenses/Extensao_I

