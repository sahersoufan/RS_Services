from sqlalchemy import create_engine

URL = 'mysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format('root','saherMysqlSoufan','localhost',3306,'recosys')
engine = create_engine(URL, encoding='utf-8')




