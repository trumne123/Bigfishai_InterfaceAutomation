import pymysql


def connect_mysql():
    connection = pymysql.connect(host='127.0.0.1', user='root', password='mnbv0987', database='dubbingshow_data')
    return connection


# 查询数据
def query_data(sql):
    conn = connect_mysql()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        results = cur.fetchall()
        # for row in results:
        #     print(row)
        #     id = row[0]
        #     name = row[1]
        #     age = row[2]
        #     print('id: ' + str(id) + '  name: ' + name + '  age: ' + str(age))
        #     pass
        return results
    except Exception as e:
        print('查询失败', e)
    finally:
        cur.close()
        conn.close()


# 插入数据
def insert_data(sql):
    conn = connect_mysql()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        print('插入成功')
    except Exception as e:
        conn.rollback()
        print('插入失败', e)
    finally:
        cur.close()
        conn.close()


# 修改数据
def update_data(sql):
    conn = connect_mysql()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        print('修改成功')
    except Exception as e:
        conn.rollback()
        print('修改失败', e)
    finally:
        cur.close()
        conn.close()


# 删除数据
def delete_data(sql):
    conn = connect_mysql()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        print('删除成功')
    except Exception as e:
        print('删除失败', e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    qu_sql = 'select value from linked_data where title = "user_dubbing_id"'
    qu_data = query_data(qu_sql)[0][0]
    print(qu_data)
    # jj = 0
    # for i in qu_data:
    #     print(type(i[1]))
