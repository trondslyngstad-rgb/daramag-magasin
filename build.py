import html, os
E = html.escape

SRC = {
 'dr': ('News From The States', 'https://www.newsfromthestates.com/article/new-mexico-judge-orders-meta-pay-state-25b'),
 'bg': ('News From The States', 'https://www.newsfromthestates.com/article/new-mexico-judge-orders-meta-pay-state-25b'),
 'meta': ('Meta Q4 2025', 'https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/Earnings-Presentation-Q4-2025-FINAL.pdf'),
 'ips': ('Ipsos', 'https://www.ipsos.com/nb-no/topic/some'),
 'mw': ('Malwarebytes', 'https://www.malwarebytes.com/blog/news/2026/07/samsung-backs-down-on-threat-to-delete-health-data'),
 'ca': ('California DOJ', 'https://oag.ca.gov/news/press-releases/attorney-general-bonta-secures-6-million-settlement-23andme-litigation'),
}
def src(lab, keys):
    return f'<p class="src">{lab} ' + ', '.join(f'<a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]} ↗</a>' for k in keys) + '.</p>'

T = {
'en': dict(
 lang='en', title='DARA The Week · Issue 01', tagline='Data, value and you. Who profits from your data, every Saturday.',
 issue='ISSUE', date='WEEK 45 · SATURDAY 7 NOVEMBER 2026', read='5 MIN READ', other=('LES PÅ NORSK', 'no/'),
 post='https://www.daramag.com/p/dara-the-week-issue-1',
 cover_lab='COVER STORY', cover_h='The price of tapping “accept”: 25 billion dollars',
 cover_sub='A US judge put a price on what Meta promised about your data.',
 cover_alt='A hand holding a smartphone against a bright background',
 wel_lab='WELCOME TO ISSUE 01',
 wel='This is the first issue of DARA The Week. Every Saturday, we bring you the stories about your data that matter most: who uses it, who earns from it, and what you can do about it. Five minutes, no jargon.',
 ai='DARA uses AI to gather stories and write drafts. Every story is read, checked against its sources and approved by the editors before it is published.',
 toc_lab='IN THIS ISSUE', toc=['The price of tapping “accept”','Notable numbers','What were you worth to Meta last year?','Samsung asked for your pulse','Your DNA can end up in a bankruptcy','Three small checks, five minutes'],
 story=['The promise you got when you tapped “accept” on Facebook now has a price tag.',
  'In September, a jury in Santa Fe found that Meta had misled users in New Mexico, among other things about who could access their data. The jury found 26 of 29 statements misleading. On 21 October, Judge Francis Mathew set the penalty at 25 billion dollars.',
  'The case began after the Cambridge Analytica scandal, when data from up to 87 million Facebook users was harvested through a third-party app. State law allows up to 5,000 dollars per violation, and the jury counted over 43 million. The money goes to New Mexico’s schools.',
  'Meta says it does not sell user data and plans to appeal. In 2019, the US Federal Trade Commission fined Meta 5 billion dollars. This penalty is five times larger, from a single state.'],
 story_end='When broken privacy promises cost billions, perhaps they will be kept. What have the apps on your phone promised you?',
 srcs='Sources:', src1='Source:',
 num_lab='NOTABLE NUMBERS', nums=[('$25bn','Penalty a New Mexico judge ordered Meta to pay for misleading users about their data.','NEWS FROM THE STATES'),('$57','Meta’s revenue per daily user in 2025, by the company’s own figures.','META, Q4 2025'),('7 mill.','Nearly that many customers were hit by the 2023 data breach at 23andMe, the DNA test company.','CALIFORNIA DOJ')],
 also='ALSO THIS WEEK',
 cards=[('meta57','A smartphone next to a cup of coffee and a croissant','YOUR VALUE','What were you worth to Meta last year?','About 57 dollars. That is Meta’s own figure for revenue per daily user across Facebook, Instagram, WhatsApp and Messenger in 2025. Alone, you are worth a dinner out. Together, the users are the whole business model. What if we negotiated as a group?',['meta'],'Photo: Theo Lonic / Unsplash'),
        ('klokke','A smartwatch with a white strap on a wrist','HEALTH DATA','Samsung asked for your pulse. Saying no came with a threat','In July, Samsung Health asked for consent to train AI on sleep, heart rate and medical data. If you said no, a warning said your health data would be deleted. After protests, Samsung backed down. A yes under threat is not a real choice.',['mw'],'Photo: Sabina / Unsplash'),
        ('dna','A smiling family of four against a light wooden wall','DNA','Your DNA can end up in a bankruptcy','When 23andMe went bankrupt in 2025, customers’ genetic data and spit samples were sold to a nonprofit led by the company’s own cofounder. California objected to the sale but lost in court. Now the state has agreed a 6 million dollar settlement over a 2023 data breach that hit nearly 7 million customers. A court must still approve it. Customers can still ask to have their data deleted.',['ca'],'Photo: Subash Than / Unsplash')],
 over_lab='OVERHEARD', quote='“The clearly intentional and systematic nature of Facebook’s repeated misstatements.”', quote_by='Judge Francis Mathew, in his ruling ordering Meta to pay 25 billion dollars.',
 try_lab='TRY THIS WEEK', try_h='Three small checks, five minutes',
 tries=[('Open the ad settings in Facebook or Instagram.','Which choice did you make, and do you remember making it?'),('Check your smartwatch or fitness app.','Which apps get your health data?'),('Have you taken a DNA test?','Look up how to delete your data and have the sample destroyed.')],
 turn_lab='YOUR TURN', turn='What would you have charged Meta for your data last year?', turn_btn='Discuss on DARA ↗', turn_note='Opens the conversation on daramag.com in a new tab.', sub_h='Get DARA The Week every Saturday', sub_note='Free. Unsubscribe whenever you like.', copied='Link copied',
 foot_h='Know someone who should read this?', foot='Send it to one person. All our sources are in the', lib='DARA Source Library', see='See you next Saturday.', share='Share DARA', sub_btn='Subscribe for free', credit='Cover photo: Todd Jiang / Unsplash. Published by DARA Redaksjonen.'),
'no': dict(
 lang='no', title='DARA The Week · Utgave 01', tagline='Data, verdi og deg. Hvem som tjener på dataene dine, hver lørdag.',
 issue='UTGAVE', date='UKE 45 · LØRDAG 7. NOVEMBER 2026', read='5 MIN LESING', other=('READ IN ENGLISH', '../'),
 post='https://www.daramag.com/p/dara-the-week-utgave-1',
 cover_lab='UKENS SAK', cover_h='Prisen for å trykke «godta»: 25 milliarder dollar',
 cover_sub='En dommer i USA satte prisen på det Meta lovet om dataene dine.',
 cover_alt='En hånd holder en mobil mot en lys bakgrunn',
 wel_lab='VELKOMMEN TIL UTGAVE 01',
 wel='Dette er første utgave av DARA The Week. Hver lørdag får du de viktigste sakene om dataene dine: hvem som bruker dem, hvem som tjener på dem, og hva du kan gjøre. Fem minutter, uten fagspråk.',
 ai='DARA bruker KI til å samle inn saker og skrive utkast. Alle saker blir lest, sjekket mot kildene og godkjent av redaksjonen før de publiseres.',
 toc_lab='I DENNE UTGAVEN', toc=['Prisen for å trykke «godta»','Ukens tall','Hva var du verdt for Meta i fjor?','Samsung ba om pulsen din','DNA-en din kan havne i et konkursbo','Tre små sjekker, fem minutter'],
 story=['Løftet du fikk da du trykket «godta» på Facebook, har fått en prislapp.',
  'En jury i Santa Fe fant i september at Meta hadde villedet brukere i New Mexico, blant annet om hvem som fikk tilgang til dataene deres. Hele 26 av 29 utsagn ble funnet villedende. 21. oktober satte dommer Francis Mathew straffen til 25 milliarder dollar.',
  'Saken startet etter Cambridge Analytica-skandalen, der data fra opptil 87 millioner Facebook-brukere ble høstet gjennom en tredjepartsapp. Delstatens lov tillater inntil 5000 dollar per brudd, og juryen talte over 43 millioner. Pengene går til skolene i New Mexico.',
  'Meta sier at selskapet ikke selger brukerdata, og vil anke. I 2019 fikk Meta en bot på 5 milliarder dollar fra handelsmyndigheten FTC. Denne gangen er beløpet fem ganger så stort, fra én enkelt delstat.'],
 story_end='Når brutte personvernløfter koster milliarder, blir de kanskje holdt. Hva har appene på telefonen din lovet deg?',
 srcs='Kilder:', src1='Kilde:',
 num_lab='UKENS TALL', nums=[('25 mrd. $','Straffen en dommer i New Mexico ga Meta for å ha villedet brukerne om dataene deres.','NEWS FROM THE STATES'),('57 $','Metas inntekt per daglige bruker i 2025, ifølge selskapets egne tall.','META, 4. KVARTAL 2025'),('7 mill.','Nesten så mange kunder ble rammet da DNA-selskapet 23andMe ble hacket i 2023.','CALIFORNIAS JUSTISDEPARTEMENT')],
 also='OGSÅ DENNE UKA',
 cards=[('meta57','En mobil ved siden av en kaffekopp og en croissant','DIN VERDI','Hva var du verdt for Meta i fjor?','Rundt 57 dollar. Det er Metas eget tall for inntekt per daglige bruker på Facebook, Instagram, WhatsApp og Messenger i 2025. Alene er du verdt en middag ute. Sammen er brukerne hele forretningsmodellen. Hva om vi forhandlet sammen?',['meta'],'Foto: Theo Lonic / Unsplash'),
        ('klokke','En smartklokke med hvit reim på et håndledd','HELSEDATA','Samsung ba om pulsen din. Et nei kom med en trussel','I juli ba Samsung Health om lov til å trene KI på søvn, puls og helsedata. Sa du nei, fikk du en advarsel om at helsedataene ville bli slettet. Etter protester snudde Samsung. Et ja under trussel er ikke et ekte valg.',['mw'],'Foto: Sabina / Unsplash'),
        ('dna','En smilende familie på fire foran en lys trevegg','DNA','DNA-en din kan havne i et konkursbo','Da 23andMe gikk konkurs i 2025, ble kundenes genetiske data og spyttprøver solgt til en stiftelse ledet av selskapets egen medgründer. California protesterte mot salget, men tapte i retten. Nå har staten inngått et forlik på 6 millioner dollar om et datainnbrudd i 2023, som rammet nesten 7 millioner kunder. Retten må fortsatt godkjenne det. Kundene kan fortsatt be om å få dataene slettet.',['ca'],'Foto: Subash Than / Unsplash')],
 over_lab='HØRT DENNE UKA', quote='«The clearly intentional and systematic nature of Facebook’s repeated misstatements.»', quote_by='Dommer Francis Mathew i dommen mot Meta. På norsk: at Facebooks gjentatte villedende utsagn var tydelig bevisste og systematiske.',
 try_lab='PRØV DENNE UKA', try_h='Tre små sjekker, fem minutter',
 tries=[('Åpne annonseinnstillingene i Facebook eller Instagram.','Hvilket valg tok du, og husker du at du tok det?'),('Sjekk smartklokka eller treningsappen.','Hvilke apper får helsedataene dine?'),('Har du tatt en DNA-test?','Finn ut hvordan du sletter dataene og får prøven destruert.')],
 turn_lab='DIN TUR', turn='Hva ville du tatt betalt av Meta for dataene dine i fjor?', turn_btn='Diskuter på DARA ↗', turn_note='Åpner samtalen på daramag.com i en ny fane.', sub_h='Få DARA The Week hver lørdag', sub_note='Gratis. Du kan melde deg av når du vil.', copied='Lenken er kopiert',
 foot_h='Kjenner du noen som burde lese dette?', foot='Send det til én person. Alle kildene våre ligger i', lib='DARA-kildebiblioteket', see='Vi ses neste lørdag.', share='Del DARA', sub_btn='Abonner gratis', credit='Forsidefoto: Todd Jiang / Unsplash. Utgitt av DARA Redaksjonen.'),
}

CSS = """
*{box-sizing:border-box}body{margin:0;background:#e9e4da;color:#1d1d1f;font-family:'Source Serif 4',Georgia,serif}
a{color:#0B1F44}a:hover{color:#8a6a2c}
.wrap{max-width:880px;margin:0 auto;background:#F7F2E8}
.lab{font-family:Inter,Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;color:#8a6a2c}
.mast{background:#0B1F44;color:#F7F2E8;padding:28px 48px 22px}
.mast .top{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;border-bottom:1px solid rgba(201,161,90,.5);padding-bottom:18px}
.logo{font-family:Fraunces,Georgia,serif;font-weight:800;font-size:64px;line-height:.9;letter-spacing:-1px}
.logo span{font-weight:400;font-style:italic;color:#C9A15A}
.tag{margin-top:10px;font-family:Inter,Arial,sans-serif;font-size:13px;letter-spacing:.5px;color:#c9d2e3}
.iss{text-align:right;font-family:Inter,Arial,sans-serif}.iss small{display:block;font-size:12px;letter-spacing:2px;color:#C9A15A}
.iss b{font-family:Fraunces,Georgia,serif;font-size:56px;font-weight:800;line-height:1}
.mast .bot{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;padding-top:12px;font-family:Inter,Arial,sans-serif;font-size:12px;letter-spacing:1.5px;color:#c9d2e3}
.mast .bot a{color:#C9A15A}
.hero{display:grid;grid-template-columns:1fr 1fr;background:#fff}
.hero img{width:100%;height:100%;min-height:420px;object-fit:cover;display:block}
.hero .txt{padding:48px;display:flex;flex-direction:column;justify-content:center;background:#F7F2E8}
.hero h1{margin:12px 0 0;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:44px;line-height:1.05;color:#0B1F44}
.hero p{margin:14px 0 0;font-size:19px;line-height:1.45;color:#3c4558}
.intro{display:grid;grid-template-columns:1fr 260px;gap:40px;padding:44px 48px 0}
.intro .w{margin:12px 0 0;font-size:19px;line-height:1.6}
.drop{float:left;font-family:Fraunces,Georgia,serif;font-size:64px;line-height:.8;padding:6px 10px 0 0;color:#0B1F44;font-weight:800}
.sig{margin:14px 0 0;font-family:Inter,Arial,sans-serif;font-size:13px;color:#6b6b6b}
.ai{margin:14px 0 0;padding:12px 14px;border-left:3px solid #C9A15A;background:#efe6d4;font-size:14px;line-height:1.5;color:#3c4558;font-style:italic}
.toc{border-left:1px solid #d9cfbd;padding-left:24px}
.toc div{display:flex;gap:12px;margin-top:14px;font-size:15px;line-height:1.35}
.toc i{font-style:normal;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:20px;color:#C9A15A;width:24px;flex:none}
.story{padding:44px 48px 0}.story .rule{height:1px;background:#d9cfbd;margin-bottom:36px}
.story h2{margin:8px 0 18px;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:34px;line-height:1.1;color:#0B1F44}
.story .cols{columns:2;column-gap:32px}.story .cols p{margin:0 0 16px;font-size:18px;line-height:1.6;break-inside:avoid}
.story .end{font-weight:600;color:#0B1F44}
.src{font-family:Inter,Arial,sans-serif;font-size:13px;color:#6b6b6b;margin:8px 0 0}
.nums{margin:48px 0 0;background:#0B1F44;padding:40px 48px}.nums .lab{color:#C9A15A}
.nums .g{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:20px}
.nums .g>div{border-top:2px solid #C9A15A;padding-top:14px}
.nums b{display:block;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:44px;line-height:1;color:#fff}
.nums p{margin:10px 0 0;font-size:15px;line-height:1.45;color:#d7deea}.nums small{display:block;margin-top:8px;font-family:Inter,Arial,sans-serif;font-size:11px;letter-spacing:1px;color:#C9A15A}
.also{padding:48px 48px 0}.cards{display:grid;grid-template-columns:1fr 1fr;gap:36px 28px;margin-top:20px}
.card img{display:block;width:100%;height:210px;object-fit:cover;border-radius:4px}
.card .k{margin-top:14px;font-family:Inter,Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:1.5px;color:#8a6a2c}
.card h3{margin:6px 0 0;font-family:Fraunces,Georgia,serif;font-weight:600;font-size:24px;line-height:1.15;color:#0B1F44}
.card p{margin:8px 0 0;font-size:16px;line-height:1.55}.card .cr{font-family:Inter,Arial,sans-serif;font-size:11px;color:#8b8b8b;margin-top:6px}
.quote{background:#efe6d4;border-radius:4px;padding:28px;display:flex;flex-direction:column;justify-content:center}
.quote q{display:block;margin:14px 0 0;font-family:Fraunces,Georgia,serif;font-style:italic;font-size:26px;line-height:1.25;color:#0B1F44;quotes:none}
.quote p{margin:14px 0 0;font-size:15px;line-height:1.45}
.try{margin:52px 48px 0;border:2px solid #0B1F44;border-radius:6px;padding:32px}
.try h2{margin:8px 0 0;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:30px;color:#0B1F44}
.try .s{display:flex;gap:16px;margin-top:18px;align-items:flex-start}
.try .n{flex:none;width:34px;height:34px;border-radius:50%;background:#C9A15A;color:#0B1F44;display:flex;align-items:center;justify-content:center;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:18px}
.try p{margin:4px 0 0;font-size:17px;line-height:1.5}
.turn{padding:52px 48px 0;text-align:center}
.turn p{margin:12px auto 0;max-width:600px;font-family:Fraunces,Georgia,serif;font-size:32px;line-height:1.2;color:#0B1F44}
.btn{display:inline-block;margin-top:22px;padding:14px 24px;border-radius:6px;font-family:Inter,Arial,sans-serif;font-size:15px;font-weight:600;text-decoration:none}
.btn.o{border:2px solid #0B1F44;color:#0B1F44}.btn.g{background:#C9A15A;color:#0B1F44;font-weight:700}.btn.w{border:2px solid #C9A15A;color:#C9A15A}
.foot{margin-top:56px;background:#0B1F44;color:#d7deea;padding:36px 48px}
.foot .r{display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.foot h4{margin:0;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:28px;color:#fff}
.foot p{margin:8px 0 0;font-size:15px}.foot a{color:#C9A15A}.foot .btns{display:flex;gap:12px;flex-wrap:wrap}.foot .btn{margin-top:0}
.note{margin:10px auto 0;font-family:Inter,Arial,sans-serif;font-size:13px;color:#6b6b6b;max-width:none!important}
.turn .note{font-family:Inter,Arial,sans-serif;font-size:13px;line-height:1.4;color:#6b6b6b;margin-top:10px}
.subbox{margin:44px 48px 0;padding:28px;background:#efe6d4;border-radius:6px;text-align:center}
.subbox h4{margin:0 0 14px;font-family:Fraunces,Georgia,serif;font-weight:800;font-size:26px;color:#0B1F44}
.subbox iframe{width:100%;max-width:480px;height:150px;border:0;background:transparent}
button.btn{border:0;cursor:pointer}.ok{font-family:Inter,Arial,sans-serif;font-size:14px;color:#C9A15A;align-self:center}
.foot .cr{margin-top:24px;font-family:Inter,Arial,sans-serif;font-size:12px;color:#8f9bb3}
@media(max-width:760px){
.mast,.hero .txt,.intro,.story,.also,.nums,.foot,.turn{padding-left:22px;padding-right:22px}
.logo{font-size:44px}.iss b{font-size:40px}
.hero,.intro,.cards,.nums .g{grid-template-columns:1fr}.hero img{min-height:280px}
.hero h1{font-size:34px}.story .cols{columns:1}.toc{border-left:0;padding-left:0}
.try,.subbox{margin:40px 22px 0;padding:22px}.turn p{font-size:26px}}
"""

def page(t, imgp):
    toc = ''.join(f'<div><i>{i+1}</i><span>{E(x)}</span></div>' for i, x in enumerate(t['toc']))
    story = ''.join(f'<p>{E(p)}</p>' for p in t['story']) + f'<p class="end">{E(t["story_end"])}</p>'
    nums = ''.join(f'<div><b>{E(n)}</b><p>{E(d)}</p><small>{E(s)}</small></div>' for n, d, s in t['nums'])
    cards = ''
    for img, alt, k, h, p, keys, cr in t['cards']:
        cards += (f'<div class="card"><img src="{imgp}{img}.jpg" alt="{E(alt)}" loading="lazy"><div class="cr">{E(cr)}</div>'
                  f'<div class="k">{E(k)}</div><h3>{E(h)}</h3><p>{E(p)}</p>{src(t["srcs"] if len(keys)>1 else t["src1"], keys)}</div>')
    cards += (f'<div class="quote"><div class="lab">{E(t["over_lab"])}</div><q>{E(t["quote"])}</q>'
              f'<p>{E(t["quote_by"])} <a href="{SRC["bg"][1]}" target="_blank" rel="noopener">News From The States ↗</a></p></div>')
    tries = ''.join(f'<div class="s"><div class="n">{i+1}</div><p><strong>{E(a)}</strong> {E(b)}</p></div>' for i, (a, b) in enumerate(t['tries']))
    w = t['wel']
    return f"""<!DOCTYPE html><html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t['title'])}</title><meta name="description" content="{E(t['cover_sub'])}">
<meta property="og:title" content="{E(t['title'])}: {E(t['cover_h'])}"><meta property="og:description" content="{E(t['cover_sub'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,800;1,9..144,400&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Inter:wght@500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
<header class="mast"><div class="top"><div><div class="logo">DARA <span>The Week</span></div><div class="tag">{E(t['tagline'])}</div></div>
<div class="iss"><small>{E(t['issue'])}</small><b>01</b></div></div>
<div class="bot"><span>{E(t['date'])}</span><span>{E(t['read'])} · <a href="{t['other'][1]}">{E(t['other'][0])}</a></span></div></header>
<section class="hero"><div class="txt"><div class="lab">{E(t['cover_lab'])}</div><h1>{E(t['cover_h'])}</h1><p>{E(t['cover_sub'])}</p></div>
<img src="{imgp}cover.jpg" alt="{E(t['cover_alt'])}"></section>
<section class="intro"><div><div class="lab">{E(t['wel_lab'])}</div><p class="w"><span class="drop">{E(w[0])}</span>{E(w[1:])}</p>
<p class="sig">DARA Redaksjonen</p><p class="ai">{E(t['ai'])}</p></div>
<nav class="toc"><div class="lab" style="margin:0">{E(t['toc_lab'])}</div>{toc}</nav></section>
<article class="story"><div class="rule"></div><div class="lab">{E(t['cover_lab'])}</div><h2>{E(t['cover_h'])}</h2>
<div class="cols">{story}</div>{src(t['src1'], ['dr'])}</article>
<section class="nums"><div class="lab">{E(t['num_lab'])}</div><div class="g">{nums}</div></section>
<section class="also"><div class="lab">{E(t['also'])}</div><div class="cards">{cards}</div></section>
<section class="try"><div class="lab">{E(t['try_lab'])}</div><h2>{E(t['try_h'])}</h2>{tries}</section>
<section class="turn"><div class="lab">{E(t['turn_lab'])}</div><p>{E(t['turn'])}</p><a class="btn o" href="{t['post']}#comments" target="_blank" rel="noopener">{E(t['turn_btn'])}</a><p class="note">{E(t['turn_note'])}</p></section>
<section class="subbox"><h4>{E(t['sub_h'])}</h4><iframe src="https://www.daramag.com/embed" title="{E(t['sub_h'])}" loading="lazy" scrolling="no"></iframe><p class="note">{E(t['sub_note'])}</p></section>
<footer class="foot"><div class="r"><div><h4>{E(t['foot_h'])}</h4><p>{E(t['foot'])} <a href="https://www.daramag.com/p/sources" target="_blank" rel="noopener">{E(t['lib'])} ↗</a>. {E(t['see'])}</p></div>
<div class="btns"><button class="btn g" id="share" type="button">{E(t['share'])}</button><span id="ok" class="ok" hidden>{E(t['copied'])}</span></div></div>
<div class="cr">{E(t['credit'])} <a href="https://www.daramag.com" target="_blank" rel="noopener">daramag.com ↗</a></div></footer>
</div>
<script>
document.getElementById('share').addEventListener('click',async()=>{{const d={{title:document.title,url:location.href}};
try{{if(navigator.share){{await navigator.share(d);return;}}}}catch(e){{return;}}
try{{await navigator.clipboard.writeText(location.href);}}catch(e){{}}
const ok=document.getElementById('ok');ok.hidden=false;setTimeout(()=>ok.hidden=true,2500);}});
</script></body></html>"""

open('01/index.html', 'w').write(page(T['en'], 'img/'))
open('01/no/index.html', 'w').write(page(T['no'], '../img/'))
open('index.html', 'w').write('<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/01/"><title>DARA The Week</title></head><body><a href="/01/">DARA The Week</a></body></html>')
open('CNAME', 'w').write('magasin.daramag.com\n')
print('ok')
