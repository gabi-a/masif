Masif site splits up PDB ids into two pairs (since the point is interaction sites).
E.g. 1AKJ_AB_DE:  
chains AB -> p1  
chains DE -> p2  
Hence the file structure ends up as:  
```
data_preperation
    04a-precomputation_9A
        precomputation
            1AKJ_AB_DE
                p1_iface_labels.npy  
                p2_iface_labels.npy  
                ...  
            ...  
```

For Masif crystal, should we split every chain? Or not split any chains?
