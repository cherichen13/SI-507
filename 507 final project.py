import requests
import json

api_key = "j-_WRt04kVT7_3EXNeW14WXvnTpv7CjEVwcqfGDFJJFNf1rFwD-cy6_42wrVJR71xiKMo1UVUMkBFu5pGolWgZBS3fzPFSJ3tjT2cIRLCLRUPmU8mdnbcXrPPtyMY3Yx"

CACHE_FILENAME = "cache_final.json"

try:
    cache_file = open(CACHE_FILENAME, 'r')
    cache_contents = cache_file.read()
    data_dict = json.loads(cache_contents)
    cache_file.close()
    
except:
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'restaurant', 
              'location': 'Michigan, Ann Arbor',
              'limit': 50}
    response = requests.get(search_api_url, headers=headers,
                            params=params, timeout=5)
    data_dict = response.json()
    
dumped_json_cache = json.dumps(data_dict)
fw = open(CACHE_FILENAME,"w")
fw.write(dumped_json_cache)
fw.close()

category_name = []
for i in range(50):
    category = data_dict['businesses'][i]['categories']
    for j in range(len(category)):
        category_name.append(category[j]['title'])
        unique_category = list(set(category_name))
        
# print(response.url)
# print(response.status_code)
# print(response.headers)
print(data_dict)

# print(data_dict)
# print(len(data_dict))