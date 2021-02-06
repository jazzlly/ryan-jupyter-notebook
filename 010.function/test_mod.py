
def bar(**kvargs):
    for k,v in kvargs.items():
        print(f'key: {k}, value: {v}')
    
def foo(*args):
    for v in args:
        print(f'args: {v}')
