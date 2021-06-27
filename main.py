import random
import sys
from random import randint
import time
import webbrowser
import os


links = [
        "https://cylonepedia.com/g-c-e-ordinary-level-past-papers-english/",
        "https://cylonepedia.com/g-c-e-ordinary-level-past-papers-tamil/",
        "https://cylonepedia.com/g-c-e-ordinary-level-past-papers-sinhala/",
        "https://cylonepedia.com/2021/02/07/2019-english-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2018-english-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2017-english-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2016-english-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2020/08/02/2015-english-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2019-sinhala-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2018-sinhala-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2017-sinhala-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2016-sinhala-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2015-sinhala-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/09/2015-tamil-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/09/2016-tamil-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/09/2017-tamil-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/09/2018-tamil-medium-gce-o-l-past-papers/",
        "https://cylonepedia.com/2021/02/07/2019-tamil-medium-gce-o-l-past-papers/"
        ]


def start_bot():
    try:
        url_link_1 = random.choice(links)
        url_link_2 = random.choice(links)
        url_link_3 = random.choice(links)
        url_link_4 = random.choice(links)
        url_link_5 = random.choice(links)

        webbrowser.open(url_link_1)
        time.sleep(45)

        webbrowser.open(url_link_2)
        time.sleep(45)

        webbrowser.open(url_link_3)
        time.sleep(45)

        webbrowser.open(url_link_4)
        time.sleep(45)

        webbrowser.open(url_link_5)
        time.sleep(45)

        os.system("./close.sh")
        time.sleep(randint(4, 10))

    except Exception:
        print("erroe")


if __name__ == '__main__':
    print("Program started")

    count = 0
    while True:
        start_bot()
        count += 1
        count_str = str(count)
        sys.stdout.write('\r ' + count_str + 'View Completed')
        del count_str
