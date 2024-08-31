import os
import json
import csv
import pandas as pd


def json_to_csv_and_excel(json_path, csv_path, excel_path):
    """将单个JSON文件转换为CSV文件和Excel文件，并保留特定字段"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    required_fields = [
        'MemberId', 'company', 'createdAt', 'currency', 'isActive',
        'lastTransactionAmount', 'lastTransactionAt', 'role', 'tier',
        'totalAmountDonated', 'type', 'profile', 'twitter', 'github', 'website'
    ]

    if data:
        # 确保每个数据项只保留需要的字段
        processed_data = [
            {field: member.get(field, 0) for field in required_fields}
            for member in data
        ]

        # 将数据写入CSV文件
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=required_fields)
            writer.writeheader()
            writer.writerows(processed_data)

        # 将数据写入Excel文件
        df = pd.DataFrame(processed_data)
        df.to_excel(excel_path, index=False, encoding='utf-8')


# def merge_csv_files(csv_folder, output_csv_path):
#     """合并CSV文件并去重"""
#     all_csv_files = [os.path.join(csv_folder, f) for f in os.listdir(csv_folder) if f.endswith('.csv')]
#     combined_csv = pd.concat([pd.read_csv(f) for f in all_csv_files])
#
#     # 按MemberId字段去重
#     combined_csv.drop_duplicates(subset='MemberId', keep='first', inplace=True)
#
#     combined_csv.to_csv(output_csv_path, index=False, encoding='utf-8')


def process_json_to_csv_and_excel_and_merge(json_folder, csv_folder, excel_folder, output_csv_path):
    """主函数：处理JSON到CSV和Excel并合并所有CSV"""
    # 创建CSV、Excel和输出文件夹，如果不存在
    os.makedirs(csv_folder, exist_ok=True)
    os.makedirs(excel_folder, exist_ok=True)
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

    # 遍历json文件夹下的所有json文件并转换为CSV和Excel
    for json_file in os.listdir(json_folder):
        if json_file.endswith('.json'):
            json_path = os.path.join(json_folder, json_file)
            csv_path = os.path.join(csv_folder, f"{os.path.splitext(json_file)[0]}.csv")
            excel_path = os.path.join(excel_folder, f"{os.path.splitext(json_file)[0]}.xlsx")
            json_to_csv_and_excel(json_path, csv_path, excel_path)

    # 合并所有CSV文件并去重
    # merge_csv_files(csv_folder, output_csv_path)


# 主函数调用
if __name__ == "__main__":
    json_folder = './json'  # JSON文件所在文件夹路径
    csv_folder = './csv'  # CSV文件保存路径
    excel_folder = './excel'  # Excel文件保存路径
    output_csv_path = './csv_all/res.csv'  # 合并后的CSV文件保存路径

    process_json_to_csv_and_excel_and_merge(json_folder, csv_folder, excel_folder, output_csv_path)
