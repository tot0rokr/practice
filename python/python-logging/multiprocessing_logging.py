import logging
import logging.handlers
import multiprocessing
import queue
import time

def worker_process(log_queue, log_queue2, name):
    logger = logging.getLogger(name)
    handler = logging.handlers.QueueHandler(log_queue)
    handler2 = logging.handlers.QueueHandler(log_queue2)
    logger.addHandler(handler)
    logger.addHandler(handler2)
    logger.setLevel(logging.DEBUG)

    for i in range(10):
        logger.info(f'Process {name}: {i}')
        time.sleep(1)

def setup_listener(log_queue):
    root = logging.getLogger()
    handler = logging.handlers.RotatingFileHandler(
        'app.log', maxBytes=1024*1024, backupCount=5)
    formatter = logging.Formatter('file: %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(log_queue, handler)
    return listener

def setup_listener2(log_queue):
    root = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('stream: %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    listener = logging.handlers.QueueListener(log_queue, handler)
    return listener

if __name__ == '__main__':
    log_queue = multiprocessing.Queue(-1)
    log_queue2 = multiprocessing.Queue(-1)
    listener = setup_listener(log_queue)
    listener2 = setup_listener2(log_queue2)
    listener.start()
    listener2.start()

    processes = []
    for i in range(4):  # 4개의 프로세스를 실행
        p = multiprocessing.Process(target=worker_process, args=(log_queue, log_queue2, f'Process_{i}',))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    log_queue.put_nowait(None)
    log_queue2.put_nowait(None)
    listener.stop()
    listener2.stop()

