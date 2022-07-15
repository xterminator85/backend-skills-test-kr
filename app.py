from fastapi import FastAPI,HTTPException,File, UploadFile
from pydantic import BaseModel
import uvicorn
from pathlib import Path
import re


app=FastAPI()


@app.get('/api')
def home():
     return 'Welcome to Artemis Health Restful API development test'


@app.post('/api/palindrome/bulk/')
def bulk_upload(fileUpload: UploadFile):

     if not fileUpload:
            raise HTTPException(status_code=404, detail="No file found ")
     if fileUpload.filename.endswith('.txt'):
        file_location = Path().absolute()/fileUpload.filename 
        
        with open(file_location) as f:
         lines = f.readlines()
         
        ans_list = []
        
        for line in lines:
            s = ''.join(e for e in line.lower() if e.isalnum())
            # s = re.sub(r"[^a-z0-9]","",line.lower())
            ans=isPalindrome(s)
            if ans :
             ans_list.append(line.strip()+'|'+'true')   
            else :
             ans_list.append(line.strip()+'|'+'false')
         
     return ans_list

@app.post("/api/palindrome/{word}")
def single_upload(word: str):   
    palindrome_str=''
    if word =='' or None:
        raise HTTPException(status_code=404, detail="The required word is missing ")
    s = ''.join(e for e in word.lower() if e.isalnum())
    ans=isPalindrome(s)
    if ans :
       palindrome_str=word.strip()+'|'+'true' 
    else :
       palindrome_str=word.strip()+'|'+'false'
             
        
    return palindrome_str


def isPalindrome(s):
    
    return s == s[::-1]


if __name__ == '__main__':
       
    uvicorn.run("app:app", host='0.0.0.0', port=5000, reload=True)