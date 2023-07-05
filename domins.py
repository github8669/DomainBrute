# coding=utf-8
from utils.crt import Crt
from utils.ilink import link
from utils.brutedns import BruteDns
from utils.configs.common import save_result,read_json
from optparse import OptionParser
from threading import Thread, current_thread

import  sys
import os

def option(domain):
    outfile = '{0}.log'.format(domain)

    script_path = os.path.dirname(os.path.abspath(__file__))

    _cache_path = os.path.join(script_path, 'result\{0}'.format(domain))
    if not os.path.exists(_cache_path):
        os.makedirs(_cache_path)

    print '[*]开始扫描{}相关的子域名....'.format(domain).decode('utf-8').encode('gbk')
    result = Crt(domain).run()
    _cache_file = os.path.join(_cache_path, 'crt.json')
    save_result(_cache_file, result)
    crtt=len(result)
    result1 = link(domain).run()
    _cache_file = os.path.join(_cache_path, 'ilink.json')
    save_result(_cache_file, result1)

    result2= BruteDns(domain).run()
    _cache_file = os.path.join(_cache_path, 'brute.json')
    save_result(_cache_file, result2)
    result3=result+result1+result2
    print '\n\t[*]总共 发现 {}个子域名'.format(str(len(result3))).decode('utf-8').encode('gbk')

    _cache_files = ['crt.json', 'ilink.json', 'brute.json']
    subdomins = []
    for file in _cache_files:
        _cache_file = os.path.join(_cache_path, file)
        json_data = read_json(_cache_file)
        if json_data:
            subdomins.extend(json_data)
    subdomins = list(set(subdomins))
    _result_file = os.path.join(script_path, outfile)
    save_result(_result_file, subdomins)
    print '相关子域名已经保存到 {2}'.format(domain, len(subdomins), _result_file).decode('utf-8').encode('gbk')

def run(options):
    # print options.filename
    with open( options.filename,'r') as fi:
        fil=fi.readlines()
        for file in fil:
            domain=file.strip('\n').strip(' ')
            option(domain)






def main():

    print '''
                   Author: xiaoyu   version: 1.0

         ___                 _      ___          _
        |   \ ___ _ __  __ _(_)_ _ | _ )_ _ _  _| |_ ___
        | |) / _ \ '  \/ _` | | ' \| _ \ '_| || |  _/ -_)
        |___/\___/_|_|_\__,_|_|_||_|___/_|  \_,_|\__\___|

           '''

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="target url for scan")
    parser.add_option("-f", "--file", dest="filename", help="file filename",metavar="file")
    parser.add_option("-t", "--thread", dest="count", type=int, default=10, help="scan thread_count")
    (options, args) = parser.parse_args()
    if options.filename:
        thread01 = Thread(target=run, args=(options,), name="t1")
        thread01.start()

        sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)
if __name__ == '__main__':

    main()





































































































