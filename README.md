# agent-skills

一组可复用的 Python 技能（Skills）集合。

---

## 技能列表

### 📅 查看当前时间戳（get_current_timestamp）

**文件：** `get_current_timestamp.py`

**描述：** 获取当前日期和时间，以 Unix 时间戳和格式化字符串的形式返回。

#### 使用方法

```python
from get_current_timestamp import get_current_timestamp

result = get_current_timestamp()
print(result["unix_timestamp"])  # 例：1772783200.49（Unix 时间戳，秒）
print(result["iso8601"])         # 例：2026-03-06T07:46:40Z（UTC，ISO 8601 格式）
print(result["formatted"])       # 例：2026-03-06 07:46:40（本地时间）
```

#### 返回值说明

| 字段名           | 类型    | 说明                                  |
|------------------|---------|---------------------------------------|
| `unix_timestamp` | `float` | Unix 时间戳（自 1970-01-01 起的秒数） |
| `iso8601`        | `str`   | UTC 时间，格式：`YYYY-MM-DDTHH:MM:SSZ` |
| `formatted`      | `str`   | 本地时间，格式：`YYYY-MM-DD HH:MM:SS` |

#### 直接运行

```bash
python get_current_timestamp.py
```

输出示例：

```
Unix Timestamp : 1772783200.494775
ISO 8601 (UTC) : 2026-03-06T07:46:40Z
Formatted      : 2026-03-06 07:46:40
```

#### 运行测试

```bash
pytest test_get_current_timestamp.py -v
```

---

### 📊 生成 Excel 数据文件（create_excel_with_data）

**文件：** `create_excel_with_data.py`

**描述：** 生成一个包含 100 条（可自定义）示例员工数据的 Excel（.xlsx）文件，并返回文件的元数据。

#### 安装依赖

```bash
pip install openpyxl
```

#### 使用方法

```python
from create_excel_with_data import create_excel_with_data

# 使用默认参数：生成 100 行，保存为 sample_data.xlsx
result = create_excel_with_data()

# 自定义文件路径和行数
result = create_excel_with_data(filepath="my_data.xlsx", row_count=200)

print(result["filepath"])    # 例：/home/user/sample_data.xlsx
print(result["row_count"])   # 例：100
print(result["sheet_name"])  # 例：员工数据
print(result["columns"])     # 例：['ID', '姓名', '年龄', '邮箱', '部门', '薪资(元)', '入职日期']
```

#### 返回值说明

| 字段名       | 类型        | 说明                      |
|--------------|-------------|---------------------------|
| `filepath`   | `str`       | 已创建文件的绝对路径       |
| `row_count`  | `int`       | 写入的数据行数             |
| `sheet_name` | `str`       | 工作表名称（`员工数据`）   |
| `columns`    | `list[str]` | 列标题列表                 |

#### Excel 列结构

| 列名      | 内容说明                        |
|-----------|---------------------------------|
| ID        | 行序号（1 ~ row_count）          |
| 姓名      | 示例中文姓名                    |
| 年龄      | 22 ~ 59 之间                    |
| 邮箱      | `userNNN@example.com`           |
| 部门      | 研发部 / 市场部 / 财务部 / 人事部 / 运营部 |
| 薪资(元)  | 8000 ~ 27000 之间               |
| 入职日期  | ISO 格式日期字符串               |

#### 直接运行

```bash
python create_excel_with_data.py
```

输出示例：

```
文件已创建  : /home/user/sample_data.xlsx
数据行数    : 100
工作表名称  : 员工数据
列标题      : ID, 姓名, 年龄, 邮箱, 部门, 薪资(元), 入职日期
```

#### 运行测试

```bash
pytest test_create_excel_with_data.py -v
```

---

## 依赖

| 技能                    | 依赖                  |
|-------------------------|-----------------------|
| `get_current_timestamp` | 无（Python 标准库）   |
| `create_excel_with_data`| `openpyxl >= 3.0`     |