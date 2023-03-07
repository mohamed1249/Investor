API_KEY = '6091795125:AAFq0sAgWNzoCiQ3_yuMTuGzc4il7ifWfIA'

HELP = """In addition to the existing list of commands you can ask for:
                
                -info for an stock, for example: FWRY
                """

STOCKS = {
    'abuk' : 'https://www.investing.com/equities/abou-kir-fertilizers-historical-data',
    'alcn' : 'https://www.investing.com/equities/alexandria-containers-and-goods-historical-data',
    'ekhoa' : 'https://www.investing.com/equities/egypt-kuwait-holding-historical-data',
    'mfpc': 'https://www.investing.com/equities/misr-fertilizers-production-co-sae-historical-data',
    'atlc': 'https://www.investing.com/equities/al-tawfeek-financial-historical-data',
    'auto': 'https://www.investing.com/equities/gb-auto-s.a.e-historical-data',
    'efid': 'https://www.investing.com/equities/edita-food-industries-historical-data',
    'orhd': 'https://www.investing.com/equities/orascom-hotels-and-development-historical-data',
    'rmda': 'https://www.investing.com/equities/tenth-of-ramadan-for-pharmaceutical-historical-data',
    'comi': 'https://www.investing.com/equities/com-intl-bk-historical-data',
    'etel': 'https://www.investing.com/equities/telecom-egypt-historical-data',
    'olfi': 'https://www.investing.com/equities/obour-land-for-food-industries-historical-data',
    'qnba': 'https://www.investing.com/equities/natl-soc-gen-b-historical-data',
    'adib': 'https://www.investing.com/equities/abu-dhabi-islamic-bank-egypt-historical-data',
    'amoc': 'https://www.investing.com/equities/alx-mineral-oi-historical-data',
    'egch' : 'https://www.investing.com/equities/egypt-chem-ind-historical-data',
    'csag' : 'https://www.investing.com/equities/canal-shipping-historical-data',
    'emfd' : 'https://www.investing.com/equities/emaar-misr-for-development-sae-historical-data',
    'orwe' : 'https://www.investing.com/equities/oriental-weave-historical-data',
    'ORAS' : 'https://www.investing.com/equities/orascom-construction-ltd-historical-data',
    'RACC' : 'https://www.investing.com/equities/raya-contact-center-historical-data',
    'skpc' : 'https://www.investing.com/equities/sidi-kerir-pet-historical-data',
    'swdy' : 'https://www.investing.com/equities/elsewedy-cable-historical-data',
    'east' : 'https://www.investing.com/equities/eastern-co-historical-data',
    'cira' : 'https://www.investing.com/equities/cairo-investment---re-development-historical-data',
    'heli' : 'https://www.investing.com/equities/heliopolis-housing-historical-data',
    'mtie' : 'https://www.investing.com/equities/mm-group-for-industry-historical-data',
    'saud' : 'https://www.investing.com/equities/barka-egypt-ba-historical-data',
    'hdbk' : 'https://www.investing.com/equities/housing---dev-historical-data',
    'tmgh' : 'https://www.investing.com/equities/t-m-g-holding-historical-data',
    'arcc' : 'https://www.investing.com/equities/arabian-cement-co-sae-historical-data',
    'ccap' : 'https://www.investing.com/equities/citadel-capita-historical-data',
    'cich' : 'https://www.investing.com/equities/ci-capital-historical-data',
    'clho' : 'https://www.investing.com/equities/cleopatra-hospital-historical-data',
    'esrs' : 'https://www.investing.com/equities/ezz-steel-historical-data',
    'hrho' : 'https://www.investing.com/equities/efg-hermes-hol-historical-data',
    'jufo' : 'https://www.investing.com/equities/juhayna-food-industries-historical-data',
    'ocdi' : 'https://www.investing.com/equities/6th-oct-dev-in-historical-data',
    'phar' : 'https://www.investing.com/equities/egypt-intl-phr-historical-data',
    'raya' : 'https://www.investing.com/equities/raya-tech---co-historical-data',
    'uasg' : 'https://www.investing.com/equities/un-arab-shippi-historical-data',
    'uegc' : 'https://www.investing.com/equities/upper-egypt-co-historical-data',
    'ascm' : 'https://www.investing.com/equities/asec-mining-co-historical-data',
    'oih' : 'https://www.investing.com/equities/orascom-telecom-media---technology-historical-data',
    'aih' : 'https://www.investing.com/equities/arabia-inv-development---cash-historical-data',
    'aspi' : 'https://www.investing.com/equities/pioneers-hldg-historical-data',
    'binv' : 'https://www.investing.com/equities/bpe-financial-historical-data',
    'btfh' : 'https://www.investing.com/equities/beltone-financial-holding-historical-data',
    'cieb' : 'https://www.investing.com/equities/credit-agricol-historical-data',
    'fait' : 'https://www.investing.com/equities/faisal-islmc-e-historical-data',
    'adpc' : 'https://www.investing.com/equities/the-arab-dairy-products-co.-historical-data',
    'domt' : 'https://www.investing.com/equities/arabian-food-industries-co-historical-data',
    'etrs' : 'https://www.investing.com/equities/egyptrans-historical-data',
    'prmh' : 'https://www.investing.com/equities/prime-holding-historical-data',
    'poul' : 'https://www.investing.com/equities/cairo-poultry-historical-data',
    'fwry' : 'https://www.investing.com/equities/fawry-banking-and-payment-historical-data',
    'mcqe' : 'https://www.investing.com/equities/misr-cement-qe-historical-data',
    'elec' : 'https://www.investing.com/equities/electro-cable-historical-data',
    'engc' : 'https://www.investing.com/equities/eng-indust(ico)-historical-data',
    'gssc' : 'https://www.investing.com/equities/silos---storag-historical-data',
    'irax' : 'https://www.investing.com/equities/el-ezz-ald-ste-historical-data',
    'ismq' : 'https://www.investing.com/equities/iron-steel-for-mines-quarries-historical-data',
    'krdi' : 'https://www.investing.com/equities/al-khair-river-for-development-historical-data',
    'lcsw' : 'https://www.investing.com/equities/lecico-egypt-historical-data',
    'nccw' : 'https://www.investing.com/equities/nasr-civil-wor-historical-data',
    'pach' : 'https://www.investing.com/equities/paint---chem-i-historical-data',
    'rubx' : 'https://www.investing.com/equities/rubex-plastic-historical-data',
    'scem' : 'https://www.investing.com/equities/sinai-cement-historical-data',
    'isph' : 'https://www.investing.com/equities/ibnsina-pharma-historical-data',
    'amer' : 'https://www.investing.com/equities/amer-group-holding-historical-data',
    'mnhd' : 'https://www.investing.com/equities/medinet-nasr-h-historical-data',
    'phdc' : 'https://www.investing.com/equities/palm-hill-dev-historical-data',

}

STOP = False

UPDATED = {}

WAIT = ['https://media.giphy.com/media/lj4gGwQ4EN9Ejkts0a/giphy.gif','https://media.giphy.com/media/xUPGcvyqs4xstt4lO0/giphy.gif','https://media.giphy.com/media/gWFTXUNVs7YGY/giphy.gif','https://media.giphy.com/media/96OcHR3Ojz9QI/giphy.gif','https://media.giphy.com/media/CZfBG2paczqnr3xXmB/giphy.gif','https://media.giphy.com/media/SWovhw1Nua7Ay5XFCb/giphy.gif','https://media.giphy.com/media/8L1q0fShuOPsVQoxDd/giphy.gif','https://media.giphy.com/media/rGBKvBKoYjh3XXfZ8i/giphy.gif','https://media.giphy.com/media/EHd2lEosyngtzIj0N5/giphy.gif','https://media.giphy.com/media/edPBGm4sZQhxBqU6qv/giphy.gif','https://media.giphy.com/media/1nb4Bse0yLito53gJI/giphy.gif','https://media.giphy.com/media/3EDdechXo4a4vMBWHG/giphy.gif','https://media.giphy.com/media/BWCu9zt5PhKtpwTUhw/giphy.gif']
DONE = ['https://media.giphy.com/media/M0EStXvkjbLMc/giphy.gif','https://media.giphy.com/media/GVdZnIUqGsJQQ/giphy.gif','https://media.giphy.com/media/3o6ZsTnhKGasJ2jurm/giphy.gif','https://media.giphy.com/media/8tbxKRmM0gHujSVTXV/giphy.gif','https://media.giphy.com/media/dmjCMRYLNG0DK/giphy.gif','https://media.giphy.com/media/wzD3nQPA4gqHK/giphy.gif','https://media.giphy.com/media/KU9xntRQg8nQc/giphy.gif','https://media.giphy.com/media/j3t3Zqn2MDxz0ETqxq/giphy.gif','https://media.giphy.com/media/Rk8wCrJCrjRJ2MyLrb/giphy.gif']
HEY = ['https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif','https://media.giphy.com/media/OnnUZxcHsbBN6/giphy.gif','https://media.giphy.com/media/fBEooAGRIJ2GrhE53W/giphy.gif','https://media.giphy.com/media/n7KBLYG0Yqs0aZa4iP/giphy.gif','https://media.giphy.com/media/ELUtlbLMx8K0U/giphy.gif','https://media.giphy.com/media/dYx3YFq2OiVLIssQH9/giphy.gif','https://media.giphy.com/media/rwsHPJ5zOkD0mVwAlC/giphy.gif','https://media.giphy.com/media/SUtKUblVAvwMkTvaiT/giphy.gif']
OK = ['https://media.giphy.com/media/QKkV58ufpV4ksJ1Okh/giphy.gif','https://media.giphy.com/media/uNKodMgFa6TXJiAAC8/giphy.gif','https://media.giphy.com/media/aFb8p2NS4mPxV1F8OM/giphy.gif','https://media.giphy.com/media/d56crtwhXYRB62P6mo/giphy.gif','https://media.giphy.com/media/H6DkR4abNR1zhi5gLc/giphy.gif']
BYE = ['https://media.giphy.com/media/JshL4uZk1tZt5W0TWV/giphy.gif','https://media.giphy.com/media/m9eG1qVjvN56H0MXt8/giphy.gif','https://media.giphy.com/media/kaBU6pgv0OsPHz2yxy/giphy.gif','https://media.giphy.com/media/2IBGFoEuwVPHv1EBq8/giphy.gif']