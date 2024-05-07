# @author xl
# @create 2022/3/30 20:53
# @program: com.xl.hlsvideo
# @E-Mail: 2199396150@qq.com
import json

import pymysql


class get_data(object):
    def __init__(self):
        super()
        self.cursor = self.get_cursor()

    def get_cursor(self):
        connect = pymysql.connect(user="root", password="Abc123..", host="120.76.99.114", port=3306, database="hls")
        self.cursor = connect.cursor(pymysql.cursors.SSDictCursor)
        return connect.cursor(pymysql.cursors.SSDictCursor)

    def get_name(self, id, obj):
        """
        :return: 返回video名称
        """
        if obj in ['computer', 'english', 'math']:
            sql = f"select id from {obj} where id={id}"
            self.cursor.execute(sql)
            obj_name = self.cursor.fetchone()
            return obj_name
        else:
            return None

    def get_all_name(self, obj):
        name_json_list = []
        if obj in ['computer', 'english', 'math']:
            sql = f"select * from {obj}"
            self.cursor.execute(sql)
            obj_name = self.cursor.fetchall()
            for i in obj_name:
                id = i.get("id")
                getname = i.get("name")
                name_json_list.append({"id": f'{id}',
                                       "name": f'{getname.replace("（", "(").replace("）", ")").replace(" ", "").strip(".mp4")}'})
        return name_json_list

    def close(self):
        if self.cursor is not None:
            self.cursor.close()


def get_jsons():
    with open('./Appconfig/nameandurl.json', 'r', encoding='utf-8') as f:
        return json.load(f)


class GetData:
    def __init__(self):
        self.json_datas = get_jsons()

    # 英语 0 - 41
    # 计算机 41 - 66
    # 数学   66 - len
    def get_name(self, id, obj):
        if obj in ['english']:
            if id > 41:
                return None
            return self.json_datas[id].get("name")
        if obj in ['computer']:
            if id > 25:
                return None
            return self.json_datas[id + 42].get("name")
        if obj in ['math']:
            if id > 34:
                return None
            return self.json_datas[id + 67].get("name")

    def get_names(self, obj):
        if obj in ['english']:
            return [
                {'id': id,
                 'name': f'{(self.json_datas[id].get("name"))}'
                 .replace("（", "(")
                 .replace("）", ")")
                 .replace(" ", ""),
                 'url': f'{(self.json_datas[id].get("url"))}'
                 }
                for id in range(len(self.json_datas[0:42]))
            ]
        if obj in ['computer']:
            return [
                {'id': id,
                 "name": f'{(self.json_datas[id + 42].get("name"))}'
                 .replace("（", "(")
                 .replace("）", ")")
                 .replace(" ", ""),
                 'url': f'{(self.json_datas[id + 42].get("url"))}'
                 }
                for id in range(len(self.json_datas[42:67]))
            ]
        if obj in ['math']:
            return [
                {'id': id,
                 "name": f'{(self.json_datas[id + 67].get("name"))}'
                 .replace("（", "(")
                 .replace("）", ")")
                 .replace(" ", ""),
                 'url': f'{(self.json_datas[id + 67].get("url"))}'
                 }
                for id in range(len(self.json_datas[68:len(self.json_datas)]) + 1)
            ]
        else:
            return None

    def get_url(self, id, obj):
        if obj == 'computer':
            if id > 25:
                return None
            return self.json_datas[id + 42].get("url")
        if obj == 'math':
            if id > 34:
                return None
            return self.json_datas[id + 67].get("url")
        if obj == 'english':
            if id > 41:
                return None
            return self.json_datas[id].get("url")


if __name__ == '__main__':
    obj = GetData()
    print(obj.json_datas)
    print(obj.get_name(0, 'english'))
    print(obj.get_name(40, 'english'))

    print(obj.get_name(0, 'computer'))
    print(obj.get_name(24, 'computer'))

    print(obj.get_name(0, 'math'))
    print(obj.get_name(34, 'math'))
    print(obj.get_names('english'))
    print(obj.get_names('computer'))
    print(obj.get_names('math'))
    print(len(obj.get_names('math')))
    # g = get_data()
    # print(g.get_name("1", "math"))
    # print(g.get_all_name("math"))
    # g.close()
