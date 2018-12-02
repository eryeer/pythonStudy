import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def pic_downloader(url: str, name: str):
    urlopen = urllib.request.urlopen(url)
    read = urlopen.read()
    file = open('D:\\' + name, 'wb')
    file.write(read)


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(pic_downloader, 'http://img2048.net/images/2018/11/16/o2018-1117-19b.jpg', '1.jpg'),
        gevent.spawn(pic_downloader, 'http://img2048.net/images/2018/11/16/o2018-1117-18b.jpg', '2.jpg')
    ])
