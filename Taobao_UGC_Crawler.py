import requests as rq
import re
import pandas as pd
import time
i=1
def nike_airforce():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('Nike耐克官方NIKE AIR FORCE 1.csv',mode='a',encoding='UTF-8')
        i=i+1


def stan_smith():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=526979860643&spuId=334863486&sellerId=446338500&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvWpvbvRpvUvCkvvvvvjiPPLzhgjlnPLz9sjYHPmPvAjrWP2dp0jtbP2LhQjYb9phv2nsGlD6hzYswzH0b7IwCvvpvCvvv2QhvCvvvMMGCvpvVvmvvvhCvmphvLv1QBvvjRixr6jZcnoYVK4mUkEp7EcqZaNpl%2B2IIwtxrQj7KHmx%2Fzj7y%2Bb8rwmz6QbmD5i31pG2y%2BnezrmphQRAn3feAOHbvTWexRduEvpv7vvvE9oHP9n7tdLJznlev0XcEKfpSp4yCvv9vvUmSeol4qdyCvm9vvvmWphvh%2Fpvv9BCvpvovvvmmvhCv2UvvvvbKphvWEvvv9BCvpvQyRphvCvvvvvm5vpvhvvmv9FyCvvpvvvvv&isg=Ao2N2J92635lEUy9CiX9fbdvnq8HasE8W4Tkjs8S2SSVxqx4l7utDKrURGZe&needFold=0&_ksTS=1511186015962_2500&callback=jsonp2501"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('adidas 阿迪达斯 三叶草 男女.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def langsha_nvneiku():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=40587386931&spuId=291009956&sellerId=272715291&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvNQvPvohvUvCkvvvvvjiPPLzhgjlWRsFy0jljPmP9zjEVnLS9sjEHR2Sp6j3vRphvChCvvvvtvpvhphvvvUhCvCwYMClaf%2FMwznQadlIu6kpum8e%2Fezrq8IwCvvBvppvviQhvChCvCCptvpvhphvvvvyCvh1mVpUvIsa9CB%2Buzj7xD7QHNZL9gCQ7nDyiLO2v5fh3ZkZH1R9t%2BFBCWDAvD40wjov0747BhC3%2BmB%2BuQj7J%2B3%2BSjLVxfXkOjoC1cXxrkphvHyCvovAQn0vxby7tSf%2BzOCODxG0DrsJivpvUphvhNJsfZTKtvpvIphvvXvvvpLYvpvAvvvCmFyCvHvvvvhnFphvpaQvvp6ivpvAvvvC2o9hCvvXvppvvvvvPvpvhvv2MMT6CvvDvp2GWw9CvxqoCvpvWzPsXcOfNznswcAx4dphvmZCCTvsLvhCNIp%3D%3D&isg=AhwcqzJ-qj0tL10Ok-oc3i4o7zzOlcC_UiMVHfYddofuQb3LHqTlTp8z1ZRE&needFold=0&_ksTS=1511186183239_2225&callback=jsonp2226"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('浪莎女士内裤.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def langsha_nanneiku():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=21485752370&spuId=213997165&sellerId=272715291&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvgQvRvp%2BvUvCkvvvvvjiPPLzhgjlRPFdv0jYHPmP9QjD8PLcUsjDbn2sWQj3W9phv2nsG1xMOzYswzvCy7u6CvvyvC2kmEmpvNHQCvpvVvmvvvhCvkphvH9vvmOh3Lg2xK46zrsaX9nexAfe6b6VivpvUvvmvdty9kwktvpvIvvvvFhCvCPyvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWEvyCvhQvTVOvCzbEKOmxdB9anuAQiNofecBv%2BneYiLUpwhKn3w0xhE3zLwex6aZtn0vHfwLpaXTAVAnl%2B8c6%2Bul1BccG1Wk4Vc3mgWLhzCOq2QhvCvvvMMGtvpvhvvvvv8wCvvpvvUmm3QhvCvvhvvmrvpvEvvpd93WLvhB6dphvmpvvxvnnLpCWT2yCvvpvvvvv&isg=AnZ2nSpXMNPj1cfYJShW4JCKxap4l7rRHMEvq-BfotnzIxe9SCZh4f4RT8Ox&needFold=0&_ksTS=1511186335624_2597&callback=jsonp2598"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('浪莎男士内裤.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def laganxiang_500():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=550092313553&spuId=849362093&sellerId=1714128138&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvuQvRvBhvUpCkvvvvvjiPPLzhgjlRnLLUljEUPmPW6jDEP2zU1jtPR2LwAjYRRghCvv147lSzGa147DiznaGtvpvhvvvvvUhCvCBkcm2zfB147DiDWYGD1TTqSEsk4gwCvvpvCvvviQhvCvvv9UUPvpvhvvvvvUyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCuphvmvvv98%2FXUMjpKphv8vvvvU1vpvLtvvmChhCvm2WvvUUvphvW9vvvvKtvpvQyvvmChhCv2mpEvpCWv84Tvvak6acEKBmAVA5vaNoxdBD68fknIOZtI2pwD7zh08TZfvDrAn1l5dUf8r1ldE7rVcvr%2BExrACkKNB3rAnClHqhIowyH64mAdphCvvOvCvvvphvtvpvhvvvvv86CvvyvCmeCYNZvwh6tvpvhvvvvvv%3D%3D&isg=AhoasbAbFAef2ZtEYeQytBweacY8S54lANXTVyST-a16l7vRDNqoNPAlE1_1&needFold=0&_ksTS=1511186406935_2595&callback=jsonp2596"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('拉杆箱499.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def laganxiang_500_1500():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=43385962395&spuId=245043562&sellerId=1708384427&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvHpvpvopvUpCkvvvvvjiPPLzhgjlEnLFOQj1VPmPvzjnCPFqwtjD8PscOzjDbPIhCvCLNt0aGdldNzY%2F3rS1fNY%2F6zYSw546Cvvyv9vhhfpvvjU%2FCvpvWz%2FalcjtwzYMNhnPwCQhvCYMNzn147uvEvpCWv3wHCBzveiy7RAYVyOvO5fVQWl4vAEyaRfU6pwethb8re169D70fdiZBEpJQD404digDN%2BCldf8re1lvI8p7%2Bu6OjomUTCh7%2Bulz8dyCvm9vvhCXvvmvPQvvp0WvvvHevvCHBpvv9BvvvhoXvvmC3vvvp0WvvUVhuphvmvvvpBt5q5iUkphvH9vvZDVHKBmTnqZKpa0th2KARLn4SfyCvpvVvUCvpvvv2QhvCvvvvvvtvpvhvvCvp8wCvvpvvhHhRphvCvvvphmjvpvhvUCvp2yCvvpvvhCvRphvCvvvphv%3D&isg=AgsLXtr81cBpqQp7WN8TUyXVmKn1oB8iia4iSH0It8qlnCr-BXHzcg_-AqCM&needFold=0&_ksTS=1511186510159_1460&callback=jsonp1461"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('拉杆箱788-988.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def laganxiang_dayu_1500():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=38501265452&spuId=269309557&sellerId=1969933424&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hv4vvPvBgvUvCkvvvvvjiPPLzhgjlURszytj3mPmPZ6j3nRFSwzjr2n2svtj38RphvCvvvvvmCvpvWzPAMcyFNznsw5Ga49phv2nsGnDzyqYswznl27uwCvvpvvUmmvphvC9vhvvCvpvyCvhQWSBwvCsXlibmxdX3tEPoxfwofde6UfJBl%2Bb8rwZXlYWFZe3WDN%2BLyafmAdcHhaNLtD40OaAuQD7zheTtYLYLZeE7rejyy%2BExr1EAKuphvmvvv98%2FXEU3dkphvH9vvmOh3Lg2xK46zrsaX9nexAfe6b6VtvpvIvvvvFhCvCPyvvUhpphvUWQvv99CvpvAvvvvmqyCv2mpvvUhpphvWEvGCvvpvvPMMRphvCvvvvvmjvpvhvvpvv2yCvvpvvvvvdphvhovUQpjq%2FQCypAeSImlmlf5Bdphvmpvhn9ERL9C6QQ%3D%3D&isg=Ajw8S4AKSt3yXX1u80o8vg7ID9zuNeBfcsM1vRa9ICcL4d1rPkTV7reTtTVn&needFold=0&_ksTS=1511186580494_873&callback=jsonp874"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('拉杆箱1880.csv',mode='a',encoding='UTF-8')
        i=i+1
        



def huaweichangxiang7():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=554919155557&spuId=860308979&sellerId=2838892713&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvu9vovxZvUvCkvvvvvjiPPLzhgjl8n2sOljD2PmPptjYUP2svzjrnP2s96jlRRphvChCvvvmCvpvZzPQwctSNznsw9REftGPwbas%2B7ekCvpvZzNQ%2BclNSznswSpB48rUh4eIudT4rvpvBohebHVOvph0rtz6HRFIAXQArvpvEphh72nUvphDudphvmZCmIvsrvhCVO86CvvDvpIpWcvCvBpOtvpvhphvvvbyCvm3vpvCyvvCCP6Cv2Uvvvh8RphvZvvvvp0nvpCCzvvC2oyCv2Uvvvhn8uphvmhCvCjz%2BOCjMkphvHyCvovAQn0vxby7tSf%2BzOCODxG0DrswEvpCWpJE%2Fv8RAVA9aUneYr2E9ZVQEfwAK5kx%2Fwm0QABoOal%2BDN%2B1lDCODN5USYE7reC618BLy1Ey7nDyiLO2v5fh3ZkZH1npaRoxBnZJt9vhCvvXvppvvvvvPvpvhvv2MMTwCvvBvpvpZ3QhvChCCvvvtvpvhphvvv86CvvDvppGZPvCvXPQ%3D&isg=AuHh3PeaH6IO1LA5hoGJMQND8qv7jlWAbxg4CkO33OhCqgB8i9-nUJcoeOLS&needFold=0&_ksTS=1511186791101_1416&callback=jsonp1417"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('华为畅享7.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def huaweinova2():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=551507842482&spuId=851701390&sellerId=2838892713&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvB9vpvopvUvCkvvvvvjiPPLzhgj1WR2qh6jivPmPOtj3CPFqvsjYWPsq9AjrUdphvmpmvsWFAvvmx%2BIhCvvswMRtJsRMwznsMcDurvpvEvUvgPv%2BvvUyMdphvhIovYPwgvvvHOAZNodHBnbu0WOwCvvpv9hCvRphvCvvvphvEvpCWvrMX0Bl1K3kOW5ZilwmOWtQBfvDr1EkK53HkLixreEKK55CwiNpfeEA4fCuYiLUpVE6Fp%2B0xhE9wjLEc6aZtn1mAVArlYb8rV8tdofyCvm9vvhCXvvmvPQvvp0WvvvHevvCHBpvv9BvvvhoXvvmC3vvvp0WvvUVhuphvmvvvpBt5hTwSkphvCIOvpyjh1vhCvvOv9hCvvvvPvpvhvv2MMTwCvvpvvhHhdphv2QRv%2Bb20vvmm8kZN7g63Wu6Cvvyv9RsIzQvv36wtvpvhvvCvpv%3D%3D&isg=Avv7jhmKJRAb-hpL6A8Dg7VliNllUA9Sek81YO25zfoXTBsudSCfohkGEtH_&needFold=0&_ksTS=1511187057040_948&callback=jsonp949"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('华为nova2.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def huaweip10():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=545896335041&spuId=724285208&sellerId=2838892713&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvuQvRvBWvUvCkvvvvvjiPPLzhgj1nPL5ZsjljPmP9AjrWPsdWtjiUPsSpQj18RphvChCvvvmCvpvZzPQwORzNznsw5Y1ftGPw0ns%2B7e9tvpvhphvvvUhCvCwYM2Y9RRMwznsY9lIu6kpum8e%2Fezrq8uwCvvBvpvpZRphvChCvvvvPvpvhvv2MMQyCvh129FOvItY0LzXW1WkwejafnDeDyBvOJ193Zi7vV36AxsBCAfyp%2B3%2BKjomBSfVTbZ9K7e0xdB%2BapVQEfakK5eUBOyTxfBKKNB9fbc7%2BuphvmhCvCjz%2BgkgYkphvCylnmvAOebyCvm3vpvCyvvCCP6Cv2Uvvvh8RphvZvvvvp0nvpCCzvvC2oyCv2Uvvvhn8vphvCyCCvvvvvUwCvvBvppvvdphvhhaVT3F8vhCaU6mYKLuAbDI%3D&isg=AhERTA__LzJ9EUDJVrG5odNTIhurfoXwXNnPYvOmS1jzmjDsO89XwEo4SFOB&needFold=0&_ksTS=1511187124182_1805&callback=jsonp1806"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('华为p10.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def vivox9():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=541396973568&spuId=709963452&sellerId=883737303&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvBvvPvpgvUpCkvvvvvjiPPLzhgj1nRLsU0jljPmPU1jn8RsdyQj1EPFcpsjlPPFyCvvpvvhCv9phvHCF5VLsjcnMNzsEDz8otgZnL9TDu2QhvCvvvvvvCvpvVvUCvpvvvmphvLUVxJz%2BaqbVQKfE9ZJ2IRfUTKFEw9bZcRbut8v2htCuXVXrQB%2BLW5C9wDVQCKWVTKLpZwvFwAb8Oe130pXcvV3KZHk62Qa7tnCpX4Z7tvpvIvvCv7pvv92GvvhnFvvvCX9vvBZZvvUhpvvChepvv9OpvvhnFvvmC38yCvv9vvhhJX1NTcIyCvv4VvhEC1WptvpvhvvCvp8wCvvpvvhHh3QhvCvmvphmrvpvEvUmrdi6vvm7ORphvCvvvphmrvpvEvUHw7JOvv2mZ9phv2nM5xiAQ7rMNz1nWzv%3D%3D&isg=AhERTGlrLzJ9S0DJVrG5odNTIhurfoXwXNnPYvOmgVjwmjDsO88Owb84SFOB&needFold=0&_ksTS=1511187177480_2739&callback=jsonp2740"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('vivox9.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def vivox20plus():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=559778877551&spuId=882954104&sellerId=883737303&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvsvvnvPpvUvCkvvvvvjiPPLzhgj1RPFSUAjD2PmPOsjrRnLdUsjYVR2SytjDP9phv2nsG2DgVzYswzUmo7IhCvCLwjjlfZJMwznAwnDS5FSA3MCH49OwCvvBvppvviQhvChCvCCptvpvhphvvvvyCvh1CoDpvI1yaUmx%2FgjZ7%2B3%2BFjomxfBeKfvyf8rClHs9lBk9vD76wdeDHEcqh68gcWhZs7T2hDCODN5HHaf9gKFnf4Hky%2Bb8rwZZaWGjxKphv8hCvvVpvvhhMphvW9vvvpItvpCpvvvC2O6Cvhjwvvhn8phvW9vvvp6uEvpvVLZ6U2EkOuphvmhCvCjz%2Bg0UTvphvCyCCvvvvvvGCvvpvvPMMRphvChCvvvvtvpvhphvvvv%3D%3D&isg=AsPDNpygnThi2VKj0DfL-z39UIFtOFd64ud9yPWgBCKctOLWfQlTytvmWnkH&needFold=0&_ksTS=1511187237540_1466&callback=jsonp1467"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('vivox20plus.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def vivox9s():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=554616411041&spuId=858199409&sellerId=883737303&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hv2QvRvPyvUvCkvvvvvjiPPLzhgj1RRsSUsjljPmPZtj3PRFdZljlER2zvtjE89phv2nsG8HGvzYswzE%2F47u6CvvDvpy9ZHQCv7sACvpvWzPQicyFSznsw5UD43QhvChCCvvmEvpvVLZ6U2EkOuphvmhCvCjz%2BgTZLKphv8hCvvVpvvhhMphvW9vvvpItvpCpvvvC2O6Cvhjwvvhn8phvW9vvvp6IEvpCWpZJ7v8RKNB9f8j7%2BhfUiB7ERiNoOej3UJHLXSfpAOHCqVUcn%2B3C1B5IUDaVTRogREcqhz8TJEct1Bz7Q%2Bul1oC69D70Oe161EcqhzvhCvvXvppvvvvvPvpvhvv2MMsyCvvBvpvvviQhvChCvCCptvpvhphvvv2yCvvBvpvvv&isg=AsnJJKET92p074jx7glxyet72vMjFr1IVCEHums-E7DusujEs2cDGGwggCv5&needFold=0&_ksTS=1511187285661_1185&callback=jsonp1186"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('vivox9s.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def meididianfanbao():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=537613055871&spuId=524183918&sellerId=2973966816&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvBpvRvpQvUvCkvvvvvjiPPLzhgj1PRFd9sjthPmPZQjEmPL5hgj3nRLsO1jiPRphvCvvvphmCvpvZzPQxcxNNznswgHrftGPw9Ys%2B7ekrvpvZ3Om7yKvvvvMnEBYaAOZzWuvTnhOtvpvhvvCvpUhCvvswM2Bwx%2FMwznAwHxujvpvhvUCvp2yCvvpvvhCv2QhvCvvvMMGEvpCWvObV130Q%2Bu6fd56eafmAdXAKNxAxfBuKHdBYVVzydi%2F4V5xjTWoXVXK4fCuYiLUpVE6Fp%2B0xhCyXjLEc6aZtn1mAVA3lYb8re4tdo4yCvv9vvhhJXAJ37IyCvv4VvhEC1WotvpvIvvCv7pvv92GvvhnFvvvCX9vvBZZvvUhpvvChepvv9OpvvhnFvvmC3vhCvvOv9hCvvvm5vpvhvvCCBv%3D%3D&isg=ApubrhwXRTB6G7orSO-j4xWFKPkFcK9y2q-VQI3YOxq1bLpOFUGDwvIucvGf&needFold=0&_ksTS=1511187375766_1149&callback=jsonp1150"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('美的电饭煲.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def suboerdianfanbao():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=533148343817&spuId=609496436&sellerId=1991887885&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvNQvovLWvUpCkvvvvvjiPPLzhgj1UPsqWzjljPmPh0j1hRLMW1j3bPsSZgjECRLyCvvpvvvvvdphvmpvh4gVOevm99T6CvvyvCVOmoh9vIvQtvpvhvvvvvUhCvCLwMhHairMwzn19GxS5MYArzR144UhCvvswMm1fKRMwznAY1lu5vpvhvvmv99GCvvpvvvvvmphvLv2slvvjfT2UibmAdcOdYExr68g7EcqpaNoUbdiQpi59waZOVoZowacvAbUfjV5vAE7nbdiQpicwkbmAdcyyYUkU%2Bb8rwZHlYWmQrETtvpvIvvvvFhCvCPyvvUhpphvUWQvv99CvpvAvvvvmqyCv2mpvvUhpphvWEUyCvvO6vvVCwZmivpvUvvmvdtDL2JOCvpvVvvpvvhCvRphvCvvvvvmjvpvhvvpvv2yCvvpvvvvvdphvmpvU3OV9IvmWxghCvvswMmlaDrMwznQC4xI%3D&isg=An19CCBO-47IDVyNmpXtrcc_jt93GrFsyGXzJj_CJVQHdpyoB2ubPNnkVJfN&needFold=0&_ksTS=1511187443664_1163&callback=jsonp1164"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('苏泊尔电饭煲.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def feike_chuifengji():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=533761887852&spuId=572776012&sellerId=763968012&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvSQvBvZWvUpCkvvvvvjiPPLzhgj1UnL5wQjEUPmPW6jE2P2cpzjiWPL5y0jDRPsyCvvpvvhCv9phvHnsG%2BH%2FQzYswzUZJ7%2FwCzCqwsHiIdphvHU7vgJBxvvmD7kZNcweHns89RFBVdphvmpmvj3i%2Bvvm3BOhCvvswjUBJXJMwznAkXDu5vpvhvvCCBvGCvvpvvvvvvphvC9mvphvvvbyCvm9vvhCXvvmvPQvvp0WvvvHevvCHBpvv9BvvvhoXvvmC3vvvp0WvvUVhuphvmvvvpBt5bt0PkphvH9vvZDVHKBmTnqZKpa0th2KARLn4SfyEvpCWv7Aw5C0thboJ%2B3%2BKaNmAdBkKN6dvtC9aeiiz7YeYr2UpVj%2BO3w0AhC%2BaWDNBlLyzhbUf8jc6%2Bu0OdeQEfwoK5d8rwATQD40XdigDNFyCvvpvvhCv3QhvCvmvphmrvpvEvvhHvXUvvE5yRphvCvvvphmrvpvEvUvch59vv8OF&isg=Aiwse8TvWu1mQk0-A7os7p6Y_wxe5dCPwpMlzYZt9ld4kc2brvT2HzzjxWTU&needFold=0&_ksTS=1511187516481_2045&callback=jsonp2046"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('飞科吹风机.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def songxia_chuifengji():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=38837853172&spuId=272153420&sellerId=669690917&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvKpvLvxvvUvCkvvvvvjiPPLzhgj1ERLcZsjnEPmPpzjrnPLzW6jEvPsqy1jlH9phvHnsGrll0zYswzmmT7%2FwCzbNwqHiIdphvmpvh0Uj1GpCynT6CvCvwmUuvo6%2BvjRonrsw6Zf5BdphvmpvUP92L6QvZ3uwCvvpvvUmmRphvCvvvvvvPvpvhvv2MMQhCvvOvCvvvphvEvpCWmvqfvvw0ljcQGb8rwZCl%2BExreEIaUExr1WAKDox%2F1n3l%2Bb8rwZElYWFZe3WDN%2BLZafmAdcHjaNLtD40OwATQD7zhe4tYLYLZeE7rebyCvm9vvvmWphvh%2Fpvv9BCvpv9svvmmvhCv2UvvvvbKphvWEvvv9BCvpvQykphvCFpvvOH1p8yCvv9vvUmSexcpsOwCvvpvCvvvdphvmpvUegCvpvvOQOhCvCRGjVXfZRMwznsagHdAZTDuk85RRphvCvvvvvmrvpvEvvpg94V3vVsndphvmpvhpOVrdpmhFLyCvvpvvvvv&isg=AjEx7Hajz9JbMmApthFZATPzQrvLHqWQPLmvwhNHbvgVOlCMW2_oYAGYKPOh&needFold=0&_ksTS=1511187569184_1766&callback=jsonp1767"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('松下吹风机.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def skg_shuihu():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=45079595545&spuId=330805197&sellerId=896004430&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvNpvEvbQvUvCkvvvvvjiPPLzhgj1bRssvtjrCPmPw6jEHR2dwsjtEPLFU6jrW3QhvCvvhvvm5vpvhvvmv9FyCvvpvvvvvKphv8vvvvU1vpvLtvvmChhCvCUvvvUUvphvW9vvvvKtvpvQyvvmChhCv2moEvpvVnvvC9cHvuphvmvvv98%2FXxueSmphvLvpbyvvj4Omxfwowderv%2B8c6gEAfalSXS47BhC3qVUcnDOmOejIUDajxALwpEcqvaNoUrCH%2Bm7zpaNpz%2BFwcoX7aHLQg4vlrlj7Q%2Bu6CvpvVvmvvvhCv2QhvCvvvMMG%3D&isg=AsfHKg1SUUwA6tYvvAMXr9khVH2RzJuuhov5RJm049Z9COfKoZwr_gVK3vWr&needFold=0&_ksTS=1511187771899_354&callback=jsonp355"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('skg水壶.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def suboer_shuihu():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=537204603238&spuId=651858013&sellerId=1991887885&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvWpvBvLWvUpCkvvvvvjiPPLzhgj1hR2LU0jivPmPWQjnCPFdpsjtUn2FWQjn8RFyCvvpvvvvvdphvmpvUEvUrbpCe4gwCvvpvCvvv2QhvCvvvvvvEvpCWCm%2Fvvvw0tRLOTCufwheQ0f0DW3CQog0HsXZpejXWAXcBlLyzOvnrQjc6%2B86DN%2B1lafm655aVsWkQ0fJ6EvLvqU0HKfE9ZasIAXZTKIyCvvO6vvVCwZmivpvUvvmvdtDEw3etvpvIvvvvFhCvCPyvvUhpphvUWQvv99CvpvAvvvvmqyCv2mpvvUhpphvWEvhCvvOvCvvvphvtvpvhvvvvv8wCvvpvvUmm9phv2Hiff%2FaAjHi47IcWzsyCvvpvvvvvdphvmpvUFQCf7QvK6T6CvCp%2Bm8hmXVpvauWidAhAZqeBCahTR46CvvyvCReCMN6vNr8CvpvZ7DSYYlfw7Di4%2F5L5MPY4iDd4z69%3D&isg=AnR0o1GMkrVv0AUWiyJ0RoZwRzTmTZg3qVrKHQ7V3f-BeRXDNlwIx2b7jYxc&needFold=0&_ksTS=1511187890077_1171&callback=jsonp1172"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('苏泊尔水壶.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def nivea_ximiannai():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=22151608347&spuId=273950430&sellerId=1123492339&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvHvvbvnpvUvCkvvvvvjiPPLzhgjn2RFFvlj3mPmPZ1jnCR2qhgjnbnLqyQjtbRphvCvvvvvmCvpvWzPAKO22NznSf%2FOt4RphvCvvvvvvCvpvVvmvvvhCvKphv8vvvvU1vpvLtvvmChhCvCUvvvUUvphvW9vvvvKtvpvQyvvmChhCv2moivpvUvvmvdtD85YAEvpvVnvvC9cHvmphvLvvWspvjbbmxYnp7RAYVyO2vqbVQWl4vsRkx5F%2BSBiVvQRQ1RoxhdJAn3feAOHLIAXcBKFyK2i56N76Xde3C%2BEc61EI7nDeDyO2vSdgPvpvhvv2MMTwCvvpvvUmm3QhvCvvhvvv%3D&isg=Avn5lA8Ah_qh8FiBvjkhebtLCmPTBu24pNH3KhsuciCfohg0Y1eviEcwUJup&needFold=0&_ksTS=1511188058828_994&callback=jsonp995"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('妮维雅洗面奶.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def baou_ximiannai():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=19478755972&spuId=273609646&sellerId=533497499&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvrvvnvPUvUvCkvvvvvjiPPLzhgjnmR2MpljYHPmPwtjDbPLcW6jYURLzwzjt89phv2nsGlDlazYswzbq47FyCvvpvvvvv9phvhisGPxIMqYswzPQB7kdoXhFD48wCvvpvvUmmRphvCvvvvvvCvpvVvvpvvhCvmphvLCBIAvvjbUklkbvi55Cw0f0DyBvOPZm93weaKdODoYjn%2BheceLQWiRAEAf8Q81mn3w0xhE3T7t5xKO6TrmYCIWeQ6XoYW6oD6O03H2uEvpvVnvvC9cHvuphvmvvv98%2FXLjoCKphv8vvvvU1vpvLtvvmChhCvm2WvvUUvphvW9vvvvKtvpvQyvvmChhCv2mpPvpvhvv2MMgwCvvpvCvvvRphvCvvvvvv%3D&isg=Ari41xXGFgnIwHlil_5wSuLki2BKIRyrDa4WSfIpLPOlDVn3mjCWO2LvsThA&needFold=0&_ksTS=1511188150285_1638&callback=jsonp1639"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('巴黎欧莱雅洗面奶.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def yujin_1():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=39934113392&spuId=284882077&sellerId=2126704766&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvvpvRvphvUvCkvvvvvjiPPLzhgjnCnLqyQj1VPmP91jrRRLSOlj1nP2qwgjDCdphvhovUXQ89IvCG%2BoeS8kH2mOcE9phv2nQw8H19zYswzHG%2F7FyCvvpvvvvvRphvCvvvvvvPvpvhvv2MMQyCvhQpfL6vC6fEDOkQ%2Bul1pzc6D70OVB60kWzxkC4AVAnlYExreCyaWGzC%2B4ZTHVEvibmxfBeKNB3rgj7gRfU0ZG5nD4mZHkx%2F1W3lYb8rkphvCFpvvOH1p8yCvv9vvUmSeZTxrbyCvm9vvvmWphvh%2Fpvv9BCvpv9svvmmvhCv2UvvvvbKphvWEvvv9BCvpvQyvphvC9vhvvCvp8wCvvpvvUmm3QhvCvvhvvmCvpvWzP1Z7qdSznswMCH4RphvCvvvvvv%3D&isg=AmdnStT98WxivHYPHOO3j7lB9J0x7DvO5utZJDnUr_YaKIbqQb50HozqPhVL&needFold=0&_ksTS=1511188301644_2142&callback=jsonp2143"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('洁丽雅浴巾.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def yujin_2():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=524884588228&spuId=276108520&sellerId=1045448342&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvnvvnvRQvUvCkvvvvvjiPPLzhgjnvRF5ZzjnEPmPZ6jEvRFzWzjEHPF5Ztj3CRphvCvvvvvmCvpvWzC1t7l5SznswM8H4iQhvCvvv9UUtvpvhvvvvvvGCvvpvvPMMmphvLv1zTQvjcn1lYboOHFU4sb2U%2Bb8raAuy%2BExreTtYhbFCSwhZDVQEfaBlY28zUl4lDf5BdfUf8zxlIE7re166%2BExr18TJEcqZa7zvd34EvpvVnvvC9cHvuphvmvvv98%2FXppOQKphv8vvvvU1vpvLtvvmChhCvm2WvvUUvphvW9vvvvKtvpvQyvvmChhCv2mpCvpvVvvpvvhCv3QhvCvvhvvvtvpvhvvvvvUhCvvswMWYaMaMwznA%2FPDI%3D&isg=Ai4udYId-AvT9g8AvYAOCKiyfYLwL_Ipd9hAa1j3izHuO8-VwL4dOdj5h5oq&needFold=0&_ksTS=1511188373683_915&callback=jsonp916"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('180*90浴巾.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def shoujike_1():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=41102854337&spuId=887979443&sellerId=1821686970&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hv4vvnvRgvUpCkvvvvvjiPPLzhgjnjP2shAjthPmPWtjr8RLLvzjiEn25p6jnHRT6CvvyvvwzPQQvv36ujvpvhvUCvp2yCvvpvvhCv2QhvCvvvvvmEvpvV39CmpwLhuphvmvvvpBt5XgPMKphv8vvvpHyvvUvMvvC2OQvv9CvvvhxHvvmChvvvBEyvvUVhvvC2OQvv9OpEvpCW9H1DXB0yHd8rejwuYWA4eo%2FAVAdhaB4AdX31bPBnRFe6nAwEewezruh6UxWnSL8AHbUf8r1lDC4AdcyyYE7r58TxEcqh18g7rEtsp9hCvvOvChCvvvm5vpvhvvCCB86CvvyvvO%2FnTpvvmX7CvpvWz%2F%2Flj8r4zYMNw8NwRphvCvvvphv%3D&isg=Anl5FDl6B3ogn9gBPrmh-TvLiuNThm04JFF3qpuugKAbIpi049QACOHw0Bsp&needFold=0&_ksTS=1511188406197_1902&callback=jsonp1903"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('手机壳25.9.csv',mode='a',encoding='UTF-8')
        i=i+1
        

def shoujike_2():
    for i in range(1,6):
        temp=str(i)
#    url="https://rate.taobao.com/feedRateList.htm?auctionNumId=45539882033&userNumId=62158293&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0&ua=233UW5TcyMNYQwiAiwZTXFIdUh1SHJOe0BuOG4%3D%7CUm5Ockp3TnVNeEJ6RnNNdiA%3D%7CU2xMHDJqA20Efx4wED4CPxExH1gxWnQidA%3D%3D%7CVGhXd1llXWBZYlpvVW1RZFphVmtJdUt%2FQH1Jck5zSX1Cf0Z%2BRHxSBA%3D%3D%7CVWldfS0TMw8xCioWKwslQjkdYgtwXCZMJQtdCw%3D%3D%7CVmNDbUMV%7CV2NDbUMV%7CWGZGFisLNhYqFSAdPQI2AjgYJBsuEzMGOwYmGiUQLQ03CTJkMg%3D%3D%7CWWBAED4QMA46ASEdIx0oCDQINQFXAQ%3D%3D%7CWmJCEjwSMmJWYlp6Rn9LcCYGOxs1GzsDNgo1YzU%3D%7CW2JfYkJ%2FX2BAfEV5WWdfZUV9SWlTa0t0VGFBfUYQ&_ksTS=1504658758434_2623&callback=jsonp_tbcrate_reviews_list"
        #url="https://rate.tmall.com/list_detail_rate.htm?itemId=43928349416&spuId=128950384&sellerId=890482188&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvtvvRvBgvUvCkvvvvvjiPPLzhgjtnPsswtjrCPmPOtjn2PFSOljE8P2MvQjY89phvHnsG%2BHzYzYswzb047%2FNpzRjwmliIdphvmpvhugVH3pv6su6CvvyvCnymcx6vWHAjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvmtvpvIvvvvk6CvvhGvvUhpphvh9vvv99CvpvAvvvvmqyCv2mpvvUhpphvWE8yCvv9vvUmSeLPUIOyCvCOvvveCUZ%2Fvlfernqwz7O2XDwetrmYCmphvLCm0v9vjfiVvQRA1%2B2n79n2IAfUTnZJt9Exre8tdpbmDYRo4ezDx0f0DyBvOJ1kHsX7ve36AxYjxAfyp%2B3%2BraNoxfXuKfvc6D7zOdiGCvpvVvmvvvhCv2QhvCvvvMM%2FrvpvZbvoq94kIv2m584G3WDRtypcBRFytvpvhvvvvvv%3D%3D&isg=AllZdJB4Z9p8PTih3lmBGdsrakMz5k2YJ8CwsnsOdQD_gngUwzcNaPYQ8HoK&needFold=0&_ksTS=1511185335631_814&callback=jsonp815"
        url="https://rate.tmall.com/list_detail_rate.htm?itemId=40934251337&spuId=329725018&sellerId=2024058652&order=3&currentPage="+temp+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvA9vRvPyvUpCkvvvvvjiPPLzhgjnjR2dvAjivPmPU6jlHP2FwAj3Cn2MUljYbnUhCvvswjmCwInMwzn1vYxuCvpvWzP1U7tjSznswSmD4iQhvCvvv9UUtvpvhvvvvvbyCvm9vvvmWphvh%2Fpvv9BCvpv9svvmmvhCv2UvvvvbKphvWEvvv9BCvpvQykphvCFpvvOH1p8yCvv9vvUmSeZ2KPpyCvhQpjlUvCld6D7zhd3OiHnFU6WQ7RAYVyO2vqbVQWl4v1nLIRfU6pwet9E7re1691bmDYEKOaZmQ0f0DW3CQog0HsXZpejXWAXcBlLyzvphvC9vhvvCvpvGCvvpvvvvv3QhvCvvhvvvtvpvhvvvvv86Cvvyv28hCbo6v3U%2Btvpvhvvvvvv%3D%3D&isg=AsHBPEclfwIo9ZDZpiHpUSOj0gvb7jXgLEk_kiMW6kgiCuDcaz_psKXImEOx&needFold=0&_ksTS=1511188456367_2961&callback=jsonp2962"
        url=str(url)
        print(url)
        myweb = rq.get(url)
        myjson = re.findall('\"rateList\":(\[.*?\])\,\"searchinfo\"', myweb.text)[0]
        mytable = pd.read_json(myjson)
        mytable.to_csv('手机壳9.9.csv',mode='a',encoding='UTF-8')
        i=i+1
        


# nike_airforce()
# stan_smith()
# langsha_nvneiku()
# langsha_nanneiku()
# laganxiang_500()
# laganxiang_500_1500()
# laganxiang_dayu_1500()
# huaweichangxiang7()
# huaweinova2()
# huaweip10()
# vivox9()
# vivox20plus()
# vivox9s()
# meididianfanbao()
# suboerdianfanbao()
# feike_chuifengji()
# songxia_chuifengji()
# skg_shuihu()
# suboer_shuihu()
# nivea_ximiannai()
# baou_ximiannai()
# yujin_1()
# yujin_2()
# shoujike_1()
# shoujike_2()



