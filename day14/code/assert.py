# assert.py

# 获取学生成绩
def get_score():
    s = int(input("请输入学生成绩: "))
    assert 0 <= s <= 100, '成绩超出范围'
    return s

try:
    score = get_score()
    print("成绩是:", score)
except AssertionError as err:
    print("断言失败!, err=", err)

