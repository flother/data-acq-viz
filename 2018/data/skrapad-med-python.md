Skrapað með Python
==================

Python á macOS
--------------

Makkar koma með Python 2.7 foruppsettu. Stýrikerfið notar þá útgáfu fyrir ýmis kerfistól. Ef við reynum að nota þá útgáfu beint getum við lent í ýmsum vandræðum með skráa- og möppuheimildir, svo ekki sé minnst á að Python 2.7 er svo gott sem úrelt og höndlar Unicode afar illa. Best er að setja upp nýjustu útgáfu Python sérstaklega (3.6.4 þegar þetta er skrifað) og stjórna handvirkt þeim pökkum og umhverfum sem við þurfum. Ein leið til þess er `pipenv`, sem er tiltölulega nýlegt pakkastjórnunarkerfi með innbyggðum stuðningi við sýndarumhverfi fyrir hvert Python-verkefni sem búið er til.

Ef þú ert nú þegar búin(n) að koma þér upp einhverju öðru vinnulagi sem virkar (t.d. með `pip`og `virtualenv` eða heildarlausn eins og `conda`) er engin ástæða til að skipta úr því. Notaðu það sem virkar fyrir þig. Ef þú ert hins vegar að setja upp Python í fyrsta skipti mæli ég með `pipenv` – og reyndar mælir python.org opinberlega með því líka síðan fyrir stuttu. Hér er crash-course í að búa til nýtt verkefni frá grunni með `pipenv`:

1. Sæktu og settu upp nýjustu útgáfu Python frá https://www.python.org/

2. Settu upp Homebrew samkvæmt leiðbeiningum af https://brew.sh/. Það eru vissulega margar aðrar leiðir en Homebrew færar til að setja upp `pipenv`, en allir Makkanotendur ættu að hafa Homebrew eða viðlíka pakkastjórnunarkerfi uppsett hvort sem er – svo nú er ágætis tímapunktur til að setja það upp ef þú hefur ekki gert það nú þegar.

3. Með Homebrew uppsett er nóg að skrifa `brew install pipenv` í Terminal til að setja `pipenv` upp.

4. Búðu til möppu fyrir verkefnið þitt og farðu inn í hana í Terminal-forritinu þínu.

5. Skrifaðu `pipenv --python 3.6`. Þetta segir `pipenv` að búa til nýtt sýndarumhverfi fyrir verkefnið þitt, í þeirri möppu sem er opin, og nota til þess útgáfu 3.6 af Python.

6. Nú er sniðugt að setja upp þá Python-pakka sem þú veist að þú munt þurfa fyrir verkefnið. `pipenv install requests beautifulsoup4` mun til dæmis setja upp þá tvo pakka sem við notuðum í tímanum til að búa til lottóskraparann (sjá `lotto-scraper.py`). `pipenv` sér til þess að pakkarnir séu settir upp fyrir þetta sýndarumhverfi eingöngu og skrifar út Pipfile-skrá sem tiltekur þá pakka sem þú ert að nota í þessu verkefni. Þetta gerir verkefnið þitt einnig færanlegra; ef þú vilt senda einhverjum skrifturnar þínar læturðu einfaldlega Pipfile-skrána fylgja með og viðtakandinn þarf þá ekki að gera annað en keyra `pipenv install` til að endurskapa nákvæmlega umhverfið sem þú notaðir. Þú getur hvenær sem er sett upp og fjarlægt pakka úr sýndarumhverfinu (og `pipenv` sér um að halda Pipfile-skránni uppfærðri).

7. Skrifaðu `pipenv shell` til að virkja nýja sýndarumhverfið með viðeigandi Python-útgáfu og -pökkum. Hér eftir ertu í nokkurs konar sandkassa þar sem ekkert sem þú gerir hefur áhrif á önnur sýndarumhverfi eða Python-uppsetningu stýrikerfisins. Frekar sneddí.

8. Til að yfirgefa sandkassann skrifarðu `exit`.


Python á Windows
----------------

Ekki mín sérgrein, en `conda` (https://conda.io) er almennt talið skotheld leið til að koma upp Python-umhverfi á Windows (og virkar reyndar á Mac og Linux einnig). Það er með innbyggðu pakkastjórnunar- og sýndarumhverfiskerfi sem virkar svipað og `pipenv`. Helstu skipanir má finna á þessu svindlblaði: https://conda.io/docs/_downloads/conda-cheatsheet.pdf

Ef þú velur `conda` mæli ég með að þú setjir upp Miniconda en ekki Anaconda (sjá https://conda.io/docs/user-guide/install/index.html). Anaconda kemur með hundruðum Python-pakka foruppsettum, sem er fullkominn óþarfi. Betra er að setja hvern og einn pakka upp eftir þörfum hvers verkefnis.


Nokkrir nytsamlegir Python-pakkar
=================================

Requests
--------
`pipenv install requests`

http://docs.python-requests.org/

Gullstandardinn þegar kemur að Python-pökkum. Allir í Python-heiminum nota `requests` fyrir allt sem viðkemur HTTP-samskiptum. Skjölunin á vefsíðu pakkans er einnig mjög góð.


BeautifulSoup
-------------
`pipenv install beautifulsoup4`

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Ýmsar leiðir eru færar til að þátta HTML-kóða og fá þægilegan aðgang að HTML-tögum og -eigindum, BeautifulSoup er einungis ein leið af mörgum (margir kjósa t.a.m. að nota `lxml` - sjá neðar). Ég notaði BeautifulSoup í sýnikennslunni og get mælt með því. Ef eitthvað skröpunarverkefni reynist þér mjög erfitt með BS er samt um að gera að tékka á öðrum kostum, til dæmis...


LXML
----
`pipenv install lxml`

http://lxml.de/

Önnur og ekki síðri leið til að vinna með HTML og XML-skjöl. Mögulega leið sem þér finnst þægilegri en BeautifulSoup. LXML getur líka notað BeutifulSoup sem parser og öfugt. Oft er gott að prófa báða kosti, sérstaklega ef (þegar) maður/kona rekst á gallaðan HTML-kóða eða illa sniðinn.


Pandas
------
`pipenv install pandas`

https://pandas.pydata.org/

Pandas er _gífurlega_ öflugt tól, og jafnvel nær því að vera forritunarmál í sjálfu sér heldur en bara venjulegur Python-pakki. Það er de-facto staðallinn í allri þungri gagnavinnslu í Python og þegar vinna þarf með stórar gagnatöflur. Það er alveg örugglega overkill fyrir það sem þið ætlið að gera, en það er samt ekki hægt að sleppa því í upptalningu á áhugaverðum Python-pökkum.


Selenium
--------
`pipenv install selenium`

http://selenium-python.readthedocs.io/index.html

Í dag er sífellt algengara að sjálft HTML-skjalið sem vefþjónninn sendir innihaldi engar nytsamlegar upplýsingar. Nútímavefkerfi (sem byggja á t.d. React eða Angular) framleiða oft innihald síðunnar jafnóðum með JavaScript. Í slíkum tilfellum er til lítils að sækja síðuna með pakka á borð við `requests` – það vantar enn vafra til að keyra JavaScript-ið og skila sjálfu innihaldinu. Þessi þróun er auðvitað hræðileg, sem er annað mál. Við getum komist framhjá þessu með því að nota „hauslausa vafra“ eins og `selenium` sem keyrir í raun viðmótslausan vafra bakvið tjöldin til að rendera síðuna. Eins og gefur að skilja er þetta allt saman klunnalegt og hægvirkt, og því kjósum við alltaf að nota einfaldar beiðnir í gegnum `requests` ef okkur framast er unnt. En ef það er ekki mögulegt er `selenium` ágætis kostur. Til þess að skipta einfaldri `requests`-beiðni út fyrir beiðni sem fer í gegnum `selenium` er yfirleitt nóg að gera `import selenium` og skipta svo


```
page = requests.get(url)
page_content = page.content
```

út fyrir

```
driver = webdriver.Chrome()
driver.get(url)
page_content = driver.page_source
driver.close()
```

Og svo má nota `page_content` breytuna á sama hátt og áður; senda hana inn í BeautifulSoup o.s.frv. Ekki mikið flóknara. Hægt er að nota `webdriver.Firefox()` eða önnur vafraheiti til að keyra síðuna gegnum aðrar vafravélar. Þar sem `selenium` keyrir upp heilt vafraforrit í bakgrunni er gott að muna eftir að kalla á `close()`.


Aðrar gagnlegar vefsíður
========================

Opinbera Python-skjölunin
-------------------------
https://docs.python.org/3/
Útskýringar og sýnidæmi fyrir allt sem er innbyggt í Python


How to Python
-------------
http://howtopython.org/en/latest/
Kenneth Reitz (maðurinn sem skrifaði `pipenv` og `requests`) er akkúrat í þessum skrifuðu orðum að koma þessari síðu upp og er hún því í stöðugri vinnslu. Stefnir í að verða mjög góð upplýsingalind. Enn sem komið er má hins vegar finna ítarlegri upplýsingar í fyrra gæluverkefni Reitz...


The Hitchhiker’s Guide to Python
--------------------------------
http://docs.python-guide.org/
Kenneth Reitz er nefnilega ofvirkur.


PEP 8
-----
https://www.python.org/dev/peps/pep-0008/
PEP-8 er opinber leiðarvísir Python um forritunarstíl. Ef þú hyggur á frama í Python fylgirðu þessum stælgæd eða hættir á að verða aðhlátursefni sjóaðra Python-forritara. Sem er ef til vill ekkert verra.


Python Module of the Week
-------------------------
https://pymotw.com/3/
Síða sem fer mjög ítarlega ofan í saumana á flestum innbyggðum eiginleikum Python. Skoðið t.d. kaflann um `itertools` – þar er pottþétt eitthvað sem þið eigið eftir að nota.