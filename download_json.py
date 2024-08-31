import os
import requests
import time
import json


def get_urls_from_file(input_file):
    """从文件中读取每一行，并生成相应的 URL"""
    urls = []
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # 去除行末的换行符
            if line:
                url = f"https://opencollective.com/{line}/members/all.json"
                urls.append((line, url))
    return urls


def save_urls_to_file(urls, output_file):
    """将生成的 URL 保存到指定的文件中"""
    with open(output_file, 'w', encoding='utf-8') as file:
        for _, url in urls:
            file.write(url + '\n')
    print(f"Saved URLs to {output_file}")


def fetch_and_save_json(urls, output_folder):
    """从给定的 URL 列表中获取 JSON 内容并保存到指定的文件夹中"""
    os.makedirs(output_folder, exist_ok=True)

    proxies = {
        "http": None,
        "https": None,
    }

    for name, url in urls:
        retries = 5
        success = False

        while retries > 0 and not success:
            try:
                response = requests.get(url, proxies=proxies, timeout=30)
                response.raise_for_status()  # 如果请求失败，抛出异常

                file_name = f"{name}.json"
                file_path = os.path.join(output_folder, file_name)

                # 将内容保存为JSON格式
                json_data = response.json()  # 解析为JSON格式
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, ensure_ascii=False, indent=4)  # 保存为格式化的JSON

                print(f"Saved JSON from {url} to {file_path}")
                success = True

            except requests.RequestException as e:
                retries -= 1
                print(f"Failed to fetch {url} (Retries left: {retries}): {e}")

                if retries == 0:
                    print(f"All retries failed for {url}, skipping to the next URL.")

            time.sleep(60)  # 请求之间的间隔时间


def main():
    input_file = 'collectiv_name/try_ccf.txt'  # 输入文件路径
    urls_file = 'collectiv_name/try_ccf_url.txt'  # URL 输出文件路径
    json_folder = './json'  # JSON 文件保存路径

    urls = get_urls_from_file(input_file)
    save_urls_to_file(urls, urls_file)
    fetch_and_save_json(urls, json_folder)


if __name__ == "__main__":
    main()
