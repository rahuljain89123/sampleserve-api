POST /api/v1/reports/create-contours HTTP/1.1
Host: test.sampleserve.dev
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 7a70b970-0d2f-9aa7-2941-c488844c9878

{
"site_id": 127,
"date_collected": "2016-12-12",
"sitemap_id": 135,
"substance_ids": [1, 2, 3, 4],
"wells": [{
  "well_id": 2421,
  "xpos": 1082,
  "ypos": 963,
  "substance_sum": 171
},
{
  "well_id": 2449,
  "xpos": 1243,
  "ypos": 828,
  "substance_sum": 157
},
{
  "well_id": 2450,
  "xpos": 1286,
  "ypos": 1103,
  "substance_sum": 199.4
}]
}


  1. upload sitemap
  2. label well locations
  3. import lab data
  4. import field data
  5. http://test.sampleserve.dev/api/v1/reports/get-sample-dates/127
  6. http://test.sampleserve.dev/api/v1/reports/query-well-data
    {
      "site_id": 127,
      "sitemap_id": 135,
      "date": "2014-01-07",
      "substance_ids": [
            35,
            30,
            34,
            135,
            33,
            301,
            32,
            302,
            303,
            31,
            28,
            27
          ]
    }


    {
      "sample_dates": [
        {
          "active": true,
          "date_analyzed": null,
          "date_collected": "2016-12-12",
          "date_extracted": null,
          "id": 1298,
          "qty_values": 363,
          "schedule_id": null,
          "site_id": 129,
          "substance_ids": [
            1,
            86,
            189,
            3,
            2,
            9,
            4,
            10,
            80,
            40,
            8
          ],
          "upload_id": null
        }
      ]
    }



    {
      "my_wells": {
        "2416": {
          "est_depth_to_water": null,
          "id": 2416,
          "site_id": 129,
          "substance_sum": 134.9,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 130
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 4.9
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-3",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2417": {
          "est_depth_to_water": null,
          "id": 2417,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-2",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2418": {
          "est_depth_to_water": null,
          "id": 2418,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-1",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2419": {
          "est_depth_to_water": null,
          "id": 2419,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-7",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2420": {
          "est_depth_to_water": null,
          "id": 2420,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-5M1",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2421": {
          "est_depth_to_water": null,
          "id": 2421,
          "site_id": 129,
          "substance_sum": 1401,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 120
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 11
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 170
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 366
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 480
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 140
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 38
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 76
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-4",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2422": {
          "est_depth_to_water": null,
          "id": 2422,
          "site_id": 129,
          "substance_sum": 2.7,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 1
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 1.7
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-5M2",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2423": {
          "est_depth_to_water": null,
          "id": 2423,
          "site_id": 129,
          "substance_sum": 13,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 13
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-16M2",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2424": {
          "est_depth_to_water": null,
          "id": 2424,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-14",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2425": {
          "est_depth_to_water": null,
          "id": 2425,
          "site_id": 129,
          "substance_sum": 4350,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 620
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 370
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 1840
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 900
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 260
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 110
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 250
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-13",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2426": {
          "est_depth_to_water": null,
          "id": 2426,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-12",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2427": {
          "est_depth_to_water": null,
          "id": 2427,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-11",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2428": {
          "est_depth_to_water": null,
          "id": 2428,
          "site_id": 129,
          "substance_sum": 11459,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 3000
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 120
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 2000
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 5059
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 820
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 210
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 250
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-21S",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2429": {
          "est_depth_to_water": null,
          "id": 2429,
          "site_id": 129,
          "substance_sum": 2.4,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 2.4
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-38",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2430": {
          "est_depth_to_water": null,
          "id": 2430,
          "site_id": 129,
          "substance_sum": 6000,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 860
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 920
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 870
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 2430
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 610
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 110
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 200
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-16S",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2431": {
          "est_depth_to_water": null,
          "id": 2431,
          "site_id": 129,
          "substance_sum": 320.5,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 3.2
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 9.2
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 62
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 115
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 85
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 13
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 7.1
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 26
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-33",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2432": {
          "est_depth_to_water": null,
          "id": 2432,
          "site_id": 129,
          "substance_sum": 11912,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 32
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 1600
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 1400
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 6600
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 1300
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 400
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 170
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 410
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-32",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2433": {
          "est_depth_to_water": null,
          "id": 2433,
          "site_id": 129,
          "substance_sum": 1372.4,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 720
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 32
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 210
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 402
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 8.4
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-35",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2434": {
          "est_depth_to_water": null,
          "id": 2434,
          "site_id": 129,
          "substance_sum": 137.3,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 59
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 2.4
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 26
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 14
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 27
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 8.9
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-34",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2435": {
          "est_depth_to_water": null,
          "id": 2435,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-37",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2436": {
          "est_depth_to_water": null,
          "id": 2436,
          "site_id": 129,
          "substance_sum": 662,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 640
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 11
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 11
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-36",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2437": {
          "est_depth_to_water": null,
          "id": 2437,
          "site_id": 129,
          "substance_sum": 3885,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 2100
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 43
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 720
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 822
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 200
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-24M2",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2438": {
          "est_depth_to_water": null,
          "id": 2438,
          "site_id": 129,
          "substance_sum": 1500.8999999999999,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 1200
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 15
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 61
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 80.3
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 41
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 5.6
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 56
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 42
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-24M1",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2439": {
          "est_depth_to_water": null,
          "id": 2439,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-21M1",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2440": {
          "est_depth_to_water": null,
          "id": 2440,
          "site_id": 129,
          "substance_sum": 22,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 22
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-24S",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2441": {
          "est_depth_to_water": null,
          "id": 2441,
          "site_id": 129,
          "substance_sum": 13.4,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 1.4
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 5.1
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 6.9
            }
          },
          "title": "MW-20M1",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2442": {
          "est_depth_to_water": null,
          "id": 2442,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-20S",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2443": {
          "est_depth_to_water": null,
          "id": 2443,
          "site_id": 129,
          "substance_sum": 8.1,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 3
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 5.1
            }
          },
          "title": "MW-24D",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2444": {
          "est_depth_to_water": null,
          "id": 2444,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-26S",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2445": {
          "est_depth_to_water": null,
          "id": 2445,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-23",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2446": {
          "est_depth_to_water": null,
          "id": 2446,
          "site_id": 129,
          "substance_sum": 0,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-17S",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2447": {
          "est_depth_to_water": null,
          "id": 2447,
          "site_id": 129,
          "substance_sum": 1.8,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 0
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 0
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 0
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 0
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 0
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 0
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 0
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 1.8
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-25",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        },
        "2448": {
          "est_depth_to_water": null,
          "id": 2448,
          "site_id": 129,
          "substance_sum": 5143,
          "substances": {
            "1": {
              "substance_id": 1,
              "substance_name": "Benzene",
              "substance_value": 2100
            },
            "2": {
              "substance_id": 2,
              "substance_name": "Toluene",
              "substance_value": 41
            },
            "3": {
              "substance_id": 3,
              "substance_name": "Ethylbenzene",
              "substance_value": 1100
            },
            "4": {
              "substance_id": 4,
              "substance_name": "Xylene",
              "substance_value": 1032
            },
            "8": {
              "substance_id": 8,
              "substance_name": "1,2,4-Trimethylbenzene",
              "substance_value": 590
            },
            "9": {
              "substance_id": 9,
              "substance_name": "1,3,5-Trimethylbenzene",
              "substance_value": 160
            },
            "10": {
              "substance_id": 10,
              "substance_name": "2-Methylnapthalene",
              "substance_value": 0
            },
            "40": {
              "substance_id": 40,
              "substance_name": "Naphthalene",
              "substance_value": 120
            },
            "80": {
              "substance_id": 80,
              "substance_name": "1,2-Dibromoethane",
              "substance_value": 0
            },
            "86": {
              "substance_id": 86,
              "substance_name": "1,2-Dichloroethane (1,2-DCE)",
              "substance_value": 0
            },
            "189": {
              "substance_id": 189,
              "substance_name": "Methyl-tert-butyl-ether",
              "substance_value": 0
            }
          },
          "title": "MW-16M1",
          "top_of_casing": 0,
          "xpos": 0,
          "xpos_fields": 0,
          "ypos": 0,
          "ypos_fields": 0
        }
      }
    }