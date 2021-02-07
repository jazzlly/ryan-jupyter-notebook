#%% 空值都是False
bool(True)

#%%
bool(123)

#%%
bool(0)

#%% 
bool(0.)

#%% 
bool('')

#%%
bool(None)

#%%
bool([])

#%%
bool(())

#%%
bool({})

#%%

a = 1
if a > 10:
    print('hahha')
elif a > 5:
    print('huahua')
else:
    print('foobar')

#%%
print('Audi'.lower() == 'audi')

#%%
('audi' == 'audi') and ('bmw' == 'bmw')

#%%
25 in range(2, 28)

#%%
34 not in range(10, 40)