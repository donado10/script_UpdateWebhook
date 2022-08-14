import requests
import NgrokAddress

def GetId(url:str,headers:dict):
    r = requests.get(url,headers=headers)
    if str(r) =="<Response [200]>":    
        d1 = {}
        for i in r.json():
            d1.update(i)
        return d1['id']
    else:
        return False

def UpdateGithubWebhooks(token,repo,user,NewAdress):

    token = token
    repo = repo
    user = user
    url = "https://api.github.com/repos/{}/{}/hooks".format(user, repo)
    headers = {"Authorization": "token {}".format(token)}
    

    hookID = GetId(url,headers)
    if hookID != False:
        url = url + '/' + f'{hookID}'

        hook= {"owner": user,"repo": repo, "hook_id": f'{hookID}',"active": True,"config":{"content_type" : "json","url":f"{NewAdress}"}}
        y = requests.patch(url,json=hook,headers=headers)

        if str(y) == "<Response [200]>":
            return "The update has been succesfull for Github :)"
        else:
            return "Error !! Something wrong happened when updating to Github :("

    else:
        return "Error !! Something wrong happened when updating to Github :("

def NotifySlack(text):
    text = '{"text" : "%s"}' % text
    
    #Adresse URL Jenkins
    url = "https://hooks.slack.com/..."

    r = requests.post(url,data=text)
    if str(r) == "<Response [200]>":
        return "The message has been succesfully send to Jenkins :)"
    else:
        return "Error !! Something wrong happened when sending to Jenkins :("


token_github = "...."
Repository = "...."
Username = "...."

NewAddress = NgrokAddress.GetAddress("curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url") + '/github-webhook/' 
Message = f"La nouvelle adresse public Jenkins est {NewAddress}"


Github = UpdateGithubWebhooks(token_github,Repository,Username,NewAddress)
print(Github)

Jenkins = NotifySlack(Message)
print(Jenkins)

  







