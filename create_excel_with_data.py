"""
Skill: Create Excel with Data
Description: Generates an Excel (.xlsx) file containing a configurable number of rows
             (default: 100) of sample data (ID, name, age, email, department, salary)
             and returns metadata about the created file.
"""

import os
from datetime import date, timedelta

import openpyxl
from openpyxl.styles import Font, PatternFill


# ---------------------------------------------------------------------------
# Sample data helpers
# ---------------------------------------------------------------------------

_DEPARTMENTS = ["研发部", "市场部", "财务部", "人事部", "运营部"]
_FIRST_NAMES = ["伟", "芳", "娜", "秀英", "敏", "静", "丽", "强", "磊", "军"]
_LAST_NAMES = ["王", "李", "张", "刘", "陈", "杨", "黄", "赵", "周", "吴"]

_MIN_AGE = 22
_MAX_AGE = 59
_AGE_RANGE = _MAX_AGE - _MIN_AGE + 1   # 38 possible values: 22 ~ 59

_MIN_SALARY = 8_000
_SALARY_STEP = 1_000
_SALARY_STEPS = 20                       # salary range: 8000 ~ 27000


def _make_row(index: int) -> tuple:
    """Return one row of deterministic sample data for the given 1-based index."""
    last = _LAST_NAMES[(index - 1) % len(_LAST_NAMES)]
    first = _FIRST_NAMES[(index - 1) % len(_FIRST_NAMES)]
    name = last + first
    age = _MIN_AGE + (index % _AGE_RANGE)
    email = f"user{index:03d}@example.com"
    dept = _DEPARTMENTS[(index - 1) % len(_DEPARTMENTS)]
    salary = _MIN_SALARY + (index % _SALARY_STEPS) * _SALARY_STEP
    entry_date = (date(2020, 1, 1) + timedelta(days=index * 7)).isoformat()
    return (index, name, age, email, dept, salary, entry_date)


# ---------------------------------------------------------------------------
# Public skill function
# ---------------------------------------------------------------------------

def create_excel_with_data(
    filepath: str = "sample_data.xlsx",
    row_count: int = 100,
) -> dict:
    """
    Create an Excel file containing *row_count* rows of sample employee data.

    Args:
        filepath (str): Destination file path.  Defaults to ``sample_data.xlsx``
                        in the current working directory.
        row_count (int): Number of data rows to generate (default 100).

    Returns:
        dict: A dictionary containing:
            - filepath (str): Absolute path of the created file.
            - row_count (int): Number of data rows written.
            - sheet_name (str): Name of the worksheet.
            - columns (list[str]): Column headers.
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "员工数据"

    # --- header row ---
    headers = ["ID", "姓名", "年龄", "邮箱", "部门", "薪资(元)", "入职日期"]
    header_fill = PatternFill(fill_type="solid", fgColor="4472C4")
    header_font = Font(bold=True, color="FFFFFF")

    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font

    # --- data rows ---
    for row_idx in range(1, row_count + 1):
        for col_idx, value in enumerate(_make_row(row_idx), start=1):
            ws.cell(row=row_idx + 1, column=col_idx, value=value)

    # --- column widths ---
    column_widths = [6, 10, 6, 26, 10, 12, 12]
    for col_idx, width in enumerate(column_widths, start=1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = width

    wb.save(filepath)
    abs_path = os.path.abspath(filepath)

    return {
        "filepath": abs_path,
        "row_count": row_count,
        "sheet_name": ws.title,
        "columns": headers,
    }


if __name__ == "__main__":
    result = create_excel_with_data()
    print(f"文件已创建  : {result['filepath']}")
    print(f"数据行数    : {result['row_count']}")
    print(f"工作表名称  : {result['sheet_name']}")
    print(f"列标题      : {', '.join(result['columns'])}")
