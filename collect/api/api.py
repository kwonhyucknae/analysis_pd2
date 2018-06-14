#FaceBook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request


SERVICE_KEY="TcT8vNWNinn6x5x7xrHsIv31tV5ls12XFGRfo5kByPx1RLH7GV3Y3Dj970BzXFALNPHcKsw3Qq0yHkDUdebQ4w%3D%3D"
BASE_URL_FB_API= "https://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"


# params dictionary 형태로 들어온다
#params{"since":20173221, "until":2018dwqdwq}




def pd_gen_travel_url(endpoint,**params):
    url='%s?%s' % (endpoint,urlencode(params))
    return url






## 여기는 유료 관광지 정보
def pd_gen_url(endpoint,**params):
    url='%s?%s'%(endpoint,urlencode(params))
    return url+"&serviceKey="+SERVICE_KEY
    #json_result=json_request(url=url)
    #return json_result.get("csForCnt")

    #for i in range(0,len(params)):
    #    print(params[i])

def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
    url=pd_gen_url(
        'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
        YM='{0:04d}{1:02d}'.format(year, month),
        SIDO=district1,
        GUNGU=district2,
        RES_NM=tourspot,
        numOfRows=10,
        _type='json',
        pageNo=1
         )
    #print(url)
    isnext=True

    json_result = json_request(url=url)
    print("json_result=", json_result)
    response = None if json_result is None else json_result.get('response')
    print("paging=", response)
    body = None if response is None else response.get('body')
    items = None if body is None else body.get('items')


    try:

        item=None if items is None else items.get('item')
        yield item
    except AttributeError:
        pass

    #print(type(item))
    #print("item==",item)
    #print("item 길이 ",len(item))

    csForCnt=0
    #return item


    '''
    for i in range(0,len(item)-1):
        k=item[i].get('csForCnt')
        csForCnt+=k

    
    print(csForCnt)
    '''






'''

def fb_gen_url(base=BASE_URL_FB_API,
               node='',
               **params):
    url='%s/%s/?%s' % (base,node,urlencode(params))
    return url


def fb_name_to_id(pagename):
    url=fb_gen_url(node=pagename,access_token=ACCESS_TOKEN)

    json_result=json_request(url=url)
    return json_result.get("id")



def fb_fetch_posts(pagename,since,until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN
    )

    print("url======"+url)

    #빈 리스트 생성
    results = []

    isnext=True
    while isnext is True:
        json_result = json_request(url=url)

        #삼항연산자로 적으면 이렇게
        paging = None if json_result is None else json_result.get('paging')
        posts=None if json_result is None else json_result.get('data')
    #리스트를 더해준다

        results+=posts

        #탈출 조건 생성
        url =None if paging is None else paging.get("next")

        isnext = url is not None

    return results



'''