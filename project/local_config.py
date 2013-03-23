import os
PROJECT_DIR='/home/david/dev7/django-timebank/'
os.environ['DB']='django-timebank'
os.environ['DB_USER']='root'
os.environ['DB_PASS']='babel'
os.environ['TEMPLATES_DIR']=PROJECT_DIR+'templates'
os.environ['DEMO_TEMPLATES_DIR']=PROJECT_DIR+'project/templates'
os.environ['TIME_BANK_TEMPLATES_DIR']=PROJECT_DIR+'timebank/templates'


os.environ['SECRET_KEY']='@k%5+3(g6o3w4nj9cbr11v%0z)1)x8u2(+v-cgl!dtk*l+mb75'
