from time import sleep

from DrissionPage import WebPage
from DrissionPage._pages.chromium_page import ChromiumPage

def getToken(name,password):
    page = ChromiumPage( timeout=3)
    token = ''
    page.listen.start('token')
    page.get('https://pass.ncist.edu.cn/portal/login.html?redirectUri=http%3A%2F%2Fpass.ncist.edu.cn%2Fsso%2Fcas3%2FAPP032%2Flogin%3Fservice%3Dhttps%253A%252F%252Fseat.ncist.edu.cn%252Fremote%252Fstatic%252FcasAuth%252FgetServiceByVerifyTicket%252FcasLogin&r=-1846859084')
    try:
        name = page.ele('#username').input(name)
        page.ele('#password').input(password)
        page.ele('#fromsubmit').click()
        print("登录成功")
        i = 0
        sleep(1)
        for packet in page.listen.steps():
            print(packet)
            if i > 3:
                token = str(packet)[-50:-2]
            i += 1
            if i > 5:
                break
    except:
        print("登录失败")
        for packet in page.listen.steps():
            print(packet)
            token=str(packet)[-50:-2]
            print(token)
            break
    finally:
        print(token)
        page.listen.stop()
        page.ele('@class=header-quit').click()
        page.ele('@class=tip-container-footer').click()
        return token
