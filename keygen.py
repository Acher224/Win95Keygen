import sys
import random

def sum_digits(n):
   sum = 0
   while n:
       sum, n = sum + n % 10, n // 10
   return sum

def genSite():
    site = random.randint(000, 999)
    if (site == 333 or site == 444 or site == 555 or site == 666 or site == 777 or site == 888 or site == 999):
        site+=1
        return site
    else:
        return site

def genKey():
    key = 999
    while(sum_digits(key) % 7 != 0):
        key = random.randint(0, 9999999)
    else:
        return key
def genDate():
    return "{0:0=3d}".format(random.randint(0, 366)) + str(random.randint(95, 99))

if ('-c' in sys.argv):
    num = int(sys.argv[sys.argv.index('-c') + 1])
else:
    num = 10
if ('--oem' in sys.argv):
    for x in range(num):
        date = genDate()
        key = "{0:0=7d}".format(genKey())
        padding = "{0:0=5d}".format(random.randint(0, 99999))
        print(f"{date}-OEM-{key}-{padding}")
else:
    for x in range(num):
        site = "{0:0=3d}".format(genSite())
        key = "{0:0=7d}".format(genKey())
        print(f"{site}-{key}")
