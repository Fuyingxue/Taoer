# Python3.x 自定义log
# 1.
def log(*args, **kwargs):
    """
    用这个 log 替代 print
    """
    print('log', *args, **kwargs)

# 2.
import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 把 unix time 转换为人类可以看懂的格式
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


# 3.  写在一个文件里
def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 把 unix time 转换为人类可以看懂的格式
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.xue.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


# 4.  写在多个文件里
import time


log_config = {}


def set_log_path():
    fmt = '%Y%m%d%H%M%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(fmt, value)
    log_config['file'] = 'logs/log.xue.{}.txt'.format(dt)


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 把 unix time 转换为人类可以看懂的格式
    fmt = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(fmt, value)
    # 这样确保了每次运行都有一个独立的 path 存放 log
    path = log_config.get('file')
    if path is None:
        set_log_path()
        path = log_config['file']
    with open(path, 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
