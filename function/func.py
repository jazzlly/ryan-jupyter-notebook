#%% 

f = open('./txt/name.txt', encoding='utf-8')
actors = f.read().split('|')
print(actors)

#%%
fWeapon = open('./txt/weapon.txt', encoding='utf-8')
weapons = fWeapon.read().split()
print(weapons)

#%%

ftxt = open('./txt/sanguo.txt', encoding='GB18030')
txt = ftxt.read().replace('\n','')
print(txt)

#%%
with open('./txt/weapon.txt', encoding='utf-8') as f:
    weapons = f.read().split()
    print(weapons)
