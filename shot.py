from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=b.new_page(viewport={'width':1300,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(sys.argv[1]);pg.wait_for_timeout(800)
    pg.screenshot(path='screenshot_timeline.png',full_page=True)
    print('errs',errs);print(pg.inner_text('#cons'));print(pg.inner_text('#regra'))
