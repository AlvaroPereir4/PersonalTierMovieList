#!/bin/bash
set -e

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Atualizar pip e instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# Coletar arquivos estáticos
python3 tierlistmovies/manage.py collectstatic --noinput

# Aplicar migrações do banco de dados
python3 tierlistmovies/manage.py migrate
