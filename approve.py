import os
import requests

def main():
    # 读取账号密码配置
    accounts_str = os.getenv("WDT_ACCOUNTS", "")
    if not accounts_str:
        print("未配置WDT_ACCOUNTS环境变量")
        return
    account_list = accounts_str.split(",")
    for item in account_list:
        if ":" not in item:
            continue
        username, pwd = item.split(":", 1)
        print(f"正在执行账号{username}退货审批任务")
        try:
            login_url = "https://cm.wdtb2bc.com/login"
            approve_url = "https://cm.wdtb2bc.com/api/return/approve"
            session = requests.Session()
            session.post(login_url, data={"username": username, "password": pwd})
            resp = session.post(approve_url, json={"status": "pass"})
            print(f"账号{username}执行结果：{resp.status_code}")
        except Exception as e:
            print(f"账号{username}执行异常：{str(e)}")

if __name__ == "__main__":
    main()

