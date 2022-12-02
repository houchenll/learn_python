import opencc

converter = opencc.OpenCC('t2s.json')
# converter = opencc.OpenCC('mix2s.json')
result = converter.convert('謗書未及明君爇，戛玉摐金永頌聲，有飶嘉豆，后歌有蟜，雲軿戾止，灑霧飄煙。')
print(result)
