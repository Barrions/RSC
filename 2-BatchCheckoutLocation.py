import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import csv

def choose_csv_file():
    global import_file
    import_file = filedialog.askopenfilename(title="选择CSV文件", filetypes=[("CSV files", "*.csv")])
    if not import_file:
        result_text.set("用户取消了文件选择。")
    else:
        result_text.set(f"已选择文件: {import_file}")

def process_csv():
    if not import_file:
        result_text.set("请先选择CSV文件。")
        return

    headers = {
        'authorization': "Bearer XXXXX",
        'accept': "application/json",
        'content-type': "application/json"
    }

    with open(import_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 1
        result_message = ""  # 用于保存处理结果的消息

        for row in csv_reader:
            id1 = row['id1']
            location1 = row.get('location1',None)
            id2 = row.get('status_id', None)
            assetid=row.get('assetid', None)

            url = f' {id1}/checkout'

            payload = {
                "checkout_to_type": "location",
                "assigned_location": location1,
               #"assigned_asset": assetid,
               #"checkout_to_type": "asset",
                "status_id": id2
            }

            response = requests.post(url, json=payload, headers=headers)

            if "Checkout target for asset" in response.json().get("messages", ""):
                error_message = f"Error processing asset {id1}: {response.json()['messages']}"
                result_message += error_message + "\n"
            else:
                success_message = response.text
                result_message += success_message + "\n"
            line_count += 1

        result_message += f'Total assets processed: {line_count}'
        
        # 显示结果弹窗
        messagebox.showinfo("处理结果", result_message)

# 创建主窗口
root = tk.Tk()
root.title("批量CheckoutLocation")

# 设置主窗口初始大小
root.geometry("650x200")

# 添加"选择CSV文件"按钮
choose_button = tk.Button(root, text="选择CSV文件", command=choose_csv_file)
choose_button.pack(pady=20)

# 防止窗口最大化
root.resizable(False, False)

# 添加"处理CSV文件"按钮
process_button = tk.Button(root, text="处理CSV文件", command=process_csv)
process_button.pack(pady=20)

# 添加文本框显示结果
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# 运行主循环
root.mainloop()
