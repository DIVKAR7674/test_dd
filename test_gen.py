# from wandb.proto import wandb_internal_pb2
# from wandb.sdk.internal import datastore
import re
import matplotlib.pyplot as plt

path = "/media/diwakar/Data/Office_Work/LAV/wandb/offline-run-20231010_222618-q0pur079/log.txt"

with open(path,'r') as f:
    rr=f.readlines()
    # print(len(rr))
    d1=[]
    # d2=[]
    d3=[]
    d4=[]

    d7=[]
    d8=[]

    d11=[]
    d12=[]
    
    kk=[]
    k=None
    c=1
for i in rr[:]:
    d0=re.findall("Epoch",i)
    # print("###",d0)
    if d0!=[]:
        k=i
    d=re.findall("summary",i)
    d_h=re.findall("history",i)
    if d!=[] or d_h!=[] and c==1:
        print("#")
        d1.append(i)
        kk0=k.split(":")[1][-1]
        print(kk0)
        kk.append(kk0)
        print(len(d1),kk0)
        c+=1
    elif c==2:
        # d2.append(i) k.split(":")[1]
        c+=1
        continue
        
    elif c==3:
        d3.append(i.split(":")[1])   
        c+=1 
    elif c==4:
        d4.append(i.split(":")[1].split("\"")[1])
        c+=1
    elif c==5 or c==6:
        # d2.append(i) 
        c+=1
        continue    

    elif c==7:
        d7.append(i)   
        c+=1 
    elif c==8:
        d8.append(i)   
        c+=1
    elif c==9 or c==10:
        # d2.append(i) 
        c+=1
        continue

    elif c==11:
        d11.append(i)   
        c+=1 
    elif c==12:
        d12.append(i)   
        c=1           
                   
print(d1,d3,d4,kk )#,d7,d8,d11,d12,kk)        
# ds = datastore.DataStore()
# ds.open_for_scan(data_path)

# for _ in range(3):  
#     data = ds.scan_record()
#     pb = wandb_internal_pb2.Record()
#     pb.ParseFromString(data[1])  
#     record_type = pb.WhichOneof("record_type")
#     print(record_type )
#     if record_type == "history":
#         tracked_value_0 = pb.history.item[0].value_json
#         print(tracked_value_0)
#         # and so on


loss_train =[float(i) for i in d4] #history.history['train_loss']

loss_val =[float(i)+2 for i in d4]# history.history['val_loss']

epochs = [int(i) for i in kk]

plt.plot(epochs, loss_train, 'g', label='Training loss')

plt.plot(epochs, loss_val, 'b', label='validation loss')

plt.title('Training and Validation loss')

plt.xlabel('Epochs')

plt.ylabel('Loss')

plt.legend()

plt.show()



###accuracy
# loss_train = history.history['acc']

# loss_val = history.history['val_acc']

# epochs = range(1,11)

# plt.plot(epochs, loss_train, 'g', label='Training accuracy')

# plt.plot(epochs, loss_val, 'b', label='validation accuracy')

# plt.title('Training and Validation accuracy')

# plt.xlabel('Epochs')

# plt.ylabel('Accuracy')

# plt.legend()

# plt.show()