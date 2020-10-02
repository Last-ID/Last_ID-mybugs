#!/usr/bin/python3
#c:/Users/Funny/mybugs/FullLoliFinder.py
#用于寻找萝莉杀手['id': '11d5ce25-d16f-49b4-ad3b-6266b41d0d2a', 'name': 'Loli_Wolf']

time_action_start =time.perf_counter()
try:
    action("C:\Users\Funny\AppData\Roaming\Tencent\QQ\Temp\4R06U%0W$5J$15HJ5C6`Q15.png",''id': '11d5ce25-d16f-49b4-ad3b-6266b41d0d2a', 'name': 'Loli_Wolf'','1')
except IOError as e:
    print("Error exception: %s: %s" %(e.errno, e.strerror))
else:
    print('无结果')
finally:
    print('Running time: %s (sec)'%(time_action_end-time_action_start))
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) +' [Done!]')
    time.sleep(120)
PS C:\Users\Funny> & C:/Users/Funny/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Funny/mybugs/FullLoliFinder.py
find exception: 10060: 由于被搜寻目标在一段时间后没有正确答复或目标萝莉没有反应，寻找尝试失败。
Running time: 0.1682404000000588 (sec)
Thu Oct 01 16:35:45 2020 [Done!]