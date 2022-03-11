#!/usr/bin/env python3

#Beispieldatei HelloName.py
import time, locale
name=input('Geben Sie einen Namen an: ')
print('Hallo %s!' % name)

# Datum und Zeit in der aktuellen Zeitzone
locale.setlocale(locale.LC_ALL, '')
time = time.strftime('Heute ist %A, der %d. %B.')
print(time)

