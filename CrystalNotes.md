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

For Masif crystal, should we split every chain? Or not split any chains? For the moment assume all chains are used.  
The chemical conditions label for each pdb will be stored in the folder as ``conds.npy``. To start with we are predicting if PEG is present or not. Therefore the labels can be categorical ["has PEG", "no PEG"]. Next could try to predict which type of PEG which is still categorical: ["PEG 3000", "PEG 10000", ...].

 => file structure is:
```
data_preperation 
    04a-precomputation_9A  
        precomputation  
            1AKJ  
                input_feat.npy 
                ...  
            ...  
```