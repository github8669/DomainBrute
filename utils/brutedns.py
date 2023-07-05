# coding=utf-8
import dns.resolver
import threading
from Queue import Queue
from configs import config
import sys

class BruteDns(object):

    def __init__(self,domain):
        self.domain=domain
        self.thread_count=config.thread_count
        self.queue=Queue()
        self.result=[]
    def run(self):
        with open('dict/di.txt')as f:
            for i in f:
                self.queue.put(i.rstrip()+'.'+self.domain)
        total=self.queue.qsize()
        threads=[]


        for i in xrange(self.thread_count):
            threads.append(self.BruteRun(self.queue,self.result,total))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        return list(set(self.result))



    class BruteRun(threading.Thread):
        def __init__(self,queue,result,total):
            threading.Thread.__init__(self)
            self._queue=queue
            self._result=result
            self._total=total
        def run(self):
            while not self._queue.empty():
                sub=self._queue.get_nowait()
                try:
                    self.msg()
                    results=dns.resolver.query(sub,'A')
                    if results.response.answer:
                        self._result.append(sub)
                except Exception,e:
                    pass

        def msg(self):

            done_count=float(self._total-self._queue.qsize())
            all_count=float(self._total)
            Found_count=len(self._result)

            msg='\t[*]完成进度为 {:.2f}%'.format((done_count/all_count)*100).decode('utf-8').encode('gbk')
            sys.stdout.write('\r'+msg)
            sys.stdout.flush()

