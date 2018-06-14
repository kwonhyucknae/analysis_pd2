import analysis_pd.collect.api.api as pdapi
import analysis_pd.collect.api.web_request as ttt

'''
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
queryParams = '?' + urlencode({ quote_plus('serviceKey') : 'TcT8vNWNinn6x5x7xrHsIv31tV5ls12XFGRfo5kByPx1RLH7GV3Y3Dj970BzXFALNPHcKsw3Qq0yHkDUdebQ4w%3D%3D', quote_plus('YM') : '201201', quote_plus('SIDO') : '부산광역시', quote_plus('GUNGU') : '해운대구', quote_plus('RES_NM') : '부산시립미술관' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
'''
'''
#url 어떻게 만드는지 테스트

url = pdapi.pd_gen_url(
'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='부산광역시',
    GUNGU='해운대구',
    RES_NM='부산시립미술관',
    numOfRows=10,
    _type='json',
    pageNo=1
)

print(url)
'''
for items in pdapi.pd_fetch_tourspot_visitor(district1='부산광역시', year=2012, month=1):
    print(items)



#tesst=ttt.html_request(url='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList')
#print(tesst)

#for items in pdapi.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
    #print(items)


