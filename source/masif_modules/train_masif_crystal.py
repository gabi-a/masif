import time
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np

# Apply mask to input_feat
def mask_input_feat(input_feat, mask):
    mymask = np.where(np.array(mask) == 0.0)[0]
    return np.delete(input_feat, mymask, axis=2)

def pad_indices(indices, max_verts):
    padded_ix = np.zeros((len(indices), max_verts), dtype=int)
    for patch_ix in range(len(indices)):
        padded_ix[patch_ix] = np.concatenate(
            [indices[patch_ix], [patch_ix] * (max_verts - len(indices[patch_ix]))]
        )
    return padded_ix

def train_test_val_split(X, test_size, val_size):
    """
    test_size is the proportion of X to be used for testing
    val_size is the proportion of X_train to be used for validation
    
    e.g. test_size = 0.4
         val_size = 0.2

         results in a split of test / val / train = 0.54 / 0.06 / 0.4
    """

    X_, X_test = train_test_split(X, test_size=test_size)
    X_train, X_val = train_test_split(X_, test_size=X_val)
    return X_train, X_val, X_test

def train_masif_site(
    learning_obj,
    params,
    batch_size=100,
    num_iterations=100,
):

    out_dir = params["model_dir"]
    logfile = open(os.path.join(out_dir, "log.txt"), "w")
    for key in params:
        logfile.write(f"{key}: {params[key]}\n")

    data_dirs = os.listdir(params["masif_precomputation_dir"])

    X_train, X_val, X_test = train_test_val_split(data_dirs, test_size=0.3, val_size=0.1)

    for pdbdir in X_train:
        # mydir = params["masif_precomputation_dir"] + pdbdir
        # pdbid, chains = pdbdir.split("_")
        
        rho_wrt_center = np.load(os.path.join(pdbdir, "rho_wrt_center.npy"))
        theta_wrt_center = np.load(os.path.join(pdbdir, "theta_wrt_center.npy"))
        input_feat = np.load(os.path.join(pdbdir, "input_feat.npy"))
        if np.sum(params["feat_mask"]) < 5:
            input_feat = mask_input_feat(input_feat, params["feat_mask"])
        
        ## What is this??
        ## Apears in guassian activations:
        ## MaSIF_site.py line 103: gauss_activations = tf.multiply(gauss_activations, mask)
        mask = np.load(os.path.join(pdbdir, "mask.npy"))
        mask = np.expand_dims(mask, 2)
        
        labels = np.load(os.path.join(pdbdir, "conds.npy")) # ["PEG", "no PEG"]

        # feed_dict = {
        #     learning_obj.rho_coords: rho_wrt_center,
        #     learning_obj.theta_coords: theta_wrt_center,
        # }