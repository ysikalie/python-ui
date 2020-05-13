# coding: utf-8
#
import uiautomator2 as u2
import time

d = u2.connect()
def process(i):
    d = u2.connect()

    d.click(0.657, 0.907)
    time.sleep(0.5)
    d.click(0.102, 0.869)
    time.sleep(0.5)
    d.click(0.724, 0.067)

    time.sleep(0.5)
    d.send_keys('%d.jpg' % i, True)
    time.sleep(0.5)
    d.click(0.724, 0.067)
    time.sleep(0.5)
    d.click(0.608, 0.202)
    time.sleep(0.5)
    d.click(0.608, 0.202)
    time.sleep(0.5)
    d.click(0.52, 0.427)


    time.sleep(4)

    d.screenshot(r"C:\Users\TAL\Desktop\screenshot\%d.jpg" % i)


    #删除
    d.click(0.28, 0.962)
    time.sleep(2)
    d.click(0.733, 0.427)
    time.sleep(2)
    d.click(0.511, 0.063)
    time.sleep(2)
    d.send_keys("%d.jpg" % i, True)
    time.sleep(2)
    d.click(0.297, 0.061)
    time.sleep(2)
    d.click(0.92, 0.2)
    time.sleep(2)
    d.click(0.688, 0.894)
    time.sleep(2)
    d.click(0.751, 0.888)
    time.sleep(2)
    d.click(0.266, 0.97)
    time.sleep(2)
    d.click(0.733, 0.526)









def main():
    for i in range(9, 0, -1):
        process(i)

main()
