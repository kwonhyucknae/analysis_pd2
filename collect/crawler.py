import os
import json
from datetime import datetime,timedelta
import analysis_pd.collect.api.api as pdapi


RESULT_DIRECTORY='__result__/crawling'


#전처리 과정

def preprocess_post(items):
    #공유수
    if 'csNatCnt' in items:
        #빠져 있다면 0
        items['count_locals']=items.pop('csNatCnt')
    if 'csForCnt' in items:
        items['count_forigner']=items.pop('csForCnt')
    if 'resNm' in items:
        items['tourist_spot']=items.pop('resNm')
    if 'ym' in items:
        items['date']=items.pop('ym')
    if 'sido' in items:
        items['restrict1']=items.pop('sido')
    if 'gungu' in items:
        items['restrict2']=items.pop('gungu')
    if 'addrCd' in items:
        items.pop('addrCd')
    if 'rnum' in items:
        items.pop('rnum')

def crawling(district1,start_year,end_year):

    results=[]
    print("results type",results)
    filename='%s/%s_%s_%s.json' %(RESULT_DIRECTORY,district1,start_year,end_year)

    #for posts in api.pd_fetch_tourspot_visitor(district1, year, month):
    #    for post in posts:
    #        preprocess_post(post)


    for j in range(start_year,end_year):
        #print(j)
        for i in range(1,3):
            #print(i)
            for items in pdapi.pd_fetch_tourspot_visitor(district1, year=j, month=i):
                print("items===",type(items),items)
                if type(items) is dict:
                    items=[items]
                #print(type(items['addrCd']))
                for item in items:
                    print("item========!!!!",item)
                    print()
                    preprocess_post(item)
                results+=items
                print("type results",type(results),results)
                #print("tmp의type=====",type(tmp),tmp)# 이건 딕셔
                #print("result의type=====",type(results), results)#이건 리스트 인데 , 여기다 딕셔를 넣음 , 키값만 보임


            #print(results)

    print("results====",results)



    #   results += posts

    #save results to file (저장, 적재)

    with open(filename,'w',encoding='utf-8') as outfile:
        json_string=json.dumps(results,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(json_string)
        #with as 구문은 close가 자동으로 된다


if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
