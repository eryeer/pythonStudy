# 记录所有的名片字典
card_list = []


def show_menu():
    """show menu"""
    print("*" * 50)
    print("欢迎使用名片管理系统 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """new card"""
    print("-" * 50)
    print("新增名片")
    name_str = input("請輸入姓名：")
    phone_str = input("請輸入電話：")
    qq_str = input("請輸入QQ")
    email_str = input("請輸入郵箱：")

    card_dic = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}
    card_list.append(card_dic)
    print("名片 %s 添加成功" % name_str)


def show_all():
    """show all cards"""
    print("-" * 50)
    if len(card_list) != 0:
        for name in ["姓名", "電話", "QQ", "email"]:
            print(name, end="\t\t")
        print("")
        print("=" * 50)
    else:
        print("沒有卡片記錄")
        return
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                        card["phone"],
                                        card["qq"],
                                        card["email"]))


def search_card():
    """ search card"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("請輸入要搜索的姓名:")
    for card_dic in card_list:
        if find_name == card_dic["name"]:
            for name in ["姓名", "電話", "QQ", "email"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"],
                                            card_dic["phone"],
                                            card_dic["qq"],
                                            card_dic["email"]))
            deal_card(card_dic)
            break
    else:
        print("抱歉沒有找到 %s" % find_name)


def deal_card(find_dict):
    """

    :param find_dict:
    """
    print(find_dict)
    action_str = input("请选择需要的操作 "
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "name:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "phone:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq:")
        find_dict["email"] = input_card_info(find_dict["email"], "email:")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")


def input_card_info(dic_value, tip_message):
    """

    :param dic_value:
    :param tip_message:
    :return:
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        dic_value
