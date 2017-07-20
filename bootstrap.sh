#/usr/bin bash
virtualenv -p python3 .
source bin/activate
pip install -r libraries/requirements.txt
npm install
gulp build
python libraries/manage.py migrate
python libraries/manage.py createsuperuser
