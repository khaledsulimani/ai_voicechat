# Voice Assistant using Python and Cohere

This project aims to build a *voice assistant* using *Python* and *Cohere API* to convert speech to text, generate responses in colloquial Arabic, and convert the text back to speech using *gTTS* or *pyttsx3. The assistant is developed using **Python 3.9.34* in the *Anaconda Navigator* environment.

## Requirements

- *Anaconda Navigator* or *Miniconda*
- *Python 3.9.34*
- *Cohere API Key*
- *Required libraries*:
  - speechrecognition
  - cohere
  - gTTS or pyttsx3
  - pygame
  - time
  - os

## Setup Steps

### 1. Create a Python Environment using Anaconda Navigator:

1. Open *Anaconda Navigator*.
2. Create a new environment with *Python 3.9.34*:
   - Go to *Environments* on the left panel.
   - Click *Create*.
   - Choose *Python 3.9.34* from the dropdown.
3. Activate the environment you created.

### 2. Install the Required Libraries:

Open *Anaconda Prompt* or *Terminal* within Anaconda Navigator and run the following commands to install the required libraries:

```bash
conda activate your_env_name  # Activate the environment
pip install SpeechRecognition pyttsx3 gTTS pygame cohere
