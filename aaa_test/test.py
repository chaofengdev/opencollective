import requests
import json


def main():
    # 清除代理设置
    proxies = {
        "http": None,
        "https": None,
    }

    # 定义要下载的 JSON 文件的网址
    url = "https://opencollective.com/ESLint/members/all.json"

    # 发起请求并获取响应
    response = requests.get(url, proxies=proxies)

    # 确保请求成功
    if response.status_code == 200:
        # 将响应内容解析为 JSON
        data = response.json()

        # 将 JSON 数据保存到本地文件
        with open("test.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("JSON 文件已成功下载并保存到本地。")
    else:
        print(f"请求失败，状态码: {response.status_code}")


if __name__ == "__main__":
    main()
