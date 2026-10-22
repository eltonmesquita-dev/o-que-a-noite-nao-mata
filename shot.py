from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=b.new_page(viewport={'width':1300,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
    pg.goto(sys.argv[1]);pg.wait_for_timeout(1000)
    pg.click("text=1º encontro: Estêvão pede ajuda >> nth=0");print(pg.inner_text('#det')[:200])
    pg.evaluate("document.getElementById('det').style.display='none'")
    pg.screenshot(path='screenshot_timeline.png',full_page=True)
    print('errs',errs);print(pg.inner_text('#cons'));print(pg.inner_text('#ordem')[:600])
