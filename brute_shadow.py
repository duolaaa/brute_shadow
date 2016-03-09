#! /usr/bin/env python
#-*- coding: utf-8 -*-
import os
import hashlib
import crypt
import click

def openfile(filename):
	if filename == None:
		print "please input all the file or --help \n"
		exit(0)
	if not os.path.isfile(filename):
		print '[-] ' + filename + ' does not exist!'
		exit(0)

	if not os.access(filename,os.R_OK):
		print '[-] ' + filename + ' access denied!'
		exit(0)

def splitpass(passstr):
	n = passstr.find('$',3)
	return n+1

def crack(dic,shadow):
	print "======================================= "
	openfile(dic)
	openfile(shadow)
	for line in open(shadow):
		if ('*' not in line) and ('!' not in line):
			shadowline = line.split(':',2)
			username = shadowline[0]
			password = shadowline[1]
			salt = password[0:splitpass(password)]

			for dicwords in open(dic):
				dicwords = dicwords.strip()
				print "[-] username:" + username + "  password:"+dicwords

				if crypt.crypt(dicwords,salt) == password:
					print "[+] username:" + username + "  password:"+dicwords + "  has been cracked"


@click.command()
@click.option('--path','-p', help='path of dic')
@click.option('--shadow','-s', help='path of shadow')

def GetPath(path,shadow):
	crack(path,shadow)


if __name__ == '__main__':
	GetPath()