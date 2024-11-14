## Setup

### 1. Download and install Git (if not yet installed)

### 2. Download and install [Python 3.13.0](https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe)

Make sure to install as administrator and add to PATH

Check Python version by running:

```{bash}
python --version
```

### 3. Clone Git repository

```{bash}
git clone https://github.com/mel-adry-olivo/holy-sheet.git
```

Or clone directly in VSCode by doing:

1. Press `Ctrl+Shift+P` to open Command Pallete.
2. Type `Git: Clone` and select it.
3. Paste the URL of the repository and press `Enter`.
4. Select destination folder
5. Open Project

### 4. Create and Activate a Virtual Environment

- **Open Terminal by pressing `Terminal -> New Terminal`**
- Make sure you are on your project folder.
- **Install virtualenv**

```{bash}
pip install virtual env
```

- **Create a virtual environment**

```{bash}
virtualenv venv
```

- **Activate virtual environment**

```{bash}
venv\Scripts\activate.bat
```

### 5. Install Dependencies

```{bash}
pip install -r requirements.txt
```

### 6. Run Flask Application
