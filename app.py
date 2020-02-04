from wxpy import *
# from pypinyin import*
# import random

# 导入消息撤回模块
from xml.etree import ElementTree

# 创建成语成语接龙词典
# idiom = {}
# all = []
# with open("all.txt","r",encoding="utf=8") as f:
#     for each in f:
#         idiom_first = lazy_pinyin(each[1:5])[0]
#         if idiom_first not in idiom:
#             idiom[idiom_first] = [each[1:5]]
#         else:
#             idiom[idiom_first].append(each[1:5])
#         all.append(each[1:5])

# with open("idiom.txt","w",encoding="utf=8") as f:
#     for each in idiom:
#         f.write(each)

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
print("机器人已启动")

# 定义一个全局变量存储卡片的原始数据
# mp_card = None

# 设置公众号名片
# @bot.register(bot.file_helper, CARD,except_self=False)
# def get_card(msg):
#     print("公众号名片",msg)
#     global mp_card
#     mp_card = msg

# 回复成语接龙消息
# group_select = bot.groups().search("怕死第一名")[0]
# @bot.register([group_select], TEXT)
# def auto_accept_groups(msg):
#     print("获取到好友消息", msg.text)
#     idiom_last = lazy_pinyin(msg.text)[len(msg.text) - 1]
#     answer = random.choice(idiom[idiom_last])
#     msg.chat.send(answer)

    # if msg.text in all:
    #     idiom_last = lazy_pinyin(msg.text)[len(msg.text)-1]
    #     answer = random.choice(idiom[idiom_last])
    #     msg.chat.send(answer)
    # else:
    #     msg.chat.send("你说的不是成语噢，换一个哼")

# 设置好友消息自动回复
# @bot.register(Friend, TEXT)
# def auto_accept_friends(msg):
#     print("获取到好友消息",msg.text)
#     if msg.text == "在吗":
#         msg.chat.send("在的")
#     elif msg.text == "微信群":
#         msg.chat.send("邀请加入某个群")
#         group_select = bot.groups().search("养猪场")[0]
#         group_select.add_members(users=msg.chat,use_invitation=True)
#     elif msg.text == "图片":
#         msg.chat.send("发送图片")
#         msg.chat.send("@img@F:/github/Wechat_auto/app.jpg")
#     elif msg.text == "公众号":
#         msg.chat.send("发送公众号名片")
#         mp_card.forward(msg.chat)

# 获取简单的好友统计
# friends_total = bot.friends().stats_text()
# print(friends_total)

# 获取微信好友总数
# wx_friends = bot.friends()
# print("获取到的微信好友数据为",len(wx_friends),wx_friends[1])
# friend_now = wx_friends[1]
# print("名称name",friend_now.name)
# print("头像",friend_now.get_avatar())
# print("性别sex(1为男性,2为女性)",friend_now.sex)
# print("地区:省份城市",friend_now.province,friend_now.city)
# print("个性签名",friend_now.signature)

# 获取微信群总数
# wx_groups = bot.groups()
# print("获取到的微信群数据为",len(wx_groups))
#
# # 获取微信群总数
# wx_mps = bot.mps()
# print("获取到的公众号数据为",len(wx_mps))

# 好友消息防撤回
@bot.register(Friend, NOTE,except_self=False)
def get_revoked(msg):
    print("获取到好友消息",msg)

    # 检查 NOTE 是否包含撤回信息
    revoked = ElementTree.fromstring(msg.raw['Content']).find("revokemsg")
    print(revoked)
    if revoked:
        # 获取原消息
        revoked_msg = bot.messages.search(id=int(revoked.find("msgid").text))[0]
        # 获取原发送者(群聊时为成员)
        sender = msg.member or msg.sender
        revoked_msg.forward(bot.file_helper,prefix=f"{sender.name}撤回了:")

# 仅仅堵塞线程
bot.join()