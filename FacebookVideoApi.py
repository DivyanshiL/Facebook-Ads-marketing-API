from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.adimage import AdImage


access_token = input('Enter access token')
app_secret = input('Enter app secret')
app_id = input('Enter app id')
ad_account_id = input('Enter ad account id')
page_ID=input('Enter page Id')

FacebookAdsApi.init(access_token=access_token)

#To get campaign Id
def campaign(cname):
    params = { 
    'name': cname, 
    'objective':input('Enter objective for campaign(https://developers.facebook.com/docs/instagram/ads-api/reference/data-cta-requirements/'), 
    'status': 'PAUSED',
    'special_ad_categories': [None],
    }
    print(params)

    campaign_result = AdAccount(ad_account_id).create_campaign(params=params)
    print(campaign_result)

#Information about interest persons
def information(q):
  params = {
   'q': q,
   'type': 'adinterest',
  }
  resp = TargetingSearch.search(params=params)
  print(resp)

#targetting interest by providing information
def target_by_intrest(adset,budget,bid,billing_event,opt_goal,start_time,end_time,campaign_id,country,count_key,city_key,city_radius,gender,age_min,age_max,device_platform,interest_id,interest_name):
    params = {
      'name': adset,
     'daily_budget': budget,
     'bid_amount': bid,
     'billing_event': billing_event,
     'optimization_goal': opt_goal,
     'start_time': start_time,
     'end_time': end_time,
     'campaign_id': campaign_id,
     'promoted_object': {'page_id':page_ID},
     'targeting': {'facebook_positions':['feed'],'geo_locations':{'countries':[country],'regions':[{'key':count_key}],'cities':[{'key':city_key,'radius':city_radius,'distance_unit':'mile'}]},'genders':[gender],'age_max':age_max,'age_min':age_min,'publisher_platforms':['facebook','audience_network'],'device_platforms':[device_platform],'flexible_spec':[{'interests':[{'id':interest_id,'name':interest_name}]}]},
     'status': 'PAUSED',
    }
    adset_id=AdAccount(ad_account_id).create_ad_set(
     params=params,
    )
    print(adset_id)
    return adset_id

#To get hash image value
def hash_image(image_adress):
    image=AdImage(parent_id=ad_account_id)
    image[AdImage.Field.filename]=image_adress
    image.remote_create()
    hash_value=image[AdImage.Field.hash]
    print(hash_value)
    return hash_value
    

#adcreative Id is generated
def AdCreative_for_vedio():
    params = {
     'name': input('Enter name for adcreative'),
     'object_story_spec': {'page_id':page_ID,'video_data':{'image_url':input('Enter image url'),'video_id':input('Enter video Id'),'call_to_action':{'type':input('Enter call to action type'),'value':{'page':page_ID}}}},
    }
    advedio=AdAccount(ad_account_id).create_ad_creative(
    params=params,
    )
    print(advedio)
    return advedio

#ad is creataed
def ads_value():
    fields = []
    params = {  
    'name': int(input('Enter ad name')),  
    'adset_id':input('Enter adset id from above information'),  
    'creative': {'creative_id':int(input('Enter the adcreative Id from above information'))},
    'status': 'PAUSED'}
    print(AdAccount(ad_account_id).create_ad(fields=fields, params=params))


if __name__=="__main__":
    cname=input('Enter campaign name')
    campaign(cname)
    q=input('Enter the specific target area to get information')
    information(q)
    adset=input('enter the adset name')
    budget=input('enter budget for your adset')
    bid=input('enter the bid for adset')
    billing_event=input('enter the billing event for adset (https://developers.facebook.com/docs/marketing-api/bidding/overview/billing-events/) ')
    opt_goal=input('enter optimization goal for adset (https://developers.facebook.com/docs/marketing-api/bidding/overview/)')
    start_time=input('enter the start time for adset')
    end_time=input('enter the end time for adset')
    campaign_id=input('Enter the campaign ID for adset')
    country=input('Enter the targetting country for adset')
    count_key=input('Enter the targetting country key')
    city_key=int(input('Enter the targetting city key '))
    city_radius=int(input('Enter the radius of the city'))
    gender=int(input('Enter the gender'))
    age_min=int(input('Enter the minimum age group for targetting'))
    age_max=int(input('Enter the max age group for targetting'))
    device_platform=input('Enter device platform for targetting')
    interest_id=input('Enter the interest id')
    interest_name=input('Enter interest name')
    adset_id=target_by_intrest(adset,budget,bid,billing_event,opt_goal,start_time,end_time,campaign_id,country,count_key,city_key,city_radius,gender,age_min,age_max,device_platform,interest_id,interest_name)
    image_adress=input('Enter the location of image')
    hashed_id=hash_image(image_adress)
    Link=input('Enter the link address for ad creative')
    creative_id=AdCreative_for_vedio()
    ads_value()








