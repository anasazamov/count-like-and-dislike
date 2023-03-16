import requests
TOKEN="6058623152:AAGROkpnAa7tK6gXhGiE_F-DpMqqFuxK8ns"
BASE_URL="https://api.telegram.org/bot{}/".format(TOKEN)

def sendLike_and_Dislike(chat_id,text):
    payload={"chat_id":chat_id,"text":text}
    requests.get(BASE_URL+"sendMessage",params=payload)
    

count_like=0
count_dislike=0
l1=-1
for i in requests.get(BASE_URL+"getUpdates").json()["result"]:
    if (i["message"].get("text")=="👍 Like"):
        count_like+=1
    elif( i["message"].get("text")=="👎 Dislike"):
        count_dislike+=1
print("like :",count_like)
print("dislike :",count_dislike)
j=0
while True:
    l2=(requests.get(BASE_URL+"getUpdates").json()["result"][-1]["message"]["date"])
    
    
    print("len2 line {}:".format(j),l2)
    
    j+=1
    
    chat_id=requests.get(BASE_URL+"getUpdates").json()["result"][-1]["message"]["from"]["id"]
    
    if l1!=l2:
        print("len1:",l1)
        
        i=requests.get(BASE_URL+"getUpdates").json()["result"][-1]
        if (i["message"].get("text")=="👍 Like"):
            count_like+=1
        elif( i["message"].get("text")=="👎 Dislike"):
            count_dislike+=1
            
        print(sendLike_and_Dislike(chat_id, f'👍 Like : {count_like}\n\n👎 Dislike : {count_dislike}'))
        l1=(requests.get(BASE_URL+"getUpdates").json()["result"][-1]["message"]["date"])