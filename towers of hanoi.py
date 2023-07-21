def towers_of_hanoi(disks,source,auxillary,target):
    if disks==1:
        print(f"move disk {disks} from rod{source} to rod{target}")
        
    else:
       towers_of_hanoi(disks-1,source,target,auxillary)
       print(f"move disk {disks} from rod {source} to rod {target}",)
       towers_of_hanoi(disks-1,auxillary,source,target)
    
n= int(input())
towers_of_hanoi(n,"A","B","C")