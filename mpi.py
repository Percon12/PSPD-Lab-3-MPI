from mpi4py import MPI

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

number_of_words = 0
cont1 = 0
cont2 = 0

if my_rank != 0:
    with open(r'arq.txt','r') as arq:

        data = arq.read()
        lines = arq.split()
        number_of_words += len(lines)

        for j in lines:
            if j == " " or "\n" or "\t":
                if len(j) < 6:
                    cont1=cont1+1
                elif len(j) >= 6 and len(j) <= 10:
                    cont2=cont2+1
        

        message = "\nMenos que 6: ",cont1 + "\nEntre 6 e 10: ",cont2 + "\nTotal de palavras: ",number_of_words + "\nMeu rank: "+str(my_rank)
        comm.send(message, dest=0)
        arq.close()
else:
    for procid in range (1,p):
        message = comm.recv(source=procid)
        print ("process 0 receives message from process", \
            procid, ":", message)