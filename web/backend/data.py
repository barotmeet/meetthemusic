"""Static seed data for ClassicalVerse — mirrors src/data/seed.ts."""

RAGAS = [
    # --- Original entries ---
    {"slug": "yaman", "name": "Yaman", "tradition": "Hindustani", "thaat": "Kalyan", "time": "Evening (6-9 PM)", "mood": "Devotional, romantic", "aroh": "N R G M' D N S'", "avroh": "S' N D P M' G R S", "pakad": "N R G, M' D N S'", "vadi": "Ga", "samvadi": "Ni", "description": "One of the most fundamental ragas of Hindustani music, Yaman uses all natural notes with a sharp Madhyam. Its sweeping, romantic character makes it the first raga taught to many students."},
    {"slug": "bhairav", "name": "Bhairav", "tradition": "Hindustani", "thaat": "Bhairav", "time": "Early morning (7-10 AM)", "mood": "Solemn, meditative", "aroh": "S r G M P d N S'", "avroh": "S' N d P M G r S", "pakad": "D M r, G M P, M G, r S", "vadi": "Dha", "samvadi": "Re", "description": "An ancient morning raga that evokes austerity and devotion. Bhairav uses komal Re and komal Dha with characteristic andolan (oscillation)."},
    {"slug": "darbari", "name": "Darbari Kanada", "tradition": "Hindustani", "thaat": "Asavari", "time": "Late night (1-4 AM)", "mood": "Grave, majestic", "aroh": ".n S R g R S, M P d n R' S'", "avroh": "S' d n P, M P, g M R S", "pakad": "g M R S, .d .n S R S", "vadi": "Re", "samvadi": "Pa", "description": "Attributed to Mian Tansen of Akbar's court, Darbari is the regal night raga known for its slow, deep andolan on komal Ga and Dha."},
    {"slug": "bhimpalasi", "name": "Bhimpalasi", "tradition": "Hindustani", "thaat": "Kafi", "time": "Afternoon (10 AM - 1 PM)", "mood": "Longing, devotional", "aroh": ".n S g M P n S'", "avroh": "S' n D P M g R S", "pakad": ".n S M, M P g, M g R S", "vadi": "Ma", "samvadi": "Sa", "description": "A pentatonic-ascent raga of late afternoon, Bhimpalasi expresses yearning and is widely used in semi-classical forms."},
    {"slug": "malkauns", "name": "Malkauns", "tradition": "Hindustani", "thaat": "Bhairavi", "time": "Midnight (1-4 AM)", "mood": "Mystical, profound", "aroh": ".n S g M d n S'", "avroh": "S' n d M g M g S", "pakad": "M g, M d n d, M g, M g, S", "vadi": "Ma", "samvadi": "Sa", "description": "An ancient pentatonic raga of midnight, said to have the power to summon spirits. Uses komal Ga, Ma, Dha, Ni; omits Re and Pa."},
    {"slug": "shankarabharanam", "name": "Shankarabharanam", "tradition": "Carnatic", "thaat": "29th Melakarta", "time": "Anytime", "mood": "Auspicious, expansive", "aroh": "S R G M P D N S'", "avroh": "S' N D P M G R S", "pakad": "—", "vadi": "—", "samvadi": "—", "description": "The 29th Melakarta, equivalent to the Western major scale. A vast canvas for both kritis and elaborate raga alapana."},
    {"slug": "kalyani", "name": "Kalyani", "tradition": "Carnatic", "thaat": "65th Melakarta", "time": "Evening", "mood": "Joyful, auspicious", "aroh": "S R G M' P D N S'", "avroh": "S' N D P M' G R S", "pakad": "—", "vadi": "—", "samvadi": "—", "description": "The 65th Melakarta — the Carnatic counterpart of Yaman. Considered highly auspicious and a favorite of Tyagaraja."},
    {"slug": "carnatic-todi", "name": "Todi (Carnatic)", "tradition": "Carnatic", "thaat": "8th Melakarta (Hanumatodi)", "time": "Morning", "mood": "Pleading, devotional", "aroh": "S r g M P d n S'", "avroh": "S' n d P M g r S", "pakad": "—", "vadi": "—", "samvadi": "—", "description": "Hanumatodi — the 8th Melakarta. A deeply emotive raga that has inspired countless kritis."},
    # --- Bulk data (85 ragas) ---
    {"slug": "aabhogi", "name": "Aabhogi", "tradition": "Hindustani", "thaat": "Kafi", "time": "Morning", "mood": "Serene", "aroh": "S R g M D S'", "avroh": "S' D M g R S", "pakad": "D S R g M R S", "vadi": "Sa", "samvadi": "Ma", "description": "A morning raga from the Kafi thaat, Aabhogi is pentatonic and has a serene, devotional quality."},
    {"slug": "abhogi-kanhra", "name": "Abhogi Kanhra", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 AM to 1 PM", "mood": "Serene", "aroh": "S R g M D S'", "avroh": "S' D M g R S, .D S", "pakad": "M g R S, .D S R g, M D M g, R S", "vadi": "Sa", "samvadi": "Ma", "description": "A morning raga combining elements of Abhogi and Kanhra."},
    {"slug": "adana", "name": "Adana", "tradition": "Hindustani", "thaat": "Asavari", "time": "1 to 4 AM", "mood": "Intense, late night", "aroh": "S R M P, d N S'", "avroh": "S' d n P M P, g M R S", "pakad": "S' d N S', d, n P M P, g M R S", "vadi": "Sa'", "samvadi": "Pa", "description": "A powerful late-night raga from the Asavari thaat, Adana evokes intensity and grandeur."},
    {"slug": "ahir-bhairav", "name": "Ahir Bhairav", "tradition": "Hindustani", "thaat": "Bhairav", "time": "Morning", "mood": "Devotional, pastoral", "aroh": "S r G M, P D n S'", "avroh": "S' n D P, M G r S", "pakad": "G M r S, .D .N r S", "vadi": "Ma", "samvadi": "Sa", "description": "A morning raga combining Ahir and Bhairav elements, evoking pastoral devotion."},
    {"slug": "alahiya-bilaval", "name": "Alahiya Bilaval", "tradition": "Hindustani", "thaat": "Bilaval", "time": "Morning", "mood": "Bright, auspicious", "aroh": "S R G M G R, G P, D N S'", "avroh": "S' N D P, D n D P, M G M R S", "pakad": "G R G P, M G M R, G P D n D P", "vadi": "Dha", "samvadi": "Ga", "description": "A morning raga of Bilaval thaat, Alahiya Bilaval is bright and expansive."},
    {"slug": "asavari", "name": "Asavari", "tradition": "Hindustani", "thaat": "Asavari", "time": "10 AM to 1 PM", "mood": "Serious, contemplative", "aroh": "S R M P d S'", "avroh": "S' n d P M g R S", "pakad": "R M P, n d P, d M P, g R S", "vadi": "Dha", "samvadi": "Ga", "description": "A serious morning raga, Asavari is one of the ten parent thaats of Hindustani music."},
    {"slug": "bageshri", "name": "Bageshri", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 PM to 1 AM", "mood": "Romantic, longing", "aroh": "S g M D n S'", "avroh": "S' n D M g R S", "pakad": "S .n .D S, M g, M D n D, M g, M g R S", "vadi": "Ma", "samvadi": "Sa", "description": "A romantic night raga, Bageshri is beloved for its tender, yearning quality."},
    {"slug": "bahar", "name": "Bahar", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 AM to 1 PM", "mood": "Joyful, spring", "aroh": ".n S, g M P, g M, n D N S'", "avroh": "S' n D n P, M P g M R S", "pakad": "M P g M D N S'", "vadi": "Ma", "samvadi": "Sa", "description": "A raga of spring (bahar means spring), Bahar evokes joy and the arrival of the new season."},
    {"slug": "basant", "name": "Basant", "tradition": "Hindustani", "thaat": "Poorvi", "time": "4 to 7 AM", "mood": "Joyful, spring", "aroh": "S G M' d r' S'", "avroh": "r' N d P, M' G, M' d M' G, r S", "pakad": "M' d r' S', r' N d P, M' G M' G", "vadi": "Sa'", "samvadi": "Pa", "description": "A spring raga sung at dawn, Basant is festive and filled with the joy of the season."},
    {"slug": "bhairavi", "name": "Bhairavi", "tradition": "Hindustani", "thaat": "Bhairavi", "time": "Morning", "mood": "Tender, sorrowful", "aroh": "S r g M P d n S'", "avroh": "S' n d P M g r S", "pakad": "S g M P, d — P", "vadi": "Ma", "samvadi": "Sa", "description": "Traditionally the concluding raga of a concert, Bhairavi is deeply emotive and uses all flat notes."},
    {"slug": "bhupali", "name": "Bhupali", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Peaceful, devotional", "aroh": "S R G P D S'", "avroh": "S' D P G R S", "pakad": "G R S' D, S R G, P G, D P G, R S", "vadi": "Ga", "samvadi": "Dha", "description": "A pentatonic evening raga, Bhupali is serene and widely used in light classical and devotional music."},
    {"slug": "bihag", "name": "Bihag", "tradition": "Hindustani", "thaat": "Bilaval", "time": "7 to 10 PM", "mood": "Romantic, sweet", "aroh": ".N S G M P N S'", "avroh": "S' N D P M G R S", "pakad": ".N S, G M P, G M G, R S", "vadi": "Ga", "samvadi": "Ni", "description": "A romantic evening raga, Bihag is known for its sweet, delicate melodic phrases."},
    {"slug": "bihagra", "name": "Bihagra", "tradition": "Hindustani", "thaat": "Bilaval", "time": "10 PM to 1 AM", "mood": "Sweet, romantic", "aroh": ".N S G, G M P D n D P, N S'", "avroh": "S' N D, n D P, G M G R S", "pakad": "G M P D n D P, G M G R S", "vadi": "Ma", "samvadi": "Sa", "description": "A late-night raga combining elements of Bihag, sometimes also using tivra Madhyam."},
    {"slug": "bilaskhani-todi", "name": "Bilaskhani Todi", "tradition": "Hindustani", "thaat": "Bhairavi", "time": "10 AM to 1 PM", "mood": "Melancholic, deep", "aroh": "S r g, M g, P d, n d, S'", "avroh": "S' r' n d P, M g r g r S' .d S r g, M g, r g, r S", "pakad": "S r g, M g, r g, r S", "vadi": "Dha", "samvadi": "Ga", "description": "Said to have been created by Bilaskhani, son of Tansen, this raga is deeply melancholic and meditative."},
    {"slug": "bilaval", "name": "Bilaval", "tradition": "Hindustani", "thaat": "Bilaval", "time": "Morning", "mood": "Bright, auspicious", "aroh": "S R G M P D S'", "avroh": "S' N D P M G R S", "pakad": "G R G P, D N S' D", "vadi": "Ga", "samvadi": "Ni", "description": "The parent thaat raga of Bilaval, equivalent to the natural major scale, bright and auspicious."},
    {"slug": "chandrakauns", "name": "Chandrakauns", "tradition": "Hindustani", "thaat": "—", "time": "Midnight", "mood": "Mysterious, profound", "aroh": ".N S g M d N S'", "avroh": "S' N d M g M g S", "pakad": "g M N d M g M g .N S", "vadi": "Ma", "samvadi": "Sa", "description": "A midnight raga of deep mystery, Chandrakauns omits Re and Pa and uses komal Ga, Dha, and Ni."},
    {"slug": "chayanat", "name": "Chayanat", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Majestic, romantic", "aroh": "S, R G M P, D P, N D, S'", "avroh": "S' N D P, M' P D P, R G M P, G M R S", "pakad": "P — R, R G M P, M G M R, S", "vadi": "Re", "samvadi": "Pa", "description": "An evening raga of Kalyan thaat with a grand, romantic character."},
    {"slug": "des", "name": "Des", "tradition": "Hindustani", "thaat": "Khamaj", "time": "7 to 10 PM", "mood": "Romantic, light", "aroh": "S R M P N S'", "avroh": "S' n D P M G R G S", "pakad": "R M P, n D P, D M G R, G .N S", "vadi": "Pa", "samvadi": "Re", "description": "A popular evening raga widely used in semi-classical and film music, Des is warm and romantic."},
    {"slug": "deshkar", "name": "Deshkar", "tradition": "Hindustani", "thaat": "Bilaval", "time": "7 to 10 AM", "mood": "Bright, morning", "aroh": "S R G P D, S'", "avroh": "S' D P, G R S", "pakad": "D D P, G P D P, G R S", "vadi": "Dha", "samvadi": "Ga", "description": "A morning raga similar to Bhupali but from Bilaval thaat, Deshkar is bright and auspicious."},
    {"slug": "desi", "name": "Desi", "tradition": "Hindustani", "thaat": "Asavari", "time": "10 AM to 1 PM", "mood": "Folk, rustic", "aroh": "R g R S R .n S, R M P n S'", "avroh": "S' P -, D M P R g S R .n S", "pakad": "R g R S R .n S, R M P D M P g R g R S R .n S", "vadi": "Pa", "samvadi": "Re", "description": "A raga with a folk-like character, Desi evokes rustic simplicity and rural life."},
    {"slug": "dhanashri", "name": "Dhanashri", "tradition": "Hindustani", "thaat": "Kafi", "time": "1 to 4 PM", "mood": "Gentle, afternoon", "aroh": ".n S, g M P, n S'", "avroh": "S' n D P, M P g, M g R S", "pakad": ".n S, G M P, g, M g R S", "vadi": "Pa", "samvadi": "Sa", "description": "An afternoon raga of the Kafi thaat with a gentle, introspective quality."},
    {"slug": "durga", "name": "Durga", "tradition": "Hindustani", "thaat": "Bilaval", "time": "10 AM to 1 PM", "mood": "Powerful, bright", "aroh": "S R M P D S'", "avroh": "S' D P M R S", "pakad": "D M R, M P D M R, .D S", "vadi": "Ma", "samvadi": "Sa", "description": "A pentatonic raga named after the goddess Durga, bright and powerful in character."},
    {"slug": "gaur-malhar", "name": "Gaur Malhar", "tradition": "Hindustani", "thaat": "Kafi", "time": "1 to 4 PM", "mood": "Monsoon, joyful", "aroh": "R G R M, G R S, M R P M P, D S'", "avroh": "S' n D n P, D G P M, R G R M G R S", "pakad": "R G R M, G R S, P M, P D, S', D P M", "vadi": "Ma", "samvadi": "Sa", "description": "A monsoon raga combining Gaur and Malhar elements, evoking rain and joy."},
    {"slug": "gaur-sarang", "name": "Gaur Sarang", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 AM", "mood": "Bright, morning", "aroh": "S, G R, M' G, P M', D P, N D, S'", "avroh": "S' D N P, D M' P G, M R, P R, S", "pakad": "S, G R M G, P R S", "vadi": "Ga", "samvadi": "Dha", "description": "A morning raga combining Gaur and Sarang, with a bright, expansive quality."},
    {"slug": "gurjari-todi", "name": "Gurjari Todi", "tradition": "Hindustani", "thaat": "Todi", "time": "10 AM to 1 PM", "mood": "Melancholic, serious", "aroh": "S r g M' d N S'", "avroh": "S' n d M' g r, g r S", "pakad": ".d .n S r g, r S, M' g r g r S", "vadi": "Dha", "samvadi": "Re", "description": "A variant of Todi with a serious, melancholic mood."},
    {"slug": "hamir", "name": "Hamir", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Majestic, romantic", "aroh": "S R S, G M D, N D S'", "avroh": "S' N D P, M' P D P, G M R S", "pakad": "S R S, G M D", "vadi": "Dha", "samvadi": "Ga", "description": "A majestic evening raga of Kalyan thaat, Hamir has a grand and expansive character."},
    {"slug": "hansadhvani", "name": "Hansadhvani", "tradition": "Hindustani", "thaat": "Bilaval", "time": "7 to 10 PM", "mood": "Auspicious, bright", "aroh": "S G R, G P, N S'", "avroh": "S' N P, G P G R, S", "pakad": "S G R S, .N .P, G R, G P G R, S", "vadi": "Sa", "samvadi": "Pa", "description": "A pentatonic evening raga (omits Ma and Dha), Hansadhvani is auspicious and joyful."},
    {"slug": "hindol", "name": "Hindol", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 AM", "mood": "Majestic, spring", "aroh": "S G, M' D N D, S'", "avroh": "S', N D, M' G, S", "pakad": "S G, M' D N D, M' G S", "vadi": "Dha", "samvadi": "Ga", "description": "A pentatonic morning raga omitting Re and Pa, Hindol has a majestic, spring-like quality."},
    {"slug": "jai-jai-vanti", "name": "Jai Jai Vanti", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 AM to 1 PM", "mood": "Devotional, majestic", "aroh": "S, R g R S, .n .D .P, R, G M P, N S'", "avroh": "S' n D P, G M, R g R S", "pakad": "R g R S, .n .D .P, R, G M, R g R S", "vadi": "Re", "samvadi": "Pa", "description": "A raga of majestic character associated with devotional and classical compositions."},
    {"slug": "jaunpuri", "name": "Jaunpuri", "tradition": "Hindustani", "thaat": "Asavari", "time": "10 AM to 1 PM", "mood": "Serious, contemplative", "aroh": "S R M P d n S'", "avroh": "S' n d P, M g R S", "pakad": "R M P, n d P, d M P, g R S", "vadi": "Dha", "samvadi": "Ga", "description": "A morning raga similar to Asavari, Jaunpuri has a serious, contemplative quality."},
    {"slug": "jhinjhoti", "name": "Jhinjhoti", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 AM to 1 PM", "mood": "Light, romantic", "aroh": "S R G M P D n S'", "avroh": "S' n D P M G R S", "pakad": ".D S, R M, G, P M G R, S .n .D .P", "vadi": "Ga", "samvadi": "Ni", "description": "A light and romantic raga often used in thumri and semi-classical forms."},
    {"slug": "jogiya", "name": "Jogiya", "tradition": "Hindustani", "thaat": "Bhairav", "time": "Morning", "mood": "Austere, devotional", "aroh": "S r M P d S'", "avroh": "S' N d P M r S", "pakad": "M, r S, S r r M r S", "vadi": "Ma", "samvadi": "Sa", "description": "A pentatonic morning raga associated with the wandering yogi, austere and meditative."},
    {"slug": "kafi", "name": "Kafi", "tradition": "Hindustani", "thaat": "Kafi", "time": "1 to 3 PM", "mood": "Romantic, folk", "aroh": "S R g M P D n S'", "avroh": "S' n D P M g R S", "pakad": "S R R g g M M P", "vadi": "Pa", "samvadi": "Re", "description": "The parent thaat raga of Kafi, associated with the Holi season and semi-classical forms."},
    {"slug": "kalavati", "name": "Kalavati", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 PM to 1 AM", "mood": "Sweet, delicate", "aroh": "S G P D n S'", "avroh": "S' n D P G S", "pakad": "G P D n D P, G P G S", "vadi": "Pa", "samvadi": "Sa", "description": "A pentatonic night raga with a sweet, delicate character."},
    {"slug": "kamod", "name": "Kamod", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Joyful, romantic", "aroh": "S, R P, M' P D P, N D S'", "avroh": "S' N D P, M' P D P, G M P, G M, R S", "pakad": "R P, M' P D P, G M P, G M R S", "vadi": "Pa", "samvadi": "Sa", "description": "An evening raga of joy and romance from the Kalyan thaat."},
    {"slug": "kausi-kanhda", "name": "Kausi Kanhda", "tradition": "Hindustani", "thaat": "Asavari", "time": "10 PM to 1 AM", "mood": "Serious, late night", "aroh": "S R g M P D n S'", "avroh": "S' n D P M g R S", "pakad": "—", "vadi": "Ma", "samvadi": "Sa", "description": "A late-night raga with Bageshri ang, combining elements of Kanhra and Asavari."},
    {"slug": "kedar", "name": "Kedar", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Devotional, majestic", "aroh": "S M, M P, D P, N D S'", "avroh": "S' N D P, M' P D P M, P M R S", "pakad": "S M, M P, D P M, P M R S", "vadi": "Sa", "samvadi": "Ma", "description": "A devotional evening raga of Kalyan thaat, Kedar is associated with temples and worship."},
    {"slug": "khamaj", "name": "Khamaj", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 PM to 1 AM", "mood": "Romantic, playful", "aroh": "S G M P D N S'", "avroh": "S' n D P M G R S", "pakad": "G M P D n D, M P D, M G", "vadi": "Ga", "samvadi": "Ni", "description": "The parent thaat raga of Khamaj, romantic and playful, widely used in thumri."},
    {"slug": "lalit", "name": "Lalit", "tradition": "Hindustani", "thaat": "Marva", "time": "4 to 7 AM", "mood": "Serious, profound", "aroh": ".N r G M, M' M G, M' D S'", "avroh": "R' N D, M' D M' M G, R S", "pakad": ".N R G M, D M', M G, M' G R S", "vadi": "Ma", "samvadi": "Sa", "description": "A pre-dawn raga of deep seriousness, Lalit uses both Madhyams and omits Pa."},
    {"slug": "madhuvanti", "name": "Madhuvanti", "tradition": "Hindustani", "thaat": "Todi", "time": "4 to 7 PM", "mood": "Sweet, romantic", "aroh": ".N S g M' P N S'", "avroh": "S' N D P M' g R S", "pakad": ".N S G M' P, M' G R S", "vadi": "Pa", "samvadi": "Sa", "description": "An evening raga from the Todi thaat combining sweetness (madhu = honey) with longing."},
    {"slug": "madhyamad-sarang", "name": "Madhyamad Sarang", "tradition": "Hindustani", "thaat": "Kafi", "time": "7 to 10 AM", "mood": "Bright, morning", "aroh": ".n S R M P n S'", "avroh": "S' n P, M R S", "pakad": ".n S R, R M R P R, n P, M R S", "vadi": "Re", "samvadi": "Pa", "description": "A morning raga of the Sarang family with a bright, active character."},
    {"slug": "malgunji", "name": "Malgunji", "tradition": "Hindustani", "thaat": "Kafi", "time": "Night", "mood": "Romantic, complex", "aroh": ".D .N S R G M, G M, D N S'", "avroh": "S' N D P M G, M g R S", "pakad": "G M g R S, .D .n S R G M", "vadi": "Sa", "samvadi": "Ma", "description": "A complex night raga combining elements of Malhar and Bahar, rich and romantic."},
    {"slug": "mand", "name": "Mand", "tradition": "Hindustani", "thaat": "Bilaval", "time": "All time", "mood": "Folk, light", "aroh": "S G R M G, P M D P, N D S'", "avroh": "S' D N P, D M P G M S", "pakad": "S, R G, S, R, M M P, D, P D S'", "vadi": "Sa", "samvadi": "Pa", "description": "A folk-based raga of Rajasthan, Mand can be sung at any time and is very popular in light classical music."},
    {"slug": "maru-bihag", "name": "Maru Bihag", "tradition": "Hindustani", "thaat": "Kalyan", "time": "10 PM to 1 AM", "mood": "Romantic, sweet", "aroh": ".N S G M P N S'", "avroh": "S' N D P, M' G M' G R S", "pakad": "M' G, R S, R S, S M G P, M' G M' G R S", "vadi": "Ga", "samvadi": "Ni", "description": "A romantic late-night raga combining Maru and Bihag elements with tivra Madhyam."},
    {"slug": "marva", "name": "Marva", "tradition": "Hindustani", "thaat": "Marva", "time": "Evening (Sandhi Prakash)", "mood": "Serious, twilight", "aroh": ".N r G M' D N S'", "avroh": "S' N D M' G r S", "pakad": "D, M' G r, G M' G r S", "vadi": "Dha", "samvadi": "Re", "description": "A Sandhi Prakash raga sung at dusk, Marva omits Pa and has a serious, twilight character."},
    {"slug": "miya-ki-sarang", "name": "Miya Ki Sarang", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 AM to 1 PM", "mood": "Bright, energetic", "aroh": "S R M R, M P n D N S'", "avroh": "S' n D n P, M P, M R M R, S .N S", "pakad": "S R S, .n D .n P, .M .P .n .D .N S, R, M R, P M R .N S", "vadi": "Re", "samvadi": "Pa", "description": "A morning raga attributed to Mian Tansen, energetic and bright."},
    {"slug": "miya-malhar", "name": "Miya Malhar", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 PM to 1 AM", "mood": "Monsoon, majestic", "aroh": "R M R S, M R P, M P n D, N S'", "avroh": "S' n D, n M P, g M R S", "pakad": "R M R S .n .p, .M .P .n .D .N S, P g M R S", "vadi": "Ma", "samvadi": "Sa", "description": "Attributed to Tansen, Miya Malhar is the most majestic of monsoon ragas."},
    {"slug": "multani", "name": "Multani", "tradition": "Hindustani", "thaat": "Todi", "time": "1 to 4 PM", "mood": "Serious, afternoon", "aroh": ".N S g M' P N S'", "avroh": "S' N d P M' g r S", "pakad": ".N S, M' g, P g, r S", "vadi": "Pa", "samvadi": "Sa", "description": "An afternoon raga from the Todi thaat, Multani is serious and meditative."},
    {"slug": "nand-anandi", "name": "Nand – Anandi", "tradition": "Hindustani", "thaat": "Kalyan", "time": "10 PM to 1 AM", "mood": "Deep, late night", "aroh": "S G M, P D, N P S'", "avroh": "S' D, N P, D M' P, G M D P R S", "pakad": "G M D P, R S G M", "vadi": "Sa", "samvadi": "Pa", "description": "A late-night raga combining Nand and Anandi elements with a deep, contemplative quality."},
    {"slug": "pahadi", "name": "Pahadi", "tradition": "Hindustani", "thaat": "Bilaval", "time": "All time", "mood": "Folk, light", "aroh": "S R G P D S'", "avroh": "S' D P, G P, G R S", "pakad": "G, R S, .D, .P .D S", "vadi": "Sa", "samvadi": "Pa", "description": "A folk-inspired raga from the hills, Pahadi can be sung at any time and is very popular."},
    {"slug": "paraj", "name": "Paraj", "tradition": "Hindustani", "thaat": "Poorvi", "time": "4 to 7 AM", "mood": "Serious, pre-dawn", "aroh": ".N S G, M' d N S'", "avroh": "S' N d P, M' P d P, G M G, M' G r S", "pakad": "S', N d P, M' P d P, G M G", "vadi": "Sa'", "samvadi": "Pa", "description": "A pre-dawn raga of Poorvi thaat, serious and contemplative."},
    {"slug": "patdeep", "name": "Patdeep", "tradition": "Hindustani", "thaat": "Kafi", "time": "1 to 4 PM", "mood": "Gentle, afternoon", "aroh": "S g M P N S'", "avroh": "S' N D P M g R S", "pakad": "D P, g, M P N S'", "vadi": "Pa", "samvadi": "Sa", "description": "An afternoon raga with a gentle character; its Ni is slightly sharp."},
    {"slug": "piloo", "name": "Piloo (Pilu)", "tradition": "Hindustani", "thaat": "Kafi", "time": "1 to 4 PM", "mood": "Light, romantic", "aroh": ".N S G M P N S'", "avroh": "S' n D P n d P d P M g S .N S", "pakad": ".P .N S R g S, G M P g S, .N S", "vadi": "Ga", "samvadi": "Ni", "description": "A light raga that uses all 12 notes, Piloo is popular in thumri and dadra."},
    {"slug": "pooriya", "name": "Pooriya", "tradition": "Hindustani", "thaat": "Marva", "time": "Evening (Sandhi Prakash)", "mood": "Serious, twilight", "aroh": ".N r S, G, M' D, N r' S'", "avroh": "S' N D M' G r S", "pakad": "G, .N r S, .N .D .N .M' .D, r S", "vadi": "Ga", "samvadi": "Ma'", "description": "A Sandhi Prakash evening raga, serious and profound, without Pa."},
    {"slug": "pooriya-dhanashri", "name": "Pooriya Dhanashri", "tradition": "Hindustani", "thaat": "Poorvi", "time": "Evening (Sandhi Prakash)", "mood": "Serious, twilight", "aroh": ".N r G M' P, d P, N S'", "avroh": "S' N d P, M' G M' r G, r S", "pakad": ".N r G, M' P, d P, M' G, M' r G, r S", "vadi": "Pa", "samvadi": "Re", "description": "A Sandhi Prakash evening raga combining Pooriya and Dhanashri elements."},
    {"slug": "poorvi", "name": "Poorvi", "tradition": "Hindustani", "thaat": "Poorvi", "time": "Evening (Sandhi Prakash)", "mood": "Serious, twilight", "aroh": ".N r G, M' P, d N S'", "avroh": "S' N d P M', G M G, r S", "pakad": ".N, S r G, M G, M' G r S", "vadi": "Ga", "samvadi": "Ni", "description": "The parent thaat raga of Poorvi, a Sandhi Prakash raga of evening twilight."},
    {"slug": "rageshwari", "name": "Rageshwari", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 PM to 1 AM", "mood": "Romantic, serene", "aroh": "S G M D N S'", "avroh": "S' n D M G R S", "pakad": "G M D N S' n D M, G M R S, .D .n S G M", "vadi": "Ma", "samvadi": "Sa", "description": "A night raga of serene romanticism from the Khamaj thaat."},
    {"slug": "ramdasi-malhar", "name": "Ramdasi Malhar", "tradition": "Hindustani", "thaat": "Kafi", "time": "Rainy season", "mood": "Monsoon, majestic", "aroh": ".N S, R G M, n D n P N S'", "avroh": "S' n D n P, D P M, P g, M P g, M R S", "pakad": "R P M G M, n P g M R S", "vadi": "Ma", "samvadi": "Sa", "description": "A monsoon raga with complex, majestic phrases, associated with devotion."},
    {"slug": "ramkali", "name": "Ramkali", "tradition": "Hindustani", "thaat": "Bhairav", "time": "Morning", "mood": "Devotional, solemn", "aroh": "S r G M P d N S'", "avroh": "S' N d P, M' P d n d P, G M r S", "pakad": "d P, M' P d n d P, G M', r P M G r S", "vadi": "Pa", "samvadi": "Sa", "description": "A morning raga of Bhairav thaat with a devotional, solemn quality."},
    {"slug": "rasranjani", "name": "Rasranjani", "tradition": "Hindustani", "thaat": "Bilaval", "time": "Midnight", "mood": "Romantic, midnight", "aroh": "S R M D N S'", "avroh": "S' N D M, D M R S", "pakad": "—", "vadi": "Ma", "samvadi": "Sa", "description": "A midnight raga of romantic character from the Bilaval thaat."},
    {"slug": "saraswati", "name": "Saraswati", "tradition": "Hindustani", "thaat": "Khamaj", "time": "Midnight", "mood": "Serene, midnight", "aroh": "S R M' P, n D P, n D S'", "avroh": "R' n D P M' R M P, M' R S", "pakad": "—", "vadi": "Pa", "samvadi": "Re", "description": "A midnight raga named after the goddess of music, serene and contemplative."},
    {"slug": "shankara", "name": "Shankara", "tradition": "Hindustani", "thaat": "Bilaval", "time": "10 PM to 1 AM", "mood": "Devotional, majestic", "aroh": "S G P N S'", "avroh": "S' N P, N D S' N P, G P G S", "pakad": "S' N P, N D S' N P, G P G S", "vadi": "Ga", "samvadi": "Ni", "description": "A pentatonic night raga dedicated to Lord Shiva, devotional and majestic."},
    {"slug": "shivranjani", "name": "Shivranjani", "tradition": "Hindustani", "thaat": "Kafi", "time": "Midnight", "mood": "Devotional, sweet", "aroh": "S R g P D S'", "avroh": "S' D P g R S", "pakad": "—", "vadi": "Pa", "samvadi": "Sa", "description": "A pentatonic raga dedicated to Lord Shiva, sweet and devotional."},
    {"slug": "shri", "name": "Shri", "tradition": "Hindustani", "thaat": "Poorvi", "time": "Evening (Sandhi Prakash)", "mood": "Serious, twilight", "aroh": "S r r S, r M' P N S'", "avroh": "S' N d P, M' P d M' G r, P r G r S", "pakad": "S r r S, r M' P, d M' G r G r S", "vadi": "Re", "samvadi": "Pa", "description": "A Sandhi Prakash evening raga, serious and profound, associated with twilight devotion."},
    {"slug": "shuddh-kalyan", "name": "Shuddh Kalyan", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Serene, evening", "aroh": "S R G P D S'", "avroh": "S' N D, N D P, M' G R, G R P R G R S", "pakad": "G R S, .N .D .N .D .P, S, G R, P R, G R S", "vadi": "Ga", "samvadi": "Dha", "description": "An evening raga of Kalyan thaat without the sharp Madhyam, serene and bright."},
    {"slug": "shuddh-sarang", "name": "Shuddh Sarang", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 AM to 1 PM", "mood": "Bright, energetic", "aroh": "S R M P, M' P N S'", "avroh": "S' N D P M' G R S", "pakad": "—", "vadi": "Re", "samvadi": "Pa", "description": "A morning raga of the Sarang family, bright and energetic."},
    {"slug": "shyam-kalyan", "name": "Shyam Kalyan", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Romantic, evening", "aroh": ".N S R M' P N S'", "avroh": "S' N D P M' P G M R .N S", "pakad": ".N S R M' P, G M R .N S", "vadi": "Pa", "samvadi": "Sa", "description": "An evening raga combining Shyam and Kalyan elements, romantic and sweet."},
    {"slug": "sindhu-bhairavi", "name": "Sindhu Bhairavi", "tradition": "Hindustani", "thaat": "Asavari", "time": "10 AM to 1 PM", "mood": "Tender, semi-classical", "aroh": "S R g M P d n S'", "avroh": "S' n d P M g R S", "pakad": "—", "vadi": "Ma", "samvadi": "Sa", "description": "A light, semi-classical raga widely used in thumri and ghazal."},
    {"slug": "sohni", "name": "Sohni", "tradition": "Hindustani", "thaat": "Marva", "time": "4 to 7 AM", "mood": "Romantic, pre-dawn", "aroh": "S G M' D N S'", "avroh": "S' r' S' N D, G M' D, G M' G, M' G r S", "pakad": "S' N D, G M' D N S' r' S'", "vadi": "Dha", "samvadi": "Ga", "description": "A pre-dawn Marva raga of romantic, longing character."},
    {"slug": "sughrai", "name": "Sughrai", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 AM to 1 PM", "mood": "Bright, morning", "aroh": ".n S R g, M P, N S'", "avroh": "S' D, N P, M P, g, M R S", "pakad": ".n S R g, M P n P, D P, M P g M R S", "vadi": "Pa", "samvadi": "Sa", "description": "A morning raga of Kafi thaat with a bright, active character."},
    {"slug": "tilak-kamod", "name": "Tilak Kamod", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 PM to 1 AM", "mood": "Romantic, sweet", "aroh": "S R G S, R M P D, M P, S'", "avroh": "S' P D M G, S R G, S .N", "pakad": ".P .N S R G, S, R P M G, S .N", "vadi": "Re", "samvadi": "Pa", "description": "A romantic night raga combining Tilang and Kamod elements."},
    {"slug": "tilang", "name": "Tilang", "tradition": "Hindustani", "thaat": "Khamaj", "time": "10 PM to 1 AM", "mood": "Romantic, light", "aroh": "S G M P N S'", "avroh": "S' n P M G S", "pakad": ".N S G M P, N S', S' n P, G M G S", "vadi": "Ga", "samvadi": "Ni", "description": "A pentatonic night raga, romantic and light, popular in thumri."},
    {"slug": "hindustani-todi", "name": "Todi (Hindustani)", "tradition": "Hindustani", "thaat": "Todi", "time": "10 AM to 1 PM", "mood": "Melancholic, serious", "aroh": "S r g M' P d N S'", "avroh": "S' N d P M' g r S", "pakad": ".d N S, r, g r, s, M' g r g r S", "vadi": "Dha", "samvadi": "Ga", "description": "The Hindustani Todi, one of the grandest morning ragas, deeply melancholic and meditative."},
    {"slug": "vibhas", "name": "Vibhas", "tradition": "Hindustani", "thaat": "Bhairav", "time": "Morning", "mood": "Austere, morning", "aroh": "S r G P d P S'", "avroh": "S' d P G P d P, G r S", "pakad": "d, P, G P, G r S", "vadi": "Dha", "samvadi": "Ga", "description": "A pentatonic morning raga of Bhairav thaat, austere and meditative."},
    {"slug": "vrindavani-sarang", "name": "Vrindavani Sarang", "tradition": "Hindustani", "thaat": "Kafi", "time": "10 AM to 1 PM", "mood": "Bright, devotional", "aroh": "S R M P N S'", "avroh": "S' n P M R S", "pakad": ".N S R, M R, P M R, S", "vadi": "Pa", "samvadi": "Re", "description": "A morning raga associated with the forests of Vrindavan, bright and devotional."},
    {"slug": "yaman-kalyan", "name": "Yaman Kalyan", "tradition": "Hindustani", "thaat": "Kalyan", "time": "7 to 10 PM", "mood": "Romantic, serene", "aroh": "S R G M' P D N S'", "avroh": "S' N D P M' G R S", "pakad": ".N R G, R S, P M' G R S", "vadi": "Ga", "samvadi": "Ni", "description": "A combination of Yaman and Kalyan, this is one of the most popular evening ragas."},
    {"slug": "yamani-bilaval", "name": "Yamani Bilaval", "tradition": "Hindustani", "thaat": "Bilaval", "time": "Morning", "mood": "Bright, morning", "aroh": ".N R G, M R G P, M' P, D N S'", "avroh": "S' N D P, M' P M G, R G R S", "pakad": ".N R G, M' P M G, R G R S", "vadi": "Pa", "samvadi": "Sa", "description": "A morning raga combining elements of Yaman and Bilaval."},
    {"slug": "hemant", "name": "Hemant", "tradition": "Hindustani", "thaat": "Bilaval", "time": "9 PM to 12 midnight", "mood": "Romantic, winter", "aroh": "S G M D N S'", "avroh": "S' N D P M G R S", "pakad": "G M D N D, M P M, N D P M, G M G R S", "vadi": "Ma", "samvadi": "Sa", "description": "A night raga associated with winter (hemant = early winter), romantic and serene."},
    {"slug": "kirwani", "name": "Kirwani", "tradition": "Hindustani", "thaat": "—", "time": "Midnight", "mood": "Romantic, night", "aroh": "S R g M P d N S'", "avroh": "S' N d P M g R S", "pakad": "d P g R S R, R g M P d P", "vadi": "—", "samvadi": "—", "description": "A night raga with both sharp and flat notes, popular in sitar and semi-classical styles."},
    {"slug": "jog", "name": "Jog", "tradition": "Hindustani", "thaat": "Kafi", "time": "9 PM to 12 midnight", "mood": "Romantic, night", "aroh": "S G M P n S'", "avroh": "S' n P M G M g S", "pakad": "G M P n P, P n P M G M g S", "vadi": "Ma", "samvadi": "Sa", "description": "A night raga of romantic character, Jog is popular in both classical and light classical music."},
]

BANDISHES = [
    {"slug": "piya-bawari", "title": "Piya Bawari", "raga": "Yaman", "taal": "Teentaal", "composer": "Traditional", "language": "Braj", "difficulty": "Intermediate", "lyrics": "Piya bawari saari raina jaagi…", "translation": "My beloved, I have stayed awake the whole night…", "youtube": "https://www.youtube.com/results?search_query=Piya+Bawari+Yaman+bandish", "spotify": "https://open.spotify.com/search/Piya%20Bawari"},
    {"slug": "jago-mohan-pyare", "title": "Jago Mohan Pyare", "raga": "Bhairav", "taal": "Ektaal", "composer": "Surdas", "language": "Braj", "difficulty": "Beginner", "lyrics": "Jago Mohan pyare, saanjh bhayi…", "translation": "Awake, beloved Mohan, the evening has come…", "youtube": "https://www.youtube.com/results?search_query=Jago+Mohan+Pyare+Bhairav", "spotify": "https://open.spotify.com/search/Jago%20Mohan%20Pyare"},
    {"slug": "rangi-saari", "title": "Rangi Saari", "raga": "Bhimpalasi", "taal": "Teentaal", "composer": "Amir Khusrau", "language": "Hindavi", "difficulty": "Intermediate", "lyrics": "Rangi saari gulabi chunariya re…", "translation": "My pink veil is stained with color…", "youtube": "https://www.youtube.com/results?search_query=Rangi+Saari+Bhimpalasi", "spotify": "https://open.spotify.com/search/Rangi%20Saari"},
    {"slug": "jagadodharana", "title": "Jagadodharana", "raga": "Kapi", "taal": "Adi", "composer": "Purandara Dasa", "language": "Kannada", "difficulty": "Advanced", "lyrics": "Jagadodharana aadisidaḷe Yashode…", "translation": "Yashoda played with the savior of the world…", "youtube": "https://www.youtube.com/results?search_query=Jagadodharana+Purandara+Dasa", "spotify": "https://open.spotify.com/search/Jagadodharana"},
    {"slug": "vatapi-ganapatim", "title": "Vatapi Ganapatim", "raga": "Hamsadhwani", "taal": "Adi", "composer": "Muthuswami Dikshitar", "language": "Sanskrit", "difficulty": "Advanced", "lyrics": "Vātāpi Gaṇapatim bhajeham…", "translation": "I worship Ganapati of Vatapi…", "youtube": "https://www.youtube.com/results?search_query=Vatapi+Ganapatim+Dikshitar", "spotify": "https://open.spotify.com/search/Vatapi%20Ganapatim"},
    {"slug": "endaro-mahanubhavulu", "title": "Endaro Mahanubhavulu", "raga": "Sri", "taal": "Adi", "composer": "Tyagaraja", "language": "Telugu", "difficulty": "Advanced", "lyrics": "Endarō mahānubhāvulu andarikī vandanamulu…", "translation": "There are many great souls, salutations to them all…", "youtube": "https://www.youtube.com/results?search_query=Endaro+Mahanubhavulu+Tyagaraja", "spotify": "https://open.spotify.com/search/Endaro%20Mahanubhavulu"},
]

TAALS = [
    # ── 6-beat ──
    {"slug": "dadra", "name": "Dadra", "beats": 6, "structure": "3+3", "claps": "X 0", "bols": "Dha Dhin Na | Dha Tin Na", "tradition": "Hindustani", "context": "Light classical (Ghazal, Thumri, Bhajan)", "youtube": "https://www.youtube.com/results?search_query=Dadra+taal+theka", "spotify": "https://open.spotify.com/search/Dadra%20taal"},
    # ── 7-beat ──
    {"slug": "rupak", "name": "Rupak", "beats": 7, "structure": "3+2+2", "claps": "0 1 2", "bols": "Tin Tin Na | Dhin Na | Dhin Na", "tradition": "Hindustani", "context": "Classical & Light classical (unique Khali start)", "youtube": "https://www.youtube.com/results?search_query=Rupak+taal+theka", "spotify": "https://open.spotify.com/search/Rupak%20taal"},
    {"slug": "teevra", "name": "Teevra", "beats": 7, "structure": "3+2+2", "claps": "X 2 3", "bols": "Dha Din Ta | Tite Kata Gadi Gana", "tradition": "Hindustani", "context": "Fast, powerful Pakhawaj rhythm", "youtube": "https://www.youtube.com/results?search_query=Teevra+taal+pakhawaj", "spotify": "https://open.spotify.com/search/Teevra%20taal"},
    # ── 8-beat ──
    {"slug": "keharwa", "name": "Keharwa", "beats": 8, "structure": "4+4", "claps": "X 0", "bols": "Dha Ge Na Tin | Na Ka Dhin Na", "tradition": "Hindustani", "context": "Folk, Bollywood, semi-classical", "youtube": "https://www.youtube.com/results?search_query=Keharwa+taal+theka", "spotify": "https://open.spotify.com/search/Keharwa%20taal"},
    {"slug": "bhajani", "name": "Bhajani", "beats": 8, "structure": "4+4", "claps": "X 0", "bols": "Dha Ge Na Tin | Na Ge Din Na (variation)", "tradition": "Hindustani", "context": "Devotional music (Bhajans)", "youtube": "https://www.youtube.com/results?search_query=Bhajani+taal+tabla", "spotify": "https://open.spotify.com/search/Bhajani%20taal"},
    {"slug": "adi-tala", "name": "Adi Tala", "beats": 8, "structure": "4+2+2", "claps": "Laghu Drutam Drutam", "bols": "Ta Ka Dhi Mi | Ta Ka | Jho Nu", "tradition": "Carnatic", "context": "Foundation of Carnatic music — kritis and varnas", "youtube": "https://www.youtube.com/results?search_query=Adi+Tala+mridangam", "spotify": "https://open.spotify.com/search/Adi%20Tala"},
    # ── 10-beat ──
    {"slug": "jhaptal", "name": "Jhaptal", "beats": 10, "structure": "2+3+2+3", "claps": "X 2 0 3", "bols": "Dhi Na | Dhi Dhi Na | Ti Na | Dhi Dhi Na", "tradition": "Hindustani", "context": "Structured, peaceful classical Khayal", "youtube": "https://www.youtube.com/results?search_query=Jhaptal+theka", "spotify": "https://open.spotify.com/search/Jhaptal"},
    {"slug": "sultaal", "name": "Sultaal", "beats": 10, "structure": "2+2+2+2+2", "claps": "X 2 3 4 5", "bols": "Dha Dha Din Ta | Kita Dha Din Ta | Tita Kata", "tradition": "Hindustani", "context": "Fast, powerful Dhrupad (Pakhawaj)", "youtube": "https://www.youtube.com/results?search_query=Sultaal+pakhawaj+theka", "spotify": "https://open.spotify.com/search/Sultaal"},
    # ── 12-beat ──
    {"slug": "ektaal", "name": "Ektaal", "beats": 12, "structure": "2+2+2+2+2+2", "claps": "X 0 2 0 3 4", "bols": "Dhin Dhin | Dha Ge | Tirakita | Tu Na | Kat Ta | Dha Ge", "tradition": "Hindustani", "context": "Classical vocal — Vilambit to Drut Khayal", "youtube": "https://www.youtube.com/results?search_query=Ektaal+theka", "spotify": "https://open.spotify.com/search/Ektaal"},
    {"slug": "chautaal", "name": "Chautaal", "beats": 12, "structure": "2+2+2+2+2+2", "claps": "X 2 0 3 0 4", "bols": "Dha Dha Din Ta | Kita Dha Din Ta | Tita Kata Ga Di Na", "tradition": "Hindustani", "context": "Standard classical Dhrupad cycle", "youtube": "https://www.youtube.com/results?search_query=Chautaal+pakhawaj+theka", "spotify": "https://open.spotify.com/search/Chautaal"},
    {"slug": "rupaka-tala", "name": "Rupaka Tala", "beats": 6, "structure": "2+4", "claps": "Drutam Laghu", "bols": "Ta Ki | Ta Ka Dhi Mi", "tradition": "Carnatic", "context": "Classical Carnatic compositions", "youtube": "https://www.youtube.com/results?search_query=Rupaka+Tala", "spotify": "https://open.spotify.com/search/Rupaka%20Tala"},
    # ── 14-beat ──
    {"slug": "adachautaal", "name": "Adachautaal", "beats": 14, "structure": "2+2+2+2+2+2+2", "claps": "X 2 0 3 0 4 0", "bols": "Dhin Tirakita Dhi Na | Tu Na Kat Ta | Dhin Dhin Ta | Tita Kata Ga Di Na", "tradition": "Hindustani", "context": "Complex, traditional vocal cycle", "youtube": "https://www.youtube.com/results?search_query=Adachautaal+theka", "spotify": "https://open.spotify.com/search/Adachautaal"},
    {"slug": "jhumra", "name": "Jhumra", "beats": 14, "structure": "3+4+3+4", "claps": "X 2 0 3", "bols": "Dhin - Dha Tirakita | Dhin Dhin Dhage Tirakita | Tu - Na Kata | Dhin Dhin Dhage Tirakita", "tradition": "Hindustani", "context": "Rare, graceful, very slow Vilambit Khayal", "youtube": "https://www.youtube.com/results?search_query=Jhumra+taal+theka", "spotify": "https://open.spotify.com/search/Jhumra%20taal"},
    {"slug": "dhamar", "name": "Dhamar", "beats": 14, "structure": "5+2+3+4", "claps": "X 2 0 3", "bols": "Ka Dhi Ta Dhi Ta | Dha - | Ga Di Na | Dhi Na Dha", "tradition": "Hindustani", "context": "Dhrupad-style Holi festival songs", "youtube": "https://www.youtube.com/results?search_query=Dhamar+taal+theka", "spotify": "https://open.spotify.com/search/Dhamar%20taal"},
    # ── 16-beat ──
    {"slug": "teentaal", "name": "Teentaal", "beats": 16, "structure": "4+4+4+4", "claps": "X 2 0 3", "bols": "Dha Dhin Dhin Dha | Dha Dhin Dhin Dha | Dha Tin Tin Ta | Ta Dhin Dhin Dha", "tradition": "Hindustani", "context": "Universal standard — the king of rhythms", "youtube": "https://www.youtube.com/results?search_query=Teentaal+theka+tabla", "spotify": "https://open.spotify.com/search/Teentaal"},
    {"slug": "tilwada", "name": "Tilwada", "beats": 16, "structure": "4+4+4+4", "claps": "X 2 0 3", "bols": "Dha Tirakita Dhin Dhin | Dha Dha Tin Tin | Ta Tirakita Dhin Dhin | Dha Dha Dhin Dhin", "tradition": "Hindustani", "context": "Slow-tempo variation of Teentaal", "youtube": "https://www.youtube.com/results?search_query=Tilwada+taal+theka", "spotify": "https://open.spotify.com/search/Tilwada%20taal"},
    # ── 18-beat ──
    {"slug": "matta", "name": "Matta", "beats": 18, "structure": "9+9", "claps": "X 2", "bols": "Highly intricate — customized variations per gharana", "tradition": "Hindustani", "context": "Rare, mathematically challenging cycle", "youtube": "https://www.youtube.com/results?search_query=Matta+taal+tabla", "spotify": "https://open.spotify.com/search/Matta%20taal"},
]

ARTISTS = [
    {"slug": "bhimsen-joshi", "name": "Pt. Bhimsen Joshi", "gharana": "Kirana", "instruments": ["Vocal"], "era": "1922–2011", "bio": "Bharat Ratna recipient, towering Hindustani vocalist of the Kirana gharana known for his powerful voice and Khayal renditions.", "youtube": "https://www.youtube.com/results?search_query=Bhimsen+Joshi", "spotify": "https://open.spotify.com/search/Bhimsen%20Joshi"},
    {"slug": "kishori-amonkar", "name": "Kishori Amonkar", "gharana": "Jaipur-Atrauli", "instruments": ["Vocal"], "era": "1932–2017", "bio": "One of the foremost vocalists of her generation, celebrated for her introspective and emotive approach to Khayal.", "youtube": "https://www.youtube.com/results?search_query=Kishori+Amonkar", "spotify": "https://open.spotify.com/search/Kishori%20Amonkar"},
    {"slug": "ravi-shankar", "name": "Pt. Ravi Shankar", "gharana": "Maihar", "instruments": ["Sitar"], "era": "1920–2012", "bio": "The global ambassador of Indian classical music whose sitar brought Hindustani tradition to world audiences.", "youtube": "https://www.youtube.com/results?search_query=Ravi+Shankar+sitar", "spotify": "https://open.spotify.com/search/Ravi%20Shankar"},
    {"slug": "zakir-hussain", "name": "Ustad Zakir Hussain", "gharana": "Punjab", "instruments": ["Tabla"], "era": "1951–present", "bio": "Tabla virtuoso and composer who has redefined percussion in classical and fusion contexts.", "youtube": "https://www.youtube.com/results?search_query=Zakir+Hussain+tabla", "spotify": "https://open.spotify.com/search/Zakir%20Hussain"},
    {"slug": "ms-subbulakshmi", "name": "M. S. Subbulakshmi", "gharana": "—", "instruments": ["Vocal"], "era": "1916–2004", "bio": "Bharat Ratna laureate and the first musician to receive the Ramon Magsaysay Award. Carnatic vocalist of unparalleled stature.", "youtube": "https://www.youtube.com/results?search_query=MS+Subbulakshmi", "spotify": "https://open.spotify.com/search/MS%20Subbulakshmi"},
    {"slug": "balamuralikrishna", "name": "M. Balamuralikrishna", "gharana": "—", "instruments": ["Vocal", "Viola"], "era": "1930–2016", "bio": "Carnatic vocalist, composer, and multi-instrumentalist who created new ragas and talas.", "youtube": "https://www.youtube.com/results?search_query=Balamuralikrishna", "spotify": "https://open.spotify.com/search/Balamuralikrishna"},
]

GURUS = [
    {"slug": "guruji-anand", "name": "Pt. Anand Kulkarni", "specialty": "Khayal — Gwalior", "experience": "30+ years", "mode": "Online & in-person (Pune)", "rating": 4.9, "students": 240, "bio": "Disciple of the late Pt. Ulhas Kashalkar. Teaches foundations through advanced bandish elaboration.", "youtube": "https://www.youtube.com/results?search_query=Anand+Kulkarni+Khayal", "spotify": ""},
    {"slug": "guruji-savitha", "name": "Smt. Savitha Iyer", "specialty": "Carnatic Vocal", "experience": "22 years", "mode": "Online (Chennai)", "rating": 4.8, "students": 180, "bio": "Trained under Shri T. R. Subramanyam. Focuses on manodharma and kriti interpretation.", "youtube": "https://www.youtube.com/results?search_query=Savitha+Iyer+Carnatic", "spotify": ""},
    {"slug": "guruji-rohan", "name": "Rohan Deshpande", "specialty": "Tabla — Punjab Gharana", "experience": "15 years", "mode": "Online", "rating": 4.9, "students": 320, "bio": "Performer and educator. Specializes in laykari and accompaniment.", "youtube": "https://www.youtube.com/results?search_query=Rohan+Deshpande+tabla", "spotify": ""},
    {"slug": "guruji-meera", "name": "Meera Subramaniam", "specialty": "Veena", "experience": "25 years", "mode": "In-person (Bengaluru)", "rating": 5.0, "students": 90, "bio": "Awarded artist of All India Radio. Teaches Saraswati Veena in the traditional gurukul style.", "youtube": "https://www.youtube.com/results?search_query=Meera+Subramaniam+veena", "spotify": ""},
]

CONCERTS = [
    {"slug": "monsoon-malhar-mumbai", "title": "Monsoon Malhar Festival", "date": "Aug 14, 2026", "city": "Mumbai", "venue": "NCPA, Tata Theatre", "artist": "Pt. Anand Kulkarni & ensemble", "type": "Festival", "livestream": True, "youtube": "https://www.youtube.com/results?search_query=Monsoon+Malhar+Festival+Mumbai", "spotify": ""},
    {"slug": "tyagaraja-aradhana-2026", "title": "Tyagaraja Aradhana", "date": "Jan 22, 2026", "city": "Thiruvaiyaru", "venue": "Tyagaraja Samadhi", "artist": "Pancharatna Goshti", "type": "Tradition", "livestream": True, "youtube": "https://www.youtube.com/results?search_query=Tyagaraja+Aradhana+Thiruvaiyaru", "spotify": ""},
    {"slug": "saptak-2027", "title": "Saptak Annual Festival", "date": "Jan 1–13, 2027", "city": "Ahmedabad", "venue": "Saptak Archives", "artist": "Various", "type": "Festival", "livestream": False, "youtube": "https://www.youtube.com/results?search_query=Saptak+Annual+Festival", "spotify": ""},
    {"slug": "sawai-gandharva", "title": "Sawai Gandharva Bhimsen Festival", "date": "Dec 9–13, 2026", "city": "Pune", "venue": "Mukundnagar Grounds", "artist": "Various", "type": "Festival", "livestream": True, "youtube": "https://www.youtube.com/results?search_query=Sawai+Gandharva+Festival+Pune", "spotify": ""},
]

COURSES = [
    {"slug": "foundations", "title": "Foundations of Indian Classical", "level": "Beginner", "lessons": 24, "duration": "8 weeks", "description": "Sa to Sa: notes, sargams, basic taal, your first raga.", "youtube": "https://www.youtube.com/results?search_query=Foundations+Indian+Classical+music", "spotify": ""},
    {"slug": "raga-shastra", "title": "Raga Shastra: Structure & Theory", "level": "Intermediate", "lessons": 36, "duration": "12 weeks", "description": "Thaat, Melakarta, vadi-samvadi, time theory, and chalan.", "youtube": "https://www.youtube.com/results?search_query=Raga+Shastra+theory", "spotify": ""},
    {"slug": "khayal-craft", "title": "The Craft of Khayal", "level": "Advanced", "lessons": 48, "duration": "16 weeks", "description": "Vilambit & drut bandish, alap, bol-banao, taan, and improvisation.", "youtube": "https://www.youtube.com/results?search_query=Khayal+craft+improvisation", "spotify": ""},
    {"slug": "tabla-laykari", "title": "Tabla Laykari Workshop", "level": "Intermediate", "lessons": 20, "duration": "6 weeks", "description": "Tihai, chakradar, and rhythmic composition.", "youtube": "https://www.youtube.com/results?search_query=Tabla+Laykari+workshop", "spotify": ""},
]

FORUM_THREADS = [
    {"slug": "samay-relevance", "title": "Does samay (time) theory still hold meaning in recordings?", "author": "Aarav Mehta", "replies": 42, "tag": "Theory", "body": "Time theory has long prescribed ragas for particular hours. With the global reach of recordings, do these conventions still serve listeners, or are they a teaching device? Practitioners and students weigh in.", "youtube": "", "spotify": ""},
    {"slug": "best-tanpura-app", "title": "Best digital tanpura for daily riyaaz?", "author": "Priya Iyer", "replies": 27, "tag": "Practice", "body": "From iTabla Pro to SwarMala — share the digital tanpura apps that survive your daily riyaaz, and the ones that drift in pitch after twenty minutes.", "youtube": "", "spotify": ""},
    {"slug": "gharana-vs-style", "title": "Gharana vs. personal style — where is the line?", "author": "Devansh Rao", "replies": 64, "tag": "Discussion", "body": "How much of a performing artist's identity is inherited from their gharana, and how much is personal voice? A long thread on the boundaries between lineage and invention.", "youtube": "", "spotify": ""},
    {"slug": "carnatic-for-hindustani-learners", "title": "A Hindustani student's guide to listening to Carnatic", "author": "Meera S.", "replies": 19, "tag": "Learning", "body": "A friendly, beginner-friendly map of where to begin: kriti structure, the concept of sangati, and a starter playlist of foundational composers.", "youtube": "", "spotify": "https://open.spotify.com/search/Carnatic%20vocal%20beginners"},
]

ARCHIVES = [
    {"slug": "all-india-radio-1955", "title": "All India Radio Sangeet Sammelan, 1955", "type": "Recording", "year": 1955, "description": "Rare reel-to-reel recordings featuring Ustad Bade Ghulam Ali Khan.", "youtube": "https://www.youtube.com/results?search_query=Bade+Ghulam+Ali+Khan+AIR+1955", "spotify": "https://open.spotify.com/search/Bade%20Ghulam%20Ali%20Khan"},
    {"slug": "tansen-manuscript", "title": "Manuscript fragments attributed to Mian Tansen", "type": "Manuscript", "year": 1580, "description": "Devanagari notations of dhrupad bandishes, conserved at Gwalior.", "youtube": "https://www.youtube.com/results?search_query=Mian+Tansen+dhrupad", "spotify": "https://open.spotify.com/search/Mian%20Tansen"},
    {"slug": "subbulakshmi-un-1966", "title": "M. S. Subbulakshmi at the UN, 1966", "type": "Concert", "year": 1966, "description": "Historic concert at the United Nations General Assembly.", "youtube": "https://www.youtube.com/results?search_query=MS+Subbulakshmi+UN+1966", "spotify": "https://open.spotify.com/search/MS%20Subbulakshmi"},
    {"slug": "kumar-gandharva-interview", "title": "Kumar Gandharva — 1982 interview", "type": "Interview", "year": 1982, "description": "Hour-long conversation on Nirgun bhakti and folk influences.", "youtube": "https://www.youtube.com/results?search_query=Kumar+Gandharva+interview+1982", "spotify": "https://open.spotify.com/search/Kumar%20Gandharva"},
]

MODULES = [
    {"slug": "ragas", "title": "Ragaverse", "tagline": "The complete raga atlas", "count": len(RAGAS), "suffix": "ragas"},
    {"slug": "bandishes", "title": "Bandishverse", "tagline": "Compositions across traditions", "count": len(BANDISHES), "suffix": "bandishes"},
    {"slug": "taals", "title": "Taalverse", "tagline": "Rhythm cycles, visualised", "count": len(TAALS), "suffix": "taals"},
    {"slug": "artists", "title": "Artistverse", "tagline": "Maestros across generations", "count": len(ARTISTS), "suffix": "artists"},
    {"slug": "gurus", "title": "Guruverse", "tagline": "Teachers and the gurukul tradition", "count": len(GURUS), "suffix": "gurus"},
    {"slug": "concerts", "title": "Concertverse", "tagline": "Live and streamed performances", "count": len(CONCERTS), "suffix": "events"},
    {"slug": "learn", "title": "Learnverse", "tagline": "Structured learning paths", "count": len(COURSES), "suffix": "courses"},
    {"slug": "community", "title": "Communityverse", "tagline": "Forums, threads, and people", "count": len(FORUM_THREADS), "suffix": "threads"},
    {"slug": "archive", "title": "Archiveverse", "tagline": "Preserving rare and historic works", "count": len(ARCHIVES), "suffix": "items"},
    {"slug": "knowledge", "title": "Knowledgeverse", "tagline": "The graph of how it all connects", "count": 1, "suffix": "entities"},
]

DATASETS = {
    "ragas": RAGAS, "bandishes": BANDISHES, "taals": TAALS, "artists": ARTISTS,
    "gurus": GURUS, "concerts": CONCERTS, "courses": COURSES,
    "forum_threads": FORUM_THREADS, "archives": ARCHIVES, "modules": MODULES,
}

# Knowledgeverse — free-form articles contributed by users (after admin approval).
KNOWLEDGE = [
    {
        "slug": "what-is-a-raga",
        "title": "What is a raga?",
        "body": (
            "A raga is more than a scale — it is a melodic framework with rules for "
            "ascending (aroh), descending (avroh), dominant note (vadi), and characteristic "
            "phrases (pakad). Each raga is tied to a time of day and a mood."
        ),
        "tags": ["theory", "beginner"],
    },
]


# ---- Mutators used by the submission/approval pipeline ----

def _dedupe_by_slug(items: list[dict], payload: dict) -> None:
    """Remove any existing entry with the same slug before inserting."""
    slug = payload.get("slug")
    if not slug:
        return
    for i in range(len(items) - 1, -1, -1):
        if items[i].get("slug") == slug:
            items.pop(i)


def add_raga(payload: dict) -> dict:
    _dedupe_by_slug(RAGAS, payload)
    RAGAS.append(payload)
    MODULES[0]["count"] = len(RAGAS)
    return payload


def add_taal(payload: dict) -> dict:
    _dedupe_by_slug(TAALS, payload)
    TAALS.append(payload)
    MODULES[2]["count"] = len(TAALS)
    return payload


def add_knowledge(payload: dict) -> dict:
    _dedupe_by_slug(KNOWLEDGE, payload)
    KNOWLEDGE.append(payload)
    MODULES[9]["count"] = len(KNOWLEDGE)
    return payload


def add_bandish(payload: dict) -> dict:
    _dedupe_by_slug(BANDISHES, payload)
    BANDISHES.append(payload)
    MODULES[1]["count"] = len(BANDISHES)
    return payload


def add_artist(payload: dict) -> dict:
    _dedupe_by_slug(ARTISTS, payload)
    ARTISTS.append(payload)
    MODULES[3]["count"] = len(ARTISTS)
    return payload


def add_guru(payload: dict) -> dict:
    _dedupe_by_slug(GURUS, payload)
    GURUS.append(payload)
    MODULES[4]["count"] = len(GURUS)
    return payload


def add_concert(payload: dict) -> dict:
    _dedupe_by_slug(CONCERTS, payload)
    CONCERTS.append(payload)
    MODULES[5]["count"] = len(CONCERTS)
    return payload


def add_course(payload: dict) -> dict:
    _dedupe_by_slug(COURSES, payload)
    COURSES.append(payload)
    MODULES[6]["count"] = len(COURSES)
    return payload


def add_thread(payload: dict) -> dict:
    for i in range(len(FORUM_THREADS) - 1, -1, -1):
        if FORUM_THREADS[i].get("title") == payload.get("title"):
            FORUM_THREADS.pop(i)
    payload.setdefault("author", "Community")
    payload.setdefault("replies", 0)
    FORUM_THREADS.append(payload)
    MODULES[7]["count"] = len(FORUM_THREADS)
    return payload


def add_archive(payload: dict) -> dict:
    _dedupe_by_slug(ARCHIVES, payload)
    ARCHIVES.append(payload)
    MODULES[8]["count"] = len(ARCHIVES)
    return payload
