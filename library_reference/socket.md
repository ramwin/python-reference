**Xiang Wang @ 2020-03-27 14:51:44**


# Example
* 第一个例子，把所有的数据都echo出来  
`./socket/socket_serverserver.py` `./socket/socket_client.py`
* socket监听时绑定了宿IP和宿端口。当用户访问这个地址时，也会发送自己的源IP和源端口
* 一个新的请求过来时，会创建一个新的socket封装这些信息。所以每个socket都不一样，系统根据源IP，源端口，宿IP，宿端口来判断这个数据应该交给谁处理  
比如我在服务器上绑定了`ramwin.com:50008`, 然后本地去请求时。

# 本地和服务器交互(多了一层运营商，所以不好看)
* 示例
```
    本地的socket信息: 本地IP 192.168.10.128:42536(动态生成的端口) 链接到了服务器47.100.203.184:50008
    <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.10.128', 42536), raddr=('47.100.203.184', 50008)>
    服务器的socket信息: 116.226.45.62:42536(本地的运营商IP地址) 链接到了服务器的172.19.162.85:50008(服务器内部IP)
    <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.19.162.85', 50008), raddr=('116.226.45.62', 42536)>
```

# 两台服务器交互
    ```
    本地的socket信息:  IP: 47.241.21.44, 私有IP: 172.21.50.108
    <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.21.50.108', 49702), raddr=('47.100.203.184', 50008)>
    接受方的socket信息:  IP: 47.100.203.184, 私有IP: 172.19.162.85
    <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.19.162.85', 50008), raddr=('47.241.21.44', 49702)>
    ```

# 多个socket线程来接听
[stackoverflow](https://stackoverflow.com/questions/10810249/python-socket-multiple-clients)
