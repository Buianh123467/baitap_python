
import pandas as pd

# Đọc dữ liệu từ file Excel
url = "https://docs.google.com/spreadsheets/d/1e9rRiwAmRYq60Lx2PBMZcSOA8jC-rmoL/export?format=xlsx"
data = pd.read_excel(url)

# Ép kiểu dữ liệu về số (nếu có lỗi thì đặt NaN)
numeric_cols = ['vpv1', 'pCharge', 'SOC', 'ppv1', 'ppv2', 'ppv3']
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')  # Chuyển sai kiểu thành NaN

# Lọc dữ liệu theo điều kiện và tạo bản sao
filtered_data = data[(data['vpv1'] != 0) & (data['pCharge'] != 0) & (data['SOC'] > 8)].copy()

# Tính tổng các cột ppv1, ppv2, ppv3
filtered_data['Sum_PPV'] = filtered_data[['ppv1', 'ppv2', 'ppv3']].sum(axis=1)

# Lưu dữ liệu ra file CSV
filtered_data.to_csv('Data_new.csv', index=False)

print("Dữ liệu đã được lọc và lưu vào file Data_new.csv")
