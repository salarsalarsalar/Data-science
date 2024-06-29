{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0b23854d",
   "metadata": {},
   "source": [
    "# NumPy Assignment"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1daa8418",
   "metadata": {},
   "source": [
    "# Q1: Find the counts of unique values row-wise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "6f498c4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 9,  9,  4,  8,  8,  1,  5,  3,  6,  3],\n",
       "       [ 3,  3,  2,  1,  9,  5,  1, 10,  7,  3],\n",
       "       [ 5,  2,  6,  4,  5,  5,  4,  8,  2,  2],\n",
       "       [ 8,  8,  1,  3, 10, 10,  4,  3,  6,  9],\n",
       "       [ 2,  1,  8,  7,  3,  1,  9,  3,  6,  2],\n",
       "       [ 9,  2,  6,  5,  3,  9,  4,  6,  1, 10]])"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.random.seed(100)\n",
    "arr = np.random.randint(1,11,size=(6, 10))\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 287,
   "id": "dbc704d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 2, 1, 1, 1, 0, 2, 2, 0],\n",
       "       [2, 1, 3, 0, 1, 0, 1, 0, 1, 1],\n",
       "       [0, 3, 0, 2, 3, 1, 0, 1, 0, 0],\n",
       "       [1, 0, 2, 1, 0, 1, 0, 2, 1, 2],\n",
       "       [2, 2, 2, 0, 0, 1, 1, 1, 1, 0],\n",
       "       [1, 1, 1, 1, 1, 2, 0, 0, 2, 1]])"
      ]
     },
     "execution_count": 287,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Output for just above example\n",
    "e"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 326,
   "id": "3c3e8f81-52a4-4d10-921f-298c25b99720",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "0\n",
      "2\n",
      "1\n",
      "1\n",
      "1\n",
      "0\n",
      "2\n",
      "2\n",
      "0\n",
      "2\n",
      "1\n",
      "3\n",
      "0\n",
      "1\n",
      "0\n",
      "1\n",
      "0\n",
      "1\n",
      "0\n",
      "0\n",
      "3\n",
      "0\n",
      "2\n",
      "3\n",
      "1\n",
      "0\n",
      "1\n",
      "0\n",
      "0\n",
      "1\n",
      "0\n",
      "2\n",
      "1\n",
      "0\n",
      "1\n",
      "0\n",
      "2\n",
      "1\n",
      "0\n",
      "2\n",
      "2\n",
      "2\n",
      "0\n",
      "0\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# li = []\n",
    "# for i in range(len(arr)):\n",
    "#     lis = arr[i,:]\n",
    "#     unique,count = np.unique(lis, return_counts =True)\n",
    "#     li.append(count)\n",
    "# li\n",
    "\n",
    "li = np.arange(0,11)\n",
    "a = np.sort(arr)\n",
    "for i in (range(len(a)-1)):\n",
    "    for j in (range(len(a[i]))):\n",
    "        b=np.count_nonzero(a[i] == li[j])\n",
    "        print(b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "id": "e5554e27-85a5-46d2-8faa-2111b3bdee24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  3,  3,  4,  5,  6,  8,  8,  9,  9],\n",
       "       [ 1,  1,  2,  3,  3,  3,  5,  7,  9, 10],\n",
       "       [ 2,  2,  2,  4,  4,  5,  5,  5,  6,  8],\n",
       "       [ 1,  3,  3,  4,  6,  8,  8,  9, 10, 10],\n",
       "       [ 1,  1,  2,  2,  3,  3,  6,  7,  8,  9],\n",
       "       [ 1,  2,  3,  4,  5,  6,  6,  9,  9, 10]])"
      ]
     },
     "execution_count": 280,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "id": "6e66bb23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60"
      ]
     },
     "execution_count": 305,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#your code here\n",
    "b = np.array(range(1,11))\n",
    "a = np.sort(arr)\n",
    "c = np.count_nonzero(a)\n",
    "c"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "257be926",
   "metadata": {},
   "source": [
    "Your Output should have 10 columns (numbers from 1 to 10). The values are the counts of the numbers in the respective rows.\n",
    "For example, Cell(0,8) has the value 2, which means, the number 8 occurs exactly 2 times in the 1st row."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a123cd8c",
   "metadata": {},
   "source": [
    "# Q2: Create this pattern of zeros and ones using only slicing approach. Your code must not be more than 6 lines."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "673dc537",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "2ebf5162",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 0, 1, 0, 1, 0, 1, 0, 1],\n",
       "       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],\n",
       "       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],\n",
       "       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],\n",
       "       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],\n",
       "       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],\n",
       "       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],\n",
       "       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],\n",
       "       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],\n",
       "       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]])"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#your code here\n",
    "n = 10\n",
    "arr = np.zeros((n, n), dtype = int)\n",
    "arr[0:n:2,1:n:2] = 1\n",
    "arr[1:n:2,0:n:2] = 1\n",
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "309724c9",
   "metadata": {},
   "source": [
    "# Q3: Given below a Numpy Array, display odd rows and even columns. you are not allowed to use loop. Do it with slicing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "125349c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy\n",
    "sampleArray = numpy.array([[3 ,8, 9, 11], [15 ,18, 21, 24], \n",
    "[27 ,29, 33, 34], [39 ,42, 45, 48], [51 ,52, 57, 53]]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "cd94a6c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 8, 11],\n",
       "       [29, 34],\n",
       "       [52, 53]])"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#your code here\n",
    "sampleArray[::2, 1::2]#2 steps in rows, start from 1 in column and step is 2 in column"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6be141a",
   "metadata": {},
   "source": [
    "# Q4: Detecting all the humps in a 1 Dimentional np array. Humps are values encircled by lower values on both sides. Use NumPy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3db0278e",
   "metadata": {},
   "source": [
    "Input: np.array([1,2,9,1,3,7,1,2,10])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "451efc8b",
   "metadata": {},
   "source": [
    "Output: 9, 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "id": "ca67df3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 7]"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#your code here\n",
    "n=len(a)\n",
    "# t = n-2\n",
    "# t2 =1\n",
    "a1=np.array([1,2,9,1,3,7,1,2,10])\n",
    "# a[1]\n",
    "# a[7]\n",
    "# a1[t]\n",
    "# a1[t2]\n",
    "li = []\n",
    "for i in range(len(a1)-1):\n",
    "    if (a1[i]>a1[i-1]) & (a1[i]>a1[i+1]):\n",
    "        li.append(a1[i])\n",
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "494a9810-e3bb-43de-8421-07fd7423e2fa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
