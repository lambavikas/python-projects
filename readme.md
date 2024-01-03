# Setting up a Virtual Environment (VENV) in Python
[Virtual Environment Guide](https://python.land/virtual-environments/virtualenv)

1. Issue this from root folder `python` to create a sub-directory named `venv` in your project where all files for managin virtual env are placed
```
python -m venv <nameOfProject\venv>
``````

2. Activate an environment
```
cd <nameOfProject>
# In cmd.exe
    venv\Scripts\activate.bat
# In PowerShell
    venv\Scripts\Activate.ps1
```
Note: Anything you install using pip will now be restricted to this venv alone

3. Deactivate an environment
```
cd <nameOfProject\venv\Scripts>
deactivate 
```
4. Delete an environment
```
- First exit from the environment using step 3
- Delete the folder venv
```
