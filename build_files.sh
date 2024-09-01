#!/bin/bash
set -e

# Verificar versão do Python
echo "Verificando versão do Python:"
python3 --version

# Instalar Python 3 se necessário
yum install -y python3

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Atualizar pip
pip install --upgrade pip

# Instalar dependências do projeto
pip install -r requirements.txt

# Garantir que o diretório de arquivos estáticos seja limpo e criado
echo "Limpando e criando o diretório de arquivos estáticos:"
rm -rf tierlistmovies/staticfiles
mkdir -p tierlistmovies/staticfiles

# Verificar a versão do Python novamente (opcional)
echo "Verificando versão do Python novamente:"
python3 --version

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos:"
python3 tierlistmovies/manage.py collectstatic --noinput

# Verificar o conteúdo do diretório staticfiles
echo "Conteúdo do diretório tierlistmovies/staticfiles:"
ls -R tierlistmovies/staticfiles
