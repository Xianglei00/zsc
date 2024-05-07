# @author xl
# @create 2022/3/29 21:05
# @program: com.xl.hlsvideo
# @E-Mail: 2199396150@qq.com
import logging
import time


class Log():
    localtime = time.localtime()
    from logging.handlers import RotatingFileHandler
    logging.basicConfig(level=logging.INFO)
    file_log_header = RotatingFileHandler(f"./logs/app{localtime.tm_year}-{localtime.tm_mon}-{localtime.tm_mday}.log", maxBytes=1024 * 100, backupCount=5)
    formatter = logging.Formatter('%(message)s - %(levelname)s - %(lineno)s')
    file_log_header.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_header)


if __name__ == '__main__':
    pass
