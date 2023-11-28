import requests
for i in range (1,5000):
    url=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    data= requests.get(url=url)
    if data.status_code==200:
        print(url)
    else:
        continue