# -*- coding: utf-8 -*-
"""DGA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LXznbmvDzcQfPhvwo-cdkJB6uh_WZKN8
"""

from torch import FloatTensor
from torch.autograd import Variable
import torch
 
# Definimos los nodos
a1 = Variable(FloatTensor([4]))
a2 = Variable(FloatTensor([3]))
 
# Definimos las variables con gradientes requeridos
w=Variable(FloatTensor([2,5,9,7,3]), requires_grad=True)
 
b1 = w[0] * a1 + w[1] * a2 #b1=2*4+5*3=23
b2 = w[2] * a1 #b2=9*4=36
c = w[3] * b1 + w[4] * b2
L = (15 - c)
 
L.backward()
 
gradient = w.grad.data
for i in range(0, 5):
    print(f"Gradiente de w{i} respecto a L: {gradient[i]}")