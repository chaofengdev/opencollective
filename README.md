# 数据分析demo
该仓库包含用于分析与 Open Collective 项目和 GitHub 仓库相关信息的脚本和数据。提供的脚本用于从 GitHub 和 Open Collective 获取数据、处理数据，并将其转换为更易于使用的格式（如 CSV）。

## 项目结构

- `.gitattributes`：Git 属性配置文件。
- `download_json.py`：用于从各种来源下载 JSON 数据的脚本。
- `get_all_users.py`：获取所有用户信息的脚本。
- `get_repo_contri.py`：获取指定仓库贡献者信息的脚本。
- `get_repo_info.py`：获取仓库详细信息的脚本。
- `get_user_info.py`：获取用户详细信息的脚本。
- `json_to_csv.py`：将 JSON 数据转换为 CSV 格式的脚本。
- `excel/`：包含 Vue 和 Webpack 项目的 Excel 数据文件。
- `github/`：包含与 GitHub 仓库及贡献者相关的 JSON 数据。
- `json/`：包含各种开源项目的 JSON 数据文件（如 Babel、Vue、Webpack 等）。

## 使用说明

1.**获取数据**：
使用提供的脚本从 GitHub 或 Open Collective 下载数据。示例：

```bash
python download_json.py
```

2.**处理数据**： 下载数据后，可以使用 `json_to_csv.py` 脚本将 JSON 数据转换为 CSV 格式，以便于进一步分析。 示例：

```
python json_to_csv.py
```

3.**数据分析**： 数据转换为 CSV 格式后，可以使用 Excel 或 Pandas 等工具进行分析。

## 相关依赖

- Python 3.x
- Requests 库（可以通过以下命令安装：`pip install requests`）

## 其他

api均来自官网，官网还有其他类型的api，此仓库的代码仅用作演示。
