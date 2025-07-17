import pandas as pd

# 示例数据
l3tag = pd.DataFrame({
    'addr': [49, 51, 200, 300, 400]
})

malloc = pd.DataFrame({
    'addr': [50, 150, 250, 350],
    'size': [100, 100, 100, 100],
    'structType': ['A', 'B', 'C', 'D']
})

# 计算 malloc 的结束地址
malloc['end_addr'] = malloc['addr'] + malloc['size']

# 排序（merge_asof 要求右表按 key 排序）
malloc_sorted = malloc.sort_values('addr')

# 使用 merge_asof 找到 addr 小于等于 l3tag.addr 的最后一行
merged = pd.merge_asof(
    l3tag.sort_values('addr'),
    malloc_sorted[['addr', 'end_addr', 'structType']],
    on='addr',
    direction='backward'
)

# 过滤掉不在区间内的匹配
merged['structType'] = merged.apply(
    lambda row: row['structType'] if row['addr'] < row['end_addr'] else None,
    axis=1
)

# 清理列
result = merged[['addr', 'structType']]

print(result)
