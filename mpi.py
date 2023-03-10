from mpi4py import MPI
import string
import random

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

number_of_words = 0
cont1 = 0
cont2 = 0

if my_rank != 0:

    number_of_strings = random.randint(1,660000)

    arq =  open('arq.txt','w')
    for x in range(number_of_strings):
        length_of_string = random.randint(1,15)
        arq.write(''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in range(length_of_string)))
    arq.close()

    arq =  open('arq.txt')
    arqread = arq.read()
    lines = arqread.split()
    number_of_words += len(lines)
    for j in lines:
        #print("entrei no for")
        if j == " " or "\n" or "\t":
            if len(j) < 6:
                cont1=cont1+1
            elif len(j) >= 6 and len(j) <= 10:
                cont2=cont2+1
    arq.close()

    message = "\nMenos que 6: "+str(cont1) + "\nEntre 6 e 10: "+str(cont2) + "\nTotal de palavras: "+str(number_of_words) + "\nMeu rank: "+str(my_rank)
    comm.send(message, dest=0)
else:
    for procid in range (1,p):
        message = comm.recv(source=procid)
        print ("Proc ID:",procid, message)
        print("\n")