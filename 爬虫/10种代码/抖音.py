def get_json(url):
  headers = {
    'User-Agent':
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
  }

  params = {
    'page_size': 10,
    'next_offset': str(num),
    'tag': '今日热门',
    'platform': 'pc'
  }

  try:
    html = requests.get(url, params=params, headers=headers)
    return html.json()

  except BaseException:
    print('request error')
    pass

def download(url,path):
  start = time.time() # 开始时间
  size = 0
  headers = {
    'User-Agent': 
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
  }

  response = requests.get(url,headers=headers,stream=True) 
  chunk_size = 1024 
  content_size = int(response.headers['content-length']) 
  if response.status_code == 200:
    with open(path,'wb') as file:
      for data in response.iter_content(chunk_size=chunk_size):
        file.write(data)
        size += len(data)