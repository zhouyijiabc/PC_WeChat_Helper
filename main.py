import uiautomation as uia


wechat_window = uia.WindowControl(searchDepth=1, Name='微信', ClassName='WechatMainWndForPC')
# print(dir(wechat_window))

msgs = wechat_window.ListItemControl(Name='消息')
for msg in msgs.GetChildren():
    content = msg.Name

    print(content)
# uia.ButtonControl(searchDepth=9, Name='进入微信').Click()

# for msg in msgs.Get
