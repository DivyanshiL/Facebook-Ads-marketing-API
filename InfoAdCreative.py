
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.api import FacebookAdsApi

access_token=input('Enter the access token ')
page_ID=input('Enter the page id')
ad_account_id = input('Enter the ad account id')
FacebookAdsApi.init(access_token=access_token)

def information_of_behavior():
    params = {
     'type': 'adTargetingCategory',
     'class': 'behaviors',
    }
    resp = TargetingSearch.search(params=params)
    print(resp)

def information():
  params = {
   'q': input('Enter interest name to target'),
   'type': 'adinterest',
  }
  resp = TargetingSearch.search(params=params)
  print(resp)

def target_location():
    params = {
    'q': input('Enter country name'),
    'type': 'adgeolocation',
    'location_types': ['country'],
    }

    resp1 = TargetingSearch.search(params=params)
    print(resp1)

    params = {
     'q': input('Enter reagion of given comtry'),
    'type': 'adgeolocation',
    'location_types': ['region'],
    }

    resp2 = TargetingSearch.search(params=params)
    print(resp2)

    params = {
    'q': input('Enter City for given contry'),
    'type': 'adgeolocation',
    'location_types': ['city'],
    }

    resp3 = TargetingSearch.search(params=params)
    print(resp3)


print('*******************************************')
print('Information about tergeting Behavior')
print('*******************************************')
information_of_behavior()
print('*******************************************')
print('Information about targeting Intreset')
print('*******************************************')
information()
print('*******************************************')
print('Information about targeting location')
print('*******************************************')
target_location()
   
