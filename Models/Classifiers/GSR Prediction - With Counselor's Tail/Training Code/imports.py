import pandas as pd
import numpy as np
from tqdm import tqdm_pandas
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import os
import time
import pickle as pkl
import sys
import json
import re

tqdm.pandas()

# specifc imports
import random
from transformers import BertModel, BertTokenizerFast, Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer, BertForSequenceClassification, BertTokenizer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score, fbeta_score, classification_report, precision_score, recall_score, f1_score
from datasets import Dataset, load_dataset
import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl
from pytorch_lightning.callbacks import TQDMProgressBar
from torch.utils.data import DataLoader
from torch.utils.data import Dataset as torchDataset
from transformers import logging
logging.set_verbosity_error()
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from itertools import product
from datetime import datetime
from collections import defaultdict, Counter
from scipy.spatial import distance

def seed_everything(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark  = False

    try:
        import cupy
        cupy.random.seed(seed)
    except:
        pass

    os.environ['PYTHONHASHSEED'] = str(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

def memory_usage():
    import GPUtil
    torch.cuda.empty_cache()
    gpus = GPUtil.getGPUs()

    if len(gpus) > 0:
        gpu = gpus[0] 

        print(f"Total GPU Memory: {gpu.memoryTotal} MB")
        print(f"Free GPU Memory: {gpu.memoryFree} MB")
        print(f"GPU Memory in Use: {gpu.memoryUsed} MB")
    else:
        print("No GPU available.")