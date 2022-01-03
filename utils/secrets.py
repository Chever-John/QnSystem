
class Secrets:
    class Email:
        emailHost = 'smtp.163.com'
        emailPort = 25
        emailAddr = '17696748602@163.com'
        emailPasswd = '*******************'# 邮箱 SMTP 授权码，此处为虚拟，须修改

    class DataBase:
        # database information

        host = 'localhost'
        user = 'root'
        passwd = '740309'  # 修改为您本地或远程的 mysql数据库信息
        db = 'database_test'

    class Host:  # 修改为django允许运行的网址
        allowedHost = ['localhost', '127.0.0.1', 'xxxxx']

    class RootUrl:
        webFront = 'http://127.0.0.1:8080'

        # webBack = 'http://127.0.0.1:8000'
        webBack = 'http://127.0.0.1:8000/api/api/qs'
