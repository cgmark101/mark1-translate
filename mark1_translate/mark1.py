import re, requests

agent = {
    'User-Agent': "Mozilla/4.0 (compatible;MSIE 6.0;Windows NT 5.1;SV1;.NET CLR 1.1.4322;.NET CLR 2.0.50727;.NET CLR 3.0.04506.30)"}


def translate(to_translate, to_language="auto", from_language="auto"):
    base_link = f"http://translate.google.com/m?tl={to_language}&sl={from_language}&q={to_translate}"
    request = requests.get(base_link, headers=agent)
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    re_result = re.findall(expr, request.text)
    if (len(re_result) == 0):
        result = ""
    else:
        result = re_result[0]
    return (result)

