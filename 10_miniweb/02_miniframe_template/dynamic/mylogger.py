import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
log_file = './log/log.txt'
fh = logging.FileHandler(log_file, mode='a', encoding="UTF-8")  # open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG)

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)


def info(content):
    logger.info(content)


def debug(content):
    logger.debug(content)


def error(content):
    logger.error(content)


def critical(content):
    logger.critical(content)


def warning(content):
    logger.warning(content)

if __name__ == '__main__':
    info("hello")
