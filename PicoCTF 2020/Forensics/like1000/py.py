#!/usr/bin/env python3
import tarfile
for i in range(1000, 1, -1):
	k = str(i)
	tf = tarfile.open('tarred/' + k + '.tar')
	tf.extractall('tarred/')
