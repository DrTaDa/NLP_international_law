unwanted_words = [
    'GENERAL ASSEMBLY OFFICIAL RECORDS',
    'SECURITY COUNCIL', 
    'GENERAL ASSEMBLY, OFFICIAL RECORDS', 
    'RESOLUTIONS AND DECISIONS ADOPTED BY THE GENERAL ASSEMBLY DURING',
    'SC BOOK OF RESOLUTIONS AND DECISIONS',
    'LETTER DATED',
    'IDENTICAL LETTERS',
    'LETTER', 
    'IDENTICAL NOTES VERBALES',
    'REPORT ADDENDUM',
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY',
    'THURSDAY',
    'FRIDAY',
    'SATURDAY',
    'CURRICULA VITAE',
    'PLENARY','SECRETARIAT', 
    'UNITED NATIONS DOCUMENTS INDEX', 
    'NOTE VERBALE',
    'VERBATIM RECORD',
    'PROVISIONAL AGENDA',
    'ANNOTED AGENDA',
    'ANNOTATED DRAFT AGENDA',
    'WORLD PLAN OF ACTION',
    'STRATEGIC FRAMEWORK',
    'DAILY LIST',
    'THE INDEPENDENCE AND IMPARTIALITY OF THE JUDICIARY', 
    'INDEPENDENCE OF JUDGES AND LAWYERS',
    'REPORT OF THE SECOND COMMITTEE',
    'REPORT OF THE 2ND COMMITTEE',
    'REPORT OF THE THIRD COMMITTEE',
    'REPORT OF THE 3RD COMMITTEE',     
]

topics = {
    'threats_to_peace_security': ['THREAT TO PEACE AND SECURITY', 'SITUATION IN', 'QUESTION OF PALESTINE', 'OCCUPIED PALESTINIAN TERRITORY'],
    'terrorism': ['TERRORISM', 'TERRORIST'],
    'disarmament': ['DISARMAMENT', 'PROLIFERATION', 'NUCLEAR WEAPONS', 'NUCLEAR','CHEMICAL WEAPONS','BACTERIOLOGICAL', 'TOXIN WEAPONS', 'SMALL ARMS', 'LIGHT WEAPONS', 'FIREARMS', 'ARMS', 'AMMUNITION'],
    'arms_embargo': ['ARMS EMBARGO'], 
    'peace_security_in_specific_regions': ['Indian Ocean Peace Zone', 'Andean Zone of Peace', 'African Nuclear-Weapon-Free Zone', 
        'security and cooperation in the Mediterranean region', 'good-neighbourly relations among Balkan States'],
    'outer_space': ['Direct Television Broadcasting', 'outer space'],
    'mercenaries': ['MERCENARIES', 'MERCENARY'],
    'international_security': ['Strengthening of International Security', 'protection and security of small states'],
    'Cybercrime': ['cybercrime', 'information and telecommunications in the context of international security'],
    'crime_against_peace': ['crimes against peace', 'crimes against the peace'],
    'state_succession': ['Succession of States'],
    'trade_embargo': ['Financial Embargo imposed by the United States of America against Cuba', 'Trade embargo', 'embargo against Nicaragua', 'embargo against South Africa'],
    'ucm': ['UNILATERAL COERCIVE MEASURES', 'UNILATERAL ECONOMIC MEASURES','ECONOMIC MEASURES','UNILATERAL MEASURE', 
        'ECONOMIC COERCION','ECONOMIC SANCTION','UNILATERAL ACTS'],
    'economic_cultural_right': ['Economic, social and cultural rights', 'ICESCR'],
    'esc': ['ECONOMIC AND SOCIAL COUNCIL', 'ECONOMIC AND SOCIAL',
           'INTERNATIONAL ECONOMIC CO-OPERATION',
           'WORLD SOCIAL SITUATION'],
    'right_to_development': ['right to development', 'SUSTAINABLE DEVELOPMENT', 'ECONOMIC SECURITY', 'DEVELOPMENT AS A HUMAN RIGHT','INTERNATIONAL DEVELOPMENT COOPERATION'],
    'NIEO': ['New International Economic Order', 'NIEO', 'Permanent Sovereignty over Natural Resources', 'Charter of Economic Rights and Duties of States'],
    'trade_development': ['UNCTAD', 'TRADE AND DEVELOPMENT','United Nations Conference on Trade and Development', 'Action Programme of Lima', 'Lima Declaration', 'Industrial Development'],
    'financial_aid_technical_assistance': ['FINANCING FOR DEVELOPMENT', 'the terms and conditions of aid', 'Development Assistance Committee', 'Council for Mutual Economic Assistance', 
        'political dialogue between creditor and debtor countries', 'foreign debt', 'Financing for Development to Review the Implementation of the Monterrey Consensus'],
    'transnational_corporations': ['transnational corporations', 'TNCs'],
    'credentials': ['Credentials committee', 'Credential'],
    'election_interference': ['Election itnerference', 'electoral interference', 'election intervention','electoral intervention', 'electoral process',
        'Respect for the principles of national sovereignty and non-interference in the internal affairs of States in their electoral processes'],
    'broadcasting_propaganda': ['Direct Television Broadcasting', 'propaganda', 'war-mongering'], 
    'disinformation': ['Disinformation', 'freedom of information', 'countering the use of information and communication technologies for criminal purposes', 'Committee on Information', 'information and communication technologies',
        'Strengthening of United Nations action in the human rights field through the promotion of international co-operation and the strict observance of the principle of non-intervention'],
    'diplomatic_protection': ['diplomatic protection', 'Vienna Convention on Diplomatic Relations', 'Draft Articles on Diplomatic Protection'],
    'asylum': ['Right of asylum', 'diplomatic asylum'],
    'diplomatic_immunities': ['privileges and immunities', 'jurisdiction immunities of states', 'Diplomatic Intercourse and Immunities', 'Immunity of State Officials'],
    'foreign_agent': ['foreign agent', 'espionage', 'sabotage'],
    'human_rights': ['HUMAN RIGHTS','non-indifference', 'World Conference on Human Rights', 'NATIONAL REPORT', 'PERIODIC REPORT', 'UNIVERSAL PERIODIC REVIEW', 
                    'CONCLUDING OBSERVATIONS', 'CORE DOCUMENT', 'REPORTS SUBMITTED BY STATES PARTIES', 'human rights situation', 'situaiton of human rights'],
    'torture': ['Torture, and other cruel, inhuman or degrading treatment or punishment', 'torture'],
    'civil_political_rights': ['International Covenant on Civil and Political Rights', 'ICCPR'],
    'democracy': ['DEMOCRACY','DEMOCRATIC', 'DEMOCRATIZATION', 'GENUINE AND PERIODIC ELECTION', 'Exercise of the Holding of Elections',
        'promotion of a democratic and equitable international order', 'promotion and consolidation of democracy'],
    'right_to_life': ['right to life'], 
    'right_to_peace': ['Right of peoples to peace', 'Promotion of peace as a vital requirement for the full enjoyment of all human rights by all', 
        'Implementation of the Declaration on the Right of Peoples to Peace', 'Promotion of the right of peoples to peace'],
    'self-determination': ['self-determination', 'Granting of Independence to Colonial Countries and Peoples', 
        'Universal Realization of the Right of Peoples to Self-determination', 'Armed intervention and the right of peoples to self-determination'],
    'Migration': ['migration', 'migrants', 'refugee', 'mass exoduses', 'displaced persons'], 
    'genocide': ['GENOCIDE', 'CRIMES AGAINST HUMANITY'],
    'detention': ['ARBITRARY DETENTION','DETENTION','ENFORCED DISAPPEARANCE'],
    'racism':['RACISM', 'DISCRIMINATION', 'XENOPHOBIA', 'RACIST','APARTHEID'],
    'minority': ['MINORITY', 'MINORITIES', 'Prevention of Discrimination and Protection of Minorities'],
    'r2p':['RESPONSIBILITY TO PROTECT', 'World Summit Outcome', 'New International Humanitarian Order', 'HUMAN SECURITY'],
    'child': ['RIGHTS OF THE CHILD', 'CHILD'],
    'foreign_criminal_jurisdiction': ['foreign criminal jurisdiction', 'universal jurisdiction', 'Rome Statute', 'international criminal court', 'immunity of State officials from foreign criminal jurisdiction'], 
    'Religious freedom': ['Declaration on the Elimination of All Forms of Intolerance and of Discrimination Based on Religion or Belief', 'religious freedom', 'RELIGION', 'RELIGIOUS', 'RELIGIOUS INTOLERANCE'],
    'NGO_interference': ['subversive', 'NON-GOVERNMENTAL ORGANIZATION', 'NGO'], 
    'disaster_relief': ['Protection of persons in the event of disasters', 'disaster relief', 'humanitarian assistance'],
    'Capital Punishment': ['Capital Punishment'], 
    'UN_role': ['Strengthening of the role of the United Nations', 
        'strengthening the relationship and cooperation between the United Nations and regional arrangements or agencies in the peaceful settlement of disputes',
        'fundamentals of the legal basis for United Nations peacekeeping operations in the context of Chapter VI of the Charter of the United Nations'],
    'decade_of_international_law': ['Decade of International law'],
    'Millennium Declaration': ['Millennium Declaration'], 
    'rule_of_law': ['Rule of Law', 'Rule of law, crime prevention and criminal justice in the United Nations development agenda beyond 2015'],
    'trade_law': ['Progressive development of the law of international trade', 'UN Commission on the International Trade Law', 'UNCITRAL'],
    'charter_review': ['Review of the Charter of the UN', 'need to consider suggestions regarding the review of the Charter of the United Nations', 'view of the Charter of the United Nations'],
    'negotiation': ['INTERNATIONAL NEGOTIATIONS'],
    'enforcement': ['Enhancing international law enforcement cooperation'],
    'special committee': ['Definition of Aggression', 'Principles of International Law Concerning Friendly Relations', 'Enhancing the Effectiveness of the Principle of Non-Use of Force in International Relation'],
    'ilc': ['UN Declaration on Rights and Duties of States', 'State responsibility','Law of treaties', 'Identification of customary international law', 'General principles of law', 
        'Fragmentation', 'Protection of the environment in relation to armed conflicts', 'Unilateral acts of States', 'Protection of the atmosphere', 'arbitral procedures', 
        'draft articles on special missions', 'draft articles on Representation of states in their relations with international organizations'],
    'icj': ['ICJ', 'international court of justice'], 
    'drug': ['DRUG', 'NARCOTIC', 'ILLCIT OPIATES', 'ALTERNATIVE DEVELOPMENT', 'PSYCHOACTIVE'],
    'corruption': ['CORRUPTION','ASSET RECOVERY', 'Convention against Corruption', 'EFFECTIVE GOVERNANCE'],
    'transnational_organized_crime': ['TRANSNATIONAL ORGANIZED CRIME', 'TRANSNATIONAL CRIME', 'ILLEGAL TRANSFER OF FUNDS'],
    'trafficking': ['Drug trafficking', 'Trafficking in Firearms', 'Trafficking in Cultural Property', 'Cultural Property'], 
    'south_south': ['SOUTH-SOUTH COOPERATION', 'SOUTH-SOUTH', 'SOUTH-SOUT', 'SOUTH SOUTH','DOHA PLAN OF ACTION',
        'Addis Ababa Action Agenda of the Third International Conference on Financing for Development',
        'Role of South-South cooperation and the implementation of the 2030 Agenda for Sustainable Development', 
        'New Agenda for the Development of Africa', 'United Nations Conference on the Least Developed Countries','Poverty eradication',
        'High-level conference of middle-income countries', 'Trends and progress in international development cooperation',
        'Operational activities for development', 'United Nations Conference on South-South Cooperation'],
    'international_economic_cooperation': ['Declaration on International Economic Co-operation', 'international cooperation in energy production, new and renewable energy sources'],
    'social_development': ['World Summit for Social Development', 'Declaration on Social Progress and Development', 'Scientific and technological progress in the interests of peace and for the benefit of mankind'],
    'Environment': ['A GLOBAL PACT FOR THE ENVIRONMENT', 'ASEAN AGREEMENT ON TRANSBOUNDARY HAZE POLLUTION'], 
    'Law of the sea': ['LAW OF THE SEA', 'unclos', 'flag state', 'co-operation in maritime merchant shipping', 'International Tribunal for the Law of the Sea', 'International Seabed Authority'],
    'Peacekeeping_Peacebuilding': ['PEACEKEEPING', 'PEACE-KEEPING', 'PEACEBUILDING', 'PROMOTION OF PEACE', 'AGENDA FOR PEACE'],
    'UN_mandates': ['UN OPERATION', 'STABILIZATION MISSION', 'UN HYBRID OPERATION',
                    'STABILIZATION AND RESTORATION','FACT-FINDING MISSION',
                    'UNMISS','UNAMI','UNISFA','MONUSCO','UNMIL','UNOCI','UNIOGBIS',
                    'INTERIM SECURITY FORCE','MANDATE','FACT-FINDING',
                   'MINUSCA', 'UNITED NATIONS GOOD OFFICES MISSION'],
    'peace_security': ['Comprehensive system of international peace and Security'],
    'prevention': ['Preventive Diplomacy', 'Conflict Prevention'],
    'confidence-building': ['CONFIDENCE-BUILDING', 'confidence building'],
    'peaceful settlement': ['Peaceful settlement of disputes', 'mediation'],
    'society_peace': ['Preparation of societies for life in peace'],
    'neutrality': ['neutrality', 'international neutrality day', 'INTERNATIONAL DAY OF NEUTRALITY'],
    'ecolatin': ['Economic commission for Latin America and the Caribbean'],
    'ecoafr': ['Economic Commission for Africa'],
    'United Nations Economic Commission for Europe': ['UNECE'],
    'NAM': ['Non-aligned movement', 'non aligned', 'non-aligned'],
    'league_arab': ['League of Arab States'],
    'group_arab': ['Group of Arab States'],
    'G77': ['G77 and China'],
    'Contadora': ['Contadora Group'],
    'islamic': ['Islamic Conference'],
    'rio': ['Rio Group'],
    'ECOWAS': ['Economic Community of West African States', 'ECOWAS'],
    'OAS': ['Organization of American States', 'OAS'],
    'Gulf': ['Gulf Cooperation Council'],
    'Asian': ['Asian Group'],
    'ASEAN': ['ASEAN', 'Association of Southeast Asian Nations']
}

topics_unrelated = {
    'health': ['the enjoyment of the highest attainable standard of physical and mental health', 'fight against HIV', 'HIV'],
    'housing': ['housing', 'right to adequate housing'],
    'food_water': ['right to food', 'water resources', 'ERADICATION OF HUNGER'],
    'families': ['protection of families'],
    'land': ['desertification', 'deforestation','land'],
    'climate': ['climate change', 'resource conservation'],
    'cultural_life': ['Right to take part in cultural life'],
    'work_eduation': ['right to work', 'right to education'],
    'women': ['women','elimination of discrimination against women', 'BEIJING DECLARATION', 'BEIJING PLATFORM', 'SEXUAL VIOLENCE IN CONFLICT'],
    'population': ['world population', 'fertility promotion'],
    'indigenous': ['indigenous peoples'], 
    'expression': ['freedom of expression and opinions', 'freedom of peaceful assembly'],
    'NGO activities': ['non-interference with the NGO’s activities'],
    'investigation': ['investigation functions'],
    'un_justice': ['administration of justice at the UN'],
    'judicial_independence': ['independence and impartiality'],
    'trustee': ['OVERSEAS DEPENDENT TERRITORIES', 'TRUSTEESHIP','NATIONAL LIBERATION MOVEMENTS'],
    'budget': ['BUDGET'],
}