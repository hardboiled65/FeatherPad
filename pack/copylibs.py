#!/usr/bin/env python3
import os
import subprocess
import shutil
import re

def parse_excludelist(text):
    l = []
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            continue
        if line == '':
            continue
        line = re.sub(' *#.*', '', line)
        l.append(line)
    return l

try:
    f = open('excludelist', 'r')
    excludelist_text = f.read()
    f.close()
except FileNotFoundError:
    print('excludelist file not found. Please run download.sh first.')
excludelist = parse_excludelist(excludelist_text)


ldd_result = subprocess.run(
    ['ldd', 'FeatherPad.AppDir/usr/bin/featherpad'],
    stdout=subprocess.PIPE
)

ldd = {}
ldd_result = ldd_result.stdout.decode()
for ldd_line in ldd_result.split('\n'):
    ldd_line = ldd_line.strip()
    kv = ldd_line.split(' => ')
    # Pass linux-vdso.so.1
    if len(kv) == 1:
        pass
    else:
        k = kv[0]
        v = kv[1]
        v = re.sub(' \(.*\)', '', v)
        if k == '/lib64/ld-linux-x86-64.so.2':
            continue
        if k in excludelist:
            continue
        print(f'{k}: copy {v}')
        shutil.copyfile(v, 'FeatherPad.AppDir/usr/lib/' + os.path.basename(v))
        shutil.copymode(v, 'FeatherPad.AppDir/usr/lib/' + os.path.basename(v))
