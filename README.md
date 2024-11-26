# Silva Framework

**Silva Framework** é um projeto 100% brasileiro que nasceu da necessidade de simplificar o desenvolvimento web em Python. A ideia surgiu durante um período de cansaço extremo, em meio a um burnout, quando percebi que os frameworks web mais populares do Python, apesar de muito bons, são frequentemente complexos e difíceis de utilizar de forma eficiente. Por outro lado, os frameworks menos conhecidos carecem de suporte e robustez, tornando-se difíceis de serem usados em produção.

A proposta do **Silva Framework** é oferecer uma solução mais simples, rápida e prática para o desenvolvimento de aplicações web em Python, mantendo a eficiência e a flexibilidade necessárias para competir com frameworks modernos de JavaScript. Ao longo do tempo, venho aprimorando e atualizando o projeto, com muito carinho e dedicação, pois acredito que ele pode ajudar a tornar o desenvolvimento web mais acessível e ágil para todos os desenvolvedores Python.

Este framework é projetado para ser intuitivo e de fácil integração, com o objetivo de fornecer aos desenvolvedores uma ferramenta poderosa sem sobrecarregar com complexidade desnecessária. Embora o projeto ainda esteja em desenvolvimento, o plano é continuar aprimorando e expandindo seus recursos, oferecendo a melhor experiência possível para a comunidade Python.

---

### Objetivos do Projeto

- **Simplicidade**: Facilitar a criação de aplicações web em Python sem a necessidade de lidar com configurações complexas ou bibliotecas excessivas.
- **Desempenho**: Foco na criação de um framework rápido e leve, adequado tanto para pequenos projetos quanto para aplicações de grande escala.
- **Robustez**: Garantir que o framework seja resiliente, flexível e bem estruturado, com foco em atender a requisitos comuns de produção.
- **Atualizações contínuas**: A equipe (eu) está constantemente melhorando o framework, com foco em feedback da comunidade e evolução do ecossistema Python.

---

### Visão Futura

Com o **Silva Framework**, a intenção é fornecer uma solução sólida que possa competir de forma saudável com os frameworks de JavaScript, mas com a praticidade e o estilo do Python. As melhorias futuras incluirão maior suporte para integração com bancos de dados, otimização de desempenho e novos recursos para facilitar ainda mais o desenvolvimento.

Agradeço a todos os que estão acompanhando e contribuindo para o crescimento do projeto. Se você tem sugestões ou deseja contribuir, fique à vontade para abrir uma issue ou pull request. A colaboração é sempre bem-vinda!


# Estrutura Inicial

```bash
silva-framework/
├── silva/                    # Diretório principal do framework
│   ├── __init__.py           # Inicialização do pacote
│   ├── core/                 # Lógica central do framework
│   │   ├── app.py            # Arquivo principal que inicializa o framework
│   │   ├── server.py         # Servidor HTTP
│   │   └── middleware.py     # Middleware (autenticação, logs, etc)
│   ├── router/               # Módulo de roteamento
│   │   └── router.py         # Lógica de roteamento
│   ├── views/                # Lógica de renderização de views/templates
│   │   └── views.py          # Lógica de renderização de views
│   ├── utils/                # Utilitários gerais
│   │   └── utils.py          # Funções auxiliares
├── examples/                 # Exemplos de uso
│   └── basic_app.py          # Exemplo básico de aplicação usando o framework
├── tests/                    # Diretório de testes
│   ├── core/                 # Testes da lógica central
│   │   ├── test_server.py    # Testes do servidor HTTP
│   │   └── test_middleware.py # Testes dos middlewares
│   ├── router/               # Testes de roteamento
│   │   └── test_router.py    # Testes do roteador
│   ├── views/                # Testes de views
│   │   └── test_views.py     # Testes das views
├── .gitignore                # Arquivo para ignorar arquivos no Git
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do framework
└── setup.py                  # Script de instalação do framework
```           


# Descrição dos Arquivos


```bash

silva/app.py: O arquivo principal que inicializa o framework. Ele pode configurar o servidor, o roteamento e o gerenciamento de middlewares.

silva/router.py: Responsável por gerenciar o roteamento de requisições HTTP, como definir as rotas, associar funções aos endpoints, etc.

silva/server.py: Implementação do servidor web. Pode usar o asyncio ou qualquer outra biblioteca para criar o servidor HTTP. Pode também fornecer integração com o WSGI ou ASGI, dependendo da sua escolha.

silva/views.py: Lida com a renderização de views, como HTML ou templates, para as respostas do servidor.

silva/middleware.py: Aqui você pode implementar funcionalidades intermediárias, como autenticação, verificação de permissões, ou logs.

silva/utils.py: Funções auxiliares para operações comuns que o framework pode precisar, como manipulação de strings, datas, etc.

tests/: Diretório para testes unitários e integração, o que é essencial para garantir que o framework se comporta como esperado.

examples/: Exemplos de como usar o framework. Este diretório serve para fornecer casos de uso práticos e funcionais para desenvolvedores.

requirements.txt: Arquivo de dependências. Você pode começar com as bibliotecas necessárias para o framework. Por exemplo, asyncio, jinja2 (se você for usar templates HTML), etc.

setup.py: Script que permitirá instalar o framework como um pacote Python.

```

# Versão do Python

```bash 
^3.12
````