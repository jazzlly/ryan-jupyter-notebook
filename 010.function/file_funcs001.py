#%%

with open('./txt/name.txt',mode='r', encoding='utf-8') as sanguo:
    actors = sanguo.read().split('|')
    print(actors)

#%% read lines

with open('./txt/weapon.txt', mode='r', encoding='utf-8') as weapons:
    for w in weapons:
        w = w.strip()
        if w:
            print(w)

#%%
with open('./txt/weapon.txt', mode='r', encoding='utf-8') as weapons:
    lines = weapons.readlines();

for line in lines:
    line = line.rstrip();
    if line:
        print(line)
            
#%%
f = open('./txt/name.txt', encoding='utf-8')
actors = f.read().split('|')
print(actors)

#%%
fWeapon = open('./txt/weapon.txt', encoding='utf-8')
weapons = fWeapon.read().split() # split all white space
print(weapons)

#%%

ftxt = open('./txt/sanguo.txt', encoding='GB18030')
txt = ftxt.read().replace('\n','')
print(txt)

#%%
with open('./txt/weapon.txt', encoding='utf-8') as f:
    weapons = f.read().split()
    print(weapons)

#%%
import re

with open('./txt/sanguo.txt', encoding='GB18030') as f:
    sanguo = f.read().replace('\n','')

    all = re.findall('諸葛亮', sanguo)
    print(len(all))