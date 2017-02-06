list = ["5mil", "10mil","20mil","30mil","40mil","50mil"]

for depth in list:
    RNF43_659fs_list = []
    RNF43_117fs_list = []
    RNF43_659fs_COF = 0
    RNF43_659fs_LOF = 0
    RNF43_659fs_GOF = 0
    RNF43_659fs_Neutral = 0
    RNF43_117fs_COF = 0
    RNF43_117fs_LOF = 0
    RNF43_117fs_GOF = 0
    RNF43_117fs_Neutral = 0
    for i in range(100):
        f = open("/scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_predict_0.05.txt", "r")
        f_out= open("/scratch/althornt/eVIP/eVIP_"+str(depth)+"/RNF43_eVIP_count.txt","w")
        for line in f:
            if line.split()[1] == "RNF43_659fs":
                RNF43_659fs_list.append(line.split()[13])
                if line.split()[13] == "COF":
                    RNF43_659fs_COF +=1
                if line.split()[13] == "GOF":
                    RNF43_659fs_GOF += 1
                if line.split()[13] == "LOF":
                    RNF43_659fs_LOF += 1
                if line.split()[13] == "Neutral":
                    RNF43_659fs_Neutral += 1
            if line.split()[1] == "RNF43_117fs":
                RNF43_117fs_list.append(line.split()[13])
                if line.split()[13] == "COF":
                    RNF43_117fs_COF += 1
                if line.split()[13] == "GOF":
                    RNF43_117fs_GOF += 1
                if line.split()[13] == "LOF":
                    RNF43_117fs_LOF += 1
                if line.split()[13] == "Neutral":
                    RNF43_117fs_Neutral += 1
    f_out.writelines("RNF43_659fs_COF:"+str(RNF43_659fs_COF)+"\n")
    f_out.writelines("RNF43_659fs_LOF:"+str(RNF43_659fs_LOF)+"\n")
    f_out.writelines("RNF43_659fs_GOF:"+str(RNF43_659fs_GOF)+"\n")
    f_out.writelines("RNF43_659fs_Neutral:"+str(RNF43_659fs_Neutral)+"\n")
    f_out.writelines("RNF43_117fs_COF:"+str(RNF43_117fs_COF)+"\n")
    f_out.writelines("RNF43_117fs_LOF:"+str(RNF43_117fs_LOF)+"\n")
    f_out.writelines("RNF43_117fs_GOF:"+str(RNF43_117fs_GOF)+"\n")
    f_out.writelines("RNF43_117fs_Neutral:"+str(RNF43_117fs_Neutral)+"\n")
