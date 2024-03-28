# [imapclient](https://github.com/mjs/imapclient)
邮件客户端
* 搜索邮件
```
client = IMAPClient(host="imap.qq.com")
password = input("输入密码")
client.login("ramwin@qq.com", password)
message_ids = client.search(
  [u'SINCE', date(2021, 4, 8)],
)
>>> [393]
```

* 获取邮件
```
message_id = 393
content = client.fetch(message_id, ['FLAGS', 'RFC822'])[393][b'RFC822']
```

* 解析邮件
```
import mailparser
mail = mailparser.parse_from_bytes(content)
print(mail.headers['Subject'])
print(mail.body)
```

* 设置已读
```
client.set_flags(messages, imapclient.SEEN)
```
