import os
import json
from datetime import datetime,timedelta
from .api import api


RESULT_DIRECTORY='__result__/crawling'


#전처리 과정

def preprocess_post(post):
    #공유수
    if 'shares' not in post:
        #빠져 있다면 0
        post['count_shares']=0
    else:
        post['count_shares']=post['shares']['count']
    #전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions']=0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']
    #전체 코멘트 수
    if 'comments' not in post:
        post['count_comments']=0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']
    #시간대 변경
    # KST=UTC+9
    kst=datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    kst += timedelta(hours=9)
    post['created_time']=kst.strftime('%Y-%m-%d %H:%M:%S')



def crawling(district1,start_year,end_year):

    results=[]
    filename='%s/%s_%s_%s.json' %(RESULT_DIRECTORY,district1,start_year,end_year)

    #for posts in api.pd_fetch_tourspot_visitor(district1, year, month):
    #    for post in posts:
    #        preprocess_post(post)


    for i in range(1,13):
        for items in api.pd_fetch_tourspot_visitor(district1, start_year, i):
            results += items



    #   results += posts

    #save results to file (저장, 적재)

    with open(filename,'w',encoding='utf-8') as outfile:
        json_string=json.dumps(results,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(json_string)
        #with as 구문은 close가 자동으로 된다


if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
