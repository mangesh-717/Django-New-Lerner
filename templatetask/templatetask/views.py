from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def second(request):
    text=request.GET.get('text','default')
    remove_punc=request.GET.get('rum1','off')
    capitalize=request.GET.get('rum2','off')
    space_remover=request.GET.get('rum3','off')
    letter_counter=request.GET.get('rum4','off')
    uppe=''
    rspace=''
    count=''
    if remove_punc=='on':
        pun="""<>?:"{}[]'()*_-&^%$#@!~\/`<>,.;?/|"""
        r_punc=''.join(i for i in text if i not in pun)
    if capitalize=='on':
        uppe=text
    if space_remover=='on':
        rspace=''
        for j in range(len(text)-1):
            if not(text[j]==text[j+1]):
                rspace+=text[j]
    if letter_counter == 'on':
        count=len(text)
    dic={'remove_puncutation':r_punc,'Capatialize':uppe.upper(),'Remove_space':rspace,'later_counter':count}
    return render(request,'second.html',dic)