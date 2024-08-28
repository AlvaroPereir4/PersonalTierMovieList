#!/bin/bash

# Exibir mensagens de log para debugging
echo "Iniciando o script de build..."

# Instalar dependências do sistema necessárias (se aplicável)
echo "Instalando Python 3..."
yum install -y python3

# Atualizar pip para a versão mais recente
echo "Atualizando pip..."
python3 -m pip install --upgrade pip

# Instalar dependências do projeto
echo "Instalando dependências do projeto..."
pip install -r requirements.txt

# Verificar a versão do Python para garantir que é a 3.x
echo "Versão do Python:"
python3 --version

# Executar o comando de build (se houver algum build específico do npm)
# Se o projeto não tiver um comando `npm run build`, você pode remover ou comentar essa linha.
echo "Executando o comando de build do npm..."
npm run build

# Executar o comando de coleta de arquivos estáticos do Django
echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo "Script de build concluído com sucesso."
