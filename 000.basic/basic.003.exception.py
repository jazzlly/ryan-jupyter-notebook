
#%%
'''
try:
    < 语句 >
except  [(Error1, Error2, ...)[as e]]:
    < 语句 >  # 如果在try中引发了'Error1'异常
except  [(Error3, Error4, ...)[as e]]:
    < 语句 >  # 如果在try中引发了'Error3'异常
except Exception as e:
    < 语句 > # Exception是通用的异常
except:
    < 语句 >  # 如果在try中引发了其他异常
'''

#%%
try:
    year = int(input("请输入年份："))
    print(year)
except ValueError:
    print("年份必须是数字")

#%%
try:
    raise ValueError('foobar')
except ValueError:
    print("got foo error!")

#%% 

try:
    f = open('a.html', 'r')
except Exception as e:
    print(e)
finally:
    # f.close()
    print('foobar')




#%%

# 使用traceback可查看异常详细信息
import traceback as tb

try:
    import urllib.request
    req = urllib.request.urlopen('http://www.paidu.com')
    print(req.read())
except FloatingPointError:
    print("Capture FloatingPointError")
except IOError as e:
    print("Capture IOError")
    print(e.args)
    print(e.errno)
    print(e.strerror)
    tb.print_exc(file=sys.stderr)
except Exception:
    print("Capture Error")
except:
    print("Capture Error")


#%% zero exception

def func(num):
  try:
    return 42/num
  except ZeroDivisionError:
    print('Error: Invalid argument!')

func(0)

#%% file not found!

try:
  f = open('a.html', 'r')
  print(f.read())
except FileNotFoundError:
    print("file not found!")

#%% file not found!

# 简化写法
try:
    with open('a.html', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('file not found!')