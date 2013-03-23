import os
PROJECT_DIR='/project/dir/'
os.environ['DB']='YOUR_DB'
os.environ['DB_USER']='YOUR_DB_USER'
os.environ['DB_PASS']='YOUR_PASS'
os.environ['TEMPLATES_DIR']=PROJECT_DIR+'templates'
os.environ['SECRET_KEY']=''
os.environ['DEMO_TEMPLATES_DIR']=PROJECT_DIR+'project/templates'
os.environ['TIME_BANK_TEMPLATES_DIR']=PROJECT_DIR+'timebank/templates'
os.environ['PROJECT_DIR']=PROJECT_DIR
