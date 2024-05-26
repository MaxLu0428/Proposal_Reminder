import os
import pandas as pd
from .models import vDRM

def update_drm_from_csv(file_path):
    # 構建完整的文件路徑
    full_path = os.path.join(file_path)

    # 讀取CSV文件
    df = pd.read_csv(full_path)

    # 獲取CSV文件中的所有名稱
    csv_names = set(df['Name'])

    # 更新或創建DRM數據
    for index, row in df.iterrows():
        vDRM.objects.update_or_create(
            name=row['Name'],
            defaults={'Document_Number': row['Document_Number'], 'Description': row['Description']}
        )

    # 刪除不在CSV文件中的DRM數據
    DRM.objects.exclude(name__in=csv_names).delete()
