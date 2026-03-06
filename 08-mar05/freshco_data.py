import requests
import json

url_freshco_mar_5_11_2026 = "https://dam.flippenterprise.net/flyerkit/publication/7813184/products?display_type=all&locale=en&access_token=881f0b9feea3693a704952a69b2a037a"

# get data
def get_data(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()  # Automatically parses the JSON response
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()
  except json.JSONDecodeError:
    print("Error decoding JSON")
    exit()
  return data

data_freshco = get_data(url_freshco_mar_5_11_2026)
print(len(data_freshco))
print(type(data_freshco))
#print(data_freshco[0])

results_Freshco = [{'name': item['name'], 'price': item['price_text'], 'pic': item['image_url']} for item in data_freshco]
print(results_Freshco[0])

max_length_name = 0
for product in results_Freshco:
    if len(product['name']) > max_length_name:
        max_length_name = len(product['name'])
        print(max_length_name)
        
# print("NAME".center(156), "PRICE")        
# for product in results_Freshco:
#     print(product['name'].center(156), product['price'])
    

# filter out no price items
filtered_products = [d for d in results_Freshco if d['price'] == ""]
print(len(filtered_products))
print(filtered_products)