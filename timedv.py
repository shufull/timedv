#####
# usage
# python timedv.py {filename} {H:M}
#
# {filename}
# hh:mm形式のタイムのみが羅列されたcsvファイルのfilepath
#
# {H:M}
# 偏差値が知りたいタイム
#####
import sys
import csv
import datetime
from statistics import stdev
from statistics import mean

CSV_FILE = sys.argv[1]
VALUE = sys.argv[2]

populations = [] # 母集団
adv = 0 # 平均値
ev = 0 # 標準偏差

def enc_sec(time_str):
	dt = datetime.datetime.strptime(time_str, "%H:%M")
	return datetime.timedelta(hours=dt.hour, minutes=dt.minute).total_seconds()

def dec_sec(sec):
	return datetime.timedelta(seconds=sec)

def calc_dv(score):
	return 50 - ( (score - adv) * 10 / ev )

# 母集団を分で取得
with open(CSV_FILE) as f:
	reader = csv.reader(f)
	for r in reader:
		# タイムを分にして保存
		populations.append(enc_sec(r[0]))

# 平均値と標準偏差を導く
adv = mean(populations)
ev = stdev(populations)

# 指定値の偏差値を求める
print(round(calc_dv(enc_sec(VALUE)), 1))