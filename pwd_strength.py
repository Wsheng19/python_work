"""
    功能：判断密码强度
          保存密码及强度到文件中
          定义一个password的类
          定义一个文件工具类
"""


class PasswordTool:
    """
        密码工具箱
    """
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    # 类的方法
    def is_number_exist(self):
        """
            判断字符串是否含有数字
        """
        for x in self.password:
            if x.isnumeric():
                return True
        return False

    def is_letter_exist(self):
        """
            判断字符串是否含有字母
        """
        for x in self.password:
            if x.isalpha():
                return True
        return False

    def strength_pwd(self):
        if self.strength_level == 1:
            return '弱'
        elif self.strength_level == 2:
            return '中'
        elif self.strength_level == 3:
            return '强'

    def process_word(self):
        # 规则一：长度是否大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码要求至少8位！')
        # 规则二：包含数字
        if self.is_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')
        # 规则三：包含字母
        if self.is_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')
        self.strength_level = self.strength_pwd()


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, str):
        f = open(self.filepath, 'a')
        f.write(str)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """
    # 实例化文件工具对象
    file_tool = FileTool('password.txt')
    try_times = 5
    while try_times > 0:
        password = input('请输入密码：')

        # 实例化对象
        password_tool = PasswordTool(password)
        password_tool.process_word()

        # 保存密码
        line = '密码是：{}，其强度为：{}\n'.format(password, password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == '强':
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1
        print()

    if try_times == 0:
        print('尝试次数过多！密码设置失败！')

    # 读取文件
    lines = file_tool.read_from_file()
    for line in lines:
        print(line)
    # f = open('password.txt', 'r')
    # # 1. read() 把整个内容读取为一个字符串
    # # content = f.read()
    # # 2.readline() 每次只读一行
    # # line = f.readline()
    # # 3.readlines() 返回值为整个文件内容值的列表
    # for line in f.readlines():                          # 直接 for line in f: 也行
    #     print('read：{}'.format(line))
    # f.close()


if __name__ == '__main__':
    main()
