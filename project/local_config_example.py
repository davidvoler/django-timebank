import os
PROJECT_DIR='/project/dir/'
os.environ['DB']='YOUR_DB'
os.environ['DB_USER']='YOUR_DB_USER'
os.environ['DB_PASS']='YOUR_PASS'
os.environ['TEMPLATES_DIR']=PROJECT_DIR+'templates'
os.environ['SECRET_KEY']=''