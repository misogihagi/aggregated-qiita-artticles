import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime
from bs4 import BeautifulSoup

start_year = 2011
start_month = 9
end_year = 2022
end_month = 3

start = datetime(start_year, start_month, 1)
end = datetime(end_year, end_month, 1)

left = datetime(start_year, start_month, 1)
right = left + relativedelta(months=1)

result = ""
while left <= end:

    params = {
        "q": "created:>{} created:<{}".format(
            left.strftime("%Y-%m"), right.strftime("%Y-%m")
        )
    }
    res = requests.get("https://qiita.com/search", params=params)
    soup = BeautifulSoup(res.text, features="html.parser")
    total = soup.select(".badge")[0].string
    print(left.strftime("%Y/%m:") + total)
    result += left.strftime("%Y,%m,") + total + "\n"
    left = right
    right = left + relativedelta(months=1)


with open("result.csv", "w") as f:
    f.write(result)

