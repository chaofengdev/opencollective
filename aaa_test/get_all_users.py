import requests
import json
import os


def fetch_users(token, max_users=10000):
    url = "https://api.github.com/users"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    users = []
    page = 1
    per_page = 100  # 每页返回的用户数
    while len(users) < max_users:
        response = requests.get(f"{url}?page={page}&per_page={per_page}", headers=headers)

        if response.status_code == 200:
            page_users = response.json()
            if not page_users:
                break
            users.extend(page_users)
            if len(users) >= max_users:
                users = users[:max_users]
                break
            page += 1
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break

    return users


def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    token = ""  # 你的 GitHub 令牌

    users = fetch_users(token, max_users=10000)

    if users:
        # 确保保存目录存在
        directory = "github/users"
        os.makedirs(directory, exist_ok=True)

        # 设置保存文件的路径
        file_path = os.path.join(directory, "github_users.json")

        # 保存 JSON 数据到文件
        save_to_json(users, file_path)
        print(f"Users information saved to {file_path}")


if __name__ == "__main__":
    main()
