def dbcall(name):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://fridgebbridge.firebaseio.com/', None)
    result=firebase.get('Users',name)
    if result==None:
        result=0
    data={
        name:result+1,
        
    }
    result = firebase.patch('/Users/',data)
