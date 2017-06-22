#### Xiang Wang @ 2017-06-16 14:58:59


# 上传文件
```
    from qiniu import put_file, Auth
    access_key = 'Zy3HE44UK9tRACuAeEL3mxc8aTTj0jgZkrjxrJAB'
    secret_key = 'wLXODkNWpzFj_SI60zu5GjjOVZzxmvlNJ0tLOR3K'
    q = Auth(access_key, secret_key)
    bucket_name = 'sharegine-public-test'
    key = 'avatar-user-0.png'
    token = q.upload_token(bucket_name, key, 3600, policy={
        # 'bucket': 'sharegine-public-test',
        # 'key': 'avatar-user-0.png',
        'insertOnly': 0,
    })
    ret, into = put_file(token, key, './portrait.png')
    # ret, into = put_file(token, key, './android.png')
```
