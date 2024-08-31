import subprocess
import json
import os


def get_repo_info_with_curl(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    command = [
        'curl',
        '-H', f"Authorization: token {token}",
        '-H', "Accept: application/vnd.github.v3+json",
        url
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        # 解析 JSON 响应
        repo_info = json.loads(result.stdout)
        return repo_info
    else:
        print(f"Error: {result.stderr}")
        return None


def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    owner = "babel"  # 仓库所有者
    repo = "babel"  # 仓库名称
    token = ""  # 你的 GitHub 令牌

    repo_info = get_repo_info_with_curl(owner, repo, token)

    if repo_info:
        # 确保保存目录存在
        directory = "github/repo"
        os.makedirs(directory, exist_ok=True)

        # 设置保存文件的路径
        file_path = os.path.join(directory, f"{repo}.json")

        # 保存 JSON 数据到文件
        save_to_json(repo_info, file_path)
        print(f"Repository information saved to {file_path}")


if __name__ == "__main__":
    main()
