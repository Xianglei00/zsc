# @author xl
# @create 2022/4/5 13:35
# @program: com.xl.hlsvideo
# @E-Mail: 2199396150@qq.com
import os
path = r"D:\pycharm_work\com.xl.hlsvideo\static\pdf"
listdir = os.listdir(path)
for i in listdir:
    os_path_join = os.path.join(path, i)
    try:
        os_listdir = os.listdir(os_path_join)
        for j in os_listdir:
            print(j)
    except Exception as e:
        print(e)