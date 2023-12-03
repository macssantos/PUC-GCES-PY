# Use a imagem oficial do MongoDB
FROM mongo:latest

# Configurar credenciais (substitua pelos valores reais)
ENV MONGO_INITDB_ROOT_USERNAME=lappis
ENV MONGO_INITDB_ROOT_PASSWORD=lappis

# Criar banco de dados inicial (opcional)
ENV MONGO_INITDB_DATABASE=lappis

# Copiar scripts de inicialização (se necessário)
COPY ./scripts /docker-entrypoint-initdb.d/

