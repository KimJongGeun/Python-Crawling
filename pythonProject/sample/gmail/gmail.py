import smtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


config = configparser.ConfigParser()

config.read('config.ini')

# 발신자 이메일 주소 및 비밀번호
sender_email = config['MailAccount']['ID']
sender_password = config['MailAccount']['PW']

# 수신자 이메일 주소
receiver_email = config['MailAccount']['ID']

# 이메일 제목 및 내용
subject = "테스트 이메일"
body = "파이썬 테스트 메일"

# MIME(Multipurpose Internet Mail Extensions) 객체 생성
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# 이메일 내용 추가
message.attach(MIMEText(body, "plain"))

# SMTP 서버 설정 (Gmail의 경우)
smtp_server = "smtp.gmail.com"
smtp_port = 587


# TLS 연결 설정
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()

    # 로그인
    server.login(sender_email, sender_password)

    # 이메일 전송
    server.send_message(message)

print("이메일이 성공적으로 전송되었습니다.")
