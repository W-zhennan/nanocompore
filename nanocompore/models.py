# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~RNA MODEL~~~~~~~~~~~~~~#

# ont_model_name	r9.4_180mv_70bps_5mer_RNA
# kit	r9.4_70bps
# strand	template
# k	5
# alphabet	u_to_t_rna
# original_file	r9.4_180mv_70bps_5mer_RNA/template_median69pA.model
# from nanopolish package https://github.com/jts/nanopolish
# for each entry: kmer_sequence = (level_mean, level_stdv)

RNA_model_dict = {
	'AAAAA': (108.901413, 2.676522),
	'AAAAC': (107.754232, 2.676522),
	'AAAAG': (101.724425, 2.676522),
	'AAAAT': (112.768194, 2.676522),
	'AAACA': (99.384679, 3.449749),
	'AAACC': (99.995527, 3.449749),
	'AAACG': (101.014242, 3.449749),
	'AAACT': (106.914144, 3.449749),
	'AAAGA': (110.541286, 4.062744),
	'AAAGC': (107.69345, 4.062744),
	'AAAGG': (108.28725, 4.062744),
	'AAAGT': (108.731506, 4.062744),
	'AAATA': (114.105726, 3.108588),
	'AAATC': (112.204348, 3.108588),
	'AAATG': (110.666258, 3.108588),
	'AAATT': (115.980739, 3.108588),
	'AACAA': (87.823777, 3.181436),
	'AACAC': (89.760969, 3.181436),
	'AACAG': (86.535661, 3.181436),
	'AACAT': (87.87631, 3.181436),
	'AACCA': (82.923787, 2.8125),
	'AACCC': (84.523756, 2.8125),
	'AACCG': (84.372558, 2.8125),
	'AACCT': (84.272303, 2.8125),
	'AACGA': (79.826259, 3.180457),
	'AACGC': (80.646898, 3.180457),
	'AACGG': (83.667276, 3.180457),
	'AACGT': (80.070168, 3.180457),
	'AACTA': (92.912342, 2.731261),
	'AACTC': (92.393785, 2.731261),
	'AACTG': (92.985289, 2.731261),
	'AACTT': (92.871956, 2.731261),
	'AAGAA': (122.139294, 5.872282),
	'AAGAC': (121.025135, 5.872282),
	'AAGAG': (122.095254, 5.872282),
	'AAGAT': (124.17474, 5.872282),
	'AAGCA': (107.336731, 3.017274),
	'AAGCC': (102.836148, 3.017274),
	'AAGCG': (109.951791, 3.017274),
	'AAGCT': (110.976336, 3.017274),
	'AAGGA': (114.014784, 7.840309),
	'AAGGC': (115.200439, 7.840309),
	'AAGGG': (113.123905, 7.840309),
	'AAGGT': (115.608986, 7.840309),
	'AAGTA': (119.31216, 4.029736),
	'AAGTC': (114.941808, 4.029736),
	'AAGTG': (117.293827, 4.029736),
	'AAGTT': (119.408277, 4.029736),
	'AATAA': (97.174409, 6.278645),
	'AATAC': (102.57511, 6.278645),
	'AATAG': (99.736573, 6.278645),
	'AATAT': (99.116744, 6.278645),
	'AATCA': (100.237818, 5.702234),
	'AATCC': (103.249725, 5.702234),
	'AATCG': (101.466911, 5.702234),
	'AATCT': (101.610711, 5.702234),
	'AATGA': (85.255182, 3.868907),
	'AATGC': (81.803851, 3.868907),
	'AATGG': (89.309222, 3.868907),
	'AATGT': (82.193226, 3.868907),
	'AATTA': (101.015119, 5.532156),
	'AATTC': (101.901081, 5.532156),
	'AATTG': (100.780633, 5.532156),
	'AATTT': (100.946682, 5.532156),
	'ACAAA': (82.446931, 3.018476),
	'ACAAC': (80.964607, 3.018476),
	'ACAAG': (78.46435, 3.018476),
	'ACAAT': (84.126436, 3.018476),
	'ACACA': (73.593076, 1.875816),
	'ACACC': (72.157345, 1.875816),
	'ACACG': (74.894231, 1.875816),
	'ACACT': (77.763958, 1.875816),
	'ACAGA': (96.555442, 5.093152),
	'ACAGC': (87.785962, 5.093152),
	'ACAGG': (84.200224, 5.093152),
	'ACAGT': (91.620597, 5.093152),
	'ACATA': (80.762856, 2.134613),
	'ACATC': (78.737631, 2.134613),
	'ACATG': (79.175014, 2.134613),
	'ACATT': (84.224654, 2.134613),
	'ACCAA': (74.583242, 2.107591),
	'ACCAC': (73.952994, 2.107591),
	'ACCAG': (72.329156, 2.107591),
	'ACCAT': (74.74115, 2.107591),
	'ACCCA': (66.29861, 2.070961),
	'ACCCC': (66.655278, 2.070961),
	'ACCCG': (67.209854, 2.070961),
	'ACCCT': (68.103653, 2.070961),
	'ACCGA': (82.817398, 2.778549),
	'ACCGC': (77.156491, 2.778549),
	'ACCGG': (76.543903, 2.778549),
	'ACCGT': (77.731098, 2.778549),
	'ACCTA': (69.022895, 2.349865),
	'ACCTC': (69.473323, 2.349865),
	'ACCTG': (70.748003, 2.349865),
	'ACCTT': (72.214658, 2.349865),
	'ACGAA': (85.738453, 3.990469),
	'ACGAC': (85.837941, 3.990469),
	'ACGAG': (84.299668, 3.990469),
	'ACGAT': (87.507643, 3.990469),
	'ACGCA': (76.327788, 2.600796),
	'ACGCC': (74.767402, 2.600796),
	'ACGCG': (77.116883, 2.600796),
	'ACGCT': (79.972499, 2.600796),
	'ACGGA': (96.55849, 4.981474),
	'ACGGC': (85.580326, 4.981474),
	'ACGGG': (83.393928, 4.981474),
	'ACGGT': (89.182212, 4.981474),
	'ACGTA': (101.495469, 3.049711),
	'ACGTC': (78.177926, 3.049711),
	'ACGTG': (78.194744, 3.049711),
	'ACGTT': (82.520253, 3.049711),
	'ACTAA': (86.712697, 2.631718),
	'ACTAC': (86.582543, 2.631718),
	'ACTAG': (86.098935, 2.631718),
	'ACTAT': (86.600747, 2.631718),
	'ACTCA': (81.845266, 2.848865),
	'ACTCC': (80.737367, 2.848865),
	'ACTCG': (80.877383, 2.848865),
	'ACTCT': (83.723176, 2.848865),
	'ACTGA': (93.408051, 2.85022),
	'ACTGC': (86.110953, 2.85022),
	'ACTGG': (87.124537, 2.85022),
	'ACTGT': (87.174256, 2.85022),
	'ACTTA': (77.863849, 2.416143),
	'ACTTC': (80.337425, 2.416143),
	'ACTTG': (80.104596, 2.416143),
	'ACTTT': (82.378469, 2.416143),
	'AGAAA': (128.133534, 5.559623),
	'AGAAC': (128.772325, 5.559623),
	'AGAAG': (123.663906, 5.559623),
	'AGAAT': (129.862932, 5.559623),
	'AGACA': (125.561516, 4.794395),
	'AGACC': (125.603209, 4.794395),
	'AGACG': (127.315213, 4.794395),
	'AGACT': (129.80722, 4.794395),
	'AGAGA': (127.709315, 5.691493),
	'AGAGC': (128.622891, 5.691493),
	'AGAGG': (123.332959, 5.691493),
	'AGAGT': (128.245512, 5.691493),
	'AGATA': (134.100055, 5.101816),
	'AGATC': (134.081251, 5.101816),
	'AGATG': (133.603178, 5.101816),
	'AGATT': (136.888917, 5.101816),
	'AGCAA': (115.20057, 3.856268),
	'AGCAC': (117.191419, 3.856268),
	'AGCAG': (112.16599, 3.856268),
	'AGCAT': (114.889148, 3.856268),
	'AGCCA': (109.316961, 3.291378),
	'AGCCC': (111.179412, 3.291378),
	'AGCCG': (109.945677, 3.291378),
	'AGCCT': (111.210293, 3.291378),
	'AGCGA': (105.688034, 8.394211),
	'AGCGC': (110.343163, 8.394211),
	'AGCGG': (106.831009, 8.394211),
	'AGCGT': (107.964723, 8.394211),
	'AGCTA': (117.176759, 3.551179),
	'AGCTC': (118.063757, 3.551179),
	'AGCTG': (117.440806, 3.551179),
	'AGCTT': (118.185419, 3.551179),
	'AGGAA': (117.457668, 3.173751),
	'AGGAC': (115.917559, 3.173751),
	'AGGAG': (116.685364, 3.173751),
	'AGGAT': (120.367899, 3.173751),
	'AGGCA': (109.736888, 5.310878),
	'AGGCC': (109.162065, 5.310878),
	'AGGCG': (112.237084, 5.310878),
	'AGGCT': (120.311348, 5.310878),
	'AGGGA': (115.882913, 4.047423),
	'AGGGC': (116.404557, 4.047423),
	'AGGGG': (113.610452, 4.047423),
	'AGGGT': (117.277569, 4.047423),
	'AGGTA': (119.513047, 3.368228),
	'AGGTC': (116.546344, 3.368228),
	'AGGTG': (117.246866, 3.368228),
	'AGGTT': (121.108797, 3.368228),
	'AGTAA': (123.302649, 8.555862),
	'AGTAC': (128.298724, 8.555862),
	'AGTAG': (122.886079, 8.555862),
	'AGTAT': (124.927423, 8.555862),
	'AGTCA': (122.594424, 6.071202),
	'AGTCC': (125.199218, 6.071202),
	'AGTCG': (122.920112, 6.071202),
	'AGTCT': (125.263087, 6.071202),
	'AGTGA': (100.006169, 9.689941),
	'AGTGC': (110.680015, 9.689941),
	'AGTGG': (111.727303, 9.689941),
	'AGTGT': (105.145547, 9.689941),
	'AGTTA': (118.77031, 7.489815),
	'AGTTC': (123.87167, 7.489815),
	'AGTTG': (121.107442, 7.489815),
	'AGTTT': (124.343096, 7.489815),
	'ATAAA': (86.593813, 3.040826),
	'ATAAC': (85.402731, 3.040826),
	'ATAAG': (82.488915, 3.040826),
	'ATAAT': (89.363951, 3.040826),
	'ATACA': (76.777933, 2.102993),
	'ATACC': (74.688134, 2.102993),
	'ATACG': (77.766007, 2.102993),
	'ATACT': (81.803551, 2.102993),
	'ATAGA': (103.910533, 3.781763),
	'ATAGC': (91.224691, 3.781763),
	'ATAGG': (85.792962, 3.781763),
	'ATAGT': (93.786839, 3.781763),
	'ATATA': (86.66635, 2.632201),
	'ATATC': (83.154921, 2.632201),
	'ATATG': (83.953361, 2.632201),
	'ATATT': (90.486693, 2.632201),
	'ATCAA': (78.880781, 2.300504),
	'ATCAC': (78.572102, 2.300504),
	'ATCAG': (76.739343, 2.300504),
	'ATCAT': (79.199937, 2.300504),
	'ATCCA': (70.227353, 2.29844),
	'ATCCC': (70.317427, 2.29844),
	'ATCCG': (71.191272, 2.29844),
	'ATCCT': (73.537614, 2.29844),
	'ATCGA': (84.425297, 2.302527),
	'ATCGC': (79.589757, 2.302527),
	'ATCGG': (79.88539, 2.302527),
	'ATCGT': (80.616314, 2.302527),
	'ATCTA': (76.666444, 2.065374),
	'ATCTC': (76.559406, 2.065374),
	'ATCTG': (77.109611, 2.065374),
	'ATCTT': (78.865989, 2.065374),
	'ATGAA': (94.57809, 4.487612),
	'ATGAC': (94.313336, 4.487612),
	'ATGAG': (93.097632, 4.487612),
	'ATGAT': (97.784441, 4.487612),
	'ATGCA': (84.446488, 3.125398),
	'ATGCC': (79.659624, 3.125398),
	'ATGCG': (83.143635, 3.125398),
	'ATGCT': (86.666404, 3.125398),
	'ATGGA': (100.762608, 3.994511),
	'ATGGC': (94.077436, 3.994511),
	'ATGGG': (92.935047, 3.994511),
	'ATGGT': (96.353408, 3.994511),
	'ATGTA': (88.609282, 3.775722),
	'ATGTC': (85.928321, 3.775722),
	'ATGTG': (87.079193, 3.775722),
	'ATGTT': (89.594494, 3.775722),
	'ATTAA': (85.297515, 2.458906),
	'ATTAC': (85.20998, 2.458906),
	'ATTAG': (84.559987, 2.458906),
	'ATTAT': (85.43756, 2.458906),
	'ATTCA': (78.4386, 2.072592),
	'ATTCC': (78.04618, 2.072592),
	'ATTCG': (78.538058, 2.072592),
	'ATTCT': (81.643698, 2.072592),
	'ATTGA': (90.368377, 2.64941),
	'ATTGC': (83.878953, 2.64941),
	'ATTGG': (86.040127, 2.64941),
	'ATTGT': (85.124486, 2.64941),
	'ATTTA': (77.576374, 1.969599),
	'ATTTC': (78.37344, 1.969599),
	'ATTTG': (79.100081, 1.969599),
	'ATTTT': (81.164568, 1.969599),
	'CAAAA': (105.724444, 2.676522),
	'CAAAC': (104.218946, 2.676522),
	'CAAAG': (102.997175, 2.676522),
	'CAAAT': (110.065655, 2.676522),
	'CAACA': (91.375475, 3.449749),
	'CAACC': (89.369315, 3.449749),
	'CAACG': (91.909217, 3.449749),
	'CAACT': (96.109537, 3.449749),
	'CAAGA': (110.387667, 4.062744),
	'CAAGC': (102.912958, 4.062744),
	'CAAGG': (106.169711, 4.062744),
	'CAAGT': (105.116845, 4.062744),
	'CAATA': (109.258367, 3.108588),
	'CAATC': (106.205847, 3.108588),
	'CAATG': (102.741785, 3.108588),
	'CAATT': (108.911579, 3.108588),
	'CACAA': (81.773599, 3.181436),
	'CACAC': (81.035104, 3.181436),
	'CACAG': (81.433659, 3.181436),
	'CACAT': (81.245111, 3.181436),
	'CACCA': (75.529943, 2.8125),
	'CACCC': (75.114913, 2.8125),
	'CACCG': (76.380811, 2.8125),
	'CACCT': (75.565847, 2.8125),
	'CACGA': (78.732084, 3.180457),
	'CACGC': (78.137316, 3.180457),
	'CACGG': (79.71892, 3.180457),
	'CACGT': (80.278731, 3.180457),
	'CACTA': (86.856587, 2.731261),
	'CACTC': (85.308154, 2.731261),
	'CACTG': (85.744053, 2.731261),
	'CACTT': (85.070789, 2.731261),
	'CAGAA': (108.596176, 5.872282),
	'CAGAC': (107.090001, 5.872282),
	'CAGAG': (106.732949, 5.872282),
	'CAGAT': (112.383806, 5.872282),
	'CAGCA': (108.254756, 3.017274),
	'CAGCC': (103.968265, 3.017274),
	'CAGCG': (109.18509, 3.017274),
	'CAGCT': (112.049883, 3.017274),
	'CAGGA': (98.378248, 7.840309),
	'CAGGC': (114.132204, 7.840309),
	'CAGGG': (89.169347, 7.840309),
	'CAGGT': (115.661044, 7.840309),
	'CAGTA': (123.50421, 4.029736),
	'CAGTC': (118.298104, 4.029736),
	'CAGTG': (119.527728, 4.029736),
	'CAGTT': (122.772197, 4.029736),
	'CATAA': (89.904186, 6.278645),
	'CATAC': (90.4791, 6.278645),
	'CATAG': (91.261151, 6.278645),
	'CATAT': (89.582788, 6.278645),
	'CATCA': (87.168862, 5.702234),
	'CATCC': (87.391196, 5.702234),
	'CATCG': (88.224484, 5.702234),
	'CATCT': (88.35973, 5.702234),
	'CATGA': (84.285822, 3.868907),
	'CATGC': (78.230209, 3.868907),
	'CATGG': (85.730638, 3.868907),
	'CATGT': (79.728396, 3.868907),
	'CATTA': (90.584171, 5.532156),
	'CATTC': (89.921897, 5.532156),
	'CATTG': (90.610816, 5.532156),
	'CATTT': (89.282133, 5.532156),
	'CCAAA': (87.18801, 3.018476),
	'CCAAC': (85.16373, 3.018476),
	'CCAAG': (86.10345, 3.018476),
	'CCAAT': (89.462193, 3.018476),
	'CCACA': (75.596677, 1.875816),
	'CCACC': (72.576022, 1.875816),
	'CCACG': (75.294463, 1.875816),
	'CCACT': (77.893144, 1.875816),
	'CCAGA': (76.21867, 5.093152),
	'CCAGC': (92.884026, 5.093152),
	'CCAGG': (91.801754, 5.093152),
	'CCAGT': (96.017075, 5.093152),
	'CCATA': (86.439459, 2.134613),
	'CCATC': (83.878091, 2.134613),
	'CCATG': (82.776712, 2.134613),
	'CCATT': (87.392322, 2.134613),
	'CCCAA': (73.427269, 2.107591),
	'CCCAC': (70.732523, 2.107591),
	'CCCAG': (71.951577, 2.107591),
	'CCCAT': (73.35631, 2.107591),
	'CCCCA': (62.973194, 2.070961),
	'CCCCC': (62.47677, 2.070961),
	'CCCCG': (63.753187, 2.070961),
	'CCCCT': (64.584982, 2.070961),
	'CCCGA': (83.922531, 2.778549),
	'CCCGC': (76.792394, 2.778549),
	'CCCGG': (78.031696, 2.778549),
	'CCCGT': (78.010037, 2.778549),
	'CCCTA': (69.670969, 2.349865),
	'CCCTC': (68.726024, 2.349865),
	'CCCTG': (71.635619, 2.349865),
	'CCCTT': (70.581909, 2.349865),
	'CCGAA': (97.550106, 3.990469),
	'CCGAC': (96.661828, 3.990469),
	'CCGAG': (95.856533, 3.990469),
	'CCGAT': (100.626525, 3.990469),
	'CCGCA': (87.112345, 2.600796),
	'CCGCC': (84.082353, 2.600796),
	'CCGCG': (87.086242, 2.600796),
	'CCGCT': (89.389588, 2.600796),
	'CCGGA': (106.163531, 4.981474),
	'CCGGC': (95.132647, 4.981474),
	'CCGGG': (92.989032, 4.981474),
	'CCGGT': (98.101357, 4.981474),
	'CCGTA': (92.468273, 3.049711),
	'CCGTC': (89.273835, 3.049711),
	'CCGTG': (90.049, 3.049711),
	'CCGTT': (92.470035, 3.049711),
	'CCTAA': (82.461064, 2.631718),
	'CCTAC': (79.054347, 2.631718),
	'CCTAG': (83.949886, 2.631718),
	'CCTAT': (82.627592, 2.631718),
	'CCTCA': (74.242313, 2.848865),
	'CCTCC': (72.353229, 2.848865),
	'CCTCG': (75.009135, 2.848865),
	'CCTCT': (75.306135, 2.848865),
	'CCTGA': (94.039444, 2.85022),
	'CCTGC': (84.197292, 2.85022),
	'CCTGG': (88.236624, 2.85022),
	'CCTGT': (86.87009, 2.85022),
	'CCTTA': (75.795766, 2.416143),
	'CCTTC': (75.319996, 2.416143),
	'CCTTG': (77.655142, 2.416143),
	'CCTTT': (76.374573, 2.416143),
	'CGAAA': (112.586708, 5.559623),
	'CGAAC': (111.470647, 5.559623),
	'CGAAG': (109.772606, 5.559623),
	'CGAAT': (115.648356, 5.559623),
	'CGACA': (109.269229, 4.794395),
	'CGACC': (110.091256, 4.794395),
	'CGACG': (110.9223, 4.794395),
	'CGACT': (113.970531, 4.794395),
	'CGAGA': (116.155274, 5.691493),
	'CGAGC': (110.677177, 5.691493),
	'CGAGG': (111.035628, 5.691493),
	'CGAGT': (112.737434, 5.691493),
	'CGATA': (117.344639, 5.101816),
	'CGATC': (117.717234, 5.101816),
	'CGATG': (114.129926, 5.101816),
	'CGATT': (120.276539, 5.101816),
	'CGCAA': (99.447505, 3.856268),
	'CGCAC': (101.875718, 3.856268),
	'CGCAG': (97.161063, 3.856268),
	'CGCAT': (99.569561, 3.856268),
	'CGCCA': (94.993064, 3.291378),
	'CGCCC': (96.312384, 3.291378),
	'CGCCG': (95.605523, 3.291378),
	'CGCCT': (96.759042, 3.291378),
	'CGCGA': (90.738766, 8.394211),
	'CGCGC': (90.608398, 8.394211),
	'CGCGG': (92.975641, 8.394211),
	'CGCGT': (90.718377, 8.394211),
	'CGCTA': (102.056437, 3.551179),
	'CGCTC': (102.446194, 3.551179),
	'CGCTG': (101.736582, 3.551179),
	'CGCTT': (102.109079, 3.551179),
	'CGGAA': (123.966612, 3.173751),
	'CGGAC': (120.901628, 3.173751),
	'CGGAG': (122.923242, 3.173751),
	'CGGAT': (128.823294, 3.173751),
	'CGGCA': (106.600732, 5.310878),
	'CGGCC': (103.668104, 5.310878),
	'CGGCG': (107.829566, 5.310878),
	'CGGCT': (110.544478, 5.310878),
	'CGGGA': (115.555709, 4.047423),
	'CGGGC': (113.737989, 4.047423),
	'CGGGG': (112.661902, 4.047423),
	'CGGGT': (113.905389, 4.047423),
	'CGGTA': (121.853626, 3.368228),
	'CGGTC': (117.184886, 3.368228),
	'CGGTG': (117.991203, 3.368228),
	'CGGTT': (120.767331, 3.368228),
	'CGTAA': (98.85897, 8.555862),
	'CGTAC': (102.949287, 8.555862),
	'CGTAG': (98.638064, 8.555862),
	'CGTAT': (101.566811, 8.555862),
	'CGTCA': (99.903703, 6.071202),
	'CGTCC': (102.207827, 6.071202),
	'CGTCG': (100.20425, 6.071202),
	'CGTCT': (102.027027, 6.071202),
	'CGTGA': (93.869948, 9.689941),
	'CGTGC': (89.889788, 9.689941),
	'CGTGG': (94.809034, 9.689941),
	'CGTGT': (91.659335, 9.689941),
	'CGTTA': (98.213897, 7.489815),
	'CGTTC': (100.912595, 7.489815),
	'CGTTG': (97.807475, 7.489815),
	'CGTTT': (99.903576, 7.489815),
	'CTAAA': (94.001495, 3.040826),
	'CTAAC': (91.503304, 3.040826),
	'CTAAG': (91.476358, 3.040826),
	'CTAAT': (96.70047, 3.040826),
	'CTACA': (80.29263, 2.102993),
	'CTACC': (76.498772, 2.102993),
	'CTACG': (80.581504, 2.102993),
	'CTACT': (83.468721, 2.102993),
	'CTAGA': (107.08281, 3.781763),
	'CTAGC': (97.296107, 3.781763),
	'CTAGG': (96.478532, 3.781763),
	'CTAGT': (99.587554, 3.781763),
	'CTATA': (94.690569, 2.632201),
	'CTATC': (91.526294, 2.632201),
	'CTATG': (90.280097, 2.632201),
	'CTATT': (95.551739, 2.632201),
	'CTCAA': (79.126807, 2.300504),
	'CTCAC': (76.729095, 2.300504),
	'CTCAG': (77.48486, 2.300504),
	'CTCAT': (79.739756, 2.300504),
	'CTCCA': (69.759632, 2.29844),
	'CTCCC': (67.633523, 2.29844),
	'CTCCG': (70.391059, 2.29844),
	'CTCCT': (71.318115, 2.29844),
	'CTCGA': (86.233646, 2.302527),
	'CTCGC': (79.792592, 2.302527),
	'CTCGG': (82.389078, 2.302527),
	'CTCGT': (81.943681, 2.302527),
	'CTCTA': (79.847504, 2.065374),
	'CTCTC': (77.342469, 2.065374),
	'CTCTG': (79.002204, 2.065374),
	'CTCTT': (79.011443, 2.065374),
	'CTGAA': (107.927419, 4.487612),
	'CTGAC': (107.161899, 4.487612),
	'CTGAG': (106.042371, 4.487612),
	'CTGAT': (111.640205, 4.487612),
	'CTGCA': (94.883447, 3.125398),
	'CTGCC': (90.931381, 3.125398),
	'CTGCG': (94.040237, 3.125398),
	'CTGCT': (96.865308, 3.125398),
	'CTGGA': (108.345742, 3.994511),
	'CTGGC': (102.611198, 3.994511),
	'CTGGG': (101.643559, 3.994511),
	'CTGGT': (105.22343, 3.994511),
	'CTGTA': (102.056314, 3.775722),
	'CTGTC': (98.483746, 3.775722),
	'CTGTG': (99.727199, 3.775722),
	'CTGTT': (102.17686, 3.775722),
	'CTTAA': (84.323058, 2.458906),
	'CTTAC': (81.759819, 2.458906),
	'CTTAG': (85.06359, 2.458906),
	'CTTAT': (84.65315, 2.458906),
	'CTTCA': (77.661841, 2.072592),
	'CTTCC': (74.217828, 2.072592),
	'CTTCG': (78.028442, 2.072592),
	'CTTCT': (78.042195, 2.072592),
	'CTTGA': (91.802992, 2.64941),
	'CTTGC': (84.545291, 2.64941),
	'CTTGG': (88.300823, 2.64941),
	'CTTGT': (86.773103, 2.64941),
	'CTTTA': (79.438553, 1.969599),
	'CTTTC': (77.724359, 1.969599),
	'CTTTG': (80.359399, 1.969599),
	'CTTTT': (79.706453, 1.969599),
	'GAAAA': (106.417182, 2.676522),
	'GAAAC': (105.923314, 2.676522),
	'GAAAG': (103.812292, 2.676522),
	'GAAAT': (111.123449, 2.676522),
	'GAACA': (95.518188, 3.449749),
	'GAACC': (94.695014, 3.449749),
	'GAACG': (96.735979, 3.449749),
	'GAACT': (100.790006, 3.449749),
	'GAAGA': (105.35778, 4.062744),
	'GAAGC': (100.441004, 4.062744),
	'GAAGG': (105.256818, 4.062744),
	'GAAGT': (103.994043, 4.062744),
	'GAATA': (111.538011, 3.108588),
	'GAATC': (109.543621, 3.108588),
	'GAATG': (107.509864, 3.108588),
	'GAATT': (112.107008, 3.108588),
	'GACAA': (80.850283, 3.181436),
	'GACAC': (84.444571, 3.181436),
	'GACAG': (80.987648, 3.181436),
	'GACAT': (82.607304, 3.181436),
	'GACCA': (79.015681, 2.8125),
	'GACCC': (79.175974, 2.8125),
	'GACCG': (79.366723, 2.8125),
	'GACCT': (79.904812, 2.8125),
	'GACGA': (75.702193, 3.180457),
	'GACGC': (73.050304, 3.180457),
	'GACGG': (77.571244, 3.180457),
	'GACGT': (75.245744, 3.180457),
	'GACTA': (90.235941, 2.731261),
	'GACTC': (88.671729, 2.731261),
	'GACTG': (88.632815, 2.731261),
	'GACTT': (89.12293, 2.731261),
	'GAGAA': (125.757042, 5.872282),
	'GAGAC': (123.324763, 5.872282),
	'GAGAG': (124.524117, 5.872282),
	'GAGAT': (130.18195, 5.872282),
	'GAGCA': (107.012728, 3.017274),
	'GAGCC': (103.081095, 3.017274),
	'GAGCG': (109.620464, 3.017274),
	'GAGCT': (112.005913, 3.017274),
	'GAGGA': (112.671894, 7.840309),
	'GAGGC': (113.935395, 7.840309),
	'GAGGG': (115.248936, 7.840309),
	'GAGGT': (112.282643, 7.840309),
	'GAGTA': (123.381585, 4.029736),
	'GAGTC': (117.524297, 4.029736),
	'GAGTG': (120.912293, 4.029736),
	'GAGTT': (123.901001, 4.029736),
	'GATAA': (88.342579, 6.278645),
	'GATAC': (94.910185, 6.278645),
	'GATAG': (90.963031, 6.278645),
	'GATAT': (88.946304, 6.278645),
	'GATCA': (93.448757, 5.702234),
	'GATCC': (95.14068, 5.702234),
	'GATCG': (95.150868, 5.702234),
	'GATCT': (95.383665, 5.702234),
	'GATGA': (79.43519, 3.868907),
	'GATGC': (75.419335, 3.868907),
	'GATGG': (82.943318, 3.868907),
	'GATGT': (76.83845, 3.868907),
	'GATTA': (96.012405, 5.532156),
	'GATTC': (96.042397, 5.532156),
	'GATTG': (96.095711, 5.532156),
	'GATTT': (94.713886, 5.532156),
	'GCAAA': (84.463941, 3.018476),
	'GCAAC': (82.484518, 3.018476),
	'GCAAG': (81.86329, 3.018476),
	'GCAAT': (86.302178, 3.018476),
	'GCACA': (73.145516, 1.875816),
	'GCACC': (70.716194, 1.875816),
	'GCACG': (73.836896, 1.875816),
	'GCACT': (77.182899, 1.875816),
	'GCAGA': (99.930045, 5.093152),
	'GCAGC': (89.545715, 5.093152),
	'GCAGG': (87.860142, 5.093152),
	'GCAGT': (91.458345, 5.093152),
	'GCATA': (82.80756, 2.134613),
	'GCATC': (80.540925, 2.134613),
	'GCATG': (80.707449, 2.134613),
	'GCATT': (85.122196, 2.134613),
	'GCCAA': (73.255993, 2.107591),
	'GCCAC': (71.672481, 2.107591),
	'GCCAG': (71.083389, 2.107591),
	'GCCAT': (73.701553, 2.107591),
	'GCCCA': (64.626903, 2.070961),
	'GCCCC': (64.850173, 2.070961),
	'GCCCG': (65.639915, 2.070961),
	'GCCCT': (66.352446, 2.070961),
	'GCCGA': (81.386803, 2.778549),
	'GCCGC': (76.262836, 2.778549),
	'GCCGG': (75.728029, 2.778549),
	'GCCGT': (76.98295, 2.778549),
	'GCCTA': (68.430678, 2.349865),
	'GCCTC': (67.98625, 2.349865),
	'GCCTG': (69.957644, 2.349865),
	'GCCTT': (70.994549, 2.349865),
	'GCGAA': (92.586828, 3.990469),
	'GCGAC': (91.214195, 3.990469),
	'GCGAG': (90.142127, 3.990469),
	'GCGAT': (95.899993, 3.990469),
	'GCGCA': (80.887105, 2.600796),
	'GCGCC': (78.753951, 2.600796),
	'GCGCG': (80.592982, 2.600796),
	'GCGCT': (83.20545, 2.600796),
	'GCGGA': (100.670666, 4.981474),
	'GCGGC': (90.29309, 4.981474),
	'GCGGG': (87.603071, 4.981474),
	'GCGGT': (92.738763, 4.981474),
	'GCGTA': (84.849331, 3.049711),
	'GCGTC': (82.777181, 3.049711),
	'GCGTG': (83.37308, 3.049711),
	'GCGTT': (86.636417, 3.049711),
	'GCTAA': (84.404682, 2.631718),
	'GCTAC': (85.335403, 2.631718),
	'GCTAG': (84.436792, 2.631718),
	'GCTAT': (84.827557, 2.631718),
	'GCTCA': (76.96812, 2.848865),
	'GCTCC': (78.882359, 2.848865),
	'GCTCG': (78.058375, 2.848865),
	'GCTCT': (80.104367, 2.848865),
	'GCTGA': (89.958937, 2.85022),
	'GCTGC': (83.434922, 2.85022),
	'GCTGG': (85.531612, 2.85022),
	'GCTGT': (84.347111, 2.85022),
	'GCTTA': (77.596356, 2.416143),
	'GCTTC': (77.979596, 2.416143),
	'GCTTG': (79.568036, 2.416143),
	'GCTTT': (80.135777, 2.416143),
	'GGAAA': (121.472353, 5.559623),
	'GGAAC': (121.878077, 5.559623),
	'GGAAG': (115.76285, 5.559623),
	'GGAAT': (123.503365, 5.559623),
	'GGACA': (118.398012, 4.794395),
	'GGACC': (119.234723, 4.794395),
	'GGACG': (120.922346, 4.794395),
	'GGACT': (123.834135, 4.794395),
	'GGAGA': (119.434686, 5.691493),
	'GGAGC': (121.187789, 5.691493),
	'GGAGG': (114.428791, 5.691493),
	'GGAGT': (117.274779, 5.691493),
	'GGATA': (126.875295, 5.101816),
	'GGATC': (127.167558, 5.101816),
	'GGATG': (126.022338, 5.101816),
	'GGATT': (129.827199, 5.101816),
	'GGCAA': (108.942858, 3.856268),
	'GGCAC': (111.254903, 3.856268),
	'GGCAG': (105.659758, 3.856268),
	'GGCAT': (109.069062, 3.856268),
	'GGCCA': (103.130746, 3.291378),
	'GGCCC': (105.110774, 3.291378),
	'GGCCG': (104.042571, 3.291378),
	'GGCCT': (105.481062, 3.291378),
	'GGCGA': (92.444142, 8.394211),
	'GGCGC': (100.100489, 8.394211),
	'GGCGG': (98.786021, 8.394211),
	'GGCGT': (95.65598, 8.394211),
	'GGCTA': (110.693339, 3.551179),
	'GGCTC': (111.329712, 3.551179),
	'GGCTG': (111.283445, 3.551179),
	'GGCTT': (112.465273, 3.551179),
	'GGGAA': (120.765797, 3.173751),
	'GGGAC': (118.289222, 3.173751),
	'GGGAG': (120.289092, 3.173751),
	'GGGAT': (124.022802, 3.173751),
	'GGGCA': (106.356917, 5.310878),
	'GGGCC': (104.099241, 5.310878),
	'GGGCG': (108.228545, 5.310878),
	'GGGCT': (113.279865, 5.310878),
	'GGGGA': (114.799941, 4.047423),
	'GGGGC': (113.915524, 4.047423),
	'GGGGG': (110.710467, 4.047423),
	'GGGGT': (113.895885, 4.047423),
	'GGGTA': (119.336919, 3.368228),
	'GGGTC': (114.734501, 3.368228),
	'GGGTG': (115.897733, 3.368228),
	'GGGTT': (119.328531, 3.368228),
	'GGTAA': (113.286729, 8.555862),
	'GGTAC': (118.692017, 8.555862),
	'GGTAG': (107.544746, 8.555862),
	'GGTAT': (114.714143, 8.555862),
	'GGTCA': (112.905071, 6.071202),
	'GGTCC': (116.089711, 6.071202),
	'GGTCG': (115.677666, 6.071202),
	'GGTCT': (117.089991, 6.071202),
	'GGTGA': (94.587253, 9.689941),
	'GGTGC': (93.689325, 9.689941),
	'GGTGG': (99.471489, 9.689941),
	'GGTGT': (93.0397, 9.689941),
	'GGTTA': (109.619445, 7.489815),
	'GGTTC': (114.367087, 7.489815),
	'GGTTG': (109.940264, 7.489815),
	'GGTTT': (112.498453, 7.489815),
	'GTAAA': (88.783209, 3.040826),
	'GTAAC': (87.408144, 3.040826),
	'GTAAG': (85.907661, 3.040826),
	'GTAAT': (91.846761, 3.040826),
	'GTACA': (76.340673, 2.102993),
	'GTACC': (73.994145, 2.102993),
	'GTACG': (77.413261, 2.102993),
	'GTACT': (81.125916, 2.102993),
	'GTAGA': (102.409502, 3.781763),
	'GTAGC': (92.905249, 3.781763),
	'GTAGG': (113.507644, 3.781763),
	'GTAGT': (93.937556, 3.781763),
	'GTATA': (89.664332, 2.632201),
	'GTATC': (86.997922, 2.632201),
	'GTATG': (86.70817, 2.632201),
	'GTATT': (91.860975, 2.632201),
	'GTCAA': (77.558218, 2.300504),
	'GTCAC': (76.200107, 2.300504),
	'GTCAG': (75.633527, 2.300504),
	'GTCAT': (78.480856, 2.300504),
	'GTCCA': (68.750632, 2.29844),
	'GTCCC': (68.271499, 2.29844),
	'GTCCG': (69.693728, 2.29844),
	'GTCCT': (70.254407, 2.29844),
	'GTCGA': (83.261071, 2.302527),
	'GTCGC': (78.622211, 2.302527),
	'GTCGG': (79.123155, 2.302527),
	'GTCGT': (79.776852, 2.302527),
	'GTCTA': (77.221483, 2.065374),
	'GTCTC': (76.088681, 2.065374),
	'GTCTG': (77.441233, 2.065374),
	'GTCTT': (77.911303, 2.065374),
	'GTGAA': (101.502426, 4.487612),
	'GTGAC': (99.690026, 4.487612),
	'GTGAG': (99.325519, 4.487612),
	'GTGAT': (105.21547, 4.487612),
	'GTGCA': (87.074004, 3.125398),
	'GTGCC': (83.63007, 3.125398),
	'GTGCG': (87.121505, 3.125398),
	'GTGCT': (90.013484, 3.125398),
	'GTGGA': (103.597649, 3.994511),
	'GTGGC': (96.907775, 3.994511),
	'GTGGG': (94.433499, 3.994511),
	'GTGGT': (98.902261, 3.994511),
	'GTGTA': (93.808736, 3.775722),
	'GTGTC': (90.407547, 3.775722),
	'GTGTG': (90.872067, 3.775722),
	'GTGTT': (95.076695, 3.775722),
	'GTTAA': (83.143687, 2.458906),
	'GTTAC': (82.192014, 2.458906),
	'GTTAG': (82.234327, 2.458906),
	'GTTAT': (83.687266, 2.458906),
	'GTTCA': (76.776405, 2.072592),
	'GTTCC': (75.95087, 2.072592),
	'GTTCG': (76.911413, 2.072592),
	'GTTCT': (77.377615, 2.072592),
	'GTTGA': (88.48406, 2.64941),
	'GTTGC': (81.946813, 2.64941),
	'GTTGG': (84.702338, 2.64941),
	'GTTGT': (83.61846, 2.64941),
	'GTTTA': (77.979258, 1.969599),
	'GTTTC': (77.60531, 1.969599),
	'GTTTG': (78.970582, 1.969599),
	'GTTTT': (78.700758, 1.969599),
	'TAAAA': (104.532801, 2.676522),
	'TAAAC': (103.44806, 2.676522),
	'TAAAG': (102.281548, 2.676522),
	'TAAAT': (108.512552, 2.676522),
	'TAACA': (93.834782, 3.449749),
	'TAACC': (93.341858, 3.449749),
	'TAACG': (95.297372, 3.449749),
	'TAACT': (99.065298, 3.449749),
	'TAAGA': (107.757941, 4.062744),
	'TAAGC': (101.583416, 4.062744),
	'TAAGG': (103.92047, 4.062744),
	'TAAGT': (104.095042, 4.062744),
	'TAATA': (108.459316, 3.108588),
	'TAATC': (106.551687, 3.108588),
	'TAATG': (104.66253, 3.108588),
	'TAATT': (109.834489, 3.108588),
	'TACAA': (83.03721, 3.181436),
	'TACAC': (84.223213, 3.181436),
	'TACAG': (79.554841, 3.181436),
	'TACAT': (83.152532, 3.181436),
	'TACCA': (77.842866, 2.8125),
	'TACCC': (78.84423, 2.8125),
	'TACCG': (78.268785, 2.8125),
	'TACCT': (79.015265, 2.8125),
	'TACGA': (79.560849, 3.180457),
	'TACGC': (78.112805, 3.180457),
	'TACGG': (80.133722, 3.180457),
	'TACGT': (79.237142, 3.180457),
	'TACTA': (87.983707, 2.731261),
	'TACTC': (87.806457, 2.731261),
	'TACTG': (87.789603, 2.731261),
	'TACTT': (88.099745, 2.731261),
	'TAGAA': (122.169039, 5.872282),
	'TAGAC': (120.421736, 5.872282),
	'TAGAG': (121.126709, 5.872282),
	'TAGAT': (126.659807, 5.872282),
	'TAGCA': (105.355994, 3.017274),
	'TAGCC': (101.168169, 3.017274),
	'TAGCG': (105.732615, 3.017274),
	'TAGCT': (109.433183, 3.017274),
	'TAGGA': (100.227487, 7.840309),
	'TAGGC': (93.67486, 7.840309),
	'TAGGG': (89.436063, 7.840309),
	'TAGGT': (96.83117, 7.840309),
	'TAGTA': (118.823116, 4.029736),
	'TAGTC': (113.727764, 4.029736),
	'TAGTG': (115.893989, 4.029736),
	'TAGTT': (118.667582, 4.029736),
	'TATAA': (92.840964, 6.278645),
	'TATAC': (95.089351, 6.278645),
	'TATAG': (92.782758, 6.278645),
	'TATAT': (93.546451, 6.278645),
	'TATCA': (92.764259, 5.702234),
	'TATCC': (94.256226, 5.702234),
	'TATCG': (94.102591, 5.702234),
	'TATCT': (94.806013, 5.702234),
	'TATGA': (82.979728, 3.868907),
	'TATGC': (78.952386, 3.868907),
	'TATGG': (86.356502, 3.868907),
	'TATGT': (80.19974, 3.868907),
	'TATTA': (94.34585, 5.532156),
	'TATTC': (95.059591, 5.532156),
	'TATTG': (94.789647, 5.532156),
	'TATTT': (94.778489, 5.532156),
	'TCAAA': (87.611027, 3.018476),
	'TCAAC': (85.786031, 3.018476),
	'TCAAG': (85.704511, 3.018476),
	'TCAAT': (89.199187, 3.018476),
	'TCACA': (75.587554, 1.875816),
	'TCACC': (74.443151, 1.875816),
	'TCACG': (75.822226, 1.875816),
	'TCACT': (79.431579, 1.875816),
	'TCAGA': (100.980285, 5.093152),
	'TCAGC': (90.483847, 5.093152),
	'TCAGG': (89.105518, 5.093152),
	'TCAGT': (93.137594, 5.093152),
	'TCATA': (87.266543, 2.134613),
	'TCATC': (85.069007, 2.134613),
	'TCATG': (83.806031, 2.134613),
	'TCATT': (88.3555, 2.134613),
	'TCCAA': (74.332779, 2.107591),
	'TCCAC': (72.874417, 2.107591),
	'TCCAG': (72.520894, 2.107591),
	'TCCAT': (74.36723, 2.107591),
	'TCCCA': (64.833964, 2.070961),
	'TCCCC': (64.935394, 2.070961),
	'TCCCG': (65.580357, 2.070961),
	'TCCCT': (66.257182, 2.070961),
	'TCCGA': (81.879199, 2.778549),
	'TCCGC': (76.600631, 2.778549),
	'TCCGG': (76.572635, 2.778549),
	'TCCGT': (77.035604, 2.778549),
	'TCCTA': (70.141326, 2.349865),
	'TCCTC': (70.827724, 2.349865),
	'TCCTG': (71.639246, 2.349865),
	'TCCTT': (73.284641, 2.349865),
	'TCGAA': (96.866468, 3.990469),
	'TCGAC': (96.268265, 3.990469),
	'TCGAG': (94.813241, 3.990469),
	'TCGAT': (99.037693, 3.990469),
	'TCGCA': (87.165793, 2.600796),
	'TCGCC': (84.427951, 2.600796),
	'TCGCG': (86.827111, 2.600796),
	'TCGCT': (88.706494, 2.600796),
	'TCGGA': (102.029446, 4.981474),
	'TCGGC': (92.919744, 4.981474),
	'TCGGG': (90.954481, 4.981474),
	'TCGGT': (95.286181, 4.981474),
	'TCGTA': (91.75211, 3.049711),
	'TCGTC': (89.203426, 3.049711),
	'TCGTG': (89.971282, 3.049711),
	'TCGTT': (92.10441, 3.049711),
	'TCTAA': (84.149385, 2.631718),
	'TCTAC': (83.057752, 2.631718),
	'TCTAG': (84.052304, 2.631718),
	'TCTAT': (83.974139, 2.631718),
	'TCTCA': (76.048058, 2.848865),
	'TCTCC': (75.362909, 2.848865),
	'TCTCG': (78.424879, 2.848865),
	'TCTCT': (79.44155, 2.848865),
	'TCTGA': (91.368585, 2.85022),
	'TCTGC': (83.897234, 2.85022),
	'TCTGG': (86.500177, 2.85022),
	'TCTGT': (84.953592, 2.85022),
	'TCTTA': (77.86194, 2.416143),
	'TCTTC': (76.97494, 2.416143),
	'TCTTG': (80.890077, 2.416143),
	'TCTTT': (80.386068, 2.416143),
	'TGAAA': (118.114917, 5.559623),
	'TGAAC': (118.657969, 5.559623),
	'TGAAG': (114.748297, 5.559623),
	'TGAAT': (120.761633, 5.559623),
	'TGACA': (117.047761, 4.794395),
	'TGACC': (118.437055, 4.794395),
	'TGACG': (118.74183, 4.794395),
	'TGACT': (121.90253, 4.794395),
	'TGAGA': (117.689804, 5.691493),
	'TGAGC': (117.855778, 5.691493),
	'TGAGG': (114.260596, 5.691493),
	'TGAGT': (116.262908, 5.691493),
	'TGATA': (124.237335, 5.101816),
	'TGATC': (124.545517, 5.101816),
	'TGATG': (123.134584, 5.101816),
	'TGATT': (127.734628, 5.101816),
	'TGCAA': (106.024708, 3.856268),
	'TGCAC': (108.558497, 3.856268),
	'TGCAG': (103.316898, 3.856268),
	'TGCAT': (106.106244, 3.856268),
	'TGCCA': (101.347109, 3.291378),
	'TGCCC': (102.953936, 3.291378),
	'TGCCG': (102.070117, 3.291378),
	'TGCCT': (102.970515, 3.291378),
	'TGCGA': (94.552419, 8.394211),
	'TGCGC': (98.581368, 8.394211),
	'TGCGG': (98.673061, 8.394211),
	'TGCGT': (96.635756, 8.394211),
	'TGCTA': (107.943353, 3.551179),
	'TGCTC': (108.757106, 3.551179),
	'TGCTG': (108.066432, 3.551179),
	'TGCTT': (109.232881, 3.551179),
	'TGGAA': (120.392424, 3.173751),
	'TGGAC': (118.046893, 3.173751),
	'TGGAG': (120.172787, 3.173751),
	'TGGAT': (125.168284, 3.173751),
	'TGGCA': (104.828979, 5.310878),
	'TGGCC': (103.755501, 5.310878),
	'TGGCG': (107.590784, 5.310878),
	'TGGCT': (108.631122, 5.310878),
	'TGGGA': (113.621342, 4.047423),
	'TGGGC': (113.117956, 4.047423),
	'TGGGG': (111.57308, 4.047423),
	'TGGGT': (112.203445, 4.047423),
	'TGGTA': (118.634757, 3.368228),
	'TGGTC': (114.414051, 3.368228),
	'TGGTG': (115.659191, 3.368228),
	'TGGTT': (118.828514, 3.368228),
	'TGTAA': (109.08326, 8.555862),
	'TGTAC': (113.988004, 8.555862),
	'TGTAG': (106.93121, 8.555862),
	'TGTAT': (110.146507, 8.555862),
	'TGTCA': (109.113377, 6.071202),
	'TGTCC': (112.006575, 6.071202),
	'TGTCG': (110.082064, 6.071202),
	'TGTCT': (111.929174, 6.071202),
	'TGTGA': (94.89796, 9.689941),
	'TGTGC': (95.267558, 9.689941),
	'TGTGG': (99.408797, 9.689941),
	'TGTGT': (93.181833, 9.689941),
	'TGTTA': (106.434881, 7.489815),
	'TGTTC': (109.695268, 7.489815),
	'TGTTG': (107.050463, 7.489815),
	'TGTTT': (109.49341, 7.489815),
	'TTAAA': (92.047985, 3.040826),
	'TTAAC': (90.306298, 3.040826),
	'TTAAG': (89.640417, 3.040826),
	'TTAAT': (94.218253, 3.040826),
	'TTACA': (79.87957, 2.102993),
	'TTACC': (76.727466, 2.102993),
	'TTACG': (80.271204, 2.102993),
	'TTACT': (84.199146, 2.102993),
	'TTAGA': (103.759006, 3.781763),
	'TTAGC': (94.883442, 3.781763),
	'TTAGG': (92.383719, 3.781763),
	'TTAGT': (95.991605, 3.781763),
	'TTATA': (93.293356, 2.632201),
	'TTATC': (90.317451, 2.632201),
	'TTATG': (89.800603, 2.632201),
	'TTATT': (94.204914, 2.632201),
	'TTCAA': (80.104941, 2.300504),
	'TTCAC': (77.152869, 2.300504),
	'TTCAG': (75.457517, 2.300504),
	'TTCAT': (80.433283, 2.300504),
	'TTCCA': (70.425126, 2.29844),
	'TTCCC': (68.771943, 2.29844),
	'TTCCG': (70.811221, 2.29844),
	'TTCCT': (72.025713, 2.29844),
	'TTCGA': (84.69738, 2.302527),
	'TTCGC': (80.794099, 2.302527),
	'TTCGG': (81.445733, 2.302527),
	'TTCGT': (81.561854, 2.302527),
	'TTCTA': (79.453763, 2.065374),
	'TTCTC': (77.296677, 2.065374),
	'TTCTG': (79.585705, 2.065374),
	'TTCTT': (79.328157, 2.065374),
	'TTGAA': (104.815901, 4.487612),
	'TTGAC': (104.197468, 4.487612),
	'TTGAG': (102.991893, 4.487612),
	'TTGAT': (108.318693, 4.487612),
	'TTGCA': (92.627509, 3.125398),
	'TTGCC': (89.54811, 3.125398),
	'TTGCG': (92.522648, 3.125398),
	'TTGCT': (94.95493, 3.125398),
	'TTGGA': (105.726794, 3.994511),
	'TTGGC': (100.451207, 3.994511),
	'TTGGG': (98.91281, 3.994511),
	'TTGGT': (102.467791, 3.994511),
	'TTGTA': (99.353452, 3.775722),
	'TTGTC': (96.281916, 3.775722),
	'TTGTG': (97.143134, 3.775722),
	'TTGTT': (99.718382, 3.775722),
	'TTTAA': (84.437742, 2.458906),
	'TTTAC': (82.79364, 2.458906),
	'TTTAG': (83.947046, 2.458906),
	'TTTAT': (84.611983, 2.458906),
	'TTTCA': (78.129826, 2.072592),
	'TTTCC': (75.285607, 2.072592),
	'TTTCG': (79.06707, 2.072592),
	'TTTCT': (79.594244, 2.072592),
	'TTTGA': (89.941598, 2.64941),
	'TTTGC': (83.798312, 2.64941),
	'TTTGG': (86.605735, 2.64941),
	'TTTGT': (85.149531, 2.64941),
	'TTTTA': (79.280022, 1.969599),
	'TTTTC': (77.911416, 1.969599),
	'TTTTG': (81.033026, 1.969599),
	'TTTTT': (80.784332, 1.969599),
}
