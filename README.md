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

## 依赖

无需额外安装第三方库，仅使用 Python 标准库（`datetime`）。