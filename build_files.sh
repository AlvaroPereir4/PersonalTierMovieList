python3 --version
yum install -y python3
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Garantir que o diretório de arquivos estáticos seja limpo
rm -rf tierlistmovies/staticfiles
mkdir -p tierlistmovies/staticfiles

python3 --version
python3 tierlistmovies/manage.py collectstatic --noinput

# Verifica o conteúdo do diretório staticfiles
echo "Conteúdo do diretório tierlistmovies:"
ls -R tierlistmovies/staticfiles
