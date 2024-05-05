# describe-a-python-project
Describe each file of a python project by asking a Generative AI model to generate a natural language explanation

## Need
- an OpenAI API Key and the relative environment variable OPENAI_API_KEY

## How
> pip install -r requirements.txt  
> streamlit run gui.py

## Guide
- copy and paste the folder you want to analyze recursively inside the text box:
![img.png](res%2Fimg.png)

### An Alternative GUI
You can choose to run a python GUI that allows you to select a local folder.  
Choose a local folder:  
![pygui1.png](res%2Fpygui1.png)  
Descriptions generated for each file:  
![pygui2.png](res%2Fpygui2.png)
### Notes
The procedure does not recursively visit all the folders; you can exclude teh files and the folders you don't want to analyze by
adding those names to the constants EXCLUDED_FOLDER_NAMES, EXCLUDED_FILENAMES

