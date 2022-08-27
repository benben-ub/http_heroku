#http request 可參考運用  判斷post get 方法 及 headers
from crypt import methods
from http.client import OK, responses
from flask import Flask,request,Response,jsonify,json,redirect
import json
import qrcode
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def httptest():
    
    print('this is a ''\'',request.method,'\'http request')
    if request.method=='GET':
        
        re1=request.args.get('name1','noinput')
        re2=request.args.get('name2','noinput')
        re=re1+re2
        print(re)
    elif request.method=='POST':
        print(request.method)
        url='https://'+request.headers.get('Host')
        data={"url":url}
        CT=request.headers.get('Content-Type')
        
        if CT=='application/json':
            #直接用 json 來傳遞參數資料    postman 使用 raw 
            print('THIS is ',CT)
            re=request.json   #@@@@@@@@@@@@
            print("re type is ",type(re))
            # print(re['1STname'])
            ha=re['input']
            print(re['input'])
            img=qrcode.make(ha)
            img.show()
            
        elif CT=='application/x-www-form-urlencoded':  
            #form 瀏覽器原生表單數據被編碼為key/value格式發送
            print('THIS is ',CT)
            re=request.form     #@@@@@@@@@@@@
            print("re type is ",type(re))
            print(re)
        elif  CT=='multipart/form-data':
        #在表單中進行文檔上傳時使用格式  postman form-data
            print('THIS is ',CT)
            re=request.data    #@@@@@@@@@@@@
            print("re type is ",type(re))
            print(CT)
    
    
    return re
    

if __name__=='__main__':
    app.run(debug=True)