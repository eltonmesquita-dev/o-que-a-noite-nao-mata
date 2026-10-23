from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=b.new_page(viewport={'width':1600,'height':1000})
    pg.goto('file:///workspace/oqannm-site/index.html');pg.wait_for_timeout(800)
    w=pg.evaluate("""()=>{const s=[...document.querySelectorAll('section')].find(x=>x.querySelector('h3')?.textContent.startsWith('Linha do tempo proporcional'));
     s.id='alvo';let n=s;while(n.parentElement){[...n.parentElement.children].forEach(c=>{if(c!==n&&c.tagName!=='SCRIPT')c.style.display='none'});n=n.parentElement}
     const h=document.createElement('h1');h.textContent='O Que A Noite Não Mata — Linha do tempo proporcional';h.style.cssText='margin:0 0 10px;font-size:28px';s.prepend(h);
     const st=document.createElement('style');st.textContent='#alvo *{overflow:visible!important} main,body,html,#alvo{margin:0!important;max-width:none!important;width:max-content!important;min-width:0!important;padding:16px!important} html,body{-webkit-print-color-adjust:exact;print-color-adjust:exact}';document.head.append(st);
     return Math.max(...[...s.querySelectorAll('*')].map(e=>e.getBoundingClientRect().right))+20}""")
    sc=max(0.1,min(1,(1587-40)/w));print('width',w,'scale',sc)
    pg.emulate_media(media='screen')
    pg.pdf(path='linha_proporcional.pdf',format='A3',landscape=True,print_background=True,scale=sc,margin={'top':'8mm','bottom':'8mm','left':'8mm','right':'8mm'})
