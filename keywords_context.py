#task: search the keywords and ascertain the context
# step 1: in the json, loop the keywords firstly in the pdf titles, and the documents match one or more keywords, take out these documents and make the keywords their context.
# step 2: for the rest of documents that titles do not match keyword, search the wordings "agenda item" that is nearest to "non-intervention" (before "non-intervention"), and loop the keywords.
# step 3: for the rest of documents that have no clear titles or no agenda item before non-intervention, search the keywords within the 100 words above and after non-intervention, or probably use distance search, the unsupervised one?


(1) Economic intervention
    'trade embargo against south africa': ['embargo','trade','trade embargo','sanction','South Africa', 'apartheid', 'race', 'racist', 'Namibia']
    'trade embargo against Nicaragua': ['embargo', 'trade', 'trade embargo','sanction','Nicaragua', 'United States']
    'trade embargo': ['embargo', 'trade', 'trade embargo', 'sanction', 'development']
    'cuba_embargo': ['Necessity of ending the economic, commercial and financial embargo imposed by the United States of America against Cuba','cuba', 'embargo', 'United States', 'blockade', 'Necessity']
    'sanctions_Syria': ['unilateral sanction', 'sanction', 'Syria','economic']
    'unilateral sanctions': ['unilateral sanction', 'sanction', 'economic', 'developing', 'targeted', 'financial', 'travel', 'aviation', 'arms', 'embargo']
    'unilateral coercive measure': ['unilateral coercive measure', 'unilateral measure', 'sanction', 'right to development', 'human rights', 'extraterritorial', 'coercive economic measures']
    'permanent rights over natural resources': ['permanent rights over natural resources', 'natural resource', 'natural wealth', 'sovereignty', 'economic independence', 'developing countries', 'raw materials']
    'national protectionism in foreign investment': ['economic development of under-developed', 'sovereignty', 'on behalf of their nationals']
    'economic cooperation': ['domestic economic affairs of other State', 'discrimination', 'trade freely', 'free trade', 'natural resources', 'Declaration on International Economic Co-operation']
    'technical assistance for economic development': ['Expanded Programme of Technical Assistance', 'technical assistance', 'economic development', 'technical personnel', 'industrialization', 'developing countries']
    'use of scientific and technological progress': ['declaration on the use of scientific and technological progress in the interests of peace and for the benefit of mankind', 'scientific and technological progress', 'peace', 'benefit', 'mankind', 'technological']
    'Technical co-operation among developing countries': ['Technical co-operation among developing countries', 'UNDP', 'developing countries', 'co-operate']
    'development': ['developing countries', 'debt servicing', 'aid', 'donor', 'growth', 'ecnomic development', 'development', 'co-operation', 'economic cooperation', 'UNDP']
    'Social Progress and Development': ['Declaration on Social Progress and Development']
    'CMEA': ['Council for Mutual Economic Assistance']
    'Lima Declaration': ['Lima Declaration and Plan of Action on Industrial Development and Cooperation','Lima Declaration and Plan of Action', 'United Nations Industrial Development Organization', 'industrial development board']
    'restrictive trade measures': ['restrictive trade measures','non-economic purposes']
    'NIEO': ['new international economic order']
    'Guadalajara Declaration': ['Guadalajara Declaration', 'economic development']
#right to negotiate': ['Madagasga']
#'Zambia': ['Zambia', 'Portugal dispute on economic independence']



(2) military intervention
    'korea': ['United Nations Commissions on Korea', 'Commission for the Unification and Rehabilitation of Korea','UNCURK']
    'Greece': ['Threats to political independence and territorial integrity of Greece']
    'morocco': ['question of Morocco']
    'Tunisian': ['tunisian question', 'internal political situation in Tunisia']
    'Algeria': ['Question of Algeria']
    'Cyprus': ['Question of Cyprus']
    'Cambodia': ['Situation in Cambodia', 'Situation in Kampuchea']
    'Territories under Portuauese administration': ['Territories under Portuauese administration','trustee territory', 'Angola independence', 'Portual colonialism']
    'Togoland':['Togoland', 'Trustee system']
    'South West Africa': ['South West Africa', 'Question of South West Africa']
    'Guinea-Bissau and Cape Verde': ['Guinea-Bissau and Cape Verde', 'Guinea-Bissau', 'Portugal illegal occupation']
    'Indian Ocean peace zone': ['Indian Ocean peace zone', 'denuclearized']
    'Trust Territory of the Pacific Islands': ['Trust Territory of the Pacific Islands']
    'Israel Egypt Dispute': ['Non-Proliferation of Nuclear Weapons', 'occupation of Arab', 'Israel', 'Egypt']
    'Israel intervention in the middle east': ['Israel', 'middle east', 'aggression', 'occupation']
    'Afganistan': [ 'withdraw of forces from Afganistan', 'aggression', 'United States', 'Soviet Union']
    'Afganistan/Pakistan': ['Situation in Afganisan','bilateral agreement between Afghanistan and Pakistan', 'its implications for international peace and security']
    'Iran/Iraq': ['situation between Iraq and Iran', 'agreement of Iraq and Iran', 'Consequences of the prolongation of the armed conflict between Iran and Iraq']
    'Tunisia and Libya': ['Dispute between Tunisia and the Libyan Arab Jamahiriya', 'peaceful settlement']
    'situation in central america': ['situation in central america', 'peace in Central America', 'Contadora Group']
    'weapon arm smuggling into Chile, terrorism': ['massive quantity of weapons and war', 'Chile','smuggle', 'terrorism']
    'Palestine': ['question of Palestine', 'withdraw', 'all Occupied Arab territories', 'Palestinc Liberation Orqanization']
    'Nicaragua against US': ['United States embargo against Nicaragua', 'Military and Paramilitary Activities in and against Nicaragua ']
    'US intervention in Panama': ['United States Army in Panama', 'incursion into Panamanian territory', 'Panama Canal Treaties', 'military harassment', 'aggressive policy']


# 'Cuba intervention in Haiti': ['Cuba intervention in Haiti']
# 'Cuban intervention in Chile': []   
# 'Iraqi intervention in Kuwait': []
# 'Yemen foreign troops in Oman': []
# 'cuban intervention in Venezuela': []
    


(3) international cooperation (terrorism, corruption, drug, disarmament)
    'corruption': ['United Nations Convention against Corruption']
    'drug/colombia': ['world drug', 'drug', 'colombia', 'drug trafficking', 'traffick']
    'mercenaries': ['Mercenarism', 'mercenaries']
    'drug': ['international drug control', 'international cooperation against the world drug problem', 'drug trafficking', 'trafficking of drug', 'world drug problem'],
    'arms': ['arms trade','arms trade treaty', 'small arms', 'light weapons','firearms', 'ammunition', 'arms trafficking', 'private military and security companies', 'international transfers'],
    'disarmament': ['disarmament', 'committee on disarmament', 'conference on disarmament', 'disarmament commission', 'arms race', 'renunciation of force', 
                    'peaceful settlement', 'settlement of disputes', 'confidence-building', 'peace', 'security', 'international peace and security', 
                    'arms limitation', 'non-proliferation of nuclear weapon',],
    'terrorism': ['comprehensive convention on international terrorism', 'counter-terrorism', 'terrorism'],
    'transnational crime': ['Commission on Crime Prevention and Criminal Justice', 'Economic and Social Council', 'transnational crime'],
    'nuclear': ['atomic energy', 'Atomic Energy Commission', 'peaceful uses of atomic energy', 'nuclear', 'International Atomic Energy Agency'], 
    'peaceful uses of outer space': ['peaceful uses of outer space', 'militarisation', 'outer space']


(4) humanitarian, peacekeeping, peace/security
    'peacekeeping': ['peacekeeping', 'Peacekeeping operations', 'Peace operation', 'department of peacekeeping']
    'Special Committee on Peacekeeping Operations': ['Special Committee on Peacekeeping Operations']
    'Comprehensive review of the whole question of peace-keeping operations in all their aspects': ['Comprehensive review of the whole question of peace-keeping operations in all their aspects']
    'Peacebuilding in central america': ['Procedures for the establishment of a firm and lasting peace and progress','central america', 'peace, freedom, democracy and development'],
    'peacebuilding': ['peacebuilding', 'peacebuilding commission', 'early warning', 'good offices', 'non-military measures'],
    'promotion of the right of peoples to peace': ['promotion of the right of peoples to peace', 'international disputes', 'peaceful means', 'Declaration of the Right of Peoples to Peace']
    'humanitarian assistance': ['humanitarian assistance', 'right to humanitarian assistance', 'humanitarian aid', 'unlawful intervention','tension', 'principle of subsidiarity', 'rights-based approach', 'Mohonk Criteria']
    'Strengthening of security and cooperation in the Mediterranean region': ['Strengthening of security and cooperation in the Mediterranean region', 'cooperation in the Mediterranean region']
    'Crimes against the Peace and Security': ['Crimes against the Peace and Security'],
    'right to peace': ['right to peace', 'fundamental human right', 'Universal Declaration of Human Rights']
    'Declaration on the Right of Peoples to Peace': ['Declaration on the Right of Peoples to Peace']
    'Strengthening of International Security': ['declaration on the stregthening of international security', 'détente', 'international peace and security']
    'comprehensive system of international peace and security': ['comprehensive system of international peace and security', 'establishment of a comprehensive system of international peace and security ']
    'declaration on the preparation on societies for life in peace': ['declaration on the preparation on societies for life in peace', 'preparation on societies for life in peace'],
    'situation in Yemen': ['situation in the Republic of Yemen', 'resolution 924']

#'UN intervention in Iran in 2018'
# 'United Nations Monitoring Mechanism for the Syrian Arab Republic'


(5) human rights:
    'human rights': ['human rights', 'humanitarian assistance', 'humanitarianism', 'non-indifference', 'universal declaration of human rights'],
    'protection of persons in the event of disasters': ['protection of persons in the event of disasters', 'international law commission', 'natural disasters', 'United Nations Disaster Relief']
    'genocide': ['genocide', 'Rwanda', 'ethnic cleansing', 'crimes against humanity', 'atrocities', 'war crimes']
    'responsibility to protect': ['responsibility to protect']
    'humanitarian intervention': ['humanitarian intervention', 'responsibility to protect']
    'apartheid': ['human right', 'indian origin', 'south africa', 'discriminatory measures', 'racial doctrines', 'measures of discrimination', 'segregation','race conflict']
    'criminal court': ['international criminal court', 'establishment of international criminal court', 'jurisdiction']
    'self-determination': ['self-determination', 'inalienable rights of peoples', 'declaration on the granting of independence to colonial countries and peoples']
    'forced labour': ['forced labour', 'right to petition'],
    'diplomatic asylum': ['diplomatic asylum']
    'Torture and other cruel, inhuman or degrading treatment or punishment in relation to detention and imprisonment': ['Torture and other cruel, inhuman or degrading treatment or punishment', 'Torture and other cruel, inhuman or degrading treatment or punishment in relation to detention and imprisonment', 'detention and imprisonment' ]
    'protection of minorities': ['protection of minorities']
    'Human rights in armed conflicts': ['Human rights in armed conflict', 'right to life', 'protection of journalists', 'dangerous missions in areas of armed conflict']
    'Stateless persons': ['Convention on the Reduction of Statelessness', 'stateless persons']
    'women right': ['international womens year', 'women']
    #i don't know how to add women's year, instead of women year.
    'human rights in Chile': ['Protection ofhuman rights in Chile']
    'refugee': ['Human riqhts and mass exoduses', 'refugee', 'principle of cooperation']
    'alternative approach and ways and means within the United Nations System for improving the effective enjoyment of human rights and fundamental freedoms': ['alternative approach and ways and means', 'improving the effective enjoyment of human rights and fundamental freedoms']
    'Strengthening of United Nations action in the human rights field through the promotion of international co-operation and the strict observance of the principle of non-intervention': ['Strengthening of United Nations action in the human rights field through the promotion of international co-operation and the strict observance of the principle of non-intervention', 'promotion of internotional co-operation and the strict observance of the principle of non-intervention', 'non-selectivity, impartiality and objectivity']
    'enhancing the effectivenss of the principle of periodic and genuine elections': ['enhancing the effectivenss of the principle of periodic and genuine elections', 'principle of periodic and genuine elections']
    'Trade-union rights': ['Trade-union rights', 'economic development']
    'Haiti': ['question concerning Haiti', 'situation of democracy and human rights in Haiti']
    'Promotion of a democratic and equitable international order': ['Promotion of a democratic and equitable international order']

(6) UN laws
    'UN Declaration on Rights and Duties of States': ['Declaration on Rights and Duties of States']
    'admission of new members': ['admission of new members']
    'ILC Draft on arbitral procedures': ['international law commission', 'arbitral procedures', 'Drfat on arbitral procedures']   
    'codification and progressive development of international law': ['codification and progressive development of international law']
    'principles of international law concerning friendly relations': ['principles of international law concerning friendly relations']
    'jus cogens': ['international law commission', 'jus cogens', 'law of treaties']
    'Progressive development of the law of international trade': ['Progressive development of the law of international trade', 'international trade law', 
        'law of international trade',  'progressive development', 'national independence', 'United Nations Commission on International Trade Law']
    'diplomatic immunity': ['diplomatic privilege', 'immunity', 'immunities', 'international law commission']
    'enlarge UN cooperation in conflict resolving': ['Strengthening of the role of the United Nations', 'maintenance and consolidation of international peace and security', 'co-operation among all nations', 'promotion of the rules of international law in relations between States']
    'review of the Charter of the United Nation': ['review of the Charter of the United Nations', 'Charter of the United Nations']
    'un decade of international law': ['un decade of international law', 'promotion of acceptance of and respect for principles of international law']
    'Draft United Nations Millennium Declaration': ['Draft United Nations Millennium Declaration', 'Millennium Declaration']

#'peaceful co-existence': []
#'Chinese Seat at UN'
# 'Application from the German Democratic Republic for membership in UNESCO'
#'Draft international covenants on human rights': ['Draft international covenants on human rights']
# 'ILC draft articles on special missions (vienna convention on diplomatic relations)': ['vienna convention', 'special mission']
# 'suggested to replace non-interference with non-intervention'
# state responsibility': ['international law commission', 'restitutio in integrum', 'domestic jurisdiction']

(7) political intervention
    'broadcasting': ['inflammatory', 'subversive', 'broadcast', 'war propaganda', 'propaganda', ]
    'Artificial Earth Satellites': ['international convention on principles governing the use by States of Artificial Earth Satellites', 'Artificial Earth Satellites', 'direct television broadcasting']
    'Freedom of Information': ['Convantion on Freedom of Information', 'freedom of information', 'Declaration on Freedom of Information']
    'diplomatic immunity': ['immunity of State officials', 'international law commission']
    
(8) Regional movements:
    'Non-aligned movement': ['non-aligned countries', 'non-aligned movement']
    'League of Arab States': ['League of Arab States']
    'Contadora group': ['Contadora group']
    'Group of 77 and China': ['Group of 77 and China']
    'Islamic Conference': ['Islamic Conference']
    'Rio Group': ['Rio Group']
    'Group of Arab States': ['Group of Arab States']
    'ECOWAS': ['ECOWAS', 'Economic Community of West African States']
    'OAS': ['Organization of American States']
    'Gulf Cooperation Council': ['Gulf Cooperation Council']
    'Asian Group': ['Asian Group']
    'ASEAN': ['ASEAN']
    
#'domestic constitution': ['constitution'],
