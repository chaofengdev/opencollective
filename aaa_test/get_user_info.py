import subprocess
import json
import os


def get_user_info_with_curl(username, token):
    url = f"https://api.github.com/users/{username}"
    command = [
        'curl',
        '-H', f"Authorization: token {token}",
        '-H', "Accept: application/vnd.github.v3+json",
        url
    ]

    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

    if result.returncode == 0:
        # 解析 JSON 响应
        user_info = json.loads(result.stdout)
        return user_info
    else:
        print(f"Error: {result.stderr}")
        return None


def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    username = "kangax"  # 要查询的用户名
    token = ""  # 你的 GitHub 令牌

    user_info = get_user_info_with_curl(username, token)

    if user_info:
        # 确保保存目录存在
        directory = "github/user"
        os.makedirs(directory, exist_ok=True)

        # 设置保存文件的路径
        file_path = os.path.join(directory, f"{username}.json")

        # 保存 JSON 数据到文件
        save_to_json(user_info, file_path)
        print(f"User information saved to {file_path}")


if __name__ == "__main__":
    main()
