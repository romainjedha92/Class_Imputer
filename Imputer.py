{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# IMPUTER voici la première classe créée avec la promotion JEDHA data analytics\n",
    "### C'est le code entier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Imputer():\n",
    "    def __init__(self,data_liste):\n",
    "        self.list=data_liste\n",
    "    def avg(self):\n",
    "        sum_values = 0         \n",
    "        nb_values = 0           \n",
    "        for elt in self.list:  \n",
    "            if elt != None:\n",
    "                sum_values += elt  \n",
    "                nb_values += 1    \n",
    "        replace = sum_values/nb_values     \n",
    "\n",
    "        for i in range(len(self.list)):  \n",
    "            if self.list[i] == None:\n",
    "                self.list[i] = replace\n",
    "        return self.list\n",
    "    \n",
    "    def median(self):             \n",
    "    \n",
    "        new_list=[]              \n",
    "        for elt in self.list:\n",
    "            if elt != None:\n",
    "                new_list.append(elt)\n",
    "        print(new_list)\n",
    "\n",
    "        new_list.sort()          \n",
    "        print(new_list)\n",
    "\n",
    "\n",
    "        nb_values = len(new_list)\n",
    "\n",
    "        if nb_values%2 != 0:\n",
    "            med = new_list[(nb_values-1)// 2]\n",
    "        else:\n",
    "            nb_values%2 == 0\n",
    "            med = (new_list[(nb_values//2)] + new_list[(nb_values//2)-1])/2\n",
    "\n",
    "        for i in range(len(self.list)):\n",
    "            if self.list[i] == None:\n",
    "                self.list[i] = med\n",
    "        return self.list   "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# IMPUTER\n",
    "### Première partie du code avec la moyenne recherché"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Imputer():\n",
    "    def __init__(self,data_liste):\n",
    "        self.list=data_liste\n",
    "    def avg(self):\n",
    "        sum_values = 0         \n",
    "        nb_values = 0           \n",
    "        for elt in self.list:  \n",
    "            if elt != None:\n",
    "                sum_values += elt  \n",
    "                nb_values += 1    \n",
    "        replace = sum_values/nb_values     \n",
    "\n",
    "        for i in range(len(self.list)):  \n",
    "            if self.list[i] == None:\n",
    "                self.list[i] = replace\n",
    "        return self.list"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# IMPUTER\n",
    "### Deuxième partie du code avec la médiane recherché"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Imputer:\n",
    "    def __init__(self,data_liste):\n",
    "        self.list=data_liste\n",
    "    def median(self):             \n",
    "    \n",
    "        new_list=[]              \n",
    "        for elt in self.list:\n",
    "            if elt != None:\n",
    "                new_list.append(elt)\n",
    "        print(new_list)\n",
    "\n",
    "        new_list.sort()          \n",
    "        print(new_list)\n",
    "\n",
    "\n",
    "        nb_values = len(new_list)\n",
    "\n",
    "        if nb_values%2 != 0:\n",
    "            med = new_list[(nb_values-1)// 2]\n",
    "        else:\n",
    "            nb_values%2 == 0\n",
    "            med = (new_list[(nb_values//2)] + new_list[(nb_values//2)-1])/2\n",
    "\n",
    "        for i in range(len(self.list)):\n",
    "            if self.list[i] == None:\n",
    "                self.list[i] = med\n",
    "        return self.list    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.9.13"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
