import os,sys
from Novel_Cleaner import Clean as R_name


def make_choice():
	num = input('选择你的操作：')
	if num == '1':
		print('启动小说入库程序')
		return R_name(os.path)
	elif num == '2':
		print('显示库存情况')
	elif num == '3':
		print('数据库初始化完成')
	else:
		print('指令错误\n请重新选择')
		return make_choice()


if __name__ == '__main__':
	print('本地书库管理系统已经启动\n使用说明：\n  1.小说入库清洗\n  2.查看库存情况\n  3.建立本地数据库（已有数据库不会响应）\n回车确认')
	make_choice()
