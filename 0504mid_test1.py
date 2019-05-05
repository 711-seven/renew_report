# 读取 report.txt 文件中的成绩；
# 统计每名学生总成绩、计算平均并从高到低重新排名；
# 汇总每一科目的平均分和总平均分（见下表第一行）；
# 添加名次，替换60分以下的成绩为“不及格”；
# 将处理后的成绩另存为一个新文件。

with open('report.txt', encoding='utf-8') as f:
    report = f.readlines()

content = []
for line in report:
    line = line.strip()
    l = line.split(' ')
    content.append(l)

content[0].append('总分')
content[0].append('平均分')
for i in range(1, len(content)):
    con = content[i]
    con[1:] = [int(x) for x in con[1:]]
    summ = sum(con[1:])
    avg = round(summ/(len(con)-1), 1)
    con.append(summ)
    con.append(avg)

scores = sorted([x for x in content[1:]], key=lambda y: y[-1], reverse=True)
title = content[0]

ttl_avg = ['平均']

for i in range(1, len(title)):
    ttl = 0
    for score in scores:
        ttl += score[i]
        if score[i] < 60:
            score[i] = '不及格'
    ttl_avg.append(round(ttl/len(scores), 1))


title.insert(0, '名次')
ttl_avg.insert(0, 0)

rank = 0
for score in scores:
    rank += 1
    score.insert(0, rank)

new = []
new_report = []

new.append(title)
new.append(ttl_avg)

new += scores

for n in new:
    m = '  '.join([str(x) for x in n])
    m += '\n'
    new_report.append(m)

with open('new_report.txt', 'w', encoding='utf-8') as w:
    w.writelines(new_report)

print(new_report)



