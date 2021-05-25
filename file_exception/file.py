from math import sqrt
import json
import requests

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    #f = None
    fileName = 'C:\\Users\\PopMain\\source\\repos\\Python100Day\\Python100Day\\Python100Day\\file_exception\\TextFile.txt'
    try:
       # f = open('C:\\Users\\PopMain\\source\\repos\\Python100Day\\Python100Day\\Python100Day\\file_exception\\TextFile.txt','r', encoding='utf-8')
       # print(f.read)
       with open(fileName, 'r', encoding='utf-8') as f:
           print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时节码错误')
    #finally:
        # if f:
        #    f.close
    fileNames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for name in fileNames:
            fs_list.append(open(name, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if (is_prime(number)):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('写入操作完成!')
    try:
        with open('image.jpg', 'rb') as image: 
            data = image.read()
            print(type(data))
        with open('image_copy.jpg','wb') as image_copy:
            image_copy.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('图片复制完成')

    mydict = {
         'name':'Eric',
         'age': 28,
         'qq':12345678,
         'friends':['Jesen','Mario'],
         'cars':[
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
             ]
        }
    try:
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(mydict,json_file)
            print(json.dumps(mydict))
    except IOError as e:
        print(e)
    print('数据保存完成')

    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    deta_model = json.loads(resp.text)
    print(deta_model)
       

if __name__ == '__main__':
    main()
