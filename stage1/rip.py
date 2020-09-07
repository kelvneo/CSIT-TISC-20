#!/usr/bin/python3
import subprocess
import os
import sys

i = int(sys.argv[1])
while True:
    ftype_cmd = subprocess.run(['file', '-b', '{}'.format(i)], stdout=subprocess.PIPE)
    ftype = ftype_cmd.stdout.decode('utf-8').split()[0]
    if ftype == 'ASCII':
        if 'lines' in ftype_cmd.stdout.decode('utf-8').split():
            nxt_cmd = os.system('base64 -d {} > {}'.format(i, i + 1))
            print(i, 'is a base 64 ASCII file')
        else:
            nxt_cmd = subprocess.run(['xxd', '-r', '-p', '{}'.format(i), '{}'.format(i + 1)], stdout=subprocess.PIPE)
            print(i, 'is a hex ASCII file')
    elif ftype == 'gzip':
        nxt_cmd = subprocess.run(['cp', '{}'.format(i), '{}.gz'.format(i + 1)], stdout=subprocess.PIPE)
        nxt_cmd = subprocess.run(['gzip', '-d', '{}.gz'.format(i + 1)], stdout=subprocess.PIPE)
        print(i, 'is a gzip file')
    elif ftype == 'bzip2':
        nxt_cmd = subprocess.run(['cp', '{}'.format(i), '{}.bz'.format(i + 1)], stdout=subprocess.PIPE)
        nxt_cmd = subprocess.run(['bzip2', '-d', '{}.bz'.format(i + 1)], stdout=subprocess.PIPE)
        print(i, 'is a bzip file')
    elif ftype == 'XZ':
        nxt_cmd = subprocess.run(['mv', '{}'.format(i), '{}.xz'.format(i + 1)], stdout=subprocess.PIPE)
        nxt_cmd = subprocess.run(['xz', '-d', '{}.xz'.format(i + 1)], stdout=subprocess.PIPE)
        print(i, 'is a XZ file')
    elif ftype == 'zlib':
        nxt_cmd = subprocess.run(['mv', '{}'.format(i), '{}.zz'.format(i + 1)], stdout=subprocess.PIPE)
        nxt_cmd = subprocess.run(['pigz', '-d', '-z', '{}.zz'.format(i + 1)], stdout=subprocess.PIPE)
        #os.system("printf '\\x1f\\x8b\\08\\x00\\x00\\x00\\x00\\x00' | cat - {} | gzip -dc > {}".format(i, i+1))
        #os.system('/bin/bash -i -c "dczlib {} {}"'.format(i, i + 1))
        #nxt_cmd = subprocess.run(['printf', '"\\x1f\\x8b\\x08\\x00\\x00\\x00\\x00\\x00"', "|", "cat", "-" , "{}".format(i), "|", "gzip", '-dc', '>', '{}'.format(i + 1)], stdout=subprocess.PIPE)
        #nxt_cmd = subprocess.run(['dczlib', '{}'.format(i), '{}'.format(i + 1)], stdout=subprocess.PIPE, shell=True)
        print(i, 'is a zlib file')
    else:
        print('Could not decode:', ftype)
        print(ftype_cmd.stdout.decode('utf-8'))
        break
    i += 1

