import collect.crawler
import analyze
import visualize


if __name__=='__main__':
    items = [
        {'district1':'부산광역시','year':2012,'month':'1'},

    ]

    collect.crawler.crawling(district1='부산광역시',start_year=2012,end_year=2012)
    #데이터 수집 (collection)
    '''
    for item in items:
        collect.crawler.crawling(**item)
    '''


    #데이터 분석(analyze)


    #데이터 시각화(visualize)

print('run analysis_fb...')

