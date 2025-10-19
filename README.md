This repository contains two complementary components:  

1. **Classifiers** – Supervised models for detecting suicidality and subject prediction tasks using volunteer-anonymized mental health chat data.  
2. **Generative** – coming soon

The repository provides code, training scripts, and evaluation pipelines for both tasks.



## ⚙️ Setup & Installation

### Prerequisites
Before setting up the repository, make sure you have the following installed:
- **Python 3.9+**
- **pip** (Python package manager) or **conda**
- **CUDA-enabled GPU** (recommended for training large models)

### Clone the Repository
```bash
git clone https://github.com/AyalSwaid/Mental-Health-models-Arabic.git
cd Mental-Health-models
```

### Install Dependencies

We recommend creating a virtual environment before installing dependencies.

```
# Create virtual environment
python -m venv venv

# Activate environment
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### GPU Support
For optimal performance, ensure you have CUDA-compatible PyTorch installed if you plan to use GPU acceleration. The requirements.txt includes the basic PyTorch installation, but you may need to install the CUDA-specific version based on your system configuration.

## Model Weights Access
The models are trained on unique datasets from Sahar.

➡️ **To gain access to the model weights, you must fill out a request form.**  
This ensures compliance with ethical guidelines & privacy requirements.

🔗 [Request Model Weights Access Form](https://docs.google.com/forms/d/e/1FAIpQLSd3z7Dso0sIjGbTtSYxv-Pwd336PUvzsJsma44nBNUSG74J1A/viewform?usp=sf_link)

---

##  Models

This repository provides both **classifier models** for risk detection and **generative models** for supportive response generation, all fine-tuned on Arabic data.

### 🔍 Classifiers
- **Fine-tuned Arabic models** to identify **multiple risk levels** in conversations.  
- Tasks include:
  - **GSR Prediction** (binary suicidality detection for General Suicide Risk)  
  - **IMSR Prediction** (binary suicidality detection for Immediate Suicide Risk)  
  - **Subject Prediction** (binary classification for depression, self-harm, sexual harm)  
- Implemented using **AraBERTv0.2 large**, **Gemma-3**, and **Fanar** models.  
- Trained on anonymized **help-seeker messages**

### 🧠 Generative
- coming soon

Together, these models allow for:
1. **Risk detection** – automatically identifying high-risk conversations.  
2. **Response generation** – producing empathetic counselor-style messages to assist in support settings.  



## Fine-tuning Classifiers

All fine-tune scripts here are based on the Sahar dataset. 
Here is some background:


### Dataset
Both datasets contains more information, but We will describe only what's neccessary.

**Messages** contains 
* engagement_id 
* text (original messages) 

**Conversation info** contains
* engagement_id
* gsr (suicide score assessment - 0 or 1)
* Subject (conversation subject)

### Flow of the model
We try to predict whether a help-seeker is suicidal based on a combination of the chat.

This model takes into account only the messages of the help seeker,

and it does not takes into account the counselor messages.

* We merge both datasets based on engagement_id.
* We tokenize every batch
* We train the model


## Fine-tuning the Generative Model

coming soon



##  Inference

After fine-tuning, you can run both **classifier** and **generative** models for predictions.

### Classifier (AraBERT)
- Load the tokenizer and model (aubmindlab/bert-large-arabertv02).  
- Load your saved weights (`.pth` file).  
- Tokenize input text and run it through the model.  
- Output is **0 = Not Suicidal** or **1 = Suicidal**.  

### Generative (Gemma-3)
coming soon






