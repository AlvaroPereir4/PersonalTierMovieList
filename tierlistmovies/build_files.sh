#!/bin/bash

# Instalar Python 3
yum install -y python3

# Atualizar pip para Python 3
python3 -m pip install --upgrade pip

# Instalar dependências do projeto
pip install -r requirements.txt

# Verificar a versão do Python para garantir que é o 3.x
python3 --version

# Executar o comando de build
npm run build

# Executar o comando de coleta de arquivos estáticos do Django
python3 manage.py collectstatic --noinput
