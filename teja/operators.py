""" For practising operators examples"""
import copy
from util import logger
import requests  # Web scraping
import paramiko  # to connect remote machine over ssh/telenet/scp then run command and get o/p
# =============== Arithmetic ================ #


logger = logger.get_logger()

a = 4
b = 2

logger.info(a + b)
logger.info(a - b)
logger.info(a / b)  # Python3 2.0 python2 2
logger.info(a // b)
logger.info(a % b)
logger.info(a ** b)

logger.info(3 / 2)    # 1.5
logger.info(3 // 2)   # 1
logger.info(3 // 2.0)  # 1.0

# ============== Assignment Operators ============= #
a = 4
a += 2  # 6  -> a = a + 2
logger.info(a)
a -= 2  # a -= 2  ->  a = a -2 -> 4
logger.info(a)
a *=2  # a = a * 2
#
# # ================= Relational Operators ================== #
# success_code = 200
# response_code = 500
logger.info(1 == 2)
logger.info("python" == "java")

res = requests.get("http://www.engineersindia.com")
logger.info(res.status_code)

logger.info(res.text)

logger.info(res.status_code == 200)
logger.info(res.status_code != 200)
logger.info(1 > 2)
logger.info(1 < 2)
logger.info(1 >= 2)
logger.info(1 <= 2)
logger.info("java" == "avaj")
#
# # ================== Logical/ Conditional Operators =========== #
# and or not
# && ||

# False -> zero number, and empty string, list, tuple, dictionary, set, frozenset, and None
# True

# not will change boolean value False to True and True to False
# =========== and ============= #
# if both True -> True
# else False
# 1 and 2 -> 2

# ============== or ============ #
# if any condition is True -> True
# else False
# 1 or 2 -> 1


status = []   # False
dict1 = {"1":22, "2":33}
# dict1 = {}
if not dict1:
    logger.error("Dictionary is Empty")
    logger.info("Program is exiting.....")
    exit()

logger.info(not status)  # True
logger.info(not "")     # True
logger.info(not 1)      # False
logger.info( not None)  # True
# status_code = 500
logger.info([] and 2)  # False > [] -> []
logger.info([] and 2)   # False -> []
logger.info(1 or [] )  # True -> 1
#
logger.info("status_code %s",res.status_code)

if res.status_code == 200 or res.status_code == 300:
    logger.info("Connection is succesful")
    logger.info(res.content)

elif res.status_code >=400 and res.status_code < 500:
    logger.error("Client side error")

elif res.status_code >=500 and res.status_code <600:
    logger.error(("Server side error"))



logger.info(1 and 2 )   # 2
logger.info("hello" and "World") # World
logger.info(1 or 2 ) # 1

# dict1 = {"1":"hello"}
dict1 = {}
content = dict1 and dict1["1"]
# content = dict1["1"]
logger.info(content)

# if dict1:
#     content = dict1["1"]
#
# if content:




# #
# # a = 1
# # a = a+1
# # #
# # a and a+1 and logger.info(a)
# #
# # # ==================== Membership Operators ================ #
# logger.info("p" in "python")
# logger.info("p" not in "python")
# logger.info("python" in "p")  # False
# logger.info("emp1" in {"emp1":1 , "emp2":2})
# logger.info(1 in {"emp1":1 , "emp2":2})  # False Note: key existence
# #
# #
# # # ====================== #
# a = 1
# b =1
# logger.info(a is b)
# logger.info(id(a) == id(b))
#
# logger.info(a is not b)  #= Address Identity Operator ============ #
# a = 1
#
# list1 = [1, 2, 3]
# list2 = copy.deepcopy(list1)
# logger.info(list1 is list2)  # False
# logger.info(list1 == list2)  # True
# #
# # # ========================== Bitwise Operators =================== #
# a = 1
# b = 2
# logger.info(a & b)
# logger.info(a | b)
#
# logger.info(a << 1)   # 0 0 0 1 << 2 -> 0 0 1 0 -> 3
# logger.info(a >> 1)   # 0 0 0 1 >> 2 -> 0 0 0 0 -> 0
# #
# # ~, ^
#
# # =================  Operator Precedence ========================== #
# logger.info( not 0)  # True
# logger.info( not 1)  # False
# logger.info(0 and 1)   # 0
# logger.info( 1 and 20)   # 20
# logger.info({} and [])   # {}
# logger.info({} or 6)    # 6
#
# # logger.info({} and 6)   # {}
# # logger.info({} or 6)    # 6
# # logger.info(6 and {})   # {}
# # logger.info(6 or {})    # 6
# #
# # logger.info(6 and 7)   # 7
# # logger.info(6 or 7)     # 6
# #
# #
# r = 13 and {} and 5  or [] and 6  # {} and 5 or [] and 6 -> {} or [] and 6 -> {} or [] -> []
# logger.info(r)
# r = 22 and [] or 32 and 0 or 67  # [] or 32 and 0 or 67 -> [] or 0 or 67  -> 0 or 67 -> 67
# logger.info(r)
