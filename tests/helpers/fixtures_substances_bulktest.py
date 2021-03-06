
data = [
    (1,1,True,1,'Benzene','71-43-2',1,'PPB',1,0.0000),
    (2,1,True,1,'Toluene','108883',2,'PPB',1,0.0000),
    (3,1,True,1,'Ethylbenzene','100414',3,'PPB',1,0.0000),
    (4,1,True,1,'Xylene','1330-20-7',4,'PPB',1,0.0000),
    (8,1,True,0,'1,2,4-Trimethylbenzene','95636',8,'PPB',1,0.0000),
    (9,1,True,0,'1,3,5-Trimethylbenzene','108678',9,'PPB',1,0.0000),
    (10,1,True,0,'2-Methylnapthalene','91576',40,'PPB',1,0.0000),
    (11,2,True,0,'Acenaphthene','83-32-9',11,'PPB',1,0.0000),
    (12,2,True,0,'Acenaphthylene','208-96-8',12,'PPB',1,0.0000),
    (13,2,True,0,'Anthracene','120-12-7 ',13,'PPB',1,0.0000),
    (14,2,True,0,'Benzo(a)anthracene','56-55-3 ',14,'PPB',1,0.0000),
    (15,2,True,0,'Benzo(a)pyrene','819804-28-9 ',15,'PPB',1,0.0000),
    (16,2,True,0,'Benzo(b)fluoranthene','205-99-2',16,'PPB',1,0.0000),
    (17,2,True,0,'Benzo(g,h,i)perylene','191-24-2',17,'PPB',1,0.0000),
    (18,2,True,0,'Benzo(k)fluoranthene','207-08-9 ',18,'PPB',1,0.0000),
    (19,2,True,0,'Chrysene','8007-45-2 ',19,'PPB',1,0.0000),
    (20,2,True,0,'Dibenzo(a,h)anthracene','56-56-4 ',20,'PPB',1,0.0000),
    (21,2,True,0,'Fluoranthene','76774-50-0 ',21,'PPB',1,0.0000),
    (22,2,True,0,'Indeno(1,2,3-cd)pyrene','193-39-5',23,'PPB',1,0.0000),
    (23,2,True,0,'Fluorene','86-73-7 ',22,'PPB',1,0.0000),
    (24,2,False,0,'Naphthalene','',24,'PPB',0,260.0000),
    (25,2,True,0,'Phenanthrene','94-09-7 ',26,'PPB',1,0.0000),
    (26,2,True,0,'Pyrene','76165-23-6 ',25,'PPB',1,0.0000),
    (27,10,True,1,'Free Product','',27,'ft',-1,0.0000),
    (28,10,True,1,'Depth to Free Product','',28,'ft',2,0.0000),
    (30,10,True,0,'Temp','',35,'Celcius',1,0.0000),
    (31,10,True,0,'pH','',31,'',2,0.0000),
    (32,10,True,0,'Dissoloved Oxygen','',34,'mg/L',2,0.0000),
    (33,10,True,0,'Conductivity','',32,'ms/cm',3,0.0000),
    (34,10,True,0,'Turbidity','',33,'NTU',0,0.0000),
    (35,10,True,1,'Depth to Water','',30,'ft',2,0.0000),
    (36,10,False,0,'Depth to Bottom','',36,'',1,0.0000),
    (38,3,False,0,'New Substance','',38,'PPB',1,0.0000),
    (39,3,False,0,'Methyl-tert-butyl-ether','1634-04-4',39,'PPB',2,0.0000),
    (40,1,True,0,'Naphthalene','91203',10,'PPB',1,0.0000),
    (41,14,False,0,'Benzene','',41,'PPB',2,0.0000),
    (42,14,False,0,'Ethlybenzene','',42,'PPB',2,0.0000),
    (43,14,False,0,'Toluene','',43,'PPB',2,0.0000),
    (44,14,False,0,'Xylene','',44,'PPB',2,0.0000),
    (45,14,False,0,'1,2,4, Trimethylbenzene','',45,'PPB',2,0.0000),
    (46,14,False,0,'1,3,5, Trimethylbenzene','',46,'PPB',2,0.0000),
    (47,14,False,0,'Napthalene','',47,'PPB',2,0.0000),
    (48,14,False,0,'2, Methylnapthalene','',48,'PPB',2,0.0000),
    (49,14,False,0,'1, 2-Dibromoethane (ethylene dibromide EDB)','',49,'PPB',2,0.0000),
    (50,14,False,0,'MTBE','',51,'PPB',2,0.0000),
    (51,14,False,0,'1, 2-Dichloroethane','',50,'PPB',2,0.0000),
    (52,1,False,0,'1, 2-Dibromoethane','',52,'PPB',1,0.0500),
    (53,1,False,0,'1, 2-Dichloroethane','',53,'PPB',1,5.0000),
    (54,15,True,0,'Lead-Dissolved','7439-92-1D',131,'PPB',3,4.0000),
    (55,15,True,0,'Cadmium - Total','7440-43-9T',54,'PPB',1,5.0000),
    (56,15,True,0,'Chromium (III)','7440-47-3T',55,'PPB',1,100.0000),
    (57,15,True,0,'Chromium (VI)','18540-29-9T',56,'PPB',1,100.0000),
    (58,1,False,0,'1,2,-Dibromoethane','106-93-4',58,'PPB',2,0.0000),
    (59,3,False,0,'Toluene','',59,'PPB',2,790.0000),
    (60,3,False,0,'Ethylbenzene','',60,'PPB',2,74.0000),
    (61,3,False,0,'Xylene','',61,'PPB',2,280.0000),
    (62,1,False,0,'1,2,-Dichloroethane','107062',62,'PPB',2,0.0000),
    (63,16,True,0,'Bromobenzene','108-86-1',63,'PPB',4,0.0000),
    (64,16,True,0,'Bromochloromethane','74-97-5',64,'PPB',4,0.0000),
    (65,16,True,0,'Bromodichloromethane','75-27-4 ',65,'PPB',4,0.0000),
    (66,16,True,0,'Bromoform','75-25-2',66,'PPB',4,0.0000),
    (67,16,True,0,'Bromomethane','74-83-9',67,'PPB',4,0.0000),
    (68,16,True,0,'n-Butylbenzene','104-51-8',68,'PPB',4,0.0000),
    (69,16,True,0,'s-Butylbenzene','135-98-8',69,'PPB',4,0.0000),
    (70,16,False,0,'t-Butylbenzene','98-06-6',70,'PPB',4,0.0000),
    (71,16,True,0,'Carbon Disulfide','75-15-0',71,'PPB',4,0.0000),
    (72,16,True,0,'Carbon Tetrachloride','56-23-5 ',72,'PPB',4,0.0000),
    (73,16,True,0,'Chlorobenzene','108-90-7',73,'PPB',4,0.0000),
    (74,16,True,0,'Chloroform','67-66-3',74,'ppb',4,0.0000),
    (75,16,True,0,'Chloroethane','75-00-3',75,'PPB',4,0.0000),
    (76,16,True,0,'Chloromethane','74-87-3',76,'PPB',4,0.0000),
    (77,16,True,0,'Dibromochloromethane','124-48-1',77,'PPB',4,0.0000),
    (78,16,True,0,'Dibromo-methane','74-95-3 ',78,'PPB',4,0.0000),
    (79,16,False,0,'1,2-Dibromochloropropane','96-12-8',80,'PPB',4,0.0000),
    (80,16,True,0,'1,2-Dibromoethane','106-93-4 ',81,'PPB',4,0.0000),
    (81,16,True,0,'1,2-Dichlorobenzene','95-50-1',82,'PPB',4,0.0000),
    (82,16,True,0,'1,3-Dichlorobenzene','541-73-1',83,'PPB',4,0.0000),
    (83,16,True,0,'1,4-Dichlorobenzene','106-46-7 ',84,'PPB',4,0.0000),
    (84,16,True,0,'Dichlorodifluoromethane','75-71-8 ',79,'PPB',4,0.0000),
    (85,16,True,0,'1,1-Dichloroethane (1,1-DCA)','75-34-3',85,'PPB',4,0.0000),
    (86,16,True,0,'1,2-Dichloroethane (1,2-DCE)','107-06-2',86,'PPB',4,0.0000),
    (87,16,True,0,'1,1-dichloroethene (1,1-DCE)','75-35-4',87,'PPB',4,0.0000),
    (88,16,True,0,'cis-1,2-Dichloroethene (cis-1,2-DI)','156-59-2',88,'ppb',4,0.0000),
    (89,16,True,0,'trans-1,2-Dichloroethene (trans-1,2-DI)','156-60-5',89,'ppb',2,0.0000),
    (90,16,True,0,'1,2-Dichloropropane','78-87-5',90,'PPB',4,0.0000),
    (91,16,True,0,'cis-1,3-Dichloropropene','10061-01-5',91,'PPB',4,0.0000),
    (92,16,True,0,'trans-1,3-Dichloropropene','10061-02-6',92,'PPB',4,0.0000),
    (93,16,True,0,'Diethyl Ether','60-29-7',93,'PPB',4,0.0000),
    (94,16,False,0,'Ethylbenzene','',94,'PPB',4,74.0000),
    (95,16,False,0,'Iodomethane','74-88-4',95,'PPB',4,0.0000),
    (96,16,True,0,'Isopropylbenzene','98-82-8 ',96,'PPB',4,0.0000),
    (97,16,True,0,'Isopropyltoluene','95660-61-0 ',97,'PPB',4,0.0000),
    (98,16,False,0,'METHYL ETHYL KETONE','78-93-3 ',98,'PPB',4,0.0000),
    (99,16,False,0,'Do Not Use - Use Other MTBE','1634-04-4',99,'PPB',4,40.0000),
    (100,16,True,0,'Methylene chloride','75-09-2',100,'PPB',4,0.0000),
    (101,16,False,0,'Methyl Isobutyl Ketone (MIBK)','108-10-1 ',101,'PPB',4,0.0000),
    (102,16,False,0,'2-Methylnapthalene','',102,'PPB',4,260.0000),
    (103,16,False,0,'Naphthalene','',103,'PPB',4,520.0000),
    (104,16,True,0,'n-Propylbenzene','103-65-1',104,'PPB',4,0.0000),
    (105,16,True,0,'Styrene','100-42-5',105,'PPB',4,0.0000),
    (106,16,True,0,'1,1,1,2-Tetrachloroethane','630-20-6 ',106,'PPB',4,0.0000),
    (107,16,True,0,'1,1,2,2-Tetrachloroethane','79-34-5',107,'PPB',4,0.0000),
    (108,16,True,0,'Tetrachloroethene (PCE)','127-18-4',108,'ppb',2,0.0000),
    (109,16,False,0,'Toluene','',109,'PPB',4,790.0000),
    (110,16,True,0,'1,2,3-Trichlorobenzene','87-61-6',110,'PPB',4,0.0000),
    (111,16,True,0,'1,2,4-Trichlorobenzene','120-82-1',111,'PPB',4,0.0000),
    (112,16,True,0,'1,1,1-Trichloroethane','71-55-6',112,'PPB',4,0.0000),
    (113,16,True,0,'1,1,2-Trichloroethane','79-00-5',113,'PPB',4,0.0000),
    (114,16,True,0,'Trichloroethene (TCE)','79-01-6',114,'ppb',3,0.0000),
    (115,16,True,0,'Trichlorfluoromethane','75694',115,'PPB',4,0.0000),
    (116,16,True,0,'1,2,3-trichloropropane','96-18-4 ',116,'PPB',4,0.0000),
    (117,16,False,0,'1,2,4-Trimethylbenzene','',117,'PPB',4,63.0000),
    (118,16,False,0,'1,3,5-Trimethylbenzene','',118,'PPB',4,72.0000),
    (119,16,False,0,'Vinyl Chloride (VC)','75-01-4',119,'PPB',4,0.0000),
    (120,16,False,0,'Xylene','',120,'PPB',4,280.0000),
    (121,15,True,0,'Arsenic - Total','7440-38-2T',121,'PPB',4,0.0000),
    (122,15,True,0,'Barium - Total','7440-39-3T',130,'PPB',4,2000.0000),
    (123,15,True,0,'CALCIUM  EPA 6020','',123,'PPB',4,0.0000),
    (124,15,True,0,'Copper - Total','7440-50-8T',124,'PPB',4,1000.0000),
    (125,15,True,0,'Iron-Total','8053-60-9T',125,'ppm',4,300.0000),
    (126,15,True,0,'Iron-Dissolved','8053-60-9D',126,'PPB',4,300.0000),
    (127,15,True,0,'Magnesium-Total','7439-95-4T',133,'PPB',4,400000.0000),
    (128,15,True,0,'Manganese-Dissolved','7439-96-5D',164,'ppm',5,50.0000),
    (129,15,True,0,'Manganese-Total','7439-96-5T',163,'ppm',5,50.0000),
    (130,15,True,0,'Mercury - Total','7439-97-6T',165,'PPB',4,2.0000),
    (131,15,True,0,'Selenium - Total','7782-49-2T',177,'PPB',4,50.0000),
    (132,15,True,0,'Silver - Total','7440-22-4T',179,'PPB',4,34.0000),
    (133,15,True,0,'Zinc - Total','7440-66-6',184,'PPB',4,2400.0000),
    (134,15,True,0,'Lead - Total','7439-92-1T',132,'PPB',4,4.0000),
    (135,10,True,0,'Oxygen Reduction Potential (ORP)','',135,'mv',0,0.0000),
    (136,17,True,0,'HARDNESS(CALC)  SM2340-B','',136,'PPB',4,0.0000),
    (137,17,False,0,'NITROGEN, AMMONIA - EPA 350.1','7664-41-7',137,'PPB',4,10000.0000),
    (138,17,True,0,'NITROGEN, NITRATE - EPA 353.2','',138,'PPB',4,10000.0000),
    (139,18,False,0,'Benzene','',139,'PPB',4,5.0000),
    (140,20,True,0,'Mercury','92786-62-4',140,'PPB',4,1.3000),
    (141,22,True,0,'Chloride','16887006',141,'ppm',2,0.0000),
    (142,23,True,0,'Sulfate','14808-79-8',142,'ppm',2,0.0000),
    (143,24,True,0,'Nitrate','84145-82-4',143,'ppm',3,0.0000),
    (144,15,True,0,'Magnesium-Dissolved','7439-95-4D',134,'ppb',4,400000.0000),
    (145,16,True,0,'1,2,3-Trimethylbenzene','526-73-8',145,'',4,0.0000),
    (146,16,True,0,'2-Hexanone','591-78-6 ',146,'PPB',4,0.0000),
    (147,16,True,0,'Acrylonitrile','63908-52-1 ',147,'',4,0.0000),
    (148,16,False,0,'Alkalinity (as CaCO3)','10001',148,'ppm',2,0.0000),
    (149,16,True,0,'Cyclohexane','110-82-7',149,'PPB',4,0.0000),
    (150,16,True,0,'Diisopropyl Ether','108-20-3 ',150,'',4,0.0000),
    (151,16,True,0,'Ethyl-tertiary-butyl-ether','637-92-3',151,'ppb',4,49.0000),
    (152,16,True,0,'Hexachloroethane','98299-61-7 ',152,'',4,0.0000),
    (153,16,True,0,'Methyl iodide','74-88-4 ',153,'',4,0.0000),
    (154,25,True,0,'Nitrite','14797-65-0',154,'ppm',3,0.0000),
    (155,26,True,0,'Nitrate + Nitrite','7727-37-9',155,'ppm',3,0.0000),
    (156,16,True,0,'tertiary Butyl Alcohol','75-65-0',156,'',4,0.0000),
    (157,16,True,0,'tertiaryAmylmethylether','994-05-8',157,'',4,0.0000),
    (158,16,True,0,'Tetrahydrofuran','77392-70-2 ',158,'',4,0.0000),
    (159,16,True,0,'trans-1,4-Dichloro-2-butene','764-41-0 ',159,'',4,0.0000),
    (160,16,True,0,'Acetone','67-64-1',160,'ppb',2,0.0000),
    (161,27,False,0,'Dissolved Lead, EPA 200.8','7439-92-1',161,'ppb',2,4.0000),
    (162,15,True,0,'Cyanide - Total','57-12-5T',193,'ppb',2,0.0000),
    (163,15,True,0,'Antimony','7440-36-0T',194,'ppb',2,0.0000),
    (164,15,True,0,'Nickel','7440-02-0T',196,'ppb',2,0.0000),
    (165,15,True,0,'Thallium','7440-28-0T',198,'ppb',2,0.0000),
    (166,15,True,0,'Chromium - Total','7440-47-3T',57,'ppb',2,0.0000),
    (167,16,True,0,'1,4-Dioxane','123-91-1',167,'ppb',2,0.0000),
    (168,28,True,0,'Oil & Grease','30216',168,'ppm',1,0.0000),
    (169,29,True,0,'Chemical Oxygen Demand','10004',169,'ppm',2,0.0000),
    (170,30,True,0,'Total Suspended Solids','10053',170,'ppm',2,0.0000),
    (171,17,True,0,'Ammonia','7664-41-7',171,'ppm',2,0.0000),
    (172,15,False,0,'Phosphate - Total','',172,'ppm',2,0.0000),
    (173,17,True,0,'Phosphate - Total','98059-61-1',173,'ppm',2,0.0000),
    (174,31,True,0,'Bromine','10097-32-2',174,'ppm',2,0.0000),
    (175,32,True,0,'Total Dissolved Solids','',175,'ppm',2,0.0000),
    (176,33,True,0,'Color','',176,'ppm',2,0.0000),
    (177,15,True,0,'Aluminum','7429-90-5',201,'ppm',2,0.0000),
    (178,15,True,0,'Beryllium','7440-41-7T',202,'ppm',2,0.0000),
    (179,15,True,0,'Sodium','82115-62-6',203,'ppm',2,0.0000),
    (180,15,False,0,'Thallium','',200,'ppm',2,0.0000),
    (181,34,True,0,'Total Recoverable Petroleum Hydrocarbons','30140',181,'ppm',2,0.0000),
    (182,35,True,0,'CTAS','',182,'ppm',2,0.0000),
    (183,36,True,0,'Sulfide','18496-25-8',183,'ppm',2,0.0000),
    (184,15,True,0,'Lithium','7439-93-2',259,'ppm',4,0.0000),
    (185,37,True,0,'Vinclozolin (Ronilan)','50471-44-8',185,'ppm',4,0.0000),
    (186,16,True,0,'Methyl Acetate','79-20-9',186,'ppm',4,0.0000),
    (187,16,True,0,'Methylcyclohexane','108-87-2',187,'ppm',4,0.0000),
    (188,16,True,0,'1,1,2-Trichloro-1,2,2-Trifluoroethane','76-13-1',188,'ppb',4,0.0000),
    (189,38,True,0,'Methyl-tert-butyl-ether','1634-04-4',189,'ppb',4,0.0000),
    (190,39,True,0,'Formaldehyde','8615-67-9',190,'ppb',2,0.0000),
    (191,15,True,0,'Vanadium','7440-62-2',260,'ppm',4,0.0000),
    (192,40,True,0,'PLFA','',192,'',4,0.0000),
    (193,15,True,0,'Thallium - Dissolved','7440-28-0D',199,'ppb',2,0.0000),
    (194,15,True,0,'Nickel - Dissolved','7440-02-0D',197,'ppb',2,0.0000),
    (195,15,True,0,'Cadmium - Dissolved','7440-43-9D',128,'ppb',1,5.0000),
    (196,15,True,0,'Antimony - Dissolved','7440-36-0D',195,'ppb',2,0.0000),
    (197,15,True,0,'Chromium - Dissolved','7440-47-3D',128,'ppb',2,0.0000),
    (198,15,True,0,'Arsenic - Dissolved','7440-38-2D',122,'ppb',4,0.0000),
    (199,15,True,0,'Copper - Dissolved','7440-50-8',162,'ppb',4,1000.0000),
    (200,15,True,0,'Mercury - Dissolved','7439-97-6D',166,'ppb',4,2.0000),
    (201,15,True,0,'Selenium - Dissolved','7782-49-2D',178,'ppb',4,50.0000),
    (202,15,True,0,'Silver - Dissolved','7440-22-4D',180,'ppb',4,34.0000),
    (203,15,True,0,'Zinc - Dissolved','7440-66-6',191,'ppb',4,2400.0000),
    (204,41,True,0,'Carbon Dioxide (CO2)','124-38-9',204,'ppm',4,0.0000),
    (205,41,True,0,'Methane','74-82-8',205,'ppm',4,0.0000),
    (206,41,True,0,'Ethene','74-85-1',206,'ppm',4,0.0000),
    (207,41,True,0,'Ethane','74-84-0',207,'ppm',4,0.0000),
    (208,42,True,0,'Total Organic Carbon (TOC)','7440-44-0',208,'ppm',2,0.0000),
    (209,43,True,0,'1,1-Biphenyl (Diphenyl) ','92-52-4',209,'ppb',4,0.0000),
    (210,43,True,0,'2,3,4,6-Tetrachlorophenol','58-90-2',210,'ppb',4,0.0000),
    (211,43,True,0,'2,4,5-Trichlorophenol','95-95-4',211,'ppb',4,730.0000),
    (212,43,True,0,'2,4,6-Trichlorophenol','88-06-2',212,'ppb',4,120.0000),
    (213,43,False,0,'2,4,6-Trichlorophenol','88-06-2',213,'ppb',4,120.0000),
    (214,43,True,0,'2,4-Dichlorophenol','120-83-2',214,'ppb',4,73.0000),
    (215,43,True,0,'2,4-Dimethylphenol','105-67-9',215,'ppb',4,370.0000),
    (216,43,True,0,'2,4-Dinitrophenol','51-28-5',216,'ppb',4,0.0000),
    (217,43,True,0,'2,4-Dinitrotoluene','121-14-2',217,'ppb',4,7.7000),
    (218,43,True,0,'2,6-Dinitrotoluene','606-20-2',218,'ppb',4,0.0000),
    (219,43,True,0,'2-Chloronaphthalene','91-58-7',219,'ppb',4,1800.0000),
    (220,43,True,0,'2-Chlorophenol','95-57-8',220,'ppb',4,45.0000),
    (221,43,True,0,'2-methylphenol','95-48-7',221,'ppb',4,0.0000),
    (222,43,True,0,'2-Nitroaniline','88-74-4',222,'ppb',4,0.0000),
    (223,43,True,0,'2-Nitrophenol','88-75-5',223,'ppb',4,20.0000),
    (224,43,True,0,'3&4-Methylphenol','30030',224,'',4,0.0000),
    (225,43,True,0,'3,3-Dichlorobenzidine','91-94-1',225,'ppb',4,0.0000),
    (226,43,True,0,'3-Nitroaniline','99-09-2',226,'ppb',4,0.0000),
    (227,43,True,0,'4,6-dinitro-2-methyl phenol','534-52-1',227,'ppb',4,20.0000),
    (228,43,True,0,'4-Bromophenyl-phenylether','101-55-3',228,'ppb',4,0.0000),
    (229,43,True,0,'4-chloro-3-methylphenol','59-50-7',229,'ppb',4,150.0000),
    (230,43,True,0,'4-Chloroaniline','106-47-8',230,'ppb',4,0.0000),
    (231,43,True,0,'4-Chlorophenyl Phenyl Ether','7005-72-3',231,'ppb',4,0.0000),
    (232,43,True,0,'4-Nitroaniline','100-01-6',232,'ppb',4,0.0000),
    (233,43,True,0,'4-Nitrophenol','100-02-7',233,'ppb',4,0.0000),
    (234,43,True,0,'Acetophenone','98-86-2',234,'ppb',4,1500.0000),
    (235,43,True,0,'bis(2-chloroethoxy) methane','111-91-1',235,'ppb',4,0.0000),
    (236,43,True,0,'bis(2-chloroethyl) ether','111-44-4',236,'ppb',4,2.0000),
    (237,43,True,0,'bis(2-chloroisopropyl) ether','39638-32-9',237,'ppb',4,0.0000),
    (238,43,True,0,'bis(2-ethylhexyl) phthalate','117-81-7',238,'ppb',4,6.0000),
    (239,43,True,0,'Butylbenzylphthalate','85-68-7',239,'ppb',4,1200.0000),
    (240,43,True,0,'Caprolactam','105-60-2',240,'ppb',4,5800.0000),
    (241,43,True,0,'Carbazole','86-74-8',241,'ppb',4,85.0000),
    (242,43,True,0,'Dibenzofuran','132-64-9',242,'ppb',4,0.0000),
    (243,43,True,0,'Diethyl Phthalate','84-66-2',243,'ppb',4,5500.0000),
    (244,43,True,0,'Dimethyl Phthalate','131-11-3',244,'ppb',4,73000.0000),
    (245,43,True,0,'di-n-Butyl Phthalate','84-74-2',245,'ppb',4,880.0000),
    (246,43,True,0,'di-n-Octyl Phthalate','117-84-0',246,'ppb',4,130.0000),
    (247,43,True,0,'Hexachlorobenzene','118-74-1',247,'ppb',4,1.0000),
    (248,43,True,0,'Hexachlorobutadiene','87-68-3',248,'ppb',4,15.0000),
    (249,43,True,0,'Hexachlorocyclopentadiene','77-47-4',249,'ppb',4,50.0000),
    (250,43,True,0,'Hexachloroethane','67-72-1',250,'ppb',4,7.3000),
    (251,43,True,0,'Isophorone','78-59-1',251,'ppb',4,770.0000),
    (252,43,False,0,'Isophorone','78-59-1',252,'ppb',4,770.0000),
    (253,43,True,0,'Nitrobenzene','98-95-3',253,'ppb',4,3.4000),
    (254,43,True,0,'N-Nitrosodi-n-Propylamine','621-64-7',254,'ppb',4,5.0000),
    (255,43,True,0,'N-Nitrosodiphenylamine','86-30-6',255,'ppb',4,270.0000),
    (256,43,True,0,'Pentachlorophenol','87-86-5',256,'ppb',4,1.0000),
    (257,43,True,0,'Phenol','108-95-2',257,'ppb',4,4400.0000),
    (258,44,True,0,'Ethanol','64-17-5',258,'ppb',2,0.0000),
    (259,15,True,0,'Ferrous Iron','15438-31-0T',127,'ppm',2,0.0000),
    (260,15,True,0,'Barium - Dissolved','7440-39-3D',129,'ppb',4,0.0000),
    (261,45,True,0,'Alkalinity','0',261,'PPB',4,0.0000),
    (262,45,True,0,'Bicarbonate Alkalinity as CaCO3','71-52-3',262,'PPB',4,0.0000),
    (263,45,True,0,'Carbonate Alkalinity as CaCO3','3812-32-6',263,'PPB',4,0.0000),
    (264,45,True,0,'Hydroxide Alkalinity','14280-30-9',264,'PPB',4,0.0000),
    (265,45,True,0,'Phenolphthalein Alkalinity','10127',265,'PPB',4,0.0000),
    (266,43,True,0,'Acrolein','25314-61-8',266,'PPB',4,0.0000),
    (267,43,False,0,'Chlorodibromomethane','124-48-1',267,'PPB',4,0.0000),
    (268,16,True,0,'sec-Butylbenzene','8411-44-9',268,'PPB',4,0.0000),
    (269,16,True,0,'tert-Butylbenzene','98-06-6',269,'PPB',4,0.0000),
    (270,16,False,0,'Chlorodibromomethane','124-48-1',270,'PPB',4,0.0000),
    (271,16,True,0,'2-Chloroethyl vinyl ether','110-75-8',271,'PPB',4,0.0000),
    (272,16,True,0,'2-Chlorotoluene','95-49-8',272,'PPB',4,0.0000),
    (273,16,True,0,'4-Chlorotoluene','3327-51-3',273,'PPB',4,0.0000),
    (274,16,True,0,'1,2-Dibromo-3-Chloropropane','96-12-8',274,'PPB',4,0.0000),
    (275,16,False,0,'1,1-Dichloroethane','75-34-3',275,'PPB',4,0.0000),
    (276,16,False,0,'1,2-Dichloroethane','107-06-2',276,'PPB',4,0.0000),
    (277,16,False,0,'1,1-Dichloroethene','75-35-4',277,'PPB',4,0.0000),
    (278,16,False,0,'cis-1,2-Dichloroethene','156-59-2',278,'PPB',4,0.0000),
    (279,16,True,0,'trans-1,2-Dichloroethene','540-59-0',279,'PPB',4,0.0000),
    (280,16,True,0,'1,1-Dichloropropene','563-58-6',280,'PPB',4,0.0000),
    (281,16,True,0,'1,3-Dichloropropane','142-28-9',281,'PPB',4,0.0000),
    (282,16,True,0,'2,2-Dichloropropane','594-20-7',282,'PPB',4,0.0000),
    (283,16,False,0,'Di-isopropyl ether','108-20-3',283,'PPB',4,0.0000),
    (284,16,False,0,'Hexachloro-1,3-butadiene','87-68-3',284,'PPB',4,0.0000),
    (285,16,True,0,'p-Isopropyltoluene','99-87-6',285,'PPB',4,0.0000),
    (286,16,True,0,'2-Butanone (MEK)','78-93-3',286,'PPB',4,0.0000),
    (287,16,True,0,'4-Methyl-2-pentanone (MIBK)','108-10-1',287,'PPB',4,0.0000),
    (288,16,False,0,'Methyl tert-butyl ether','1634-04-4',288,'PPB',4,0.0000),
    (289,16,False,0,'1,1,2-Trichloro-1,2,2-trifluoroethane','76-13-1',289,'PPB',4,0.0000),
    (290,16,False,0,'Tetrachloroethene','127-18-4',290,'PPB',4,0.0000),
    (291,16,True,0,'Trichloroethene','86-42-0',291,'PPB',4,0.0000),
    (292,16,True,0,'Trichlorofluoromethane','91315-61-6',292,'PPB',4,0.0000),
    (293,16,False,0,'1,3,5-Trimethylbenzene','108-67-8',293,'PPB',4,0.0000),
    (294,16,True,0,'Vinyl chloride','9002-86-2',294,'PPB',4,0.0000),
    (295,24,True,0,'Nitrate as N','14797-55-8',295,'PPB',4,0.0000),
    (296,16,True,0,'Vinyl Chloride (VC)','75-01-4',296,'',4,0.0000),
    (297,16,True,0,'Vinyl Acetate','108-05-4',297,'ppb',4,0.0000),
    (298,16,True,0,'m,p-Xylenes','179601-23-1',298,'PPB',4,0.0000),
    (299,16,True,0,'o-Xylene','95-47-6',299,'PPB',4,0.0000),
    (300,46,True,0,'Polychlorinated Bipheny (PCBs)','1336-36-3',300,'ppb',4,0.0000),
    (301,16,True,0,' Trans-1,4-Dichloro-2-butene','110-57-6',301,'ppb',4,0.0000),
]