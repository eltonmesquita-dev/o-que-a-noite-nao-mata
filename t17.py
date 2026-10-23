import sys
from playwright.sync_api import sync_playwright
u=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=b.new_page(viewport={'width':1400,'height':1000})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(u);pg.evaluate("localStorage.setItem('oqannm_ev_v2','[{\"id\":\"x\"}]')");pg.reload();pg.wait_for_timeout(800)
    print('aviso:',pg.inner_text('#aviso')[:90])
    pg.evaluate("localStorage.clear()");pg.reload();pg.wait_for_timeout(800)
    print('errs',errs)
    days=pg.query_selector_all('.month')[1].query_selector_all('.day')
    d=[x for x in days if x.query_selector('.n b').inner_text()=='17'][0]
    print([(c.get_attribute('data-lane'),c.inner_text()) for c in d.query_selector_all('.bar')])
    for i in ['b_pedido','b_romance']:
        print(i,pg.evaluate(f"[...document.querySelectorAll('#cal .bar')].filter(x=>x.getAttribute('onclick').includes(\"'{i}'\")).map(x=>x.dataset.lane).filter((v,i,a)=>a.indexOf(v)===i)"))
    m=pg.query_selector_all('.month')[1];m.scroll_into_view_if_needed();m.screenshot(path='shot_17mai.png');b.close()
