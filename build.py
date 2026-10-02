import json
g=open('guests.json').read()
html='''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Find Your Seat · Ankita &amp; Krishan</title>
<link rel="manifest" href="manifest.json">
<style>
:root{--g:#8a5a1f;--bg:#fbf6ee}
*{box-sizing:border-box}body{margin:0;font-family:Georgia,'Times New Roman',serif;background:var(--bg);color:#2b2118;text-align:center}
.wrap{max-width:480px;margin:0 auto;padding:28px 18px}
h1{font-size:28px;margin:6px 0 2px;color:var(--g)}.sub{color:#6b5a48;margin-bottom:22px}
input{width:100%;font-size:20px;padding:14px 16px;border:2px solid #d9c7a8;border-radius:12px;background:#fff;font-family:inherit}
input:focus{outline:none;border-color:var(--g)}
.res{margin-top:16px;text-align:left}
.card{background:#fff;border:1px solid #e6d8bd;border-radius:14px;padding:14px 16px;margin:10px 0;display:flex;justify-content:space-between;align-items:center}
.nm{font-size:19px}.tb{font-size:13px;color:#6b5a48;text-transform:uppercase;letter-spacing:.08em;text-align:right}
.tb b{display:block;font-size:34px;color:var(--g);line-height:1}
.hint{color:#8a7a68;margin-top:18px;font-size:15px}
</style></head><body><div class="wrap">
<h1>Ankita &amp; Krishan</h1><div class="sub">Reception · The Merion · October 18, 2026</div>
<input id="q" type="search" placeholder="Type your name" autocomplete="off" autocapitalize="words" autofocus>
<div class="res" id="res"></div>
<div class="hint" id="hint">Enter your first or last name to find your table.</div>
</div>
<script>
const G=__DATA__;
const norm=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase().replace(/[^a-z0-9 ]/g,' ').replace(/\\s+/g,' ').trim();
G.forEach(g=>g.k=norm(g.n));
const q=document.getElementById('q'),res=document.getElementById('res'),hint=document.getElementById('hint');
function run(){
  const t=norm(q.value);res.innerHTML='';
  if(t.length<2){hint.style.display='';hint.textContent='Enter your first or last name to find your table.';return}
  const toks=t.split(' ');
  let m=G.filter(g=>toks.every(x=>g.k.split(' ').some(w=>w.startsWith(x))));
  if(!m.length)m=G.filter(g=>toks.every(x=>g.k.includes(x)));
  if(!m.length){hint.style.display='';hint.textContent="We couldn't find that name. Try just your last name, or ask a member of the family or the planners.";return}
  hint.style.display='none';
  m.slice(0,12).forEach(g=>{const d=document.createElement('div');d.className='card';
    d.innerHTML='<div class="nm"></div><div class="tb">Table<b></b></div>';
    d.querySelector('.nm').textContent=g.n;d.querySelector('b').textContent=g.t;res.appendChild(d)});
  if(m.length>12){const p=document.createElement('div');p.className='hint';p.textContent='Showing 12 of '+m.length+'. Keep typing to narrow it down.';res.appendChild(p)}
}
q.addEventListener('input',run);
if('serviceWorker' in navigator)navigator.serviceWorker.register('sw.js').catch(()=>{});
</script></body></html>'''
open('index.html','w').write(html.replace('__DATA__',g))
