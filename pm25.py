import requests

url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"


def get_pm25_data():
    try:
        json_data = requests.get(url).json()
        datas = json_data["records"]
        columns = list(datas[0].keys())
        values = [list(data.values()) for data in datas]

        return columns, values

    except Exception as e:
        return None, str(e)


if __name__ == "__main__":
    print(get_pm25_data())
