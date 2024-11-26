FROM python:3.12-slim

WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY container/requirements.txt /app/requirements.txt

# Cria um ambiente virtual para isolar as dependências
RUN echo "Criando ambiente virtual..." && \
    python3 -m venv /venv && \
    echo "Ambiente virtual criado com sucesso!"

# Define o ambiente virtual como o padrão para o pip
ENV PATH="/venv/bin:$PATH"

# Log: Instalando dependências
RUN echo "Instalando dependências..." && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    echo "Dependências instaladas com sucesso!"

# Log: Atualizando pip
RUN echo "Atualizando o pip..." && \
    pip install --upgrade pip && \
    echo "Pip atualizado com sucesso!"

# Define o PYTHONPATH como variável de ambiente
ENV PYTHONPATH=/app/silva-framework

# Copia o projeto para o contêiner
COPY silva-framework /app/silva-framework

# Log: Comando padrão para iniciar a aplicação
CMD echo "Iniciando a aplicação..." && \
    python -m silva.core.app && \
    echo "Aplicação iniciada com sucesso!"

