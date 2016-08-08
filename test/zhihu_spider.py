from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()

try:
    client.login('wuyi365@gmail.com', '110119rick')
except NeedCaptchaException:
 
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('wuyi365@gmail.com', '110119rick', captcha)