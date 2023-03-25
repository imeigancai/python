import webbrowser
Api_Url = 'https://jx.aidouer.net/?url='
movie_url = input('请输入VIP电影或者电视链接:')
start_url = Api_Url + movie_url
webbrowser.open(start_url)
