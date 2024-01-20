import configparser

config = configparser.ConfigParser()

config.read('config.ini')

# INI 파일 읽기
config.read('config.ini')

# 'Database' 섹션의 값을 가져오기
host = config['Database']['host']
port = config['Database']['port']

# 가져온 값 출력
print(f'Host: {host}')
print(f'Port: {port}')

