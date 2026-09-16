from django.http import HttpResponse
from django.views import View
from html import escape

CATALOG = {
    "4533278555": {
        "title": "Citrus Lemons List Pad | Original Watercolor Stationery, Lined or Blank Pages",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/9abc6d/8217557160/il_fullxfull.8217557160_3jat.jpg",
        "url": "https://www.etsy.com/listing/4533278555"
    },
    "4533072418": {
        "title": "Poppy Blossoms Writing Pad | Original Watercolor Floral Stationery, Lined or Blank",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/e8d323/8263728639/il_fullxfull.8263728639_kr53.jpg",
        "url": "https://www.etsy.com/listing/4533072418"
    },
    "4316627016": {
        "title": "Winterberry (Red) Wrapping Paper",
        "price": 18.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/153777/6967855027/il_fullxfull.6967855027_mecy.jpg",
        "url": "https://www.etsy.com/listing/4316627016"
    },
    "4316600303": {
        "title": "Holiday Bells Gift Bag with Matching Gift Tag",
        "price": 10.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/1854ed/6919784786/il_fullxfull.6919784786_hx4u.jpg",
        "url": "https://www.etsy.com/listing/4316600303"
    },
    "1481577244": {
        "title": "Ivy Silver Metallic (Green) 15mm Washi Tape",
        "price": 5.98,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f6f62a/4967487440/il_fullxfull.4967487440_1lxc.jpg",
        "url": "https://www.etsy.com/listing/1481577244"
    },
    "4541878498": {
        "title": "Wildflower Meadow Writing Pad | Watercolor Botanical Stationery | Handmade Notepad",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/013d51/8330189203/il_fullxfull.8330189203_i5sq.jpg",
        "url": "https://www.etsy.com/listing/4541878498"
    },
    "4541607168": {
        "title": "Citrus Lemons Daily Planner Notepad | Monthly Desk Pad | Gouache Artwork Schedule (5.5x8.5)",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f59d69/8280335738/il_fullxfull.8280335738_cerm.jpg",
        "url": "https://www.etsy.com/listing/4541607168"
    },
    "4533578951": {
        "title": "Floral Garden Writing Pad | Original Watercolor Stationery, Personalized Note Pad",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/c8bbc7/8219849614/il_fullxfull.8219849614_11sz.jpg",
        "url": "https://www.etsy.com/listing/4533578951"
    },
    "4533576837": {
        "title": "Floral Garden List Pad | Original Watercolor Stationery, Personalized Notepad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/0dcade/8267751793/il_fullxfull.8267751793_md1q.jpg",
        "url": "https://www.etsy.com/listing/4533576837"
    },
    "4533071352": {
        "title": "Poppy Blossoms List Pad | Original Watercolor Floral Stationery, Personalized Notepad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/2c56b1/8263721021/il_fullxfull.8263721021_eg1l.jpg",
        "url": "https://www.etsy.com/listing/4533071352"
    },
    "4533069264": {
        "title": "Poppy Bouquet List Pad | Original Watercolor Floral Stationery, Personalized Note Pad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/5570cd/8263703509/il_fullxfull.8263703509_r2qr.jpg",
        "url": "https://www.etsy.com/listing/4533069264"
    },
    "4533068402": {
        "title": "Apple Orchard Writing Pad | Original Watercolor Stationery, Lined or Blank Pages",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/36de7f/8263698203/il_fullxfull.8263698203_p4ib.jpg",
        "url": "https://www.etsy.com/listing/4533068402"
    },
    "4533058477": {
        "title": "Poppy Blossoms Notepad | Original Watercolor Floral Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/c7835b/8263725099/il_fullxfull.8263725099_grat.jpg",
        "url": "https://www.etsy.com/listing/4533058477"
    },
    "4532159103": {
        "title": "Daisy Meadow Notepad | Original Watercolor Floral Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/6362fc/8256925485/il_fullxfull.8256925485_j5xb.jpg",
        "url": "https://www.etsy.com/listing/4532159103"
    },
    "4532157623": {
        "title": "Daisy Meadow List Pad | Original Watercolor Floral Stationery, Personalized Notepad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/4da261/8256848039/il_fullxfull.8256848039_906n.jpg",
        "url": "https://www.etsy.com/listing/4532157623"
    },
    "4316647130": {
        "title": "Vintage Rabbits (Taupe) Gift Bag with Matching Gift Tag",
        "price": 10.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f5956f/6919987152/il_fullxfull.6919987152_c42o.jpg",
        "url": "https://www.etsy.com/listing/4316647130"
    },
    "4316643516": {
        "title": "Cottage Garden Gift Bag with Matching Gift Tag",
        "price": 10.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/12b130/6919971814/il_fullxfull.6919971814_szv5.jpg",
        "url": "https://www.etsy.com/listing/4316643516"
    },
    "4316620890": {
        "title": "Winterberry Gift Bag ~ 2 Color Options - Each with Matching Gift Tag",
        "price": 10.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/8b6926/6919853528/il_fullxfull.6919853528_o1ic.jpg",
        "url": "https://www.etsy.com/listing/4316620890"
    },
    "4316609705": {
        "title": "Lilac Bloom Wrapping Paper",
        "price": 18.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/77b8e8/6967794789/il_fullxfull.6967794789_ewo3.jpg",
        "url": "https://www.etsy.com/listing/4316609705"
    },
    "4316594401": {
        "title": "Watercolor Songbird Stickers ~ Set of 7",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/595338/6919745058/il_fullxfull.6919745058_g0a5.jpg",
        "url": "https://www.etsy.com/listing/4316594401"
    },
    "1495769853": {
        "title": "Oranges 15mm Washi Tape",
        "price": 4.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/59c433/4967410484/il_fullxfull.4967410484_7yys.jpg",
        "url": "https://www.etsy.com/listing/1495769853"
    },
    "1495769685": {
        "title": "Morandi Gel Pens - Vintage",
        "price": 8.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/21d652/5015773975/il_fullxfull.5015773975_fsj8.jpg",
        "url": "https://www.etsy.com/listing/1495769685"
    },
    "1481578986": {
        "title": "Poppy Blossoms 15mm Washi Tape",
        "price": 4.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f93950/5015582623/il_fullxfull.5015582623_n5mc.jpg",
        "url": "https://www.etsy.com/listing/1481578986"
    },
    "1481577774": {
        "title": "Morandi Gel Pens - All 4 Sets",
        "price": 32.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/e7ff04/4967502446/il_fullxfull.4967502446_tf75.jpg",
        "url": "https://www.etsy.com/listing/1481577774"
    },
    "4571424186": {
        "title": "2027 A5 Planner | Weekly & Monthly Planner | Goal, Habit, Budget, Reflection Planner | Botanical Coil Bound Planner",
        "price": 54.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/fad6ec/8494768218/il_fullxfull.8494768218_tjfg.jpg",
        "url": "https://www.etsy.com/listing/4571424186"
    },
    "4547584549": {
        "title": "Sugaring Season Notepad | Maple Forest Watercolor Art, Lined or Blank Pages",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/2ab5b1/8322922418/il_fullxfull.8322922418_1qs0.jpg",
        "url": "https://www.etsy.com/listing/4547584549"
    },
    "4547582047": {
        "title": "Woodland Maple Forest Watercolor Writing Pad | Personalized Stationery Notepad",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f86d1e/8322892734/il_fullxfull.8322892734_rc46.jpg",
        "url": "https://www.etsy.com/listing/4547582047"
    },
    "4541590149": {
        "title": "Citrus Lemons Daily Reflection Notepad | Gratitude Journal, Self Care Planner",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/26d113/8280318476/il_fullxfull.8280318476_40df.jpg",
        "url": "https://www.etsy.com/listing/4541590149"
    },
    "4539717173": {
        "title": "Weekly Reading Log Notepad | Watercolor Artwork, Book Lover Gift, 4.25 x 8.5",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/31a41f/8314095691/il_fullxfull.8314095691_r68l.jpg",
        "url": "https://www.etsy.com/listing/4539717173"
    },
    "4538368564": {
        "title": "Daisy Meadow Daily Reflection Notepad | Gratitude Journal, Self-Care Planner, Wellness Tracker",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/853539/8328008547/il_fullxfull.8328008547_206e.jpg",
        "url": "https://www.etsy.com/listing/4538368564"
    },
    "4537748056": {
        "title": "Floral Watercolor Daily Planner Notepad | Monthly Desk Pad | Handmade Schedule To Do List",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/c9ec5c/8328158147/il_fullxfull.8328158147_f8nl.jpg",
        "url": "https://www.etsy.com/listing/4537748056"
    },
    "4537746394": {
        "title": "Daisy Meadow Daily Planner Notepad | Watercolor Floral Desk Pad (5.5x8.5)",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/75fd7f/8280137888/il_fullxfull.8280137888_nbsm.jpg",
        "url": "https://www.etsy.com/listing/4537746394"
    },
    "4537734739": {
        "title": "Blue Wildflower Daily Planner Notepad | Watercolor Floral Desk Pad (5.5x8.5)",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/7a6846/8280582436/il_fullxfull.8280582436_h2d5.jpg",
        "url": "https://www.etsy.com/listing/4537734739"
    },
    "4536747715": {
        "title": "Wilderness Canoes 4.25\" x 5.5\" Everyday Notepad | Lined Memo Pad | Handmade | Original Watercolor Stationery",
        "price": 4.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/e63a89/8291767907/il_fullxfull.8291767907_h1bu.jpg",
        "url": "https://www.etsy.com/listing/4536747715"
    },
    "4533283011": {
        "title": "Apple Orchard Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/ec49aa/8217597568/il_fullxfull.8217597568_m7qp.jpg",
        "url": "https://www.etsy.com/listing/4533283011"
    },
    "4533054259": {
        "title": "Apple Orchard Watercolor Notepad | Personalized Fruit Memo Pad, Lined or Blank Stationery",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/b28627/8263692105/il_fullxfull.8263692105_it2b.jpg",
        "url": "https://www.etsy.com/listing/4533054259"
    },
    "4533053331": {
        "title": "Apple Orchard List Pad | Original Watercolor Stationery, Farmhouse Note Pad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/71b471/8215754986/il_fullxfull.8215754986_q9d3.jpg",
        "url": "https://www.etsy.com/listing/4533053331"
    },
    "4532180946": {
        "title": "Cottage Garden Writing Pad | Original Watercolor Floral Stationery, Lined or Blank",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/71cb4a/8209071186/il_fullxfull.8209071186_cd0q.jpg",
        "url": "https://www.etsy.com/listing/4532180946"
    },
    "4532180064": {
        "title": "Cottage Garden Notepad | Original Watercolor Floral Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/39f1b8/8209064088/il_fullxfull.8209064088_ol17.jpg",
        "url": "https://www.etsy.com/listing/4532180064"
    },
    "4532166447": {
        "title": "Cottage Garden List Pad | Original Watercolor Floral Stationery, Personalized Notepad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/b39c43/8209039300/il_fullxfull.8209039300_4a5n.jpg",
        "url": "https://www.etsy.com/listing/4532166447"
    },
    "4532130985": {
        "title": "Lilac Bloom Watercolor Notepad | Personalized Floral Writing Pad, Lined Stationery",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/14dc35/8208824056/il_fullxfull.8208824056_oos7.jpg",
        "url": "https://www.etsy.com/listing/4532130985"
    },
    "4532117833": {
        "title": "Lilac Bloom Notepad | Original Watercolor Floral Memo Pad, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/b586ce/8208646236/il_fullxfull.8208646236_e5bd.jpg",
        "url": "https://www.etsy.com/listing/4532117833"
    },
    "4524775759": {
        "title": "Lilac Bloom Listpad | Original Watercolor Floral Stationery, Lined or Blank Note Pad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/3b8a92/8204985186/il_fullxfull.8204985186_ez60.jpg",
        "url": "https://www.etsy.com/listing/4524775759"
    },
    "4316604951": {
        "title": "Lilac Bloom Gift Bag with Matching Gift Tag",
        "price": 10.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/918481/6967781059/il_fullxfull.6967781059_bi58.jpg",
        "url": "https://www.etsy.com/listing/4316604951"
    },
    "1598589417": {
        "title": "Vintage Rabbits (Taupe) Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/1cfb11/8265574235/il_fullxfull.8265574235_i6qp.jpg",
        "url": "https://www.etsy.com/listing/1598589417"
    },
    "1598588937": {
        "title": "Cottage Garden Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/4136c7/8217627342/il_fullxfull.8217627342_fpg7.jpg",
        "url": "https://www.etsy.com/listing/1598588937"
    },
    "1584417758": {
        "title": "Reflective Vines (Mustard) Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f8e59d/8265549241/il_fullxfull.8265549241_j9nu.jpg",
        "url": "https://www.etsy.com/listing/1584417758"
    },
    "1495770001": {
        "title": "Sweet Oranges Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/3134f4/8265532561/il_fullxfull.8265532561_211w.jpg",
        "url": "https://www.etsy.com/listing/1495770001"
    },
    "1495768633": {
        "title": "Citrus Lemons Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/96f669/8265538471/il_fullxfull.8265538471_5blq.jpg",
        "url": "https://www.etsy.com/listing/1495768633"
    },
    "1495768499": {
        "title": "Lemons 15mm Washi Tape",
        "price": 4.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/27bf36/5015678537/il_fullxfull.5015678537_sy5n.jpg",
        "url": "https://www.etsy.com/listing/1495768499"
    },
    "1481579262": {
        "title": "Poppy Bouquet 15mm Washi Tape",
        "price": 4.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/798211/5015576821/il_fullxfull.5015576821_so6a.jpg",
        "url": "https://www.etsy.com/listing/1481579262"
    },
    "1481579142": {
        "title": "Poppy Bundle 15mm Washi Tape",
        "price": 12.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/d18af6/5015561499/il_fullxfull.5015561499_o5ks.jpg",
        "url": "https://www.etsy.com/listing/1481579142"
    },
    "1481576660": {
        "title": "Fruit Bundle 15mm Washi Tape",
        "price": 12.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/bb252f/4967430258/il_fullxfull.4967430258_kovo.jpg",
        "url": "https://www.etsy.com/listing/1481576660"
    },
    "1481576462": {
        "title": "Fruit (Apple, Lemon, Orange) Tea Towel Bundle",
        "price": 44.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/aba249/4967398786/il_fullxfull.4967398786_rxw0.jpg",
        "url": "https://www.etsy.com/listing/1481576462"
    },
    "4541632175": {
        "title": "Blue Wildflower Daily Reflection Notepad | Gratitude Journal, Self-Care Planner, Wellness Tracker",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/0c30fd/8280594792/il_fullxfull.8280594792_rptb.jpg",
        "url": "https://www.etsy.com/listing/4541632175"
    },
    "4541604241": {
        "title": "Sweet Oranges Daily Planner Notepad | Monthly Desk Pad | Original Artwork Schedule (5.5x8.5)",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/ee72f6/8328336779/il_fullxfull.8328336779_anxc.jpg",
        "url": "https://www.etsy.com/listing/4541604241"
    },
    "4536766066": {
        "title": "Wilderness Canoes 5.5\" x 8.5\" Everyday Notepad | Lined Memo Pad | Handmade | Original Watercolor Stationery",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/f1e031/8243872422/il_fullxfull.8243872422_m8mb.jpg",
        "url": "https://www.etsy.com/listing/4536766066"
    },
    "4536754430": {
        "title": "Poppy Bouquet Notepad | Original Watercolor Floral Stationery (4.25\" x 5.5\")",
        "price": 4.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/595b32/8243771292/il_fullxfull.8243771292_sg9t.jpg",
        "url": "https://www.etsy.com/listing/4536754430"
    },
    "4536730757": {
        "title": "Lilac Bloom Notepad | Purple Floral Watercolor Stationery, Lined Memo Pad",
        "price": 4.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/637f64/8243724828/il_fullxfull.8243724828_ktf9.jpg",
        "url": "https://www.etsy.com/listing/4536730757"
    },
    "4536729444": {
        "title": "Cottage Garden 4.25\" x 5.5\" Everyday Notepad | Floral Lined Memo Pad | Handmade | Original Watercolor Stationery",
        "price": 4.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/a249e4/8291492617/il_fullxfull.8291492617_3p9h.jpg",
        "url": "https://www.etsy.com/listing/4536729444"
    },
    "4536715091": {
        "title": "Daisy Meadow 5.5\" x 8.5\" Writing Pad | Floral Note Pad | Handmade | Lined | Original Watercolor Stationery",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/8706f5/8243625592/il_fullxfull.8243625592_mdi2.jpg",
        "url": "https://www.etsy.com/listing/4536715091"
    },
    "4533594836": {
        "title": "Blush Poppies Watercolor Writing Pad | Personalized Floral Stationery (5.5\" x 8.5\")",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/1c0018/8219871390/il_fullxfull.8219871390_r326.jpg",
        "url": "https://www.etsy.com/listing/4533594836"
    },
    "4533593926": {
        "title": "Blush Poppies Notepad | Original Watercolor Floral Memo Pad, Lined or Blank Stationery",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/b3490a/8219863986/il_fullxfull.8219863986_hwzh.jpg",
        "url": "https://www.etsy.com/listing/4533593926"
    },
    "4533591098": {
        "title": "Floral Garden Notepad | Original Watercolor Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/6e27a8/8219841792/il_fullxfull.8219841792_jj1v.jpg",
        "url": "https://www.etsy.com/listing/4533591098"
    },
    "4533305282": {
        "title": "Watercolor Bird Lovers Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/8b0bee/8217663550/il_fullxfull.8217663550_ebr2.jpg",
        "url": "https://www.etsy.com/listing/4533305282"
    },
    "4533293910": {
        "title": "Sweet Oranges List Pad | Original Watercolor Stationery, Handmade Notepad",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/fd21f8/8217570536/il_fullxfull.8217570536_nlpl.jpg",
        "url": "https://www.etsy.com/listing/4533293910"
    },
    "4533289665": {
        "title": "Daisy Meadow Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/49d722/8265580701/il_fullxfull.8265580701_cg5q.jpg",
        "url": "https://www.etsy.com/listing/4533289665"
    },
    "4533281127": {
        "title": "Sweet Oranges Writing Pad | Original Watercolor Stationery, Lined or Blank Pages",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/36d4fe/8217580174/il_fullxfull.8217580174_h33u.jpg",
        "url": "https://www.etsy.com/listing/4533281127"
    },
    "4533280697": {
        "title": "Sweet Oranges Watercolor Notepad | Fruit Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/740910/8217575290/il_fullxfull.8217575290_7d58.jpg",
        "url": "https://www.etsy.com/listing/4533280697"
    },
    "4533279463": {
        "title": "Citrus Lemons Writing Pad | Original Watercolor Stationery, Lined or Blank Pages",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/a01d68/8265492563/il_fullxfull.8265492563_nswt.jpg",
        "url": "https://www.etsy.com/listing/4533279463"
    },
    "4533070764": {
        "title": "Poppy Bouquet Writing Pad | Original Watercolor Floral Stationery, Lined or Blank Pages",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/990dad/8215790434/il_fullxfull.8215790434_e9us.jpg",
        "url": "https://www.etsy.com/listing/4533070764"
    },
    "4532160491": {
        "title": "Daisy Meadow Writing Pad | Original Watercolor Floral Stationery, Lined or Blank Note Pad",
        "price": 8.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/4b63fe/8209013070/il_fullxfull.8209013070_gcp5.jpg",
        "url": "https://www.etsy.com/listing/4532160491"
    },
    "4530984979": {
        "title": "Handmade Watercolor Magnetic Bookmark | Original Art Reader Accessory (2\" x 3\")",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/cd072b/8212314544/il_fullxfull.8212314544_90ey.jpg",
        "url": "https://www.etsy.com/listing/4530984979"
    },
    "1584417152": {
        "title": "Poppy Bouquet Tea Towel",
        "price": 16.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/b48a9a/8217618312/il_fullxfull.8217618312_gr4s.jpg",
        "url": "https://www.etsy.com/listing/1584417152"
    },
    "1495769387": {
        "title": "Morandi Gel Pens - Salty",
        "price": 8.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/25478b/5015780231/il_fullxfull.5015780231_g3xt.jpg",
        "url": "https://www.etsy.com/listing/1495769387"
    },
    "1495768159": {
        "title": "Ivy Silver Metallic (Blue) 15mm Washi Tape",
        "price": 5.98,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/cb75b7/5015756123/il_fullxfull.5015756123_fh9i.jpg",
        "url": "https://www.etsy.com/listing/1495768159"
    },
    "1495767949": {
        "title": "Ivy Silver Metallic (Berry) 15mm Washi Tape",
        "price": 5.98,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/3af1db/4967498682/il_fullxfull.4967498682_dlsf.jpg",
        "url": "https://www.etsy.com/listing/1495767949"
    },
    "1495767355": {
        "title": "Fruit (Apple, Lemon, Orange) Swedish Dishcloth Bundle",
        "price": 6.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/378d88/8244374486/il_fullxfull.8244374486_cqro.jpg",
        "url": "https://www.etsy.com/listing/1495767355"
    },
    "1481578848": {
        "title": "Poppy Blooms 15mm Washi Tape",
        "price": 4.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/b6bc04/5015585711/il_fullxfull.5015585711_24tm.jpg",
        "url": "https://www.etsy.com/listing/1481578848"
    },
    "1481578296": {
        "title": "Morandi Gel Pens - Sweet",
        "price": 8.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/a59bfd/4967512474/il_fullxfull.4967512474_90fm.jpg",
        "url": "https://www.etsy.com/listing/1481578296"
    },
    "1481578042": {
        "title": "Morandi Gel Pens - Nordic",
        "price": 8.99,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/5bf604/4967518724/il_fullxfull.4967518724_oku2.jpg",
        "url": "https://www.etsy.com/listing/1481578042"
    },
    "4541601445": {
        "title": "Sweet Oranges Daily Reflection Notepad | Gratitude Journal, Self Care Planner",
        "price": 11.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/47e488/8328323307/il_fullxfull.8328323307_sxlx.jpg",
        "url": "https://www.etsy.com/listing/4541601445"
    },
    "4536744409": {
        "title": "Poppy Bouquet 5.5\" x 8.5\" Writing Pad | Floral Note Pad | Handmade | Original Watercolor Stationery",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/fcb963/8291746941/il_fullxfull.8291746941_88f6.jpg",
        "url": "https://www.etsy.com/listing/4536744409"
    },
    "4533580205": {
        "title": "Blush Poppies List Pad | Original Watercolor Floral Stationery, Lined or Blank",
        "price": 5.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/d527e8/8267783217/il_fullxfull.8267783217_efk8.jpg",
        "url": "https://www.etsy.com/listing/4533580205"
    },
    "4533292568": {
        "title": "Citrus Lemons Notepad | Original Watercolor Fruit Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/868527/8265489595/il_fullxfull.8265489595_ae5w.jpg",
        "url": "https://www.etsy.com/listing/4533292568"
    },
    "4533056817": {
        "title": "Poppy Bouquet Notepad | Original Watercolor Floral Stationery, Lined or Blank Pages",
        "price": 6.95,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/eb3bad/8263708993/il_fullxfull.8263708993_eerp.jpg",
        "url": "https://www.etsy.com/listing/4533056817"
    },
    "4515138901": {
        "title": "Floral Garden Wrapping Paper",
        "price": 18.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/5f5ed1/8088783376/il_fullxfull.8088783376_s741.jpg",
        "url": "https://www.etsy.com/listing/4515138901"
    },
    "4316670170": {
        "title": "Wilderness Canoes Gift Bag with Matching Gift Tag ~ Outdoorsy, Father's Day, Adventure!",
        "price": 10.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/2ff09d/6920083990/il_fullxfull.6920083990_rnma.jpg",
        "url": "https://www.etsy.com/listing/4316670170"
    },
    "1495768055": {
        "title": "Ivy Silver Metallic (Berry, Blue, Green) 15mm Washi Tape Bundle",
        "price": 12.0,
        "currency": "USD",
        "image": "https://i.etsystatic.com/33232684/r/il/bd99dc/5015759513/il_fullxfull.5015759513_e3ia.jpg",
        "url": "https://www.etsy.com/listing/1495768055"
    }
}


class HealthView(View):
    def get(self, request):
        return HttpResponse(
            """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Winterberry Paper Co. Meta Checkout</title>
</head>
<body style="font-family:Arial,sans-serif;max-width:760px;margin:40px auto;padding:0 20px;">
<h1>Winterberry Paper Co.</h1>
<p>Meta checkout bridge is online.</p>
</body>
</html>"""
        )


class CheckoutView(View):
    def get(self, request):
        products_param = request.GET.get("products", "")
        coupon = request.GET.get("coupon", "").strip()

        product_quantities = {}
        if products_param:
            for entry in products_param.split(","):
                try:
                    product_id, quantity = entry.split(":", 1)
                    quantity = int(quantity)
                    if product_id and quantity > 0:
                        product_quantities[product_id] = quantity
                except (ValueError, TypeError):
                    continue

        items = []
        subtotal = 0.0
        unknown_ids = []

        for product_id, quantity in product_quantities.items():
            product = CATALOG.get(product_id)
            if not product:
                unknown_ids.append(product_id)
                continue

            line_total = product["price"] * quantity
            subtotal += line_total

            items.append({
                "id": product_id,
                "title": product["title"],
                "price": product["price"],
                "currency": product["currency"],
                "image": product["image"],
                "url": product["url"],
                "quantity": quantity,
                "line_total": line_total,
            })

        item_html = []
        for item in items:
            title = escape(item["title"])
            image = escape(item["image"])
            url = escape(item["url"])
            product_id = escape(item["id"])
            currency = escape(item["currency"])

            item_html.append(f"""
            <article class="cart-item" data-product-id="{product_id}">
              <img src="{image}" alt="{title}">
              <div class="item-details">
                <h2>{title}</h2>
                <p><strong>Quantity:</strong> {item["quantity"]}</p>
                <p><strong>Price:</strong> ${item["price"]:.2f} {currency} each</p>
                <p><strong>Line total:</strong> ${item["line_total"]:.2f} {currency}</p>
                <a class="etsy-button" href="{url}" target="_blank" rel="noopener">View on Etsy</a>
              </div>
            </article>
            """)

        items_markup = "\n".join(item_html) if item_html else """
        <div class="notice error">No recognized catalog products were provided.</div>
        """

        unknown_markup = ""
        if unknown_ids:
            unknown_markup = f"""
            <div class="notice warning">
              <strong>Unrecognized product IDs:</strong> {escape(", ".join(unknown_ids))}
            </div>
            """

        coupon_markup = ""
        if coupon:
            coupon_markup = f"""
            <div class="notice">
              <strong>Promo code supplied by Meta:</strong> {escape(coupon)}
            </div>
            """

        if len(items) == 1:
            etsy_action = f"""
            <a class="primary-button" href="{escape(items[0]["url"])}" target="_blank" rel="noopener">
              Continue to this item on Etsy
            </a>
            """
        elif len(items) > 1:
            etsy_action = """
            <a class="primary-button" href="https://winterberrypaperco.etsy.com" target="_blank" rel="noopener">
              Continue to Winterberry Paper Co. on Etsy
            </a>
            """
        else:
            etsy_action = ""

        page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Winterberry Paper Co. Cart</title>
<style>
:root {{
  --ink:#2f332e;
  --muted:#687166;
  --sage:#65745d;
  --sage-dark:#4d5c47;
  --paper:#fbfaf6;
  --card:#fff;
  --line:#dde2da;
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0;
  background:var(--paper);
  color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;
}}
.shell {{ max-width:860px; margin:0 auto; padding:32px 18px 56px; }}
header {{ text-align:center; margin-bottom:28px; }}
header h1 {{ margin:0 0 8px; font-family:Georgia,serif; font-weight:500; }}
header p {{ margin:0; color:var(--muted); }}
.cart-item {{
  display:grid;
  grid-template-columns:150px 1fr;
  gap:20px;
  background:var(--card);
  border:1px solid var(--line);
  border-radius:14px;
  padding:16px;
  margin-bottom:16px;
}}
.cart-item img {{
  width:150px;
  height:150px;
  object-fit:cover;
  border-radius:10px;
  border:1px solid var(--line);
}}
.item-details h2 {{ font-size:18px; margin:0 0 12px; line-height:1.35; }}
.item-details p {{ margin:7px 0; }}
.etsy-button,.primary-button {{
  display:inline-block;
  text-decoration:none;
  border-radius:9px;
  font-weight:600;
}}
.etsy-button {{
  margin-top:8px;
  padding:9px 13px;
  border:1px solid var(--sage);
  color:var(--sage-dark);
  background:#fff;
}}
.summary {{
  background:var(--card);
  border:1px solid var(--line);
  border-radius:14px;
  padding:18px;
  margin-top:22px;
}}
.subtotal {{
  display:flex;
  justify-content:space-between;
  font-size:19px;
  font-weight:700;
  margin-bottom:16px;
}}
.primary-button {{
  width:100%;
  text-align:center;
  padding:13px 18px;
  background:var(--sage);
  color:white;
}}
.notice {{
  padding:12px 14px;
  border-radius:10px;
  background:#f1f3ef;
  margin:12px 0;
}}
.warning {{ background:#fff4df; }}
.error {{ background:#fdebea; }}
.etsy-note {{
  margin-top:16px;
  color:var(--muted);
  font-size:14px;
  line-height:1.5;
}}
@media (max-width:620px) {{
  .cart-item {{ grid-template-columns:90px 1fr; }}
  .cart-item img {{ width:90px; height:90px; }}
}}
</style>
</head>
<body>
<div class="shell">
  <header>
    <h1>Winterberry Paper Co.</h1>
    <p>Your selected items</p>
  </header>

  {coupon_markup}
  {unknown_markup}
  {items_markup}

  <section class="summary">
    <div class="subtotal">
      <span>Subtotal</span>
      <span>${subtotal:.2f} USD</span>
    </div>

    {etsy_action}

    <p class="etsy-note">
      Purchases are completed securely on Etsy. Etsy does not currently provide
      this checkout bridge with a supported way to pre-fill a multi-item Etsy cart,
      so individual product links are provided above.
    </p>
  </section>
</div>
</body>
</html>"""

        return HttpResponse(page)
