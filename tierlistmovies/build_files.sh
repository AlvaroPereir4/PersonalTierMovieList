python3 --version
yum install -y python3
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 --version
npm run build
python3 manage.py collectstatic --noinput
