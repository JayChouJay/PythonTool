import pdfplumber
import xlwt
import sys

# pdf_file_path = "D:\desktop\记录\金智维\测试\python脚本测试\python脚本测试.pdf"
# 传入路径
pdf_file_path = sys.argv[1]
# 输出路径
out_file = pdf_file_path.replace("pdf", 'xls')

# 打开指定PDF
pdf = pdfplumber.open(pdf_file_path)

# 创建一个输出的工作部
wk = xlwt.Workbook()
# 工作部的页面
sheet = wk.add_sheet("demo")

rowidx = 0

# 遍历pdf每一页
for page in pdf.pages:
    # 输出整个表内容
    # print(page.extract_tables())
    for table in page.extract_tables():
        for row in table:
            # 输出一整行
            print(row)
            for I in range(len(row)):
                cell = row[I]
                # 打印单个cell内容
                # print(cell)
                # 防止有换行符
                if cell is not None:
                    cell = cell.replace("\n", "")
                sheet.write(rowidx, I, cell)
            rowidx += 1
# 写入文件
wk.save(out_file)
print("执行成功")