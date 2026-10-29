import asyncio,sys,os
base=os.path.dirname(os.path.abspath(__file__))
from playwright.async_api import async_playwright
from PIL import Image
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for c in sys.argv[1:]:
            os.makedirs(f'{base}/out/{c}',exist_ok=True)
            await pg.goto(f'file://{base}/{c}.html'); await pg.wait_for_timeout(800)
            n=await pg.locator('section').count()
            for i in range(n):
                await pg.locator('section').nth(i).screenshot(path=f'{base}/out/{c}/{i+1:02d}.png')
            ims=[Image.open(f'{base}/out/{c}/{i+1:02d}.png').resize((360,450)) for i in range(n)]
            cols=4; rows=(n+cols-1)//cols
            sh=Image.new('RGB',(cols*370+10,rows*460+10),'#222')
            for k,im in enumerate(ims): sh.paste(im,(10+(k%cols)*370,10+(k//cols)*460))
            sh.save(f'{base}/out/{c}_folha.png')
        await b.close()
asyncio.run(main())
