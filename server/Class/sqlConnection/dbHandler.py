from sqlalchemy import create_engine

URL = 'mysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format('root','saherMysqlSoufan','localhost',3306,'recosys')
engine = create_engine(URL, encoding='utf-8')


def setSqlInfo(info:dict):
    '''Set:
        1- name
        2- pass
        3- host
        4- port
        5- dbName'''
    
    lis = list(info['info'])
    global URL, engine
    print(info)
    URL = 'mysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(lis[0],lis[1],lis[2],lis[3],lis[4])
    engine = create_engine(URL, encoding='utf-8')





