import argparse
import requests
import pendulum

from github import Github

# 14 for test 12 real get up
GET_UP_ISSUE_NUMBER = 12
GET_UP_MESSAGE_TEMPLATE = (
    "今天的起床时间是--{get_up_time}.\r\n\r\n {today_feeling}\r\n\r\n >  {sentence} \r\n From: {from_who}"
)
SENTENCE_API = "https://v1.hitokoto.cn/?c=k"
DEFAULT_SENTENCE = "HODL! HODL! HODL!"
TIMEZONE = "Asia/Shanghai"

# 早起默认心情
DEAFULT_EARLY_TODAY_FEELING = "一个人知道自己为什么而活，就可以忍受任何一种生活。\r\n天纵英才，晨勃还在。"

# 晚起默认心情
DEAFULT_LATE_TODAY_FEELING = "睡懒觉！"

DEFAULT_LATE_FROM = "ISheep🐏"

# 晚起模板
GET_UP_LATE_TEMPLATE = (
    "今天的起床时间是--{get_up_time}.\r\n\r\n {today_feeling}\r\n\r\n >  {sentence} \r\n From: {from_who}"
)


def login(token):
    return Github(token)


# 获得一言的句子
def get_one_sentence():
    try:
        r = requests.get(SENTENCE_API)
        if r.ok:
            return r.json().get("hitokoto", DEFAULT_SENTENCE)
        return DEFAULT_SENTENCE
    except:
        print("get SENTENCE_API wrong")
        return DEFAULT_SENTENCE


# 获得一言的出处
def get_one_sentence_from():
    try:
        r = requests.get(SENTENCE_API)
        if r.ok:
            return r.json().get("from", "SHEEPFOLD") + "-----" + r.json().get("from_who", DEFAULT_LATE_FROM)
        return "unknown"
    except:
        print("get SENTENCE_API wrong")
        return DEFAULT_SENTENCE


def get_today_get_up_status(issue):
    comments = list(issue.get_comments())
    if not comments:
        return False
    latest_comment = comments[-1]
    now = pendulum.now(TIMEZONE)
    latest_day = pendulum.instance(latest_comment.created_at).in_timezone(
        "Asia/Shanghai"
    )
    is_today = (latest_day.day == now.day) and (latest_day.month == now.month)
    return is_today


def make_get_up_message(today_feeling):
    sentence = get_one_sentence()
    from_who = get_one_sentence_from()
    now = pendulum.now(TIMEZONE)
    # 4 - 8 means early for me
    is_get_up_early = 4 <= now.hour <= 8
    get_up_time = now.to_datetime_string()
    if is_get_up_early:
        # 如果未输入任何心情，则使用默认心情
        if(len(today_feeling) == 0):
            early_feeling = DEAFULT_EARLY_TODAY_FEELING
            body = GET_UP_MESSAGE_TEMPLATE.format(get_up_time=get_up_time, today_feeling=early_feeling, sentence=sentence, from_who=from_who)
        else:
            early_feeling = today_feeling
            body = GET_UP_MESSAGE_TEMPLATE.format(get_up_time=get_up_time, today_feeling=early_feeling, sentence=sentence, from_who=from_who)
    else:
        if(len(today_feeling) == 0):
            late_feeling = DEAFULT_LATE_TODAY_FEELING
            body = GET_UP_MESSAGE_TEMPLATE.format(get_up_time=get_up_time, today_feeling=late_feeling, sentence=sentence, from_who=from_who)
        else:
            late_feeling = today_feeling
            body = GET_UP_MESSAGE_TEMPLATE.format(get_up_time=get_up_time, today_feeling=late_feeling, sentence=sentence, from_who=from_who)
    return body, is_get_up_early


def main(github_token, repo_name, weather_message, today_feeling):
    print("天气信息： " + weather_message)
    u = login(github_token)
    repo = u.get_repo(repo_name)
    issue = repo.get_issue(GET_UP_ISSUE_NUMBER)
    is_toady = get_today_get_up_status(issue)
    if is_toady:
        print("Today I have recorded the wake up time")
        return
    early_message, is_get_up_early = make_get_up_message(today_feeling)
    body = early_message
    if weather_message:
        weather_message = f"现在的天气是{weather_message}\n"
        body = weather_message + early_message
    if is_get_up_early:
        issue.create_comment(body)
        print(body)
    else:
        issue.create_comment(body)
        print("You wake up late" + body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument(
        "--weather_message", help="weather_message", nargs="?", default="", const=""
    )
    parser.add_argument(
        "--feeling_message", help="feeling_message", nargs="?", default="", const=""
    )
    # parser.add_argument("--tele_token", help="tele_token", nargs="?", default="", const="")
    # parser.add_argument("--tele_chat_id", help="tele_chat_id", nargs="?", default="", const="")
    options = parser.parse_args()
    main(
        options.github_token,
        options.repo_name,
        options.weather_message,
        options.feeling_message,
        # options.tele_token,
        # options.tele_chat_id,
    )
