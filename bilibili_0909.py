import requests



def get_latest():
    url = 'http://space.bilibili.com/ajax/member/getSubmitVideos'
    data = {'mid': 891124,'tid':0,'pagesize':25}
    headers = {'Content-Type':'application/json;charset=utf-8'}
    data = requests.get(url=url, params=data, headers=headers)
    return data


def main():
    pass

if __name__ == "__main__":
    main()
