# -*- coding: utf-8 -*-
"""Genetic Algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_vkiPPS661PInO87gmUg0-RdprQRV70
"""

import numpy as np
import math
import random

#a+2b+3c+4d=30

class Algoritma_Genetika :
  jum_chrom = 6
  gen = ["a", "b", "c", "d"]
  nilai_per_gen = {
      'min' : 0, 'max' : 10
  }

  crossover_rate = 50/100
  mutasi_rate = 10/100
  total_gen = 24

  next_gen = np.arange(4)
  stop = False

  def __init__(self):
    self.first_chrom = np.random.randint(low=self.nilai_per_gen['min'], high=self.nilai_per_gen['max'], size=(self.jum_chrom, len(self.gen)))
    print("INISIALISASI")
    print(self.first_chrom)
    print("")

  def evaluasi_chrom(self, chrom, generasi):
    print("GENERASI ["+str(generasi)+"]")

    jum_chromo = len(chrom)
    o = np.arange(jum_chromo)
    fitness = np.arange(jum_chromo, dtype='f')

    for x in range(len(chrom)):
      fo = abs((chrom[x][0]+2*chrom[x][1]+3*chrom[x][2]+4*chrom[x][3])-30)
      o[x] = fo

      fitn = 1/(fo+1)

      fitness[x] = fitn
      if(fitn == 1):
        self.stop = True
      print("KROMOSOM {0} : {1}, fitness = {2}".format(x, np.array2string(chrom[x], separator=','), fitn))
    print("FITNESS SELESAI")
    print(o)

    Probab = np.arange(jum_chromo, dtype='f')
    total_fitness = fitness.sum()
    Probab = fitness / total_fitness
    print("Total Fitness : {}".format(str(total_fitness)))
    print("Rata-rata Fitness : {}".format(str(np.average(fitness))))
    print("Probabilitas : {}".format(np.array2string(Probab, separator=',')))
    print("Probablitias Tertinggi : {}, Pada Kromosom ke {}".format(Probab[Probab.argmax()], str(Probab.argmax())))
    print("Kromosom yang mungkin terpilih : {}".format(np.array2string(chrom[Probab.argmax()], separator=',')))
    print("")
    print("")
    self.next_gen = chrom[Probab.argmax()]

    C = np.arange(jum_chromo, dtype='f')
    total_x = 0
    for x in range(len(Probab)):
      total_x += Probab[x]
      C[x] = total_x

    R = np.random.sample(len(fitness))
    chrom_baru = np.arange(jum_chromo*len(self.gen)).reshape(jum_chromo, len(self.gen))

    for y in range(len(R)):
      for k in range(len(chrom_baru)):
        if(R[y] < C[0]):
          chrom_baru[y] = chrom[0]
        elif((C[k-1] < R[y]) & (R[y] < C[k])):
          chrom_baru[y] = chrom[k]

    R = np.random.sample(jum_chromo)
    index_chrom_parent = []
    for p in range(len(R)):
      if(R[p] < self.crossover_rate):
        index_chrom_parent.append(p)

    posisi_cros = np.random.randint(low=1, high=len(self.gen), size=len(index_chrom_parent))

    offspring = np.arange(len(self.gen)*len(index_chrom_parent)).reshape(len(index_chrom_parent), len(self.gen))
    for i_parent in range(len(index_chrom_parent)):
      index_chrome_1 = index_chrom_parent[i_parent]
      if(i_parent == len(index_chrom_parent)-1):
        index_chrome_2 = index_chrom_parent[0]
      else:
        index_chrome_2 = index_chrom_parent[i_parent+1]
      cut_point = posisi_cros[i_parent]
      for p in range(len(chrom_baru[index_chrome_1])):
        if(p >= posisi_cros[i_parent]):
          offspring[i_parent][p] = chrom_baru[index_chrome_2][p]
        else:
          offspring[i_parent][p] = chrom_baru[index_chrome_1][p]
    
    for x in range(len(offspring)):
      chrom_baru[index_chrom_parent[x]] = offspring[x]
    
    total_gen = len(chrom) * len(chrom[0])
    jum_mutasi = self.mutasi_rate * total_gen
    jum_mutasi = int(jum_mutasi)

    random_i_mutasi = np.random.randint(low=0, high=total_gen, size=jum_mutasi)

    for x in range(len(random_i_mutasi)):
      index_mutasi = random_i_mutasi[x]
      byk_kromosom = len(chrom)
      byk_gen = len(chrom[0])
      random_value = random.randint(self.nilai_per_gen['min'], self.nilai_per_gen['max'])
      if(index_mutasi <= byk_gen):
        chrom_baru[0][index_mutasi-1]
      else:
        posisi_y = index_mutasi/byk_gen
        posisi_y = int(posisi_y)
        posisi_x = index_mutasi % byk_gen
        chrom_baru[posisi_y][posisi_x] = random_value
    return chrom_baru

  def do_now(self):
    chromosome_current = self.first_chrom
    for generasi in range(0, self.total_gen):
      if(self.stop != True):
        chromosome_current = self.evaluasi_chrom(chromosome_current, generasi)
    print("")
    print("Kromosom Tertinggi dan Terbaik adalah")
    print(self.next_gen)

run = Algoritma_Genetika()
run.do_now()