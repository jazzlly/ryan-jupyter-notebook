#%%
import time

epoch=time.gmtime(0)
type(epoch)

#%%
epoch.tm_gmtoff

#%%
time.time()

#%%
from datetime import datetime

now = datetime.now()
now
