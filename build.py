# Preenche template.html com data/events.json -> index.html (mesmo método do site irmão)
import json
ev=json.load(open('data/events.json',encoding='utf-8'))
t=open('template.html',encoding='utf-8').read()
open('index.html','w',encoding='utf-8').write(t.replace('{{EVENTS}}',json.dumps(ev,ensure_ascii=False,indent=1)))
print('ok',len(ev),'eventos')
