import requests
import json
import os


def get_repo_contributors(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contributors = response.json()
        return contributors
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    owner = "babel"  # 仓库所有者用户名
    repo = "babel"  # 仓库名称
    token = ""  # 你的 GitHub 令牌

    contributors = get_repo_contributors(owner, repo, token)

    if contributors:
        # 确保保存目录存在
        directory = "github/contributors"
        os.makedirs(directory, exist_ok=True)

        # 设置保存文件的路径
        file_path = os.path.join(directory, f"{repo}_contributors.json")

        # 保存 JSON 数据到文件
        save_to_json(contributors, file_path)
        print(f"Contributors information saved to {file_path}")


if __name__ == "__main__":
    main()
