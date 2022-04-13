import pymysql
from flask import Flask, jsonify
from flask import request
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin


economics10ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass_10_economics_chapter_1_emb.pickle?alt=media&token=674d8883-4f85-413b-a531-3b9a03008c2b",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass_10_economics_chapter_1_text.pickle?alt=media&token=217c86ff-8ca0-4a6c-a84e-14ee0bdb284e",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass%2010%20economics%20chapter%201.epub?alt=media&token=5b27d802-ca76-405a-bada-4084b9095bc4"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass_10_economics_chapter_2_emb.pickle?alt=media&token=98a5c182-9785-4c38-be01-bb8e65403f83",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass_10_economics_chapter_2_text.pickle?alt=media&token=47fcd060-aa25-4056-92c1-e5a1b1f78f63",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass%2010%20economics%20chapter%202.epub?alt=media&token=02454b20-e0fc-4ca7-9bca-566c5decc01e"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass_10_economics_chapter_3_emb.pickle?alt=media&token=0b4b7d38-178f-482c-af22-7b9f729945e9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass_10_economics_chapter_3_text.pickle?alt=media&token=a7f0be66-f944-49a5-9cc3-a65bb4561a2f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass%2010%20economics%20chapter%203.epub?alt=media&token=4782d722-587d-4154-9a5c-bf512128d9c2"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass_10_economics_chapter_4_emb.pickle?alt=media&token=f6fcf9e4-ae7a-4ac2-b8b1-a6c2136da12c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass_10_economics_chapter_4_text.pickle?alt=media&token=17e38fd5-4d46-46db-9704-4f3b13b2b24e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass%2010%20economics%20chapter%204.epub?alt=media&token=ccd33e72-a7a5-44de-bc59-4fe20a90042b"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass_10_economics_chapter_5_emb.pickle?alt=media&token=49b185b0-5503-4872-8837-3ed3a2683d33",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass_10_economics_chapter_5_text.pickle?alt=media&token=b5189bee-e4e1-415e-ad61-9fe0e5cfce05",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass%2010%20economics%20chapter%205.epub?alt=media&token=98d41eee-9226-4adb-9fbc-aae57433a6f0"}
}

geography10ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass_10_geography_chapter_1_emb.pickle?alt=media&token=bda5729f-ccef-49d2-8c6d-605a0d1cff26",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass_10_geography_chapter_1_text.pickle?alt=media&token=76dd446c-513a-4e83-b059-62f25a651c6c",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass%2010%20geography%20chapter%201.epub?alt=media&token=b515d924-08d9-45a7-b249-bc2d5bfec473"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass_10_geography_chapter_2_emb.pickle?alt=media&token=3319a7ed-07cd-4a3b-98b2-2db15ac022a1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass_10_geography_chapter_2_text.pickle?alt=media&token=67df6458-f929-47b5-b420-924c2f023feb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass%2010%20geography%20chapter%202.epub?alt=media&token=5cfa4695-97dc-411b-96cf-1f32eeade35d"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass_10_geography_chapter_3_emb.pickle?alt=media&token=80091170-c686-4336-89ab-57722083a5ed",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass_10_geography_chapter_3_text.pickle?alt=media&token=6ca7dbac-ad96-4eff-a675-42c64b02edfa",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass%2010%20geography%20chapter%203.epub?alt=media&token=55c85144-4735-48c3-ac5d-a41e21dbb458"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass_10_geography_chapter_4_emb.pickle?alt=media&token=daffb7e0-37e1-4cb8-ba72-8c90228e4a1d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass_10_geography_chapter_4_text.pickle?alt=media&token=ce43268f-67d7-49d7-aaac-d8f8125beb0a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass%2010%20geography%20chapter%204.epub?alt=media&token=59e53fd2-0559-4a33-8965-4ef978ce7269"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass_10_geography_chapter_5_emb.pickle?alt=media&token=e137d09d-748e-46d2-b74b-164ccf13d668",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass_10_geography_chapter_5_text.pickle?alt=media&token=92c96ca7-0529-4b3d-bd4c-bc42ab0582e5",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass%2010%20geography%20chapter%205.epub?alt=media&token=9061d743-73fa-4fb1-88f2-e75fc30732fd"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass_10_geography_chapter_6_emb.pickle?alt=media&token=ca4a23a3-eae6-4760-8ec7-55e693b2402a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass_10_geography_chapter_6_text.pickle?alt=media&token=7fa28343-01ac-4854-81f8-4c33bf38ae70",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass%2010%20geography%20chapter%206.epub?alt=media&token=5b151890-904e-4629-8a75-ad5249d9b652"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass_10_geography_chapter_7_emb.pickle?alt=media&token=3ff866ec-5357-4131-9bda-8309c460a7b5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass_10_geography_chapter_7_text.pickle?alt=media&token=ba31f93a-05b0-4ead-abff-584b9dd9370e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass%2010%20geography%20chapter%207.epub?alt=media&token=a3f0900b-bf65-4095-a3ca-8faa81ab7939"}
}

history10ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fclass_10_history_chapter_1_emb.pickle?alt=media&token=a41b3ddd-c650-4188-a007-e9bb96e66360",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fclass_10_history_chapter_1_text.pickle?alt=media&token=4ec6175f-00dc-493e-a078-ab8103a7eb58",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fhistory%20chapter%201.epub?alt=media&token=2e456515-2b8f-4223-899c-132f0b4ad98f"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fclass_10_history_chapter_2_emb.pickle?alt=media&token=4eb30b43-e0af-4611-b01f-66a4c0de9367",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fclass_10_history_chapter_2_text.pickle?alt=media&token=b12c6518-2a11-4d3f-9a5c-6322eccec8d6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fhistory%20chapter%202.epub?alt=media&token=b4335fde-3c48-45b2-95cb-5631730c4a02"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fclass_10_history_chapter_3_emb.pickle?alt=media&token=e7a8051e-bc22-4a53-94e4-5cf7927aa27d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fclass_10_history_chapter_3_text.pickle?alt=media&token=5ba30421-8c3d-41e4-ba98-7f160d1a0c99",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fhistory%20chapter%203.epub?alt=media&token=cc72c05c-0509-49a2-8655-98e6169be454"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fclass_10_history_chapter_4_emb.pickle?alt=media&token=572c74b1-5e6a-47c2-8131-e4c19d741635",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fclass_10_history_chapter_4_text.pickle?alt=media&token=66743a78-93ea-4e7a-80d0-459349c770cc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fhistory%20chapter%204.epub?alt=media&token=b036839d-63d9-4071-8dac-c955ba13ac62"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fclass_10_history_chapter_5_emb.pickle?alt=media&token=0cfda65a-65e1-4add-84e0-bc9c51e69600",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fclass_10_history_chapter_5_text.pickle?alt=media&token=e60bd917-a392-4903-9f66-97a62e0017de",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fhistory%20chapter%205.epub?alt=media&token=bfa39eef-196a-4a6a-b6fc-bb02849e8168"}
}

mathematics10ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass_10_math_chapter_1_emb.pickle?alt=media&token=f605809f-1c58-49de-a256-eb4094df0d4e",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass_10_math_chapter_1_text.pickle?alt=media&token=e0934e22-93ae-4a52-af9e-ef03b1c8c2d4",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass%2010%20math%20chapter%201.epub?alt=media&token=6ba9aa62-6ce5-47eb-9a34-a6c5f032b4a7"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass_10_math_chapter_2_emb.pickle?alt=media&token=2ab22185-37f8-49da-8f12-3b2a201c071c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass_10_math_chapter_2_text.pickle?alt=media&token=c64adf11-c273-4bd0-805c-4c1a9fbfd1fc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass%2010%20math%20chapter%202.epub?alt=media&token=95c11b13-2893-4cab-9670-b4e2e6f0f7d8"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass_10_math_chapter_3_emb.pickle?alt=media&token=087d37f7-8ff2-4b57-8c6a-e6d41967df08",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass_10_math_chapter_3_text.pickle?alt=media&token=204b66ff-e835-4810-ac72-f31cd238e70f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass%2010%20math%20chapter%203.epub?alt=media&token=29923fd3-7f9c-47ec-8720-f4fff7d8f7fc"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass_10_math_chapter_4_emb.pickle?alt=media&token=eb4c6842-ea08-44bd-9eae-37d17bdff74a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass_10_math_chapter_4_text.pickle?alt=media&token=70eb2932-4068-48ff-855c-7247a3e1d398",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass%2010%20math%20chapter%204.epub?alt=media&token=7d8a1ac9-3bb3-4345-891a-ff764d3d3b5e"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass_10_math_chapter_5_emb.pickle?alt=media&token=6ea17c0f-5773-4e7b-bb36-f632770af032",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass_10_math_chapter_5_text.pickle?alt=media&token=fc4e2905-d93b-4e08-941b-18f803ba5fb2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass%2010%20math%20chapter%205.epub?alt=media&token=96637ad4-3d58-4b16-89ba-e15cec7e6ebd"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass_10_math_chapter_6_emb.pickle?alt=media&token=7249f28e-b37a-4de5-9e30-dc3ead3e8531",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass_10_math_chapter_6_text.pickle?alt=media&token=d55e9559-c8e1-44c8-a47b-bba02b35948b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass%2010%20math%20chapter%206.epub?alt=media&token=5f3c7b92-8b56-470a-a5bf-dcb2c0313256"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass_10_math_chapter_7_emb.pickle?alt=media&token=5ed2dbdb-460b-4c84-a763-8681b32ff728",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass_10_math_chapter_7_text.pickle?alt=media&token=95390455-6856-4312-8ca8-67716371a3e8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass%2010%20math%20chapter%207.epub?alt=media&token=23295817-f972-4867-b117-c471f94195b9"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass_10_math_chapter_8_emb.pickle?alt=media&token=08361518-58ff-4133-884b-d91c1a91f5dd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass_10_math_chapter_8_text.pickle?alt=media&token=85246b0e-6289-4139-b125-67c74d96edb7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass%2010%20math%20chapter%208.epub?alt=media&token=a8eda524-b7f6-4d00-b00c-e81f5979d74e"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass_10_math_chapter_9_emb.pickle?alt=media&token=dbdc9eaf-bf04-42c2-a3cb-359704b0b77b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass_10_math_chapter_9_text.pickle?alt=media&token=9ecf2283-1a22-4043-a1f3-f5673aa746fa",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass%2010%20math%20chapter%209.epub?alt=media&token=19215403-08e0-4109-9fee-a097e48e77fe"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass_10_math_chapter_10_emb.pickle?alt=media&token=e91ed504-7c34-4cee-aef1-af230789bd3f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass_10_math_chapter_10_text.pickle?alt=media&token=c46828a5-b8d1-4f35-b1c6-66f16d0df4c6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass%2010%20math%20chapter%2010.epub?alt=media&token=3a575a57-c57a-44ef-807b-007bcb4300eb"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass_10_math_chapter_11_emb.pickle?alt=media&token=ee0ddc86-22b5-4a7b-9ab9-64f0c239df40",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass_10_math_chapter_11_text.pickle?alt=media&token=66947e14-befe-4958-b665-38c42429e841",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass%2010%20math%20chapter%2011.epub?alt=media&token=9503dbe3-b275-4530-88d6-852ee143508a"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass_10_math_chapter_12_emb.pickle?alt=media&token=16ab50f8-862d-45db-819f-b50d70e075fa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass_10_math_chapter_12_text.pickle?alt=media&token=67295602-bfde-402e-846e-26f52127085a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass%2010%20math%20chapter%2012.epub?alt=media&token=e5051833-6981-47d9-b089-bdc533719dfd"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass_10_math_chapter_13_emb.pickle?alt=media&token=b4fc802d-4879-441f-9458-158c9f4df7ad",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass_10_math_chapter_13_text.pickle?alt=media&token=80ce2a37-a2cd-4baf-8b91-37d8036e0aa0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass%2010%20math%20chapter%2013.epub?alt=media&token=ed87ee85-68d1-452c-abe9-b35596aebbf1"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass_10_math_chapter_14_emb.pickle?alt=media&token=a5869929-69a8-4101-9db7-9db74a5d9b1e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass_10_math_chapter_14_text.pickle?alt=media&token=386afb69-9caf-48fd-9169-c0514eb38c70",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass%2010%20math%20chapter%2014.epub?alt=media&token=78f234ec-75ca-477b-9295-89b9fee4d2da"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass_10_math_chapter_15_emb.pickle?alt=media&token=9c45e7d6-f2f5-46d1-a22c-d91ea352c2d6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass_10_math_chapter_15_text.pickle?alt=media&token=f7e2f251-20a2-474e-a6f9-a55dd0bd7a90",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass%2010%20math%20chapter%2015.epub?alt=media&token=f05857f6-3366-40ce-9a1e-8b1cc9b0086a"}
}

civics10ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass_10_political_science_chapter_1_emb.pickle?alt=media&token=8609c368-55a3-4ccf-8a90-f4552c386d0d",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass_10_political_science_chapter_1_text.pickle?alt=media&token=4ca251ea-d8dd-4bd8-b98d-97b3259d2d13",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass%2010%20political%20science%20chapter%201.epub?alt=media&token=b228e88d-e166-413-5fc77830b50b"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass_10_political_science_chapter_2_emb.pickle?alt=media&token=1f4e4381-8b6d-4a47-bc27-8aee7ae2e9ba",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass_10_political_science_chapter_2_text.pickle?alt=media&token=adae8df8-7db7-4f8c-802a-85b6f30fcce0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass%2010%20political%20science%20chapter%202.epub?alt=media&token=4c3cb4fc-0fa8-433e-a21d-dc28d076ffdf"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass_10_political_science_chapter_3_emb.pickle?alt=media&token=453fee3e-5cae-4942-9508-81bb52874362",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass_10_political_science_chapter_3_text.pickle?alt=media&token=c8f3ec57-2cb0-43e5-ad9c-9d319631dcae",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass%2010%20political%20science%20chapter%203.epub?alt=media&token=a37b05fb-b3cd-4cc6-b02c-ab9d260f1823"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass_10_political_science_chapter_4_emb.pickle?alt=media&token=4720e310-1454-4063-9a58-d0198c864d08",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass_10_political_science_chapter_4_text.pickle?alt=media&token=403d8167-cf5c-4033-b838-53ae2b24018e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass%2010%20political%20science%20chapter%204.epub?alt=media&token=cf673608-4c4a-4fdd-a58b-ee58a062e654"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass_10_political_science_chapter_5_emb.pickle?alt=media&token=66ea431c-6872-4e8d-8243-a8c4f13e03b7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass_10_political_science_chapter_5_text.pickle?alt=media&token=e40a47b6-f953-4d41-b6c5-40645b0a81c6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass%2010%20political%20science%20chapter%205.epub?alt=media&token=75a70546-1f90-4fdd-bde7-bc7aadec88c7"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass_10_political_science_chapter_6_emb.pickle?alt=media&token=4287105e-bca4-4265-a052-b35c80820456",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass_10_political_science_chapter_6_text.pickle?alt=media&token=fe8f3d31-e4d6-44b0-80b2-b7982547f08b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass%2010%20political%20science%20chapter%206.epub?alt=media&token=5a852abb-8463-446e-ba8c-b96c130a1c04"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass_10_political_science_chapter_7_emb.pickle?alt=media&token=d2a076ed-e43d-4e7e-b737-0af34c91b88d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass_10_political_science_chapter_7_text.pickle?alt=media&token=32466b00-732f-4b7b-a095-a8aa4e3c626e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass%2010%20political%20science%20chapter%207.epub?alt=media&token=dad03a43-c18b-4242-a61f-f92e94d19812"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass_10_political_science_chapter_8_emb.pickle?alt=media&token=75d920de-55dc-4310-a52a-ce536af5c236",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass_10_political_science_chapter_8_text.pickle?alt=media&token=a852aecd-a6dc-4e95-9955-cf24503d2ff0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass%2010%20political%20science%20chapter%208.epub?alt=media&token=8418bd74-1b88-4288-8b96-e5e6269e37c9"}
}

science10ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fclass_10_science_chapter_1_emb.pickle?alt=media&token=31a4e158-bbc9-4c67-9548-12a4b5120e8c",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fclass_10_science_chapter_1_text.pickle?alt=media&token=872f2398-f240-4417-8938-afab74a66385",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fchapter%201.epub?alt=media&token=c7fc50ac-cb63-4e08-bcaf-99634dd51943"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fclass_10_science_chapter_2_emb.pickle?alt=media&token=77c18e3a-c145-49e5-b5d0-2571f09485e9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fclass_10_science_chapter_2_text.pickle?alt=media&token=9de01f8f-211a-4a00-81a4-5758f92c7ca1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fchapter%202.epub?alt=media&token=e8c5a4af-2dd0-4cc3-bf91-851731280ae5"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fclass_10_science_chapter_3_emb.pickle?alt=media&token=1dc9163e-3f41-41fe-8452-445802c7fd00",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fclass_10_science_chapter_3_text.pickle?alt=media&token=26ef43b0-141b-4dfb-bbcd-e0270598abeb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fchapter%203.epub?alt=media&token=3ad1ffb1-a330-4add-b21f-b88ac3f1b1bd"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fclass_10_science_chapter_4_emb.pickle?alt=media&token=9a34900f-1ac5-43e4-95ed-720bcc3c869e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fclass_10_science_chapter_4_text.pickle?alt=media&token=2d6361eb-965b-44e6-a2ca-8264de234f20",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fchapter%204.epub?alt=media&token=f2d4e134-0374-4d2c-8b2f-1bb67a90da45"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fclass_10_science_chapter_5_emb.pickle?alt=media&token=64f04259-d336-4863-b113-18f5ca0f60f7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fclass_10_science_chapter_5_text.pickle?alt=media&token=047787e5-4192-4812-b6fe-17c266bb7abc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fchapter%205.epub?alt=media&token=85605022-830d-4715-9200-fd39efbae7e3"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fclass_10_science_chapter_6_emb.pickle?alt=media&token=175ae258-720a-4558-80bd-9d3c072b3689",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fclass_10_science_chapter_6_text.pickle?alt=media&token=41fa1365-cff0-4044-a162-710eaaa3c115",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fchapter%206.epub?alt=media&token=66662e54-cfd5-4281-bd75-3013a35877fe"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fclass_10_science_chapter_7_emb.pickle?alt=media&token=59ba84e8-6912-4a0e-af39-f410aa31cb42",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fclass_10_science_chapter_7_text.pickle?alt=media&token=a383c684-6ea3-44ad-95ed-39989b70c692",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fchapter%207.epub?alt=media&token=e6283b35-c36e-4c08-8228-5d3712c57848"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fclass_10_science_chapter_8_emb.pickle?alt=media&token=3c48eb58-fd9b-4891-99e9-6e01e3e17a94",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fclass_10_science_chapter_8_text.pickle?alt=media&token=074f5ff3-1a07-4729-baf4-1e1c966dffbf",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fchapter%208.epub?alt=media&token=6bf6bfff-58e9-4ddc-879f-c7678e0e4789"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fclass_10_science_chapter_9_emb.pickle?alt=media&token=5ab6c404-aeca-4f05-9b53-495b17224150",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fclass_10_science_chapter_9_text.pickle?alt=media&token=bdd1c428-9841-4885-9937-cf7a0bdac22a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fchapter%209.epub?alt=media&token=a47526ab-bfd4-4b88-9a83-963d1d480d8b"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fclass_10_science_chapter_10_emb.pickle?alt=media&token=8ce75623-28c3-4db2-ba18-9e20823b24a8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fclass_10_science_chapter_10_text.pickle?alt=media&token=e51f5e77-10f9-4218-b71b-1d106eb1f467",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fchapter%2010.epub?alt=media&token=988a0ab6-5b8f-45a6-ba13-f8d8603cbabb"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fclass_10_science_chapter_11_emb.pickle?alt=media&token=31fcbfe9-bd93-43d1-9a5c-113a0eb52d19",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fclass_10_science_chapter_11_text.pickle?alt=media&token=d06b8cc4-e14a-4707-8740-ee83c4cda8d3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fchapter%2011.epub?alt=media&token=e6cf2759-9cba-46c1-b7ef-4462a9a669d7"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fclass_10_science_chapter_12_emb.pickle?alt=media&token=51e6330e-cb2a-4c17-a437-ed3c0c8acf22",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fclass_10_science_chapter_12_text.pickle?alt=media&token=e7623977-a0c3-4169-8d6e-3c7de6ca1890",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fchapter%2012.epub?alt=media&token=7072bd3e-a992-43ff-8e0d-580045b9aef4"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fclass_10_science_chapter_13_emb.pickle?alt=media&token=2f8093a1-2b99-4088-bc2c-989caa23c6cd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fclass_10_science_chapter_13_text.pickle?alt=media&token=782665ce-b872-46a9-a309-0bba1fe964b9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fchapter%2013.epub?alt=media&token=4808231f-f255-4912-a24c-d52343cef661"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fclass_10_science_chapter_14_emb.pickle?alt=media&token=dd06c239-068f-4062-80ab-a8ad52b0cfa5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fclass_10_science_chapter_14_text.pickle?alt=media&token=d48bc2e7-18db-4f6a-9e8c-6dc8b9ab1b48",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fchapter%2014.epub?alt=media&token=4dfce889-f5ea-4ffe-b1e1-d5c8cb64ef09"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fclass_10_science_chapter_15_emb.pickle?alt=media&token=e6c00313-dea9-47ab-94c1-a4e9fc5fddfd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fclass_10_science_chapter_15_text.pickle?alt=media&token=3d6166c2-722a-44de-a7bb-aa77e4ef3e32",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fchapter%2015.epub?alt=media&token=787d5bb8-ddcb-49bf-a5ab-82af2f1ee14b"}
}

accountancy12ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%201%2Fclass_12_accountancy_part1_chapter_1_emb.pickle?alt=media&token=33a8198d-8ff4-4c69-88a8-51c490739849",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%201%2Fclass_12_accountancy_part1_chapter_1_text.pickle?alt=media&token=2c96a1e8-ad6b-4ccc-ace3-bed16125cc19",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part1%20chapter%201.epub?alt=media&token=1c9b4dfc-5160-4233-b254-70380c660453"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%202%2Fclass_12_accountancy_part1_chapter_2_emb.pickle?alt=media&token=b1b9b5fb-bb4d-40f3-872b-d5e2e7d040d1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%202%2Fclass_12_accountancy_part1_chapter_2_text.pickle?alt=media&token=56e3c45d-9a94-47b0-808c-92857386850c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part1%20chapter%202.epub?alt=media&token=16485061-0cea-47a5-9994-1052e80a7500"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%203%2Fclass_12_accountancy_part1_chapter_3_emb.pickle?alt=media&token=cb614ddf-5d74-4b51-902e-1362c5afad10",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%203%2Fclass_12_accountancy_part1_chapter_3_text.pickle?alt=media&token=cba34da5-fdaf-4e77-ac89-2769a978496f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part1%20chapter%203.epub?alt=media&token=303ae282-4ec6-4e36-9c8e-a505854f222b"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%204%2Fclass_12_accountancy_part1_chapter_4_emb.pickle?alt=media&token=e68bc7c5-0ca8-4233-bb3a-b3dc20dc4df5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%204%2Fclass_12_accountancy_part1_chapter_4_text.pickle?alt=media&token=460e7368-f756-44b6-8cee-77e258c3ede3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part1%20chapter%204.epub?alt=media&token=422eca32-0226-4715-81c5-44e6c6af2015"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%205%2Fclass_12_accountancy_part1_chapter_5_emb.pickle?alt=media&token=831be0c3-ad91-4724-9560-2fd512dce569",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fchapter%205%2Fclass_12_accountancy_part1_chapter_5_text.pickle?alt=media&token=23cb7c14-a79c-4c2a-8a62-7621f4b22391",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%201%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part1%20chapter%205.epub?alt=media&token=0a7c4507-9e08-4171-8f8e-9870fc189443"}
}
accountancy12ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%201%2Fclass_12_accountancy_part2_chapter_1_emb.pickle?alt=media&token=3b150689-2957-4104-aa1a-ee1606383c68",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%201%2Fclass_12_accountancy_part2_chapter_1_text.pickle?alt=media&token=2f1ad03e-05ec-480e-b945-5e72fcee7924",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part2%20chapter%201.epub?alt=media&token=08e28afa-5e2a-4138-a0c4-e31b41e4c7b1"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%202%2Fclass_12_accountancy_part2_chapter_2_emb.pickle?alt=media&token=1f6bd909-0336-4b50-834c-1b13601a26c3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%202%2Fclass_12_accountancy_part2_chapter_2_text.pickle?alt=media&token=d5cbdc2e-e380-42f7-9bed-66c8c51400d9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part2%20chapter%202.epub?alt=media&token=21bdf2d5-6ac5-4c8d-b054-1af0e210344f"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%203%2Fclass_12_accountancy_part2_chapter_3_emb.pickle?alt=media&token=e66a2896-4df4-41df-8830-0af3839ff6e9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%203%2Fclass_12_accountancy_part2_chapter_3_text.pickle?alt=media&token=931cd3e2-dd6d-4599-92b7-8b6c745e0d41",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part2%20chapter%203.epub?alt=media&token=ca8e4d60-55a8-4282-83b9-b229a7d1ea97"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%204%2Fclass_12_accountancy_part2_chapter_4_emb.pickle?alt=media&token=d01d5603-0b08-48fb-867b-7c304c698dad",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%204%2Fclass_12_accountancy_part2_chapter_4_text.pickle?alt=media&token=2eddfb9e-e048-4998-9822-ea2a085830b6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part2%20chapter%204.epub?alt=media&token=e526d516-9d02-4b86-8fef-b8cb30894b5a"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%205%2Fclass_12_accountancy_part2_chapter_5_emb.pickle?alt=media&token=4a35b29f-d79d-4680-bd69-a1a8618a3e53",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%205%2Fclass_12_accountancy_part2_chapter_5_text.pickle?alt=media&token=35615e91-cd75-41f4-bfec-c4940f24ba07",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part2%20chapter%205.epub?alt=media&token=0fa7b306-3cab-4d86-b3ef-9976fcf19037"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%206%2Fclass_12_accountancy_part2_chapter_6_emb.pickle?alt=media&token=cdd78f04-c5e9-4a21-8ce1-5bb9b6918e93",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fchapter%206%2Fclass_12_accountancy_part2_chapter_6_text.pickle?alt=media&token=c323d2e1-588b-4021-a07a-89c931923c2a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%202%2Fall%20chapter's%20epub%2Fclass%2012%20accountancy%20part2%20chapter%206.epub?alt=media&token=f9e73d93-519f-4772-9f8e-f65643234302"}
}
accountancy12ncert01p03 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%201%2Fclass_12_accountancy_part3_chapter_1_emb.pickle?alt=media&token=dd4a18a1-35be-4b32-8a0e-56d20bc1c2f7",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%201%2Fclass_12_accountancy_part3_chapter_1_text.pickle?alt=media&token=8020aa82-394f-49b5-aad3-8fec625e4b55",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2012%20accountancy%20part3%20chapter%201.epub?alt=media&token=6ac4ad53-aaa9-4e70-9d2f-5ad1eb26f692"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%202%2Fclass_12_accountancy_part3_chapter_2_emb.pickle?alt=media&token=e78d22f7-1c17-448e-9421-9128a07a1844",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%202%2Fclass_12_accountancy_part3_chapter_2_text.pickle?alt=media&token=094219f7-965c-409e-a951-b10219c5fd6e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2012%20accountancy%20part3%20chapter%202.epub?alt=media&token=f5cdd8dd-5ce6-4214-bfc2-c296451f7a94"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%203%2Fclass_12_accountancy_part3_chapter_3_emb.pickle?alt=media&token=5fe95b77-f74b-444b-b786-866e9c7b2c8f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%203%2Fclass_12_accountancy_part3_chapter_3_text.pickle?alt=media&token=82bdb911-7aee-4995-aee1-8145ca818fda",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2012%20accountancy%20part3%20chapter%203.epub?alt=media&token=b0139f36-38ee-4fdc-90a5-7f13cb87cbb6"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%204%2Fclass_12_accountancy_part3_chapter_4_emb.pickle?alt=media&token=f329d64d-af1f-4185-9e7a-9e80ebed5e43",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%204%2Fclass_12_accountancy_part3_chapter_4_text.pickle?alt=media&token=32f46488-f2b9-4d6b-9d6f-d8d87ee9c2cd",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2012%20accountancy%20part3%20chapter%204.epub?alt=media&token=40b22923-4f42-45e2-b57c-792f0d6b2633"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%205%2Fclass_12_accountancy_part3_chapter_5_emb.pickle?alt=media&token=ca6b6de9-7a28-460d-aa66-e540de0bce97",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fchapter%205%2Fclass_12_accountancy_part3_chapter_5_text.pickle?alt=media&token=032685f4-a9c4-4295-abd9-a66baf47429a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2FAccountancy%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2012%20accountancy%20part3%20chapter%205.epub?alt=media&token=00067941-cb1e-4ca0-93e3-d48fbee51e06"}
}

biology12ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_1_emb.pickle?alt=media&token=11db0fb4-00b2-4e7b-8476-b1c06cd6696a",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_1_text.pickle?alt=media&token=79a21495-48b4-40b7-bd26-e7e7a439c44b",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%201.epub?alt=media&token=62a4daaf-453d-4608-bcdc-abf36c0a7af9"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_2_emb.pickle?alt=media&token=a888ab4f-7d25-4523-8e4d-2200f9bb743c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_2_text.pickle?alt=media&token=317c9dc2-0830-4dd7-9035-e3435e1894a8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%202.epub?alt=media&token=64c7fbf8-ade4-46c1-ac0a-bf37e712a01c"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_3_emb.pickle?alt=media&token=20f63f85-fc42-439d-87db-5ad7ed6d082b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_3_text.pickle?alt=media&token=522f4c4c-fa29-4b57-b0b9-0b147de8330f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%203.epub?alt=media&token=675a29e2-dddb-4101-9d1e-108d64fe9bcb"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_4_emb.pickle?alt=media&token=62dae308-40cd-4a98-9b45-7df4bfade3ee",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_4_text.pickle?alt=media&token=336d8d24-1df3-4320-9e52-3dc693b6a07b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%204.epub?alt=media&token=ddaf838c-9e4f-4942-b26d-f0d37b196456"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_5_emb.pickle?alt=media&token=205ea906-f7cd-42a6-bb2d-40cfb9b83a0d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_5_text.pickle?alt=media&token=6da572c5-3d08-4a2b-808b-aed57871ae0f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%205.epub?alt=media&token=bc4e0bbd-fc35-4677-baf2-d2b623783858"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_6_emb.pickle?alt=media&token=a9c311ed-0141-4a03-b91a-1f1e5e160227",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_6_text.pickle?alt=media&token=f48c7e84-3fb4-4251-a2d0-528e87093e7f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%206.epub?alt=media&token=61d66090-b3ea-4786-b950-cdc940dd3572"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_7_emb.pickle?alt=media&token=5871b6d2-dfc8-408e-b7a5-93aeaf308225",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_7_text.pickle?alt=media&token=0f0e8d8a-77bf-4db5-8072-77fc52706a71",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%207.epub?alt=media&token=14e27bea-9d11-4239-a252-c05f0aea2647"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_8_emb.pickle?alt=media&token=921d4c26-7f50-48b8-928c-ac4257f9c77f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_8_text.pickle?alt=media&token=42ae9ac6-0cf0-449d-9085-0a32f91e882c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%208.epub?alt=media&token=23108812-1b99-460a-bd3c-dac40c61b05d"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_9_emb.pickle?alt=media&token=023ca0b9-2287-49a5-9a3e-83fe25a20366",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_9_text.pickle?alt=media&token=73ffd41b-e930-4dc6-9ca6-e5368d7084b6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%209.epub?alt=media&token=324989a9-d272-4851-b323-0da6e9683661"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_10_emb.pickle?alt=media&token=98de4255-aa70-484e-9e2f-d26a4c57fe47",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_10_text.pickle?alt=media&token=41483df5-a47a-4f75-87f8-51ff073eb271",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2010.epub?alt=media&token=e70be6da-9403-44cf-aafc-9034bb5d9521"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_11_emb.pickle?alt=media&token=a24aa3d8-d58f-448e-8e54-13a19d87417c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_11_text.pickle?alt=media&token=aa3ed562-c7bf-41b5-b23c-c6ee85bac870",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2011.epub?alt=media&token=3db29fc1-7a12-4a92-8e08-cb2c3367f885"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_12_emb.pickle?alt=media&token=92215099-6ff1-41df-891e-3dd2f1138db8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_12_text.pickle?alt=media&token=2a5d4a5d-eb67-40d2-a5f5-2669a0faa2d6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2012.epub?alt=media&token=76ddde15-1a42-41e9-9365-caa163c5a4bb"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_13_emb.pickle?alt=media&token=48353367-841b-43c3-a37f-7c1fa9d4ef0f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_13_text.pickle?alt=media&token=0ee98fd7-8427-4b57-a666-80727d2551f4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2013.epub?alt=media&token=d59c2134-5506-4aaa-972e-d7a12aef55c6"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_14_emb.pickle?alt=media&token=375ca9e1-0f6b-4a49-883c-f9d2c49a6ea5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_14_text.pickle?alt=media&token=2b990bd2-395f-40ca-9055-4d4a7a3622eb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2014.epub?alt=media&token=cb2edc32-38d3-4ef0-9f0c-4163ae1d4059"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_15_emb.pickle?alt=media&token=15fe0293-980a-4fe6-b200-2e005013334a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_15_text.pickle?alt=media&token=c7af398e-887c-4a71-924d-0a235ddc5f71",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2015.epub?alt=media&token=111eed3d-d371-4220-ad7b-1c032d0c8fc2"},
    "chapter_16": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_16_emb.pickle?alt=media&token=27302471-c63f-4b35-88cf-b42834bacc81",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fclass_12_biology_chapter_16_text.pickle?alt=media&token=146105dc-b867-435a-a0f2-db093b732b2f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbiology%2Fall%20chapter's%20epub%2Fclass%2012%20biology%20chapter%2016.epub?alt=media&token=41755b42-d048-4773-b29e-7f472e12bf9f"}
}

businessStudies12ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_1_emb.pickle?alt=media&token=0f2b17bb-48ce-419c-beb0-7528cf4fb65b",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_1_text.pickle?alt=media&token=9b19ea1f-2b6d-4da2-b16b-fb4dece75e0a",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%201.epub?alt=media&token=facc0430-efee-4c0c-8edc-dec820d11f8e"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_2_emb.pickle?alt=media&token=93b5024b-503c-4dd8-ab3b-9d60a16bc7d2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_2_text.pickle?alt=media&token=e048457c-9642-41f2-a68e-2a13e01aab7e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%202.epub?alt=media&token=3009bf95-b690-466c-9e2e-21443baabc73"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_3_emb.pickle?alt=media&token=aca8b2e4-529f-4f16-9e78-3d2d591e5ff1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_3_text.pickle?alt=media&token=132f4b43-4f8b-40c4-bc83-a29b38b843bb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%203.epub?alt=media&token=6241e730-3eb5-48e5-935b-ea8692076484"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_4_emb.pickle?alt=media&token=fecf1114-c549-48c5-ad73-bad4a2d72bb6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_4_text.pickle?alt=media&token=cf5fd8c5-c97c-43b4-801b-8c5595caaca0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%204.epub?alt=media&token=b23cabc6-6152-4154-bdec-df779fb35b26"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_5_emb.pickle?alt=media&token=a33ff3b5-9050-4ba8-9be9-779068bb7357",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_5_text.pickle?alt=media&token=f912e35c-1b6d-468d-b260-de3558e373cd",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%205.epub?alt=media&token=f5331ed3-55dd-4d22-94c4-454920bdacc1"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_6_emb.pickle?alt=media&token=b78d1744-4768-4803-8160-fa317f9b40f1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_6_text.pickle?alt=media&token=5fbfa0c9-c4fe-4004-8a32-085adf835ba0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%206.epub?alt=media&token=723c61f3-337e-4bdc-a4d0-6079bdc8bf74"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_7_emb.pickle?alt=media&token=eaf809a6-f987-4922-b79a-3d5ccd9eb45b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_7_text.pickle?alt=media&token=e8ea3e9d-a31b-4a45-ad77-2798f8fc1c39",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%207.epub?alt=media&token=869bfff2-dc7d-44b0-ae78-852fab09c062"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_8_emb.pickle?alt=media&token=2586e536-f7f0-48d9-a6e2-66bc936506c7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fclass_12_buiseness_studies_part1_chapter_8_text.pickle?alt=media&token=5b965dd4-1237-498d-9149-aab61f4747d2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2012%20buiseness_studies%20part1%20chapter%208.epub?alt=media&token=19f90df3-7e13-44bf-90a4-3f2581a34b69"}
}
businessStudies12ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_1_emb.pickle?alt=media&token=0a795a3a-123b-4629-9f54-1f8a5c2297ad",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_1_text.pickle?alt=media&token=a159d00d-ccab-4275-a83a-26aa4cb11a5c",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass%2012%20buiseness_studies%20part2%20chapter%201.epub?alt=media&token=e5cd4a8f-99ca-471b-a9cc-7d170ed427d1"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_2_emb.pickle?alt=media&token=81833bab-9bad-4328-8872-9c8a13750f5e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_2_text.pickle?alt=media&token=9092cfc6-1b4c-4d42-8f6a-26c481361224",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass%2012%20buiseness_studies%20part2%20chapter%202.epub?alt=media&token=04048c71-2c4a-469d-91be-43818ab576e4"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_3_emb.pickle?alt=media&token=4e9d26a9-9d1c-40fa-9a27-55c94a1710bc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_3_text.pickle?alt=media&token=b6d1662c-e96e-4038-9480-2105ba5234c2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass%2012%20buiseness_studies%20part2%20chapter%203.epub?alt=media&token=785d72ec-2b07-40d3-b7d5-a10b6376cc4f"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_4_emb.pickle?alt=media&token=878b8247-3e2d-43a9-93c9-e0578b01a407",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass_12_buiseness_studies_part2_chapter_4_text.pickle?alt=media&token=6a8bacb2-6caf-4876-8572-d0023290fdff",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fbusiness%20Studies%2Fpart%202%2Fclass%2012%20buiseness_studies%20part2%20chapter%204.epub?alt=media&token=7ea587f7-ccd7-4e72-b349-890c3c1185e7"}
}

chemistry12ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_1_emb.pickle?alt=media&token=404802dd-f9ee-4f5f-bd15-6116d1b0a414",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_1_text.pickle?alt=media&token=b7253ea0-2557-460c-8d00-7c9b39bac778",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%201.epub?alt=media&token=f7621dcf-c2e7-4419-b8dd-7bd405670b4c"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_2_emb.pickle?alt=media&token=373647df-a4d2-4c89-a674-a9902da3b80e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_2_text.pickle?alt=media&token=a0563941-53be-4f87-9397-29a5b9085ac7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%202.epub?alt=media&token=2392290e-4dfd-457d-944f-18446ccabdbf"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_3_emb.pickle?alt=media&token=f5ed2607-5fdb-4b1d-92da-43c9ba5ec3aa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_3_text.pickle?alt=media&token=1943e7e4-70e9-4751-b348-ada8fa51c5d4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%203.epub?alt=media&token=928074eb-0855-4ec4-808c-02ecd8ac0965"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_4_emb.pickle?alt=media&token=204be93d-d054-41f8-9af5-52b1392b54ef",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_4_text.pickle?alt=media&token=0e3d7fea-5ee5-4bbb-8728-42568d4f1e38",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%204.epub?alt=media&token=5aa53388-a4f4-4df1-be93-2fa7fa239bec"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_5_emb.pickle?alt=media&token=44df716c-2eb7-40d2-892a-ce5067e0bfa5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_5_text.pickle?alt=media&token=e3d2a51d-77fd-422f-b59a-bf5f5753043b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%205.epub?alt=media&token=118ca7d0-11ac-4706-ba6d-283181896038"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_6_emb.pickle?alt=media&token=3d168585-b618-49f8-a990-8b21ee3a5ef2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_6_text.pickle?alt=media&token=f8695f95-25c3-4e9d-96ac-829349e918bb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%206.epub?alt=media&token=3e6e4af7-cfe6-4fac-8c41-c6f106f3b787"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_7_emb.pickle?alt=media&token=1562f4a1-5206-4438-993c-cf8a1eff0bde",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_7_text.pickle?alt=media&token=7576cd70-b516-4f1a-9a2a-5eaa47edd29a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%207.epub?alt=media&token=d449c908-bc01-4f06-ad85-cd849e8ef42a"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_8_emb.pickle?alt=media&token=65ff6758-14e2-44e2-ab98-b4b0aaaf7898",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_8_text.pickle?alt=media&token=7adea3eb-e8d1-4f4c-871c-c92885c862d4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%208.epub?alt=media&token=87988387-af90-413e-8b34-f02a2553a59d"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_9_emb.pickle?alt=media&token=0829bfbd-6c5f-4bfd-97b7-f971e42f1850",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass_12_chemistry_part1_chapter_9_text.pickle?alt=media&token=2ef3e1f7-d52b-4bb4-8e35-63fad18457af",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%201%2Fclass%2012%20chemistry%20part%201%20chapter%209.epub?alt=media&token=2aed0c27-9012-4da6-b2fa-7fd83d93b9e6"}
}
chemistry12ncert01p02 = {"chapter_10": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_10_emb.pickle?alt=media&token=33af1952-1cf4-406b-ac47-284fba50a729",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_10_text.pickle?alt=media&token=da58b08b-7c86-4466-baec-8dd8ff65fa4c",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2010.epub?alt=media&token=25e7a888-6920-433a-80f6-2d00d99f8388"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_11_emb.pickle?alt=media&token=5f87bd24-4632-4c06-9d06-cfc0e0dd085e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_11_text.pickle?alt=media&token=b1ba7bed-bda6-45c3-aabb-5e9b74c21aa3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2011.epub?alt=media&token=fd285f39-db0c-4ef0-8b85-96a6e400ad7c"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_12_emb.pickle?alt=media&token=647c78da-e6a5-44a8-a8b0-cbd3fe2799b8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_12_text.pickle?alt=media&token=75b59a63-5096-4339-aabb-228a4ce444dd",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2012.epub?alt=media&token=a266a917-49cb-4296-9950-a7a8e5ab25f0"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_13_emb.pickle?alt=media&token=8cb918a8-347d-433b-9bcc-3886878f0cae",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_13_text.pickle?alt=media&token=3bb257de-4ed9-4ea6-b950-5f4c47f7b3ba",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2013.epub?alt=media&token=636c272d-381e-49b2-81b8-0ed9070f0688"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_14_emb.pickle?alt=media&token=3ef0ae5f-a4ea-44b9-9fc4-c304aec3eb78",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_14_text.pickle?alt=media&token=1fa77dff-992a-4a50-9136-4713dd1ad8a1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2014.epub?alt=media&token=7f1cfccb-3079-4618-8bb0-30cf38a5db8c"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_15_emb.pickle?alt=media&token=a2cd3833-68ba-4c62-9ab3-f7b28b2a4678",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_15_text.pickle?alt=media&token=e349ea9a-5f32-44eb-817d-97d918dfb2e1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2015.epub?alt=media&token=13c5af88-d5ec-4ff3-ae2c-4d75f2aad529"},
    "chapter_16": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_16_emb.pickle?alt=media&token=9959390f-64d0-4e2b-acb9-fc33e8872987",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass_12_chemistry_part2_chapter_16_text.pickle?alt=media&token=568be2e0-0252-4662-9c7a-350b622e44b9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fchemistry%2Fpart%202%2Fclass%2012%20chemistry%20part%202%20chapter%2016.epub?alt=media&token=3b132c81-55cd-4ad1-aed6-2281228ab2e1"}
}

mathematics12ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_1_emb.pickle?alt=media&token=cb2e6485-ab90-44ea-9006-a987e6421977",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_1_text.pickle?alt=media&token=ff99a8cb-a64c-463a-85c2-eb8a4f24e1f6",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%201.epub?alt=media&token=45910daf-6f8a-46a5-8e4c-a661cd85ae21"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_2_emb.pickle?alt=media&token=3a922a96-bb25-4834-9746-c9a6f17ecd56",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_2_text.pickle?alt=media&token=cbd4f672-543a-43eb-b473-09d391ad290d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%202.epub?alt=media&token=c5c0dd42-a4ef-44db-abe0-1de05b1c00fc"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_3_emb.pickle?alt=media&token=2e065594-6e38-4383-ad21-a7d4c52266e8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_3_text.pickle?alt=media&token=57629d03-7cc7-45e5-9ea4-47d56942c74c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%203.epub?alt=media&token=df01a79e-3405-4c2c-83d1-b2bbe0ed03f0"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_4_emb.pickle?alt=media&token=ce20afa3-b598-4946-b557-1a85486eba2d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_4_text.pickle?alt=media&token=2bed8930-1298-4fa2-82b0-013f3e0de839",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%204.epub?alt=media&token=8e2e6622-5722-4dd0-ad33-f4ed87b35bcc"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_5_emb.pickle?alt=media&token=e64112c4-c1c0-45c1-8a37-c825782131ac",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_5_text.pickle?alt=media&token=dc84f1d9-209a-4fc5-970d-03e332e7ea6b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%205.epub?alt=media&token=e964c953-2959-46a8-9625-649c2f7111bd"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_6_emb.pickle?alt=media&token=9f7ac22d-01cf-402b-aad3-94338239eae2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_6_text.pickle?alt=media&token=7d24062e-0fcc-46fc-aa88-5e7b3e1e83a7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%206.epub?alt=media&token=73d564e4-7c7d-4e65-931e-7c60f03dd06b"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_7_emb.pickle?alt=media&token=a399bfff-91b5-46bb-a584-b3c392de21c6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_7_text.pickle?alt=media&token=6ac607b5-2489-444b-92ee-84e96eebf157",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%207.epub?alt=media&token=5293370f-4bd2-4fe1-b8a3-79e657ddc570"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_8_emb.pickle?alt=media&token=0e217c5a-92b2-4910-ad04-cfe693794aae",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_8_text.pickle?alt=media&token=34e7b095-ac41-490b-affd-a590c626b1f6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%208.epub?alt=media&token=081cf18a-0fa3-4190-93d0-73b67f9152e6"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_9_emb.pickle?alt=media&token=4f2c47ac-8725-40e7-8b5d-35a5a769fc2f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_9_text.pickle?alt=media&token=40079326-d3cb-4b9c-9b3f-37c12fd0d17e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%209.epub?alt=media&token=c7ad8ed2-00db-4e3c-8249-c61b9207c485"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_10_emb.pickle?alt=media&token=ab5a5e2c-9b01-492a-b811-08b7ca48d67e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_10_text.pickle?alt=media&token=6ee398c3-ae78-41ae-9c30-3b4d755edf2e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%2010.epub?alt=media&token=525714cb-3ed3-48df-8823-6a3079f2f5cd"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_12_emb.pickle?alt=media&token=f9382139-9ea3-4b3d-86a0-80074063538b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_12_text.pickle?alt=media&token=cde85b63-2ada-440d-ac41-1b718ea7079d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%2012.epub?alt=media&token=05a5ddf9-84a8-4171-9a25-ea0f17c5a027"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_13_emb.pickle?alt=media&token=8a9aa9e7-b2c1-41cf-a972-afb78b98c88e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass_12_math_chapter_13_text.pickle?alt=media&token=941a8452-9363-4da6-b8f0-e3374e5ab0fa",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fmathematics%2Fclass%2012%20math%20chapter%2013.epub?alt=media&token=608ed470-9f82-4703-b783-d0db88b635a3"}
}

physics12ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_1_emb.pickle?alt=media&token=59ac620d-a558-487e-8714-e0b2c40a9830",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_1_text.pickle?alt=media&token=2b573cfb-ce6c-4f64-985b-5e0b7d4fea02",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%201.epub?alt=media&token=8ac82e7a-953b-4981-b470-ff25569317fb"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_2_emb.pickle?alt=media&token=14c02949-ace9-4e34-9d30-0c9b0e5eba02",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_2_text.pickle?alt=media&token=00c906d7-71a4-4434-bdf1-9e4b21b64b3f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%202.epub?alt=media&token=eabc3496-0d87-4525-97e0-c263a77bd5cf"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_3_emb.pickle?alt=media&token=9670f9b9-7e04-4e23-afd1-c4ca4ef38212",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_3_text.pickle?alt=media&token=8222a84f-a698-4971-b074-3aa6f498036d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%203.epub?alt=media&token=5a7b6b12-586e-4e4b-9444-818706e73798"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_4_emb.pickle?alt=media&token=58839d9b-df7d-4d93-b0b3-f09ae4b2c2f5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_4_text.pickle?alt=media&token=e589edd6-4a99-4909-aa0b-e78b68edae5a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%204.epub?alt=media&token=b1d3628b-54a1-4e63-aa58-3a0f4a4a138d"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_5_emb.pickle?alt=media&token=3c20f14a-f75d-40ca-900f-2d8c18896645",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_5_text.pickle?alt=media&token=c9fee14f-bf25-4149-b4b1-83534179dbdb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%205.epub?alt=media&token=fa4b515b-6014-4b9c-bc81-b029228b18a0"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_6_emb.pickle?alt=media&token=7f1e6cb8-17d9-42d6-b5bd-0f89debf4f01",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_6_text.pickle?alt=media&token=84948f37-f0f5-4f52-963a-20bee2c14597",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%206.epub?alt=media&token=f38737ce-4a32-437c-8413-ce63aeab75df"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_7_emb.pickle?alt=media&token=b9f56263-e7d5-4be2-8006-3f25586a6214",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_7_text.pickle?alt=media&token=0b4ed85e-c243-4d10-ae6c-e1df502d6f9a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%207.epub?alt=media&token=f4cad85f-2421-42b6-b807-e6fa43d1a6e4"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_8_emb.pickle?alt=media&token=2d3fdf83-829c-43a3-bb0e-3bddbe337be6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_8_text.pickle?alt=media&token=a3e8530c-2dd8-498b-a5a3-943ca548312a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%208.epub?alt=media&token=d38bd047-87f8-495b-905c-f4f7224dd21e"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_9_emb.pickle?alt=media&token=99be27a4-60c9-46f9-89a5-7ce04e637124",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_9_text.pickle?alt=media&token=2bed4800-a230-453a-9b1f-ca995e340cb4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%209.epub?alt=media&token=b401a5a3-a8f4-4b69-ade1-f615b09cf226"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_10_emb.pickle?alt=media&token=daa8f1a7-275b-45a9-8cb9-feb0df58c7e6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_10_text.pickle?alt=media&token=8a6e8940-98dc-4183-9533-0f5ee620bcd3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%2010.epub?alt=media&token=db379007-38bd-4b2c-9e98-690d3dba5588"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_11_emb.pickle?alt=media&token=e6edb35f-09f7-46a2-8a1c-3540fc9f873b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_11_text.pickle?alt=media&token=5f5a14e9-057f-4d10-a6c3-9c32eca4d159",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%2011.epub?alt=media&token=97ceafdd-8604-48c9-9931-6d2f479f69dd"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_12_emb.pickle?alt=media&token=fcab9c48-a9d2-41ce-8452-7bac0a6eac1e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_12_text.pickle?alt=media&token=9d442c65-181d-4761-b375-36293563532f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%2012.epub?alt=media&token=eac724b0-f2c0-484c-9abf-73be9e16d065"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_13_emb.pickle?alt=media&token=c39fa439-7607-40dc-ac5b-765357d774a1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_13_text.pickle?alt=media&token=439686bb-3f61-4a1b-9182-b2488d004210",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%2013.epub?alt=media&token=fb002413-36c8-43cb-b11d-d88ed6c64bc2"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_14_emb.pickle?alt=media&token=1d83019f-d316-4ee1-809d-37dc334d154c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass_12_physics_chapter_14_text.pickle?alt=media&token=d7651b0c-7163-47e9-a806-985981a733e2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fphysics%2Fclass%2012%20physics%20chapter%2014.epub?alt=media&token=25b93ef9-a221-44d1-8efb-042193985a9f"}
}

economics12ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_1_emb.pickle?alt=media&token=5cefd3d6-a586-4b7f-b2e6-f5401d8260eb",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_1_text.pickle?alt=media&token=81a379a0-c07b-4733-9421-f8e230318432",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20chapter%201.epub?alt=media&token=5dc16044-71e7-4d57-89ef-a3fa2b162836"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_2_emb.pickle?alt=media&token=38410636-f4ba-4b0e-a7d9-e5dd75aa54ed",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_2_text.pickle?alt=media&token=869cef27-de23-4265-bb85-1813c08c6da9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20chapter%202.epub?alt=media&token=daaa4d94-9da4-4872-a2f1-b04ef5ff95da"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_3_emb.pickle?alt=media&token=a1baac16-0b06-4fb4-bacb-67d5132adce8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_3_text.pickle?alt=media&token=ec46680f-8ec7-4b50-bc29-ce100afe8244",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20chapter%203.epub?alt=media&token=0a24eb51-35fc-4d4c-8114-6f80694c25c3"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_4_emb.pickle?alt=media&token=d6613f18-730b-4866-9c8a-2e70eb0b3fdc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_4_text.pickle?alt=media&token=247c0d4e-d85b-46e4-8aa0-6932ae153a18",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20chapter%204.epub?alt=media&token=fbc690ce-2407-4778-894e-0d15150d1f8e"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_5_emb.pickle?alt=media&token=74c1617a-0a38-4a02-8939-893c05b734d4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_5_text.pickle?alt=media&token=ede53876-3380-45b4-89e1-3f4b45f241cd",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20chapter%205.epub?alt=media&token=6ba665ee-48b1-43e8-aa33-8c1bf8a6a190"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_6_emb.pickle?alt=media&token=2c041593-6ad4-4eb2-acb4-dfbbf6f580d9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_6_text.pickle?alt=media&token=484ca8e6-cf94-4d60-93e4-3bee20dafcfb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20chapter%206.epub?alt=media&token=1a3be135-922b-40ac-86fd-6597aadd794c"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_7_emb.pickle?alt=media&token=39f2619b-9de2-4dea-8e93-9cbc61b85526",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_7_text.pickle?alt=media&token=6ea8f90e-1b86-4a52-b4e5-8091dbc7eb6e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20part%202%20chapter%201.epub?alt=media&token=5df1b5cc-5e81-4adc-a961-7959e75f1db3"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_8_emb.pickle?alt=media&token=6ce07cd2-da10-452c-9eac-f8cc956e2e2a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_8_text.pickle?alt=media&token=faf6a816-f257-49f5-b21e-0e5ea850564c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20part%202%20chapter%202%20.epub?alt=media&token=69f28759-8457-412c-8426-3faf3f44987b"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_9_emb.pickle?alt=media&token=04edbab3-c948-441b-940c-cba9b9331780",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_9_text.pickle?alt=media&token=f273b1a8-a253-4749-a955-d423ff6c6d6d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20part%202%20chapter%203.epub?alt=media&token=65ee1b5b-92eb-4087-b842-157b741185e0"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_10_emb.pickle?alt=media&token=800682ab-6e64-48e3-92af-aaf85bf7f050",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_10_text.pickle?alt=media&token=84e08449-a91d-4ce7-b99a-bccb2ffe1dcf",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20part%202%20chapter%204.epub?alt=media&token=bb77a6c8-a067-492c-aae4-f9267b7a1990"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_11_emb.pickle?alt=media&token=23888113-2d7e-47cc-acf6-0d1dedf4b055",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_11_text.pickle?alt=media&token=2c852d7f-ce37-4d4f-a30c-c5e82a93ddd4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20part%202%20chapter%205.epub?alt=media&token=9ffafe22-eae3-4005-b19c-502db9480acb"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_12_emb.pickle?alt=media&token=bb0091ac-e65d-4126-b14c-3cc72b3a44bd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass_12_economics_chapter_12_text.pickle?alt=media&token=81f14868-9e4a-4c20-a1a2-330c9f9b2320",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Feconomics%2Fclass%2012%20economics%20part%202%20chapter%206.epub?alt=media&token=2b25cd25-575d-49ec-8d1e-7e87094def90"}
}

geography12ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_1_emb.pickle?alt=media&token=fc1982bf-5213-43ba-8758-555f1347f31f",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_1_text.pickle?alt=media&token=4d7bf6d1-fc8d-44f3-8027-08b955df918b",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%201.epub?alt=media&token=2671d1d6-99ab-4bf7-88a0-25674208bfed"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_2_emb.pickle?alt=media&token=f18286f0-0981-474c-be4a-5b2e96581ac2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_2_text.pickle?alt=media&token=bc67e86a-b1bf-4bac-8728-8847d3fb8e31",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%202.epub?alt=media&token=45962f02-d842-4e27-969f-f7429e069807"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_3_emb.pickle?alt=media&token=721a084c-c0f9-4728-a8c7-b5c8f00030e8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_3_text.pickle?alt=media&token=224cb54a-d707-4ba1-93dc-0bee1ce9fa90",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%203.epub?alt=media&token=1a43e142-3f81-4455-933a-d36b3855ff57"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_4_emb.pickle?alt=media&token=dccec029-a2ec-42c7-8aff-8a05689be70b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_4_text.pickle?alt=media&token=12a01217-8651-4b84-9446-bcc9b545ce90",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%204.epub?alt=media&token=eb902a8a-c71d-4286-be5d-5b3179a496e9"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_5_emb.pickle?alt=media&token=3b2621e6-ff05-435b-9073-dde40428f0c3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_5_text.pickle?alt=media&token=8cc61488-eb59-4a5b-815c-5aad3cfb18dd",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%205.epub?alt=media&token=ec913f8d-30da-48f3-b77c-fe2622de50f4"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_6_emb.pickle?alt=media&token=5b2ef4c1-be36-4507-a475-e08e22cdf456",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_6_text.pickle?alt=media&token=a2ea263f-989d-476c-a558-1ab6c74e461a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%206.epub?alt=media&token=b4888189-8b5d-4faa-978c-b724e314c465"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_7_emb.pickle?alt=media&token=99e95535-3dfa-4615-877d-07635b08100e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_7_text.pickle?alt=media&token=7b76d85a-e8ee-4fb6-bec1-989615b15448",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%207.epub?alt=media&token=38d8fa55-35cd-4308-9426-75da8826a8b4"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_8_emb.pickle?alt=media&token=959e7ee1-0ae9-48c7-ac7f-066795c7064f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_8_text.pickle?alt=media&token=311fd4ef-8ac4-41ed-b3d5-d52de587d156",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%208.epub?alt=media&token=3eaeedb0-1052-42ea-8cad-197818221b32"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_9_emb.pickle?alt=media&token=8b2ef570-7580-4ef9-8bb9-0bb66d32d1ff",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_9_text.pickle?alt=media&token=bae52608-55ee-4a1b-890a-cce5dbec3f6e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%209.epub?alt=media&token=71490478-8cf0-400a-ac49-4120c9926e74"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_10_emb.pickle?alt=media&token=bc1305f5-f297-4885-9598-2cf0ebec6159",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_12_geography_chapter_10_text.pickle?alt=media&token=33d70061-32c0-4c30-b1ef-72c25675b2a3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass%2012%20geography%20chapter%2010.epub?alt=media&token=1ec83faf-cbb9-4e0b-8250-89e823d9aaef"}
}
geography12ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_1_emb.pickle?alt=media&token=664a9158-2df9-49c9-861a-2274b3f4f521",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_1_text.pickle?alt=media&token=cafb2c96-7459-4082-92a3-a41dc873d02f",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%201.epub?alt=media&token=e0eb66da-394e-4a5e-a670-620ac12d50a2"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_2_emb.pickle?alt=media&token=464a9861-6384-42c2-bd5b-3fab01334aeb",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_2_text.pickle?alt=media&token=7a69426b-d220-4811-82ef-e0bee15a4ca6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%202.epub?alt=media&token=bf6be3f4-f3e2-4e83-b87e-6cce59e63b9e"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_3_emb.pickle?alt=media&token=e16a8e3c-2b68-43cb-95c5-f91939eb4ffe",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_3_text.pickle?alt=media&token=54e33240-1158-4ac2-a99e-145f839cd139",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%203.epub?alt=media&token=26fbde23-3be8-4622-874a-b6905bf2e03b"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_4_emb.pickle?alt=media&token=c9d197f0-115d-4a07-8328-2ee62e6a1750",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_4_text.pickle?alt=media&token=e8ab4b0c-ad7e-4020-a1f7-79579a21b82d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%204.epub?alt=media&token=fd3de680-85a1-4892-8827-ddf62fbab9c8"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_5_emb.pickle?alt=media&token=27fde660-25be-4096-a635-95931450c0a5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_5_text.pickle?alt=media&token=83307e90-80c9-4bc6-ad1f-9760eb0a5d8d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%205.epub?alt=media&token=a0b0488e-1793-4a98-a317-7c18b99aa226"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_6_emb.pickle?alt=media&token=dff31045-1ad8-4ecf-93b2-b635dbe99736",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_6_text.pickle?alt=media&token=f1ed9e66-801c-4ba3-a93f-bf9941d91af0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%206.epub?alt=media&token=21243bcc-a9b7-47aa-aff7-6b017dab6525"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_7_emb.pickle?alt=media&token=c0cc0f38-8593-4277-8f8f-b7d92459b8be",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_7_text.pickle?alt=media&token=bb2bdb7e-0146-49fb-a675-77803a17aed2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%207.epub?alt=media&token=1fccfdf6-3805-46b8-aa43-1575edc24a86"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_8_emb.pickle?alt=media&token=7050eb29-65c3-47d4-b824-edc5bbbb256f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_8_text.pickle?alt=media&token=7c5544c8-c7e6-4ccd-90e3-b21bbee1b2da",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%208.epub?alt=media&token=cdba7636-38ab-41a7-9746-01f35cf56002"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_9_emb.pickle?alt=media&token=3b6a863f-c9da-4187-8e3f-c48776f78448",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_9_text.pickle?alt=media&token=dc0e66b3-69ab-434d-b506-aeffcbec5e5d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%209.epub?alt=media&token=37bc557f-3d19-4026-8d17-60fed819f558"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_10_emb.pickle?alt=media&token=63be685c-d847-43d4-8b3f-2df2165efb07",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_10_text.pickle?alt=media&token=f4d2ba18-aac1-4a2c-b68f-5eaf95459b25",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%2010.epub?alt=media&token=c543d912-0004-432c-a168-8c9368fe7165"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_11_emb.pickle?alt=media&token=9a7754da-1177-4a35-a77e-af6476889b40",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_11_text.pickle?alt=media&token=eee86db5-92a9-49a5-84b4-4dcb0bf7f6ea",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%2011.epub?alt=media&token=20354652-08ad-4308-bc2e-24025ae117f6"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_12_emb.pickle?alt=media&token=4a6d9413-efed-44c7-b661-3233a3fd8e16",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_12_geography_part2_chapter_12_text.pickle?alt=media&token=077ea5a5-355b-4f11-93db-630b1f4bbeb7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2012%20geography%20part2%20chapter%2012.epub?alt=media&token=95b97022-ab59-49cc-b62d-ad7e3ab0e6f7"}
}
geography12ncert01p03 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_1_emb.pickle?alt=media&token=42f088dc-cdad-4324-9594-f33d57b3a8be",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_1_text.pickle?alt=media&token=e94983d9-4480-4053-a23d-376efb5727d1",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass%2012%20geography%20part3%20chapter%201.epub?alt=media&token=1e73c8db-beb7-455b-a861-b5a7a42b931b"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_2_emb.pickle?alt=media&token=ad33237c-c572-489f-ad40-688cb281cbf9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_2_text.pickle?alt=media&token=ba3841d2-c2a3-49d7-90d7-16974d95ef8c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass%2012%20geography%20part3%20chapter%202.epub?alt=media&token=0cf0e11a-ba64-43b7-837b-bd4b98da3506"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_3_emb.pickle?alt=media&token=99236f8b-7417-4ccc-a468-3a7caaba18a6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_3_text.pickle?alt=media&token=522805bc-ec3d-4717-a8d8-bc66457e7988",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass%2012%20geography%20part3%20chapter%203.epub?alt=media&token=7d344253-184c-4007-802d-98b1948767ac"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_4_emb.pickle?alt=media&token=259069b1-f76e-44c5-866a-1e3c17af42b7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_4_text.pickle?alt=media&token=23dbc65c-91fc-4cc2-8a3d-907634d2aabf",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass%2012%20geography%20part3%20chapter%204.epub?alt=media&token=a48ec489-2e93-4114-a50e-2b9427b8999d"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_5_emb.pickle?alt=media&token=1f1fd026-e0e0-4519-8e3b-5dcf0cd70171",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_5_text.pickle?alt=media&token=cfa458e7-4b29-43b0-8158-d0336b28acd3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass%2012%20geography%20part3%20chapter%205.epub?alt=media&token=985ed0c2-43c9-4713-987c-f32901e3f3f5"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_6_emb.pickle?alt=media&token=4c6c7b08-b2ed-4243-b618-ecc0922ea52b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_12_geography_part3_chapter_6_text.pickle?alt=media&token=6fef8e9d-cac3-4766-9d93-0185062402ad",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass%2012%20geography%20part3%20chapter%206.epub?alt=media&token=f6638f48-b735-41ce-a53b-0e6a2b8301e6"}
}

history12ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_1_emb.pickle?alt=media&token=5c873f8c-cbf0-43c9-aa44-da90d95fb17b",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_1_text.pickle?alt=media&token=6c8b29ac-674d-4d22-95d3-4212202ed943",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%201.epub?alt=media&token=2ea5151b-5d90-4f7b-8a67-a49a480a5452"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_2_emb.pickle?alt=media&token=d90103e6-9e4b-484b-9772-883985f0800a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_2_text.pickle?alt=media&token=10ef3a37-1a8e-40a3-b588-6bba58ef5efa",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%202.epub?alt=media&token=c9201b00-9907-491a-a46c-fcae09ed790b"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_3_emb.pickle?alt=media&token=c10d7dc6-1ea6-4aa1-a3c5-b66bd646ae76",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_3_text.pickle?alt=media&token=7d92a47f-b422-4b9d-a216-f12ba83fb69e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%203.epub?alt=media&token=035ec907-0a38-47d0-8986-15a4b2ac6ba2"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_4_emb.pickle?alt=media&token=c99205be-7d67-4487-b5e1-89abe8c72803",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_4_text.pickle?alt=media&token=e2e43ae3-0e63-4558-bddd-0a3ae1e7c5c9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%204.epub?alt=media&token=e9259fae-6f1f-46ae-a85a-58b070159b6a"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_5_emb.pickle?alt=media&token=af9cff94-7848-498d-afde-c8bba202990f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_5_text.pickle?alt=media&token=263029e2-24cf-494d-b87b-d3df18918e75",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%205.epub?alt=media&token=a4c78de3-90d3-4218-bc1b-561d0d885216"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_6_emb.pickle?alt=media&token=7ecc7c0e-62e2-4b9b-99bd-82338094901b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_6_text.pickle?alt=media&token=1903bad8-c1c3-43e8-8bf8-4a6e5eb2b93a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%206.epub?alt=media&token=41de8fe4-45d0-42a7-afc1-4fcad3561764"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_7_emb.pickle?alt=media&token=e73a929c-a27d-4eac-8938-7a62a7bc8740",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_7_text.pickle?alt=media&token=c9a74e98-cac2-4d1a-bf46-63fb9adc2695",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%207.epub?alt=media&token=697213ef-b288-44e8-a169-d751a4ecba30"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_8_emb.pickle?alt=media&token=d55b85bf-2db1-465f-96d9-6bab234a6f68",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_8_text.pickle?alt=media&token=2d6a2b3d-b90c-42ea-80ee-0481f16a66d3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%208.epub?alt=media&token=cfd2703a-5cf9-423a-b4d4-26e0c2e551f1"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_9_emb.pickle?alt=media&token=a8e602dc-014a-4d6f-9279-2b5682593e99",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_9_text.pickle?alt=media&token=3c78ec9e-1b1a-4294-99e9-1809a39a85d7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%209.epub?alt=media&token=2bd5ce69-3db3-4161-93bf-7847f0274af5"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_10_emb.pickle?alt=media&token=54d4be8f-1b5a-4e25-a68e-1dbe2633f31d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_10_text.pickle?alt=media&token=484fb955-4214-44c6-b713-05192e8d47f6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%2010.epub?alt=media&token=8eef752e-4ed1-45b6-8881-c9236f05987f"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_11_emb.pickle?alt=media&token=d5768af1-550b-436e-b9bb-e22a699e0722",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_11_text.pickle?alt=media&token=01af8743-2d0a-4a34-969a-c89df27d422f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%2011.epub?alt=media&token=ca93dd4d-b227-43db-9e33-1690e43523a4"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_12_emb.pickle?alt=media&token=5a34da8f-3cc0-4562-9d58-9d11acd7cac5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_12_text.pickle?alt=media&token=7b11e802-44b1-4d7c-827e-323ffeb098f2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%2012.epub?alt=media&token=01cd007e-a178-42fd-9b72-3e18d214ef3c"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_13_emb.pickle?alt=media&token=88d6c82e-02b6-4349-adfa-e3e9b73063f0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_13_text.pickle?alt=media&token=3810bd97-0fe4-4e1b-a2cc-1500aea7e3a9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%2013.epub?alt=media&token=a4feb7b1-e632-4a89-b925-41a01eb6e9b7"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_14_emb.pickle?alt=media&token=91ca69f2-63ef-49fb-8647-522202f99362",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_14_text.pickle?alt=media&token=afcbdb28-7ec7-476f-9fa1-0b0360de8a6d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%2014.epub?alt=media&token=06a7ab60-3b34-4546-9dad-a2c8492d3c17"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_15_emb.pickle?alt=media&token=d4653bc5-5890-45ea-a6cb-6a84bc83183b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass_12_history_chapter_15_text.pickle?alt=media&token=cf2fc2eb-224a-4889-a6e7-16096f697086",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fhistory%2Fclass%2012%20history%20chapter%2015.epub?alt=media&token=5d082039-ce57-4faf-b214-6a97cf52aace"}
}

civics12ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_1_emb.pickle?alt=media&token=1120b3ae-3e0b-4808-b130-76dbfe56aee9",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_1_text.pickle?alt=media&token=9fc93b1d-1090-4b8f-a816-1a70e690a9fe",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%201.epub?alt=media&token=330cf59c-43cf-4f66-a2a2-7cf7d0edac03"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_2_emb.pickle?alt=media&token=6983cff9-2647-4ccd-b114-967cafea0470",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_2_text.pickle?alt=media&token=66ee2e6c-5e09-4387-986b-80250487e259",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%202.epub?alt=media&token=e1ffabd6-e521-4b77-80ab-3fc3c86a65c4"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_3_emb.pickle?alt=media&token=785ddce1-d732-4936-a517-b3ffa63c5f57",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_3_text.pickle?alt=media&token=7115f011-ec9a-46b7-9f9b-838a4050805d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%203.epub?alt=media&token=786310d4-5e81-413b-97b7-931a66cb7938"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_4_emb.pickle?alt=media&token=c4d690bc-db52-40b1-bcc9-5f01fdb25492",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_4_text.pickle?alt=media&token=02929712-b477-4726-bce5-915a3f710bbc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%204.epub?alt=media&token=1a43d12d-c429-43c0-8046-fd313c7a4ebd"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_5_emb.pickle?alt=media&token=99f93cd2-0516-4e02-a017-f579e87a17e3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_5_text.pickle?alt=media&token=d1f8df1e-a04d-4bac-b7c0-77394f3467aa",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%205.epub?alt=media&token=5cd5ef0e-139c-49a6-81f0-a23eca3a2581"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_6_emb.pickle?alt=media&token=d092874b-974f-41fa-bd17-f765a6a7daa4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_6_text.pickle?alt=media&token=c04b3114-d677-4547-bd91-bab6f409b1c1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%206.epub?alt=media&token=1d51634a-9e1c-41fb-b696-0e2463acaebb"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_7_emb.pickle?alt=media&token=cc7c97db-34be-4caa-b0fe-38211798ab2e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_7_text.pickle?alt=media&token=b80bc704-316d-4711-8b31-131a99b1142c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%207.epub?alt=media&token=83abec0a-95d4-4dac-b2f9-7c753bc1e447"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_8_emb.pickle?alt=media&token=d0b43eab-1b1a-489d-b466-224a6718d6da",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_8_text.pickle?alt=media&token=db2eab69-ed22-446c-a5b8-f6cbfb77eb8f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%208.epub?alt=media&token=277cd025-5579-4efa-9c7a-b1908d067e29"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_9_emb.pickle?alt=media&token=71b6aad9-86aa-4b79-b67b-f77bf918819e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass_12_political_science_part1_chapter_9_text.pickle?alt=media&token=1169262d-6af1-4657-8792-9a7009896150",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%201%2Fclass%2012%20political_science%20part1%20chapter%209.epub?alt=media&token=f2468588-584f-4b98-a229-5f678a93445e"}
}
civics12ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_1_emb.pickle?alt=media&token=6e94124a-3549-4763-967f-154f187d6bb1",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_1_text.pickle?alt=media&token=c6e86631-5ac3-4eb4-b4bf-1cd5f8a2551a",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%201.epub?alt=media&token=fa4dda9f-01d7-4ab1-b2b6-139e517dd448"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_2_emb.pickle?alt=media&token=aba50bca-6217-47fd-811c-479b9768b63f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_2_text.pickle?alt=media&token=9fbf9bfc-98f9-467e-84a5-5230f7d6d8ba",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%202.epub?alt=media&token=3a5c0898-d5f6-4152-bd4a-b0916ac56bc1"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_3_emb.pickle?alt=media&token=05684b8f-4bc4-4d43-9376-92520423bfb4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_3_text.pickle?alt=media&token=df035b01-45b1-41cc-a006-21601e5a9b2c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%203.epub?alt=media&token=c7a60923-7e38-4ea8-866e-ce257f579af6"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_4_emb.pickle?alt=media&token=d4686ade-2838-47c2-82e2-efc1e6d3de1d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_4_text.pickle?alt=media&token=11bd3c23-073c-4c61-a506-cf97755cd8c3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%204.epub?alt=media&token=b3e4ac15-7cab-4fac-a938-e5d97903a59b"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_5_emb.pickle?alt=media&token=57ba9dc2-62c8-4f22-9713-f89f268bf442",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_5_text.pickle?alt=media&token=98a54634-4129-497b-926f-b4065b687859",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%205.epub?alt=media&token=7ff47615-361b-419f-aaab-e31ca994e8e0"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_6_emb.pickle?alt=media&token=3e69e63a-c4b8-4416-846b-7a2a27b5eef4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_6_text.pickle?alt=media&token=71f322a5-918f-4306-9134-feddf7b4ed0e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%206.epub?alt=media&token=69fb647a-ef13-4899-929d-8c807ef045b1"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_7_emb.pickle?alt=media&token=cb9289c7-e2dc-4fb3-9edf-75a284d9508f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_7_text.pickle?alt=media&token=54d79d8e-ec6f-4938-9377-4f6c1c1e218f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%207.epub?alt=media&token=c9c5dbff-bc85-4562-9de7-6682e416e663"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_8_emb.pickle?alt=media&token=2d5890ba-4fb4-484e-91be-378fa573c839",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_8_text.pickle?alt=media&token=c39cfb6f-af0b-4ab0-aeae-61bc9dae2539",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%208.epub?alt=media&token=0f9a9354-c093-4ee0-af4a-cd41101d8e7a"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_9_emb.pickle?alt=media&token=d820e2c5-e297-4b52-b354-e484b0ea3a28",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass_12_political_science_part2_chapter_9_text.pickle?alt=media&token=b42817c1-2156-4780-b17e-a2b330049c15",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2012th%2Fsocial%20science%2Fpolitical%20science%2Fpart%202%2Fclass%2012%20political_science%20part2%20chapter%209.epub?alt=media&token=fe656cb2-eb0a-4671-b9d0-c86a2877e45f"}
}

accountancy11ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%201%2Fclass_11_accountancy_part2_chapter_1_emb.pickle?alt=media&token=d7bcf779-c1ab-493b-9a27-18b83e1eee32",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%201%2Fclass_11_accountancy_part2_chapter_1_text.pickle?alt=media&token=883d3948-4eb0-4b90-9b06-a74119b1c253",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%201%2Fclass%2011%20accountancy%20part2%20chapter%201.epub?alt=media&token=40026e3f-8418-43af-a931-f810824b5389"},
                              "chapter_2": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%202%2Fclass_11_accountancy_part2_chapter_2_emb.pickle?alt=media&token=513166fc-2c16-48dc-8645-3f4a06a83f58",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%202%2Fclass_11_accountancy_part2_chapter_2_text.pickle?alt=media&token=8cf789f9-e7d1-47d8-9623-5a068f341251",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%202%2Fclass%2011%20accountancy%20part2%20chapter%202.epub?alt=media&token=4dddb271-e34c-46e5-826f-a340ef34370a"},
                              "chapter_3": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%203%2Fclass_11_accountancy_part2_chapter_3_emb.pickle?alt=media&token=f9715583-e7ac-44a9-92d2-9740760ea181",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%203%2Fclass_11_accountancy_part2_chapter_3_text.pickle?alt=media&token=f9d286d0-1fc4-4fe9-926d-20f1406a19e4",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%203%2Fclass%2011%20accountancy%20part2%20chapter%203.epub?alt=media&token=68bf16b0-0fc7-4324-bd55-0b3f053b23a9"},
                              "chapter_4": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%204%2Fclass_11_accountancy_part2_chapter_4_emb.pickle?alt=media&token=9477b993-3098-4743-b5f2-c0bd388fea78",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%204%2Fclass_11_accountancy_part2_chapter_4_text.pickle?alt=media&token=f0ff4a0f-ae55-4e14-a427-02a36536725e",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%204%2Fclass%2011%20accountancy%20part2%20chapter%204.epub?alt=media&token=1c76fb89-ca34-4cf1-ad31-9c9c9ed30b39"},
                              "chapter_5": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%205%2Fclass_11_accountancy_part2_chapter_5_emb.pickle?alt=media&token=272441d1-cc0b-4923-b71a-b968de33cf8f",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%205%2Fclass_11_accountancy_part2_chapter_5_text.pickle?alt=media&token=08fc6df0-e51e-4f88-bf97-5fe8c0f467ee",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%205%2Fclass%2011%20accountancy%20part2%20chapter%205.epub?alt=media&token=25472c9c-0ad8-439e-9212-eec011606ee0"},
                              "chapter_6": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%206%2Fclass_11_accountancy_part2_chapter_6_emb.pickle?alt=media&token=f36c9605-bc2d-4bd5-b58b-5ff5db0c4b1d",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%206%2Fclass_11_accountancy_part2_chapter_6_text.pickle?alt=media&token=fa305c8f-9274-4236-9aa4-b7a59d012761",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%206%2Fclass%2011%20accountancy%20part2%20chapter%206.epub?alt=media&token=05383bc7-726b-4012-a0b7-22c37110172f"},
                              "chapter_7": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%207%2Fclass_11_accountancy_part2_chapter_7_emb.pickle?alt=media&token=7bb2510b-4c8e-4019-ad15-5064d127d580",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%207%2Fclass_11_accountancy_part2_chapter_7_text.pickle?alt=media&token=a4632985-ca39-44ad-9763-715162bc64c5",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%207%2Fclass%2011%20accountancy%20part2%20chapter%207.epub?alt=media&token=a4d12ef6-8bc1-4804-97b0-a9f645cc5dd8"},
                              "chapter_8": {
                                  "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                  "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%208%2Fclass_11_accountancy_part2_chapter_8_emb.pickle?alt=media&token=afc82967-0ab4-4c31-bedb-544968e03b38",
                                  "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%208%2Fclass_11_accountancy_part2_chapter_8_text.pickle?alt=media&token=f4128c72-cbd0-48be-b271-e7a714cee1f0",
                                  "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%202%2Fchapter%208%2Fclass%2011%20accountancy%20part2%20chapter%208.epub?alt=media&token=eaa44a38-f700-472a-9421-db8cbf0f132d"}
                          },
accountancy11ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%201%2Fclass_11_accountancy_part1_chapter_1_emb.pickle?alt=media&token=c775bfcb-178f-40b9-8645-35e78c14edd8",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%201%2Fclass_11_accountancy_part1_chapter_1_text.pickle?alt=media&token=44263bd0-d3d1-4ea7-87c2-9b8038cb241a",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%201%2Fclass%2011%20accountancy%20part1%20chapter%201.epub?alt=media&token=f99cb741-d48a-4661-b64f-7d0080fc3eba"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%202%2Fclass_11_accountancy_part1_chapter_2_emb.pickle?alt=media&token=a2e301fb-5b47-4d68-98e2-4aab80ac3ee5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%202%2Fclass_11_accountancy_part1_chapter_2_text.pickle?alt=media&token=ca4f5617-7362-45f2-8f2d-3fe8734f4c85",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%202%2Fclass%2011%20accountancy%20part1%20chapter%202.epub?alt=media&token=69bfa1e8-5dea-42fc-a75f-813e3e0a9088"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%203%2Fclass_11_accountancy_part1_chapter_3_emb.pickle?alt=media&token=df9b9649-beed-4617-9aa2-249b32d8e8a3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%203%2Fclass_11_accountancy_part1_chapter_3_text.pickle?alt=media&token=5f9de3d5-8b62-464e-8712-432b1c4176ef",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%203%2Fclass%2011%20accountancy%20part1%20chapter%203.epub?alt=media&token=104bd35e-03bb-48cb-ba7c-9367dd34193b"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%204%2Fclass_11_accountancy_part1_chapter_4_emb.pickle?alt=media&token=345b277b-4e0f-4dc9-921f-c1dc512a1440",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%204%2Fclass_11_accountancy_part1_chapter_4_text.pickle?alt=media&token=29f72fbe-48ed-4fa7-b1b4-06d59f6436be",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%204%2Fclass%2011%20accountancy%20part1%20chapter%204.epub?alt=media&token=09fda516-61a1-4d4f-81fa-d6437aef5707"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%205%2Fclass_11_accountancy_part1_chapter_5_emb.pickle?alt=media&token=d5727f8f-17bb-4fde-89d2-9d590eba3fc6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%205%2Fclass_11_accountancy_part1_chapter_5_text.pickle?alt=media&token=f55f2100-9b66-4887-8d1a-cf4e53e63413",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Faccountancy%2Fpart%201%2Fchapter%205%2Fclass%2011%20accountancy%20part1%20chapter%205.epub?alt=media&token=4d654974-829e-47a0-86ab-2e834a8c6849"}
}

biology11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%201%2Fclass_11_biology_chapter_1_emb.pickle?alt=media&token=512c2d84-730e-4407-9b58-7a53b6b5d16f",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%201%2Fclass_11_biology_chapter_1_text.pickle?alt=media&token=e1ff26eb-edcd-4770-9d59-ec70992d41b9",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%201.epub?alt=media&token=a976aac6-572a-458a-996f-844dde4a681c"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%202%2Fclass_11_biology_chapter_2_emb.pickle?alt=media&token=cca3f41c-f24c-4c90-a4e8-0e06a8ca777f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%202%2Fclass_11_biology_chapter_2_text.pickle?alt=media&token=5b66f5cc-b94c-4bbf-9266-565c7dab5164",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%202.epub?alt=media&token=82764098-cffb-4216-bcbe-3e733ecae9f0"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%203%2Fclass_11_biology_chapter_3_emb.pickle?alt=media&token=1ddd71b6-4eee-4166-9e18-a636481989e8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%203%2Fclass_11_biology_chapter_3_text.pickle?alt=media&token=a141ac14-a88d-4d26-8e08-cacf26a47dc8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%203.epub?alt=media&token=2efdbdbe-2b71-4c83-8cae-1635e553f56c"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%204%2Fclass_11_biology_chapter_4_emb.pickle?alt=media&token=31d9769c-a713-4685-bc61-20d22cd0c887",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%204%2Fclass_11_biology_chapter_4_text.pickle?alt=media&token=f77b3705-b4db-4631-a555-691bd55e01a0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%204.epub?alt=media&token=cf16a33f-8104-4082-8cf4-2199a5324339"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%205%2Fclass_11_biology_chapter_5_emb.pickle?alt=media&token=4b5b2e5a-929e-42e8-b253-c1aef7b4afd5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%205%2Fclass_11_biology_chapter_5_text.pickle?alt=media&token=110637b9-3fd2-4cca-a909-b2b7cd4eb38b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%205.epub?alt=media&token=41ddd9f5-e87c-4493-82f5-c3d704972763"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%206%2Fclass_11_biology_chapter_6_emb.pickle?alt=media&token=461a970f-5589-4009-89cc-2fea67808393",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%206%2Fclass_11_biology_chapter_6_text.pickle?alt=media&token=58f220b6-1747-4d35-b85c-0b1a1c1dd8c4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%206.epub?alt=media&token=d973e05c-ecd2-472d-8f05-60facdec447d"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%207%2Fclass_11_biology_chapter_7_emb.pickle?alt=media&token=846c75b8-02f6-4328-aba5-94072ded25de",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%207%2Fclass_11_biology_chapter_7_text.pickle?alt=media&token=a4b3834d-6595-4a10-a3c6-ef4d85b0900b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%207.epub?alt=media&token=bfe5032b-58bc-4121-9768-bb67cc108cc5"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%208%2Fclass_11_biology_chapter_8_emb.pickle?alt=media&token=4ac19fd4-ead0-4bc6-b7ce-599add19c46c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%208%2Fclass_11_biology_chapter_8_text.pickle?alt=media&token=893576cd-5150-455f-97e8-7ff3ca997279",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%208.epub?alt=media&token=b472653f-a8c1-4227-b58e-492fa702a176"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%209%2Fclass_11_biology_chapter_9_emb.pickle?alt=media&token=6c93018b-33c8-4a3c-9f8d-bf5f62a2a8d6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%209%2Fclass_11_biology_chapter_9_text.pickle?alt=media&token=36f7be33-09a9-47b5-baff-1f7daecceeb3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%209.epub?alt=media&token=a4ed14cf-071f-44e4-98a4-a08266cf3702"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2010%2Fclass_11_biology_chapter_10_emb.pickle?alt=media&token=80a38046-8f28-4a03-b80b-574f3bf5d4c0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2010%2Fclass_11_biology_chapter_10_text.pickle?alt=media&token=82fffaf8-f47b-477f-980c-e41bf214310c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2010.epub?alt=media&token=1749e17c-7371-4ea9-a380-ad7c9c335466"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2011%2Fclass_11_biology_chapter_11_emb.pickle?alt=media&token=c8306a01-d55f-4363-8410-eecfe58438e8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2011%2Fclass_11_biology_chapter_11_text.pickle?alt=media&token=0fec42ef-5215-4c29-be28-fb9f51e086b1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2011.epub?alt=media&token=21930a72-8302-4e17-9b4a-d9116d7f9143"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2012%2Fclass_11_biology_chapter_12_emb.pickle?alt=media&token=86f40dfc-93f5-425e-8e80-389e91a0217b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2012%2Fclass_11_biology_chapter_12_text.pickle?alt=media&token=e4a05625-c1c8-4952-aff5-fb1375d16b64",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2012.epub?alt=media&token=4a09c485-3dd4-4225-993c-07170fe7cece"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2013%2Fclass_11_biology_chapter_13_emb.pickle?alt=media&token=8937f1ad-ae12-412b-b2bf-76fa5b922239",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2013%2Fclass_11_biology_chapter_13_text.pickle?alt=media&token=10269c83-44d9-4338-af53-b8ae40708f39",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2013.epub?alt=media&token=3590b85b-83e0-4d2c-bd15-60007e4dc71b"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2014%2Fclass_11_biology_chapter_14_emb.pickle?alt=media&token=e50e80ad-fa72-4edc-b967-11a74105b0c0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2014%2Fclass_11_biology_chapter_14_text.pickle?alt=media&token=66a105c4-8f94-4e72-9f13-19768f1858b0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2014.epub?alt=media&token=0651a02f-63e8-4522-81e9-5836b3f78352"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2015%2Fclass_11_biology_chapter_15_emb.pickle?alt=media&token=3e3301d5-632b-4045-bd6f-a2408ef79fdf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2015%2Fclass_11_biology_chapter_15_text.pickle?alt=media&token=261d0a15-9e3c-419f-9dfa-3c439229a6ed",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2015.epub?alt=media&token=51167d65-1be9-4684-aaaf-12f544f92ea4"},
    "chapter_16": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2016%2Fclass_11_biology_chapter_16_emb.pickle?alt=media&token=f12a84cd-c2ac-4590-be54-4a39dc56cd8c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2016%2Fclass_11_biology_chapter_16_text.pickle?alt=media&token=f237a306-80b8-4109-8373-e2efa1e7b529",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2016.epub?alt=media&token=7713de03-b359-4c51-9faf-ee7e406fee73"},
    "chapter_17": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2017%2Fclass_11_biology_chapter_17_emb.pickle?alt=media&token=a29928ac-829b-4a38-be9b-bf5627348679",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2017%2Fclass_11_biology_chapter_17_text.pickle?alt=media&token=c4031846-4b42-4a28-aae9-150394c368e3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2017.epub?alt=media&token=85d67746-b598-4a37-86d6-0e1776becf85"},
    "chapter_18": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2018%2Fclass_11_biology_chapter_18_emb.pickle?alt=media&token=31babbc5-2f29-4310-8fde-2c9d3114f213",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2018%2Fclass_11_biology_chapter_18_text.pickle?alt=media&token=099407a1-2685-46c6-994f-478e0e89402a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2018.epub?alt=media&token=290b6c24-9f52-4387-ae9c-1ce822971ad1"},
    "chapter_19": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2019%2Fclass_11_biology_chapter_19_emb.pickle?alt=media&token=e4ca7f08-96af-4c59-a72b-be36e6fd692f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2019%2Fclass_11_biology_chapter_19_text.pickle?alt=media&token=716ef45f-35dd-4fa3-8d9a-c6ec06d69bb2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2019.epub?alt=media&token=12035a70-3f13-45f0-bcd1-8204ffd44205"},
    "chapter_20": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2020%2Fclass_11_biology_chapter_20_emb.pickle?alt=media&token=d54af9bc-1fa3-4509-9697-7e794f99415d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2020%2Fclass_11_biology_chapter_20_text.pickle?alt=media&token=c5b74a05-82ad-49e8-a1ca-dad692122291",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2020.epub?alt=media&token=943119d8-ca49-4de6-b958-3722e65e09a5"},
    "chapter_21": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2021%2Fclass_11_biology_chapter_21_emb.pickle?alt=media&token=be1692ad-ab14-439a-8bbd-0eb04ebf139a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2021%2Fclass_11_biology_chapter_21_text.pickle?alt=media&token=02960a11-0c38-4227-bdeb-76caa71e9d2d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2021.epub?alt=media&token=43c8e1c6-56c8-4b1d-9f15-3e955ac1f6fd"},
    "chapter_22": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2022%2Fclass_11_biology_chapter_22_emb.pickle?alt=media&token=3cdb86c1-5f17-4c13-adbb-303f488b43d0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fchapter%2022%2Fclass_11_biology_chapter_22_text.pickle?alt=media&token=4cdd3857-2538-4e4a-98c7-1d7e8752a8a2",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbiology%2Fall%20chapter%20epub's%2Fclass%2011%20biology%20chapter%2022.epub?alt=media&token=d6060b26-4ba7-4089-9b19-0409e3a7e423"}
}

businessStudies11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%201%2Fclass_11_buiseness_studies_chapter_1_emb.pickle?alt=media&token=0539138d-a4ba-451e-b36b-757df5ffdd8d",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%201%2Fclass_11_buiseness_studies_chapter_1_text.pickle?alt=media&token=0cea986e-68f5-46d9-b04f-b52f6a52048c",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%201.epub?alt=media&token=7a6b9198-f280-4d32-9f85-e9068a13210f"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%202%2Fclass_11_buiseness_studies_chapter_2_emb.pickle?alt=media&token=327259e1-24cc-4fd0-9b25-1d3f1fb51e5d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%202%2Fclass_11_buiseness_studies_chapter_2_text.pickle?alt=media&token=1bb169e5-4651-4837-a92c-8b4776bc9fb8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%202.epub?alt=media&token=92192afd-dff2-42c4-b203-c9c3c4dff8db"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%203%2Fclass_11_buiseness_studies_chapter_3_emb.pickle?alt=media&token=03e2db8c-84c2-4e5a-b0f2-e37b10902244",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%203%2Fclass_11_buiseness_studies_chapter_3_text.pickle?alt=media&token=55e631b6-9f7b-4dc8-85a3-444147602035",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%203.epub?alt=media&token=9042781c-c8c9-495c-9ff1-aa3bf6db23c4"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%204%2Fclass_11_buiseness_studies_chapter_4_emb.pickle?alt=media&token=54d2479f-4b95-4d68-a128-bcca78a8d0d8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%204%2Fclass_11_buiseness_studies_chapter_4_text.pickle?alt=media&token=af2962fa-e864-4bfa-bcd4-df54f0eaa058",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%204.epub?alt=media&token=8befc6ce-d7d6-44d1-b677-633e2ac40fcc"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%205%2Fclass_11_buiseness_studies_chapter_5_emb.pickle?alt=media&token=293bc136-4f85-46e7-84b1-150d38109cbf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%205%2Fclass_11_buiseness_studies_chapter_5_text.pickle?alt=media&token=cbb818e6-c9f2-4873-93b4-da493968e32e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%205.epub?alt=media&token=810609bc-435f-495e-9aba-9458cc307d34"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%206%2Fclass_11_buiseness_studies_chapter_6_emb.pickle?alt=media&token=1000022e-7161-45a2-88e2-4dc23d847b6f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%206%2Fclass_11_buiseness_studies_chapter_6_text.pickle?alt=media&token=d36d88a6-5810-4714-8f15-2f04d2a173a5",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%206.epub?alt=media&token=124f7bca-a868-40dd-bb88-1d7af3676755"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%207%2Fclass_11_buiseness_studies_chapter_7_emb.pickle?alt=media&token=5bee9b83-c4d8-4fca-8fc0-9a1cdb21b93b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%207%2Fclass_11_buiseness_studies_chapter_7_text.pickle?alt=media&token=36dac77d-46db-4a8f-92eb-1d8175dd6b65",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%207.epub?alt=media&token=74a9c3e6-99be-4e7b-9950-6550f740023c"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%208%2Fclass_11_buiseness_studies_chapter_8_emb.pickle?alt=media&token=6981ecb0-28a3-416b-83ad-c29962930650",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%208%2Fclass_11_buiseness_studies_chapter_8_text.pickle?alt=media&token=20723c13-7c59-4c93-b464-2708f045f4d7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%208.epub?alt=media&token=7197b33d-041d-45a0-a62e-bf514a84c36d"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%209%2Fclass_11_buiseness_studies_chapter_9_emb.pickle?alt=media&token=7cd9e810-0286-41d6-b856-7eb5a2ca57aa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%209%2Fclass_11_buiseness_studies_chapter_9_text.pickle?alt=media&token=355caa0c-9943-41e2-bb6f-6de500e50f9d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%209.epub?alt=media&token=da368f07-fe70-41d7-b68c-e2f73945f1cf"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%2010%2Fclass_11_buiseness_studies_chapter_10_emb.pickle?alt=media&token=0ea71cec-637d-47c3-b0a6-9f711d2d9f35",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%2010%2Fclass_11_buiseness_studies_chapter_10_text.pickle?alt=media&token=d4b6c6c9-8608-438f-b3a1-f2ad2d3d9d56",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%2010.epub?alt=media&token=251354f4-2e01-4fa6-bd6c-de652d89c4d7"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%2011%2Fclass_11_buiseness_studies_chapter_11_emb.pickle?alt=media&token=e32a4e02-aee9-4569-85b0-c8d277cc4bd7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fchapter%2011%2Fclass_11_buiseness_studies_chapter_11_text.pickle?alt=media&token=82c58e93-8506-459b-a4d8-b778325a1ec6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fbusiness%20studiees%2Fall%20chapter%20epub's%2Fclass%2011%20buiseness_studies%20chapter%2011.epub?alt=media&token=4e1cf700-3e7e-479d-b784-3b116ba294a0"}
}

chemistry11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%201%2Fclass_11_chemistry_part1_chapter_1_emb.pickle?alt=media&token=e02cfb37-6697-40fa-8710-008ab91e1bcc",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%201%2Fclass_11_chemistry_part1_chapter_1_text.pickle?alt=media&token=de10f203-7cfb-4996-9343-77fbfbf7ef9e",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%201.epub?alt=media&token=ad4e09a6-c72e-4ca0-b833-99093ce2bbf5"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%202%2Fclass_11_chemistry_part1_chapter_2_emb.pickle?alt=media&token=28a450bd-514c-4b43-be29-5392564cf903",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%202%2Fclass_11_chemistry_part1_chapter_2_text.pickle?alt=media&token=cf39879d-6467-4ed4-84f0-b609f5228f7e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%202.epub?alt=media&token=8682953a-6430-4cf8-baea-4d647bd8cd3d"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%203%2Fclass_11_chemistry_part1_chapter_3_emb.pickle?alt=media&token=f24b5f95-1d6e-4f58-a368-6290b497b67f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%203%2Fclass_11_chemistry_part1_chapter_3_text.pickle?alt=media&token=7fdd51ca-2980-4bd5-9362-36180438fc56",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%203.epub?alt=media&token=c3742070-666a-47ce-9d0c-5fd6f2d58332"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%204%2Fclass_11_chemistry_part1_chapter_4_emb.pickle?alt=media&token=577a24fc-75e6-498e-a5e7-e8cbc376539f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%204%2Fclass_11_chemistry_part1_chapter_4_text.pickle?alt=media&token=23a3c384-72af-4888-a327-935b35c16cc3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%204.epub?alt=media&token=f7d39531-98f1-4724-8952-5204fb0f7ed9"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%205%2Fclass_11_chemistry_part1_chapter_5_emb.pickle?alt=media&token=9fbe5b4d-e25a-4296-a983-96de0f9bfabe",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%205%2Fclass_11_chemistry_part1_chapter_5_text.pickle?alt=media&token=41b42bcf-6ff6-4652-a13a-58aa109d746a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%205.epub?alt=media&token=447d41fa-6d6b-4dcd-b042-13cca7edf420"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%206%2Fclass_11_chemistry_part1_chapter_6_emb.pickle?alt=media&token=34f1a899-650a-48f9-b461-1bee5e086c91",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%206%2Fclass_11_chemistry_part1_chapter_6_text.pickle?alt=media&token=4e4e488d-20c1-4172-9a95-614f04ba52e4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%206.epub?alt=media&token=5b9f2fe9-6b31-48da-9f5b-bdf8e07e207c"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%207%2Fclass_11_chemistry_part1_chapter_7_emb.pickle?alt=media&token=381f846e-1c35-47ae-ab02-160107f637dc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%207%2Fclass_11_chemistry_part1_chapter_7_text.pickle?alt=media&token=d00c61c9-c64b-409f-a0ef-e794473240b6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fall%20chapter%20epub's%2Fclass%2011%20chemistry%20part%201%20chapter%207.epub?alt=media&token=a43f12ef-05f3-495f-9ce3-88cc5eaab3d8"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%208%2Fclass_11_chemistry_part2_chapter_8_emb.pickle?alt=media&token=ec89faff-2ad9-43bb-ad9b-b5fb574eae26",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%208%2Fclass_11_chemistry_part2_chapter_8_text.pickle?alt=media&token=e3af621b-7d36-4a1c-966e-50c30c98142e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%208%2Fclass%2011%20chemistry%20part%202%20chapter%208.epub?alt=media&token=ccfd40a6-b873-4249-996c-99061cd49a85"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%209%2Fclass_11_chemistry_part2_chapter_9_emb.pickle?alt=media&token=2699c585-e4cf-4344-8aa8-b657173407aa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%209%2Fclass_11_chemistry_part2_chapter_9_text.pickle?alt=media&token=126ed174-c5ed-4853-91a5-f7875d2568a6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%209%2Fclass%2011%20chemistry%20part%202%20chapter%209.epub?alt=media&token=8efb8f07-7e1f-4110-a4e6-fa7ec4c39519"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2010%2Fclass_11_chemistry_part2_chapter_10_emb.pickle?alt=media&token=b2575494-9787-448f-b3bd-cc8d2bf5f3cf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2010%2Fclass_11_chemistry_part2_chapter_10_text.pickle?alt=media&token=6722ec41-1563-4c4f-a4b9-9fdd575ef4c8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2010%2Fclass%2011%20chemistry%20part%202%20chapter%2010.epub?alt=media&token=4cc6b796-4db6-476b-882e-800b30741adf"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2011%2Fclass_11_chemistry_part2_chapter_11_emb.pickle?alt=media&token=17961c5f-4525-458e-b301-03c33cdba1bd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2011%2Fclass_11_chemistry_part2_chapter_11_text.pickle?alt=media&token=765a88ab-aafa-46de-9e29-e8b52af0b6a1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2011%2Fclass%2011%20chemistry%20part%202%20chapter%2011.epub?alt=media&token=5e00a30a-7edc-49be-b1c1-8834cfd2a635"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2012%2Fclass_11_chemistry_part2_chapter_12_emb.pickle?alt=media&token=50935629-2062-4be8-879c-19328624aaf2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2012%2Fclass_11_chemistry_part2_chapter_12_text.pickle?alt=media&token=5ff030a0-1df7-41f4-afef-14ece37f8079",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2012%2Fclass%2011%20chemistry%20part%202%20chapter%2012.epub?alt=media&token=1606f5c1-c4d5-4b09-a8f0-434103256c3e"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2013%2Fclass_11_chemistry_part2_chapter_13_emb.pickle?alt=media&token=fbe49b6b-97e6-49f8-9a8a-a2d51fce867e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2013%2Fclass_11_chemistry_part2_chapter_13_text.pickle?alt=media&token=93d1403e-09fd-497f-af7d-90c33974e7bb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2013%2Fclass%2011%20chemistry%20part%202%20chapter%2013.epub?alt=media&token=f21a6e30-96dd-4684-a675-ab01b930849c"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2014%2Fclass_11_chemistry_part2_chapter_14_emb.pickle?alt=media&token=e40d44ff-ae70-4bcb-a309-4b74fd7429e4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2014%2Fclass_11_chemistry_part2_chapter_14_text.pickle?alt=media&token=37f89f50-f187-4563-9fb8-25ca7967bdda",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fchemistry%2Fchapter%2014%2Fclass%2011%20chemistry%20part%202%20chapter%2014.epub?alt=media&token=daf56f97-a270-4121-95e2-94768596bdc3"}
}

computerScience11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%201%2Fclass_11_computer_science_chapter_1_emb.pickle?alt=media&token=56213c6e-bf2a-427b-b2a6-900fa47daf3c",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%201%2Fclass_11_computer_science_chapter_1_text.pickle?alt=media&token=fd912c86-3892-4ce7-b9c7-bfddae57b17e",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%201.epub?alt=media&token=24684604-896e-4650-9e70-e08a27152a1d"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%202%2Fclass_11_computer_science_chapter_2_emb.pickle?alt=media&token=616c389f-2cbe-4a0e-adf5-d3c5a2eeaacd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%202%2Fclass_11_computer_science_chapter_2_text.pickle?alt=media&token=836f98e1-8088-446d-be17-32ce579cd4f6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%202.epub?alt=media&token=3c911b23-596f-4275-8fe9-06b46831eeaa"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%203%2Fclass_11_computer_science_chapter_3_emb.pickle?alt=media&token=fdf8f1e0-3369-4e4f-8431-c0c2213329cd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%203%2Fclass_11_computer_science_chapter_3_text.pickle?alt=media&token=77968cf5-3721-4acd-a227-525beab4219f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%203.epub?alt=media&token=c4226425-375d-405d-8213-d1ccf3e34a5a"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%204%2Fclass_11_computer_science_chapter_4_emb.pickle?alt=media&token=4f4766f7-d04d-4a66-b3e1-815b2b9debd3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%204%2Fclass_11_computer_science_chapter_4_text.pickle?alt=media&token=eec649de-f196-4458-b17f-5c2883e816ea",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%204.epub?alt=media&token=20813406-03b0-4ff2-84d0-d22accbf3db1"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%205%2Fclass_11_computer_science_chapter_5_emb.pickle?alt=media&token=753c7485-aaa9-479f-bf65-c026c188702b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%205%2Fclass_11_computer_science_chapter_5_text.pickle?alt=media&token=9798ea47-b51f-437c-a2bb-04a39c35b8c4",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%205.epub?alt=media&token=e2c6c1f1-b593-4cb4-994c-bf357b422aaa"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%206%2Fclass_11_computer_science_chapter_6_emb.pickle?alt=media&token=aab7ea17-f352-4762-b9bf-395cf19b053b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%206%2Fclass_11_computer_science_chapter_6_text.pickle?alt=media&token=b86e06b0-d1a7-473f-a3a1-4bb5d3d4fe6b",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%206.epub?alt=media&token=d552e9e9-cb4b-44e3-a3f4-d4adfd209b34"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%207%2Fclass_11_computer_science_chapter_7_emb.pickle?alt=media&token=c395163c-7eb4-4140-8761-847c66480c30",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%207%2Fclass_11_computer_science_chapter_7_text.pickle?alt=media&token=717dfa2d-fddd-4680-b2d5-99bd44868ab0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%207.epub?alt=media&token=24b637e8-f398-46ac-a1fa-91d84d598c36"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%208%2Fclass_11_computer_science_chapter_8_emb.pickle?alt=media&token=34b59997-127c-4bd2-be7b-4cbb930518b9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%208%2Fclass_11_computer_science_chapter_8_text.pickle?alt=media&token=90a61ba3-b39a-4e5b-84fc-9e779ab6fe3f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%208.epub?alt=media&token=4d3d0967-81a7-4509-ba4d-1e92517ebfb7"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%209%2Fclass_11_computer_science_chapter_9_emb.pickle?alt=media&token=79bc591c-d6ec-4a4a-8dbf-419b04953633",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%209%2Fclass_11_computer_science_chapter_9_text.pickle?alt=media&token=d731f1ec-9779-4a41-a9bd-b214dd607fdb",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%209.epub?alt=media&token=4e7e1ad4-af6c-4cf6-9090-0123ac2e088e"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%2010%2Fclass_11_computer_science_chapter_10_emb.pickle?alt=media&token=daf17b81-24d2-4b50-8551-a37844d955b4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%2010%2Fclass_11_computer_science_chapter_10_text.pickle?alt=media&token=7a3a0186-3fdc-4e51-a668-489270f0d3c3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%2010.epub?alt=media&token=5afdf20c-bf6b-4dde-ac4d-b1f62a0821c1"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%2011%2Fclass_11_computer_science_chapter_11_emb.pickle?alt=media&token=d749ee02-709b-429d-b68f-94203349fc30",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fchapter%2011%2Fclass_11_computer_science_chapter_11_text.pickle?alt=media&token=75c50f9d-04fd-4a7d-907f-954c4d16c325",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fcomputer%20science%2Fall%20chapter%20epub's%2Fclass%2011%20computer_science%20chapter%2011.epub?alt=media&token=ce3f97d9-a5e6-4d5d-a93f-133214dc912b"}
}

mathematics11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%201%2Fclass_11_math_chapter_1_emb.pickle?alt=media&token=f532437b-e4b2-457c-aa88-0233d5752eed",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%201%2Fclass_11_math_chapter_1_text.pickle?alt=media&token=4cc75efd-b6c8-4c73-b905-2aead584e789",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%201%2Fclass%2011%20math%20chapter%201.epub?alt=media&token=be1dbc97-c14d-40d9-b877-01023891da6c"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%202%2Fclass_11_math_chapter_2_emb.pickle?alt=media&token=0d7611b7-5adc-4119-81d8-6b3e46933e53",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%202%2Fclass_11_math_chapter_2_text.pickle?alt=media&token=15b6f6a3-06d4-443f-b42e-25d4c18c8dd0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%202%2Fclass%2011%20math%20chapter%202.epub?alt=media&token=12b68063-a75a-4db7-b317-aa9ba120c35a"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%203%2Fclass_11_math_chapter_3_emb.pickle?alt=media&token=69638243-bdb3-40f2-acf4-76ab19e163a2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%203%2Fclass_11_math_chapter_3_text.pickle?alt=media&token=238d5acd-993b-4479-b598-62b64346396e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%203%2Fclass%2011%20math%20chapter%203.epub?alt=media&token=383baa9c-2407-4673-9807-4a1230ec0e1c"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%204%2Fclass_11_math_chapter_4_emb.pickle?alt=media&token=9aaec3ae-df90-4386-ba95-506d11d32df0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%204%2Fclass_11_math_chapter_4_text.pickle?alt=media&token=cb2253c5-d751-4ede-bb89-af78fe30ee75",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%204%2Fclass%2011%20math%20chapter%204_title_up.epub?alt=media&token=3ffd0006-0f60-4dc0-85df-209e6d74a8b5"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%205%2Fclass_11_math_chapter_5_emb.pickle?alt=media&token=e0c83e5b-8bb0-4a2a-9f4b-7870d6baa4e1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%205%2Fclass_11_math_chapter_5_text.pickle?alt=media&token=4973bf7b-9a51-47dc-a2f6-0d4a78735e11",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%205%2Fclass%2011%20math%20chapter%205_title_up.epub?alt=media&token=1a2b10a5-a80c-41fc-9eb8-b595e2f771c7"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%206%2Fclass_11_math_chapter_6_emb.pickle?alt=media&token=8c475ed9-439e-49c0-9c02-07dd5631af02",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%206%2Fclass_11_math_chapter_6_text.pickle?alt=media&token=f1df7c05-3f0f-4e3f-bb10-8d128a4108e7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%206%2Fclass%2011%20math%20chapter%206_title_up.epub?alt=media&token=779b8f66-36fd-470d-905f-57b631f21e1f"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%207%2Fclass_11_math_chapter_7_emb.pickle?alt=media&token=ffdc9353-3d9c-41d4-aea4-a26f324e96a1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%207%2Fclass_11_math_chapter_7_text.pickle?alt=media&token=a9f24321-8db0-4e01-8fee-b3d3034d750a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%207%2Fclass%2011%20math%20chapter%207_title_up.epub?alt=media&token=aac3958f-625d-43ec-a764-4be536221f8f"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%208%2Fclass_11_math_chapter_8_emb.pickle?alt=media&token=42377c38-d407-46f6-a979-3203b4db5a05",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%208%2Fclass_11_math_chapter_8_text.pickle?alt=media&token=511c6926-1549-449f-bde4-9da71c14193d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%208%2Fclass%2011%20math%20chapter%208_title_up.epub?alt=media&token=0f591ba7-9e3c-4464-92b6-84caf77c4e64"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%209%2Fclass_11_math_chapter_9_emb.pickle?alt=media&token=caf790c4-d0b5-4064-b0d1-02c696d72cef",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%209%2Fclass_11_math_chapter_9_text.pickle?alt=media&token=ea223074-b6cc-4c48-9741-2e818331c05e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%209%2Fclass%2011%20math%20chapter%209_title_up.epub?alt=media&token=aec34739-e88f-40d4-b90a-95a2269f8c22"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2010%2Fclass_11_math_chapter_10_emb.pickle?alt=media&token=c68dc879-2440-42a2-abac-396250d18a99",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2010%2Fclass_11_math_chapter_10_text.pickle?alt=media&token=25afb0a3-e8aa-4081-84b8-06cb6374ca49",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2010%2Fclass%2011%20math%20chapter%2010_title_up.epub?alt=media&token=364fd9ce-7a97-4cb9-a974-7c564fff8ee5"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2011%2Fclass_11_math_chapter_11_emb.pickle?alt=media&token=a2ee9b27-0578-40ea-8675-67fde8625123",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2011%2Fclass_11_math_chapter_11_text.pickle?alt=media&token=e03285d2-e459-41f8-9c36-5dcf7bfa36f3",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2011%2Fclass%2011%20math%20chapter%2011_title-up.epub?alt=media&token=a1256c1a-8d2b-4c21-ae35-8a669df71ee1"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2012%2Fclass_11_math_chapter_12_emb.pickle?alt=media&token=d6984139-3526-469c-b7fb-eeaaaf5f3329",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2012%2Fclass_11_math_chapter_12_text.pickle?alt=media&token=72314734-eee9-4d55-ad3f-fd91900b9860",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2012%2Fclass%2011%20math%20chapter%2012_title-up.epub?alt=media&token=e639bb17-0810-4dbb-8920-6d288a976df1"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2013%2Fclass_11_math_chapter_13_emb.pickle?alt=media&token=909126b2-f8bd-4468-b77c-169721736373",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2013%2Fclass_11_math_chapter_13_text.pickle?alt=media&token=55a7d60b-f84c-4784-976c-ef6606f09c15",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2013%2Fclass%2011%20math%20chapter%2013.epub?alt=media&token=4e70f6ad-f906-4241-bfb3-3cc1f3408ac1"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2014%2Fclass_11_math_chapter_14_emb.pickle?alt=media&token=337d1157-3035-465b-b3a9-34cb13bb15ff",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2014%2Fclass_11_math_chapter_14_text.pickle?alt=media&token=fd1e7290-9697-4fbd-9329-89a47de2f66e",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2014%2Fclass%2011%20math%20chapter%2014_title_up.epub?alt=media&token=583cf777-cd9d-4bdf-9e77-3953737dc0b6"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2015%2Fclass_11_math_chapter_15_emb.pickle?alt=media&token=2528a0bd-ba16-494e-85dd-4de3b26f9e9c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2015%2Fclass_11_math_chapter_15_text.pickle?alt=media&token=34973c83-7b5a-40d1-aab4-5d84d0dd0312",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2015%2Fclass%2011%20math%20chapter%2015.epub?alt=media&token=ffbee054-8f0d-4291-8be4-9dfe93f92fd6"},
    "chapter_16": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2016%2Fclass_11_math_chapter_16_emb.pickle?alt=media&token=75b7409d-47f7-463d-88c9-061a0a6ae3db",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2016%2Fclass_11_math_chapter_16_text.pickle?alt=media&token=5d2f2337-8235-4af4-ac65-5f0d8796d795",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fmath%2Fchapter%2016%2Fclass%2011%20math%20chapter%2016.epub?alt=media&token=e60478d4-0d14-48c5-bba6-9ca46660b850"}
}

physics11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%201%2Fclass_11_physics_part1_chapter_1_emb.pickle?alt=media&token=05e579f0-199d-4272-964a-a5ef89f19be6",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%201%2Fclass_11_physics_part1_chapter_1_text.pickle?alt=media&token=3a69067a-5e8d-476f-9ed3-90b738a80c8d",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%201.epub?alt=media&token=f570d617-d2cb-4cf9-95cf-ea1b1a816e53"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%202%2Fclass_11_physics_part1_chapter_2_emb.pickle?alt=media&token=969f1db0-0e54-4484-b331-2aafbb111665",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%202%2Fclass_11_physics_part1_chapter_2_text.pickle?alt=media&token=b422c95b-3f94-472c-82d5-88f4b0871807",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%202.epub?alt=media&token=54c1e8d3-bc73-4619-8e70-712b25f7a052"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%203%2Fclass_11_physics_part1_chapter_3_emb.pickle?alt=media&token=7b440810-f987-4948-aa5c-d1c2fcdcfab8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%203%2Fclass_11_physics_part1_chapter_3_text.pickle?alt=media&token=d06a95ba-d8d9-45d4-8244-3baa5dc96618",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%203.epub?alt=media&token=9172b7a5-eb1e-4b50-96cb-9309725e0f57"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%204%2Fclass_11_physics_part1_chapter_4_emb.pickle?alt=media&token=82367cf3-6090-4bbe-b90b-2c30b859f375",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%204%2Fclass_11_physics_part1_chapter_4_text.pickle?alt=media&token=25c28927-64c5-468a-9c85-d62dc3fd4e1d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%204.epub?alt=media&token=617bf470-a3ec-4715-866a-9c022f046863"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%205%2Fclass_11_physics_part1_chapter_5_emb.pickle?alt=media&token=ca9ece08-6feb-44c8-9a5e-32aee5c6fc62",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%205%2Fclass_11_physics_part1_chapter_5_text.pickle?alt=media&token=bb704fec-e89f-4760-8398-c792d755c839",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%205.epub?alt=media&token=852b8eb7-e441-4ce9-a986-2ebc9e60428f"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%206%2Fclass_11_physics_part1_chapter_6_emb.pickle?alt=media&token=a88c2f45-f997-48f8-9cca-fd2d174cab1a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%206%2Fclass_11_physics_part1_chapter_6_text.pickle?alt=media&token=fca89034-65d8-4c0b-983e-686fd1e99a7a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%206.epub?alt=media&token=f68af5ea-71de-4bf9-ae82-b0f2bcf72b6c"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%207%2Fclass_11_physics_part1_chapter_7_emb.pickle?alt=media&token=a1352e62-79dd-4efa-8afb-917a396079bb",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%207%2Fclass_11_physics_part1_chapter_7_text.pickle?alt=media&token=9f9c38a2-6f39-4732-83e0-252f6aaa4746",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%207.epub?alt=media&token=ef0a7b72-af69-4104-b6ac-ab427cc01898"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%208%2Fclass_11_physics_part1_chapter_8_emb.pickle?alt=media&token=4f1ea719-561f-4727-a709-a27a08905687",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%208%2Fclass_11_physics_part1_chapter_8_text.pickle?alt=media&token=2e0f6263-225b-46ba-a3c2-fe984842223f",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fpart%201%20all%20chapter%20epub%2Fclass%2011%20physics%20part%201%20chapter%208.epub?alt=media&token=fc9caab9-54f7-46b2-bc50-8824db88f7c0"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%209%2Fclass_11_physics_part2_chapter_9_emb.pickle?alt=media&token=90b4b7ce-e274-48e9-9722-7564c4dcf627",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%209%2Fclass_11_physics_part2_chapter_9_text.pickle?alt=media&token=172485d6-4656-4027-a1fa-0665e0c849a8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%209%2Fclass%2011%20physics%20part%202%20chapter%209.epub?alt=media&token=9dad2e62-8a6d-47b3-b38e-883fe51eb7c0"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2010%2Fclass_11_physics_part2_chapter_10_emb.pickle?alt=media&token=f5e2e3e4-858d-44c9-b175-e0c10b612d72",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2010%2Fclass_11_physics_part2_chapter_10_text.pickle?alt=media&token=10ef9f2f-bd3e-4356-87bc-2ae4b1c9a9e5",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2010%2Fclass%2011%20physics%20part%202%20chapter%2010.epub?alt=media&token=3da07f8d-d59f-4a20-b6a3-a33f9c614664"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2011%2Fclass_11_physics_part2_chapter_11_emb.pickle?alt=media&token=d46d7ab1-39f9-4a40-9fec-7057799d4092",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2011%2Fclass_11_physics_part2_chapter_11_text.pickle?alt=media&token=ca7e8128-8350-4e00-b683-e2bea7b98893",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2011%2Fclass%2011%20physics%20part%202%20chapter%2011.epub?alt=media&token=ef80c942-4080-47b9-8f3b-d2e3344449fc"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2012%2Fclass_11_physics_part2_chapter_12_emb.pickle?alt=media&token=60acf0cb-e200-47a6-887c-69c655227b6b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2012%2Fclass_11_physics_part2_chapter_12_text.pickle?alt=media&token=81090e44-099f-4d5a-a7fb-d3dbcf8ee8ed",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2012%2Fclass%2011%20physics%20part%202%20chapter%2012.epub?alt=media&token=fd7a5b32-2fd6-4ad8-820c-dc38b68d7f58"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2013%2Fclass_11_physics_part2_chapter_13_emb.pickle?alt=media&token=dcfa14bd-6e64-4aad-b666-6347880ad074",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2013%2Fclass_11_physics_part2_chapter_13_text.pickle?alt=media&token=e5c5ea5f-3401-4bec-97b3-2b5cc7c64754",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2013%2Fclass%2011%20physics%20part%202%20chapter%2013.epub?alt=media&token=15ce0b0b-8b2d-464b-bdbb-172f8bf4870d"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2014%2Fclass_11_physics_part2_chapter_14_emb.pickle?alt=media&token=dfb51334-e702-4f99-be9e-9753e6f36b1a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2014%2Fclass_11_physics_part2_chapter_14_text.pickle?alt=media&token=90ffc304-736f-48a2-a3ee-a93942742b87",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2014%2Fclass%2011%20physics%20part%202%20chapter%2014.epub?alt=media&token=c304eead-91a8-4d92-b337-af812e884617"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2015%2Fclass_11_physics_part2_chapter_15_emb.pickle?alt=media&token=8eeab482-5d2b-47c5-a034-873149912285",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2015%2Fclass_11_physics_part2_chapter_15_text.pickle?alt=media&token=856d533d-eaa4-4a19-9609-dda2de558e91",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fphysics%2Fchapter%2015%2Fclass%2011%20physics%20part%202%20chapter%2015.epub?alt=media&token=c87e51eb-dfda-49dc-860b-e3b7609e0621"}
}

economics11ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_1_emb.pickle?alt=media&token=fe8f4664-f256-4e4a-874c-944423fd05cb",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_1_text.pickle?alt=media&token=5f79bc25-a95a-4bb3-b5e0-81676cb98802",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%201.epub?alt=media&token=f0a3c37e-a6a6-4e7a-898a-338ff75b19f9"},
                            "chapter_2": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_2_emb.pickle?alt=media&token=f7ed7367-c5eb-44fa-809d-f4b8bd855ee3",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_2_text.pickle?alt=media&token=3231d848-f8a0-4be1-88e9-82b4123b41a9",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%202.epub?alt=media&token=e388cbbd-70a2-4780-94af-2d3578fda526"},
                            "chapter_3": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_3_emb.pickle?alt=media&token=da5a8192-7bea-43c5-a0ac-dc684c2d76e7",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_3_text.pickle?alt=media&token=20856949-13b3-4c4e-a097-87ceeb1c8304",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%203.epub?alt=media&token=e0df5f88-6ee8-4f01-9bd0-652ccdb9a5d0"},
                            "chapter_4": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_4_emb.pickle?alt=media&token=b661a467-4944-4f52-87db-d580f9855976",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_4_text.pickle?alt=media&token=e3edb120-0952-46ac-92d1-d35707abc749",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%204.epub?alt=media&token=9bebe0b3-4f6e-4bf9-96b4-f285b6249938"},
                            "chapter_5": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_5_emb.pickle?alt=media&token=9cc9299d-f56d-4efa-8854-20d91b73dfc5",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_5_text.pickle?alt=media&token=f8c7c643-cc3a-4023-ad05-19dd8471f56e",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%205.epub?alt=media&token=797ed33d-4413-4687-b268-486702cccf07"},
                            "chapter_6": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_6_emb.pickle?alt=media&token=0e6e10e7-75d1-444e-bd46-17bb3622e6b8",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_6_text.pickle?alt=media&token=a99ceff4-fb14-4f5e-a8aa-a16116a403bb",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%206.epub?alt=media&token=02826704-1143-47c0-9bee-7684a26d0073"},
                            "chapter_7": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_7_emb.pickle?alt=media&token=b6b0dd42-e36f-45e0-9a2e-afa7a90b2e5c",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_7_text.pickle?alt=media&token=41906448-990f-41ee-81bd-d1715f9f8d98",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%207.epub?alt=media&token=30c5574c-b8a0-4196-b770-8a6d5df75fdc"},
                            "chapter_8": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_8_emb.pickle?alt=media&token=0447588d-12cb-44fa-ab21-528fba30f0cd",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_8_text.pickle?alt=media&token=a9e47d1a-2bf9-4098-aa6a-bcc7587d1aa4",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%208.epub?alt=media&token=b90de176-164f-4528-b880-985b8216255b"},
                            "chapter_9": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_9_emb.pickle?alt=media&token=e763a074-4da8-4e00-86f5-4529163cb2e0",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_9_text.pickle?alt=media&token=3858423c-cb6f-4b60-b475-e7caf6ef3c60",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%209.epub?alt=media&token=0dfe94ce-8ecf-4816-b3d4-29c92f284a91"},
                            "chapter_10": {
                                "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
                                "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_10_emb.pickle?alt=media&token=854a1a1c-561c-4849-8276-94e6c50065a5",
                                "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fclass_11_economics_part1_chapter_10_text.pickle?alt=media&token=26b891c6-55fe-415a-964a-3a3648290b5e",
                                "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part1%20chapter%2010.epub?alt=media&token=80e7c287-12d8-4828-ba95-4adf9ef07f70"}
                        },
economics11ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_1_emb.pickle?alt=media&token=beb89998-6819-4227-bc87-d7211dac6bf7",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_1_text.pickle?alt=media&token=ce0d7f15-2452-4f04-b340-3bd3ac86457f",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%201.epub?alt=media&token=1964cb0d-e245-4a8d-8eb0-fc169c9ad873"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_2_emb.pickle?alt=media&token=2bc017bd-33f9-4209-8976-9225bb29decf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_2_text.pickle?alt=media&token=c610044d-9d6a-4656-9033-5ed50f1dd17d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%202.epub?alt=media&token=1a20bdd7-a41e-4d63-9a1c-5732810ac77a"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_3_emb.pickle?alt=media&token=0ef93e8e-859b-4c57-8353-ba98803f0953",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_3_text.pickle?alt=media&token=839cd2d5-e0f9-4840-a1c1-29f44f002b96",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%203.epub?alt=media&token=61bd81b5-87fc-482e-a22e-5c8d39183bd0"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_4_emb.pickle?alt=media&token=39aedcb5-62c5-4446-92a6-b70e2d567384",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_4_text.pickle?alt=media&token=2ee81a37-ae84-4ada-8784-42b6ccd7d118",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%204.epub?alt=media&token=27686993-d8b5-4012-8d95-618c630e24d2"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_5_emb.pickle?alt=media&token=b3857d8e-b1df-4c1d-8afe-dcdc789c65fa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_5_text.pickle?alt=media&token=827abf30-4bc7-438e-9a11-48381bc9b6c0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%205.epub?alt=media&token=30144349-4df3-4023-8561-2566e942c94e"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_6_emb.pickle?alt=media&token=274791c2-8980-4812-ba92-ae54db465ed6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_6_text.pickle?alt=media&token=fc698f4a-c631-4eec-aace-a7d505e07244",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%206.epub?alt=media&token=a89e412f-6b38-4e1b-ab2c-5bea167d973d"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_7_emb.pickle?alt=media&token=11ea815c-9d45-4233-987d-de55450a0499",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_7_text.pickle?alt=media&token=d52bfe08-520f-46be-a1e1-498c9cb355b9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%207.epub?alt=media&token=393e8f2c-2bc4-4dff-845f-60f15fd46f20"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_8_emb.pickle?alt=media&token=30fab77b-433d-42eb-b091-456edf1af8cd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_8_text.pickle?alt=media&token=4a01b533-1435-4d28-a84d-127cb3a61133",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%208.epub?alt=media&token=bbcba16f-6ae1-4b28-bfe0-ba0be8d0ebad"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_9_emb.pickle?alt=media&token=fdd8737f-0c8a-4fa1-a966-340b7e9cf236",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fclass_11_economics_part2_chapter_9_text.pickle?alt=media&token=4851a138-9462-4727-bffc-937dcf5dc9c7",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Feconomics%2Fpart%202%2Fall%20chapter%20epub's%2Fclass%2011%20economics%20part2%20chapter%209.epub?alt=media&token=4e65640e-3bd1-431e-a9ae-f15b239cc964"}
}

geography11ncert01p01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_1_emb.pickle?alt=media&token=0d235292-80c8-43a2-aa87-f73dd6eec6c3",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_1_text.pickle?alt=media&token=0ec8c48b-11b3-4bb3-b078-653cae207f1a",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%201.epub?alt=media&token=fbb4ea9b-1014-4171-80bf-b6a09f28155f"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_2_emb.pickle?alt=media&token=fec5ceba-9f21-464c-99f6-8b9392bdcc7e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_2_text.pickle?alt=media&token=f672ac61-af58-4f1c-9d1a-276bba1a8377",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%202.epub?alt=media&token=bbfd5978-29e8-4844-9844-243d360acce1"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_3_emb.pickle?alt=media&token=9f24688a-bc66-466e-a9b4-3709c03e2f3e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_3_text.pickle?alt=media&token=0c39e5d1-ec04-43e5-8ebe-df3ee6593a7d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%203.epub?alt=media&token=fa11eb9e-a67d-4c0b-9947-8c472fff90f3"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_4_emb.pickle?alt=media&token=745655ca-90cf-4b17-b5ed-d385e42b5291",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_4_text.pickle?alt=media&token=527043e5-2e76-450a-8235-c1ad8c557e59",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%204.epub?alt=media&token=2164600a-4e70-49cf-a68b-a2c8f9dfe549"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_5_emb.pickle?alt=media&token=aab48aa3-58ef-4747-b61f-3b5ef9b31e1d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_5_text.pickle?alt=media&token=6d7c4355-a030-4256-b18a-f249a1659983",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%205.epub?alt=media&token=24c17e56-d970-483d-80e4-dd0995370a49"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_6_emb.pickle?alt=media&token=757ae102-8adf-4b02-831c-11ff4874bb0d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_6_text.pickle?alt=media&token=f5050867-1de0-4f00-b20f-0325c1a154f1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%206.epub?alt=media&token=0bb20191-2878-47fa-82f6-d504778c8025"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_7_emb.pickle?alt=media&token=d96584d1-5c97-4bfe-9d5c-25a6c93727cd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_7_text.pickle?alt=media&token=308c47df-51d8-47a1-a97a-6861abf85ecc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%207.epub?alt=media&token=1f92db5b-d316-4252-b0d6-c3e2cdb37e59"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_8_emb.pickle?alt=media&token=08b0fcc7-5f1d-43a8-821b-6dcd214fb6ef",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_8_text.pickle?alt=media&token=c22febc1-fd5c-4368-b498-fdecd1c5b581",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%208.epub?alt=media&token=4918d39c-39ac-4dfb-8323-4737e47b3535"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_9_emb.pickle?alt=media&token=320170ec-ad05-4365-9a17-bd2a0a8e59ca",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_9_text.pickle?alt=media&token=b1010b12-1c55-49b0-8ad1-4a973d4f5647",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%209.epub?alt=media&token=a715152c-234b-41e8-b106-422cb59e5ffb"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_10_emb.pickle?alt=media&token=fe27549d-1335-4a8f-9141-244d2488f169",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_10_text.pickle?alt=media&token=ebd6209f-8b6a-41ad-b07a-264f2dba8334",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2010.epub?alt=media&token=f56713e7-de85-4dab-91bf-2fa74a250e63"},
    "chapter_11": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_11_emb.pickle?alt=media&token=fa0513f7-20e8-493b-a975-649ee75d2e0d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_11_text.pickle?alt=media&token=f51e819e-5fee-4815-ac75-36547c81ae4c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2011.epub?alt=media&token=bbc4afe7-5586-4c34-8604-49010172c61f"},
    "chapter_12": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_12_emb.pickle?alt=media&token=3c4f3a52-93b1-4350-95f0-85906bb60860",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_12_text.pickle?alt=media&token=edfe0ef2-28af-406f-989e-0664689de874",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2012.epub?alt=media&token=9bf2f45d-c91e-4076-9eaa-9121e85898c9"},
    "chapter_13": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_13_emb.pickle?alt=media&token=da438c6b-e8cc-4cda-9614-d360eeb20bb1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_13_text.pickle?alt=media&token=1b430f46-9ca2-4e3a-bdb5-08896383e792",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2013.epub?alt=media&token=3b145b49-d6f5-4b81-89da-fd32560d3150"},
    "chapter_14": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_14_emb.pickle?alt=media&token=8a25eef2-88fb-4b62-93ed-3e21d13e9d9b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_14_text.pickle?alt=media&token=763d3637-4c8a-4d65-9119-ab95bd06a362",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2014.epub?alt=media&token=62ec988d-4990-43f9-bb92-6a7d0566d29f"},
    "chapter_15": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_15_emb.pickle?alt=media&token=6fb06e73-b61a-4697-8caa-d4114fce537b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_15_text.pickle?alt=media&token=6242dbe0-5972-497d-9e5e-297796392b44",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2015.epub?alt=media&token=3567ca73-c969-4f25-912b-5221cf880eb3"},
    "chapter_16": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_16_emb.pickle?alt=media&token=143c283e-ecaf-4986-8efb-dfeda7838f96",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fclass_11_geography_part1_chapter_16_text.pickle?alt=media&token=653c0515-1026-4630-84ce-2df54a1cd93a",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%201%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part1%20chapter%2016.epub?alt=media&token=124602c1-c160-4d69-9553-1821ae1ef76d"}
}

geography11ncert01p02 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_1_emb.pickle?alt=media&token=9569c6e3-be97-4fb7-9395-83a46480d4c4",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_1_text.pickle?alt=media&token=a53bb035-356e-4477-a6de-b4bfe51a2ed6",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%201.epub?alt=media&token=6ec02cdc-2985-4395-a223-1f9803c8cd48"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_2_emb.pickle?alt=media&token=06742d9e-073a-4344-92f7-aef3e1f16552",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_2_text.pickle?alt=media&token=761549ee-195a-40c1-aa4d-e9949945e349",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%202.epub?alt=media&token=87d2879b-c985-471e-832b-0724d2a175e8"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_3_emb.pickle?alt=media&token=09f23a07-9d23-4fd7-b04e-2aa24d980ffc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_3_text.pickle?alt=media&token=3b180fd9-3adb-443e-9f23-1268d0dd47e6",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%203.epub?alt=media&token=8ccc9e19-d530-41a7-acc7-1273978828df"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_4_emb.pickle?alt=media&token=c93b6669-ecfb-4c13-9413-59baa03172ba",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_4_text.pickle?alt=media&token=12f8f208-e5c9-436f-8984-09454bb304b8",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%204.epub?alt=media&token=819d32f4-e4cb-49ad-adc5-a78154273e65"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_5_emb.pickle?alt=media&token=c3fe37b9-8207-49ab-bd6a-06798e0f8f09",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_5_text.pickle?alt=media&token=94371ebd-3f4d-4e0a-81b8-4b6c569078c9",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%205.epub?alt=media&token=92714963-24f1-4a2d-9f43-56a8814b19b1"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_6_emb.pickle?alt=media&token=934a994c-3028-4647-84f6-d9cc99e6555b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_6_text.pickle?alt=media&token=9b6bb336-8622-4d34-bc17-4bfb300ac18c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%206.epub?alt=media&token=236a1c5c-5245-49c9-8d9e-1bea356b15bf"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_7_emb.pickle?alt=media&token=2d9afca0-9905-4a81-8854-d0c94d1bf250",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass_11_geography_part2_chapter_7_text.pickle?alt=media&token=6f468fe8-cd04-489a-a66f-e1114449ec4d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%202%2Fclass%2011%20geography%20part2%20chapter%207.epub?alt=media&token=15cdefe9-9086-408f-bd9d-82fd682fcb3e"}
}

geography11ncert01p03 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_1_emb.pickle?alt=media&token=f09805e3-6716-46df-87b0-c7e555cfef09",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_1_text.pickle?alt=media&token=45f8f6ff-de90-4493-92e6-d80f278b1ac8",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%201.epub?alt=media&token=fe0207ea-d338-4390-b326-bfb36eb3416d"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_2_emb.pickle?alt=media&token=e5be6ab2-065b-4590-86f6-1cbe5da9b343",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_2_text.pickle?alt=media&token=1c5b209f-75bf-4a23-b4c3-44c4d3386703",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%202.epub?alt=media&token=b972bcb3-3a4d-4856-9f1d-e63d9fd57da7"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_3_emb.pickle?alt=media&token=deae90b2-67dc-4abe-8398-938e85d5f6b3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_3_text.pickle?alt=media&token=3cf32954-15a2-44aa-aaa8-258f660dd817",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%203.epub?alt=media&token=379f2b4c-4e4d-4460-90d7-e7db6405530c"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_4_emb.pickle?alt=media&token=3e548dc3-a34f-4e67-9bac-d9d143dddbd1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_4_text.pickle?alt=media&token=312c3a67-2c6b-4b16-a35a-1d79dca688ea",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%204.epub?alt=media&token=2d5d39ea-8eb1-4377-bb89-20c84e28aedb"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_5_emb.pickle?alt=media&token=9fae7f00-da0c-4596-8ecc-6c5e5119334f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_5_text.pickle?alt=media&token=ab080cc6-75d8-4cf3-888c-dda4c2fa00dc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%205.epub?alt=media&token=c3ea4f5e-ce99-4d4e-a3bb-19262a882bac"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_6_emb.pickle?alt=media&token=19e11e40-eb34-4478-80d5-db9d094b0e54",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_6_text.pickle?alt=media&token=f44ae120-2b0b-40bc-9c53-35b80f61e556",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%206.epub?alt=media&token=cff41c1d-ee1c-4281-8f1e-01fe85f2763f"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_7_emb.pickle?alt=media&token=1d4a85de-8f0c-425b-8acb-9dbe5750018e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_7_text.pickle?alt=media&token=783d5cc9-2273-4d5e-b516-0ddd750dd379",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%207.epub?alt=media&token=8e342cb7-ae3b-41e7-826b-45665e491bb1"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_8_emb.pickle?alt=media&token=a21863e4-c00b-42ba-b4dc-299cde65a8b7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fclass_11_geography_part3_chapter_8_text.pickle?alt=media&token=0ab0d059-dd1d-4bfa-844a-5585df132be1",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fgeography%2Fpart%203%2Fall%20chapter%20epub's%2Fclass%2011%20geography%20part3%20chapter%208.epub?alt=media&token=7e87b831-b37a-48a4-b4ce-843f7f14f743"}
}

history11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_1_emb.pickle?alt=media&token=f832400d-0ea4-4d6c-a2f7-b933e6504e64",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_1_text.pickle?alt=media&token=41f8c5ff-ba90-45fd-8175-d4ca35ced43c",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass%2011%20history%20chapter%201.epub?alt=media&token=28b72cbd-ecea-43be-a419-79b3efa9d750"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_2_emb.pickle?alt=media&token=49ba8b32-2301-491c-850a-3f60bd75f6c9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_2_text.pickle?alt=media&token=45e85fd3-c147-4d87-9b94-a1c1d3dc514c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass%2011%20history%20chapter%202.epub?alt=media&token=82a4767a-833d-41e4-9413-cd135fc59093"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_3_emb.pickle?alt=media&token=dbf3a94f-fadf-4870-be46-3e779f14d072",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_3_text.pickle?alt=media&token=6f04bc18-0bba-4f0e-ab26-f7511fe31312",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass%2011%20history%20chapter%203.epub?alt=media&token=739f327d-cf0a-4dff-9359-defbda502ac8"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_4_emb.pickle?alt=media&token=a56bf76b-423c-4193-968c-0a5b78fd07d8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass_11_history_chapter_4_text.pickle?alt=media&token=a1dbc337-6ca4-4418-8e2f-53f1083fcee0",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fhistory%2Fclass%2011%20history%20chapter%204.epub?alt=media&token=9e40995e-6c69-47e4-819a-c66cc9247ae7"}
}
civics11ncert01 = {"chapter_1": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
    "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_1_emb.pickle?alt=media&token=b46e41bb-7d21-47fe-8612-67a4847d203c",
    "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_1_text.pickle?alt=media&token=05b1ec48-ad3b-432d-81a6-19cb49cae519",
    "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%201.epub?alt=media&token=8df9d8af-d784-4497-bf4b-ffcbbd834ffe"},
    "chapter_2": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_2_emb.pickle?alt=media&token=ae6bc6c3-5f11-42cd-9d06-1879138ef5e5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_2_text.pickle?alt=media&token=77d89fc9-cdcf-461e-9a50-ca40d5e28788",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%202.epub?alt=media&token=665602b5-5fea-4c50-b483-b0a2009047cf"},
    "chapter_3": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_3_emb.pickle?alt=media&token=85abbf47-baa5-4e10-bace-e14f889b73ff",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_3_text.pickle?alt=media&token=edd280cc-dfc7-4ecf-b58f-eae377abba08",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%203.epub?alt=media&token=e77319b8-6adf-4508-9510-07e65c21ca44"},
    "chapter_4": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_4_emb.pickle?alt=media&token=a3604085-6ee6-47fe-8184-fd29de30f1a8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_4_text.pickle?alt=media&token=ed069dae-c797-4211-aaa5-e7487085ff42",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%204.epub?alt=media&token=ed3d0410-fbfa-4578-972c-a66ddbc41317"},
    "chapter_5": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_5_emb.pickle?alt=media&token=6c4cb8c9-85fd-4442-87f4-58576d0f7c26",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_5_text.pickle?alt=media&token=4fbf4592-ea2a-4f31-97c9-12827f62cd9c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%205.epub?alt=media&token=38996f52-726a-40c7-87a5-427ee0667680"},
    "chapter_6": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_6_emb.pickle?alt=media&token=8799e8a6-7cef-42f6-a171-3d7820ae0c6c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_6_text.pickle?alt=media&token=1ba0040b-538f-45f8-bb2a-a3c80c35720c",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%206.epub?alt=media&token=94473a6e-3399-4c09-a8a7-79e18c7644c1"},
    "chapter_7": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_7_emb.pickle?alt=media&token=f02e0ff7-2510-46bf-b43e-8c67179a318d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_7_text.pickle?alt=media&token=cf6867c4-113a-4e1c-aaff-bdb3f0d63b26",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%207.epub?alt=media&token=73a6dfa1-8ffc-4cbf-9449-3ce9a877de20"},
    "chapter_8": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_8_emb.pickle?alt=media&token=1d189137-d387-41fb-ac5a-4d71f3d00942",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_8_text.pickle?alt=media&token=13e42a06-a740-4bb3-9244-cb6b4069c972",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%208.epub?alt=media&token=c08a238a-5b22-44bf-9dce-b65fd31d22b9"},
    "chapter_9": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_9_emb.pickle?alt=media&token=c8028292-abb8-4d8e-b3fc-53ac7189a2fa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_9_text.pickle?alt=media&token=89f96673-1cc6-489c-a9b7-9fd148ae79cc",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%209.epub?alt=media&token=5bfded83-8797-476d-b0c9-91110a0037e4"},
    "chapter_10": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_10_emb.pickle?alt=media&token=a991d369-caea-45ae-a297-7d34b7262b4c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass_11_political_science_part1_chapter_10_text.pickle?alt=media&token=401b30b2-b06a-486f-b683-00e49474427d",
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2011th%2Fsocial%20science%2Fpolitical%20science%2Fclass%2011%20political_science%20part1%20chapter%2010.epub?alt=media&token=75510633-bf87-4ba5-9896-b419630e212e"}}

mathematics6ncert01 = {
    "Chapter1": {
        "EPUB_link": 'https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%201%2Fclass%206%20math%20chapter%201.epub?alt=media&token=b0f93dff-33cb-40c9-95bd-6054e27df462',
        "Text": 'https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%201%2Fclass%206%20math%20chapter%201%20cleaned.pickle?alt=media&token=daf17f39-02d9-4303-bd13-6949efb8cf18',
        "Embeddings": 'https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%201%2Fclass%206%20math%20chapter%201%20embedded.pickle?alt=media&token=1fb0f138-37c6-4f66-84eb-76a760811357'
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%202%2Fclass%206%20math%20chapter%202.epub?alt=media&token=d9e1254f-0e36-4e5c-b454-de89f62743fc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%202%2Fclass%206%20math%20chapter%202%20cleaned.pickle?alt=media&token=d677cc11-f31c-4a06-891f-161abb29efae",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%202%2Fclass%206%20math%20chapter%202%20embedded.pickle?alt=media&token=9953b71a-e952-4db8-bcd7-e4baf5c3b188"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%203%2Fclass%206%20math%20chapter%203.epub?alt=media&token=bb409c18-d4b8-4f2a-ae1e-9210b66b4ed2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%203%2Fclass%206%20math%20chapter%203%20cleaned.pickle?alt=media&token=862873f1-543e-4539-84b7-38ffe15f4f66",
        "Embeddings": 'https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%203%2Fclass%206%20math%20chapter%203%20embedded.pickle?alt=media&token=f944663c-c91c-40f7-8885-7db9e1357d05'
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%204%2Fclass%206%20math%20chapter%204.epub?alt=media&token=9fdf089a-93de-4c3b-bd3f-825a428d0785",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%204%2Fclass%206%20math%20chapter%204%20cleaned.pickle?alt=media&token=351ef871-e523-4413-974a-a7bc9b8fc24f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%204%2Fclass%206%20math%20chapter%204%20embedded.pickle?alt=media&token=7087c51e-0201-4709-9c17-dc0ca1e7dda7"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%205%2Fclass%206%20math%20chapter%205.epub?alt=media&token=a8b40627-ceb7-4102-a75a-aef3f8250060",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%205%2Fclass%206%20math%20chapter%205%20cleaned.pickle?alt=media&token=219d0a70-b3b2-42cf-8be2-2cdf920027fe",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%205%2Fclass%206%20math%20chapter%205%20embedded.pickle?alt=media&token=bfce3c51-fbcd-47b5-ada9-255c6dafd536"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%206%2Fclass%206%20math%20chapter%206.epub?alt=media&token=6c6a10d2-e9f1-428c-98a0-2083efebca2e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%206%2Fclass%206%20math%20chapter%206%20cleaned.pickle?alt=media&token=052383b2-32dc-4d52-9d90-ed1857d06536",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%206%2Fclass%206%20math%20chapter%206%20embedded.pickle?alt=media&token=08b3e919-01f1-4040-9601-17c8c8a173f5"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%207%2Fclass%206%20math%20chapter%207.epub?alt=media&token=b5506190-a5e1-4986-a62d-6ea99fd11e2a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%207%2Fclass%206%20math%20chapter%207%20cleaned.pickle?alt=media&token=908f494e-e211-4c9a-a011-c3c1cc93f053",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%207%2Fclass%206%20math%20chapter%207%20embedded.pickle?alt=media&token=da7a105c-06a0-4be8-ad42-5a1d3a2707db"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%208%2Fclass%206%20math%20chapter%208.epub?alt=media&token=d8af7c68-3233-419b-a842-ad104edb3144",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%208%2Fclass%206%20math%20chapter%208%20cleaned.pickle?alt=media&token=8035fed4-61a4-4972-a5bf-3fbf2887a359",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%208%2Fclass%206%20math%20chapter%208%20embedded.pickle?alt=media&token=5172081a-7202-4ae7-923c-cee99ba0f321"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%209%2Fclass%206%20math%20chapter%209.epub?alt=media&token=9ec7f90b-8750-41f6-aca0-872362d8100d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%209%2Fclass%206%20math%20chapter%209%20cleaned.pickle?alt=media&token=cf6bc85d-c6c7-4c76-bd4c-96af65282724",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%209%2Fclass%206%20math%20chapter%209%20embedded.pickle?alt=media&token=c25b95e8-ba40-4b88-a172-2da9b6c3cae6"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2010%2Fclass%206%20math%20chapter%2010.epub?alt=media&token=5a9cc75c-20ed-45eb-8ca1-77eae147f5cb",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2010%2Fclass%206%20math%20chapter%2010%20cleaned.pickle?alt=media&token=e35e203d-1f9c-4c01-b8a3-6d4635b6cb68",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2010%2Fclass%206%20math%20chapter%2010%20embedded.pickle?alt=media&token=a9157842-fb67-4c8d-8160-3e2caa1ada09"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2011%2Fclass%206%20math%20chapter%2011.epub?alt=media&token=724d5379-a4e2-49b3-96f3-25d2d0d1433f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2011%2Fclass%206%20math%20chapter%2011%20cleaned.pickle?alt=media&token=3c11df1b-86d0-49a0-ade2-5eda3d42fb4c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2011%2Fclass%206%20math%20chapter%2011%20embedded.pickle?alt=media&token=d88eb6a4-d9d0-4cec-b308-39b528c7b20f"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2012%2Fclass%206%20math%20chapter%2012.epub?alt=media&token=dec134ea-7b81-4b27-89b8-290114a5bfc4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2012%2Fclass%206%20math%20chapter%2012%20cleaned.pickle?alt=media&token=ccce8c0c-8e19-4f62-97e7-047ab25c2093",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2012%2Fclass%206%20math%20chapter%2012%20embedded.pickle?alt=media&token=b1338762-7a62-4dd7-96d4-df460d487cd8"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2013%2Fclass%206%20math%20chapter%2013.epub?alt=media&token=b6f9002c-b80e-4f92-9078-79b5e54df475",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2013%2Fclass%206%20math%20chapter%2013%20cleaned.pickle?alt=media&token=8f271ea7-b266-44b0-938d-50f19e3cf5f2",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2013%2Fclass%206%20math%20chapter%2013%20embedded.pickle?alt=media&token=84d0337a-cfe3-4ee3-9ec8-b9d7e0cd8083"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2014%2Fclass%206%20math%20chapter%2014.epub?alt=media&token=b1b9da26-74a3-4d07-a8ba-ad1bf2166313",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2014%2Fclass%206%20math%20chapter%2014%20cleaned.pickle?alt=media&token=f8e52131-77eb-4789-ba93-aaa17fa30655",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fmathematics%2Fchapter%2014%2Fclass%206%20math%20chapter%2014%20embedded.pickle?alt=media&token=ddf4409f-1b0c-43db-8690-58f9f481d970"
    }

}

science6ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%201%2Fclass%206%20science%20chapter%201.epub?alt=media&token=05734771-d8f8-4d0e-a4a1-76aabce55224",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%201%2Fclass%206%20science%20chapter%201%20cleaned.pickle?alt=media&token=05521fb7-e1d8-48bd-a68f-a021cee5d1a2",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%201%2Fclass%206%20science%20chapter%201%20embedded.pickle?alt=media&token=7ae265b3-27d4-48cc-9a52-8f9e5b8c6e72"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%202%2Fclass%206%20science%20chapter%202.epub?alt=media&token=e38efa66-0fe5-4cff-bbe3-a6f9a1602da3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%202%2Fclass%206%20science%20chapter%202%20cleaned.pickle?alt=media&token=bf98a9ca-8f20-4d2b-a617-503466ab9fb3",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%202%2Fclass%206%20science%20chapter%202%20embedded.pickle?alt=media&token=195a889b-6d89-4f1d-b1cd-d4e4fbe60a5d"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%203%2Fclass%206%20science%20chapter%203.epub?alt=media&token=9040aa43-b57d-47f5-a0f5-1b2d7f24bc8f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%203%2Fclass%206%20science%20chapter%203%20cleaned.pickle?alt=media&token=b6b8fbb9-9817-48c2-b745-e9f628dac6d4",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%203%2Fclass%206%20science%20chapter%203%20embedded.pickle?alt=media&token=95a85fe8-4919-41d5-933b-5fa299911461"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%204%2Fclass%206%20science%20chapter%204.epub?alt=media&token=06d1045c-b414-481f-9dd3-89380b921d47",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%204%2Fclass%206%20science%20chapter%204%20cleaned.pickle?alt=media&token=a73d3192-8f18-4a2e-bad0-5cc6ceafe5d4",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%204%2Fclass%206%20science%20chapter%204%20embedded.pickle?alt=media&token=90b07b7c-1395-463e-b67b-521091e7976b"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%205%2Fclass%206%20science%20chapter%205.epub?alt=media&token=cbf351c5-47e2-405a-807f-98beb5b1b1d8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%205%2Fclass%206%20science%20chapter%205%20cleaned.pickle?alt=media&token=c6794a70-2a9c-4eb9-aa37-32577f74b071",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%205%2Fclass%206%20science%20chapter%205%20embedded.pickle?alt=media&token=d78d8361-f275-4ae0-96f2-39b25fdac96a"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%206%2Fclass%206%20science%20chapter%206.epub?alt=media&token=27203354-f0a5-4836-a1a0-8add7e66490d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%206%2Fclass%206%20science%20chapter%206%20cleaned.pickle?alt=media&token=f37d727d-4f30-4f01-b633-56b604586dac",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%206%2Fclass%206%20science%20chapter%206%20embedded.pickle?alt=media&token=1231b2ad-a12d-40f5-b28d-240397d313ba"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%207%2Fclass%206%20science%20chapter%207.epub?alt=media&token=ca5d10bc-d4e8-4afa-890e-71b8086fe781",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%207%2Fclass%206%20science%20chapter%207%20cleaned.pickle?alt=media&token=1760970a-f7af-4d06-8137-e89b25db864f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%207%2Fclass%206%20science%20chapter%207%20embedded.pickle?alt=media&token=03256c9f-fdef-4d73-8f87-860b073bb2a9"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%208%2Fclass%206%20science%20chapter%208.epub?alt=media&token=2eb225cf-766d-4460-817a-fc1a7e0a0d65",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%208%2Fclass%206%20science%20chapter%208%20cleaned.pickle?alt=media&token=357115b3-5d63-4afb-8810-9c20f5ff5038",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%208%2Fclass%206%20science%20chapter%208%20embedded.pickle?alt=media&token=b3e8418e-94d4-4a97-ad90-7855350c9459"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%209%2Fclass%206%20science%20chapter%209.epub?alt=media&token=e0c5cd0b-1477-47b5-98fb-73eda067cbff",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%209%2Fclass%206%20science%20chapter%209%20cleaned.pickle?alt=media&token=2b9e1d22-4611-4af5-998a-660fd1b43e36",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%209%2Fclass%206%20science%20chapter%209%20embedded.pickle?alt=media&token=edad9ca5-e721-455c-a3e3-718a0fdba5ef"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2010%2Fclass%206%20science%20chapter%2010.epub?alt=media&token=e34e9663-3b7e-476e-a933-f7a362d8f518",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2010%2Fclass%206%20science%20chapter%2010%20cleaned.pickle?alt=media&token=5ad36097-5353-45e2-9dfe-4760f44fab8a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2010%2Fclass%206%20science%20chapter%2010%20embedded.pickle?alt=media&token=b88bfc60-e3f5-4148-b651-884a1185bcea"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2011%2Fclass%206%20science%20chapter%2011.epub?alt=media&token=2f105cca-c21d-457e-a7fd-72920e5f1a0b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2011%2Fclass%206%20science%20chapter%2011%20cleaned.pickle?alt=media&token=582a8286-e672-41f0-91cb-a588fd6359d7",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2011%2Fclass%206%20science%20chapter%2011%20embedded.pickle?alt=media&token=14ff065e-0514-4c30-b031-4350260de760"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2012%2Fclass%206%20science%20chapter%2012.epub?alt=media&token=17d54678-85a0-4fef-97e5-8061bbc7be75",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2012%2Fclass%206%20science%20chapter%2012%20cleaned.pickle?alt=media&token=cb24c07c-1fed-4168-a175-b3f5f790c75f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2012%2Fclass%206%20science%20chapter%2012%20embedded.pickle?alt=media&token=fd51808c-18c3-40f1-ac77-09691f8000b1"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2013%2Fclass%206%20science%20chapter%2013.epub?alt=media&token=87a4f893-653e-4273-831f-0bcc9e9b1a8e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2013%2Fclass%206%20science%20chapter%2013%20cleaned.pickle?alt=media&token=d4534377-2791-42b3-8530-d46ce4a45a85",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2013%2Fclass%206%20science%20chapter%2013%20embedded.pickle?alt=media&token=10c8fc2a-1e3e-4326-95c4-af3e7bc34d81"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2014%2Fclass%206%20science%20chapter%2014.epub?alt=media&token=7ff97f3f-bf9e-4042-b25d-1b526fb896b4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2014%2Fclass%206%20science%20chapter%2014%20cleaned.pickle?alt=media&token=7f022d45-765d-4cf9-b0d5-37464d483b53",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2014%2Fclass%206%20science%20chapter%2014%20embedded.pickle?alt=media&token=cd89b1e1-7d16-4e67-8868-29da9c209924"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2015%2Fclass%206%20science%20chapter%2015.epub?alt=media&token=1f14a0f4-a65f-48bc-a021-e0d2ea36fa90",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2015%2Fclass%206%20science%20chapter%2015%20cleaned.pickle?alt=media&token=15a9fcac-10cb-4601-bb7a-f62f03fd8c9a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2015%2Fclass%206%20science%20chapter%2015%20embedded.pickle?alt=media&token=f9bd7cfd-bbba-488c-b81b-d661e10b245a"
    },
    "Chapter16": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2016%2Fclass%206%20science%20chapter%2016.epub?alt=media&token=39ab4736-c24d-4d71-953e-9e659f6d81cd",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2016%2Fclass%206%20science%20chapter%2016%20cleaned.pickle?alt=media&token=8313493e-dd11-4c9d-9d12-ce2127d7cb09",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fscience%2Fchapter%2016%2Fclass%206%20science%20chapter%2016%20embedded.pickle?alt=media&token=58dc24ed-066b-48ca-84d2-eabdb2b9376c"
    }

}

geography6ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%206%20geography%20chapter%201.epub?alt=media&token=a270f5a9-6aee-4e8d-988d-5da00214809e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%206%20geography%20chapter%201%20cleaned.pickle?alt=media&token=91a0ef58-175a-458f-bdc4-8ed029547e0b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%206%20geography%20chapter%201%20embedded.pickle?alt=media&token=b6b26b44-8969-40e7-94c2-39fe251c5958"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%206%20geography%20chapter%202.epub?alt=media&token=9b4508a4-4d13-4ed9-9167-48898e32fee0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%206%20geography%20chapter%202%20cleaned.pickle?alt=media&token=65eff3e2-1620-4c79-ae9b-784a0d64041a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%206%20geography%20chapter%202%20embedded.pickle?alt=media&token=3b9aeb4e-48c7-4b6e-bf77-cf4e40707e37"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%206%20geography%20chapter%203.epub?alt=media&token=93736654-1f47-45bd-99d0-9cd71b984e7b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%206%20geography%20chapter%203%20cleaned.pickle?alt=media&token=82e4d159-e697-4171-bf51-0ccad3a1a4b8",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%206%20geography%20chapter%203%20embedded.pickle?alt=media&token=f0073f5a-f9fe-425c-8f0e-d5fa4defd047"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%206%20geography%20chapter%204.epub?alt=media&token=854a6e03-66b2-4716-9ebd-d65c5dab2b27",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%206%20geography%20chapter%204%20cleaned.pickle?alt=media&token=74d93487-65b2-4bc8-91ab-d64b84a44a03",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%206%20geography%20chapter%204%20embedded.pickle?alt=media&token=41833453-421a-4a85-aa48-1ca902cd4aa3"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%206%20geography%20chapter%205.epub?alt=media&token=79edadc3-1760-46d2-9500-7ce228032e4a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%206%20geography%20chapter%205%20cleaned.pickle?alt=media&token=31c33bd0-faba-4934-ad32-c980fe0b8a1e",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%206%20geography%20chapter%205%20embedded.pickle?alt=media&token=823482ab-e26b-4dd6-aeec-af093dd7864d"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%206%20geography%20chapter%206.epub?alt=media&token=102af37a-eef8-45f4-955c-3c924d1f4b52",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%206%20geography%20chapter%206%20cleaned.pickle?alt=media&token=581e8360-7c70-4ba2-98b2-f3e9c9719a48",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%206%20geography%20chapter%206%20embedded.pickle?alt=media&token=2bc6ae41-b5fd-4e60-a7ba-56ef9eba877d"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%207%2Fclass%206%20geography%20chapter%207.epub?alt=media&token=71966a9d-8bad-4de3-be18-835ed71cee69",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%207%2Fclass%206%20geography%20chapter%207%20cleaned.pickle?alt=media&token=035b65fa-3346-4090-b836-d7f618566ab8",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%207%2Fclass%206%20geography%20chapter%207%20embedded.pickle?alt=media&token=a0d99b08-75c7-43aa-81e5-50462f91e3e7"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%208%2Fclass%206%20geography%20chapter%208.epub?alt=media&token=0662c5d8-bb98-48a2-b620-16ba3a81edf6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%208%2Fclass%206%20geography%20chapter%208%20cleaned.pickle?alt=media&token=76fd04cf-1dd2-4549-8e56-40dc6d257221",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fgeography%2Fchapter%208%2Fclass%206%20geography%20chapter%208%20embedded.pickle?alt=media&token=b701bb9b-af94-40c7-b8b5-93f8d28cc9b6"
    }
}

history6ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%206%20history%20chapter%201.epub?alt=media&token=234ddc10-c945-4f6d-b9d5-ece0b1aea4c9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%206%20history%20chapter%201%20cleaned.pickle?alt=media&token=4ebda39e-e180-400f-a936-3a41554e026c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%206%20history%20chapter%201%20embedded.pickle?alt=media&token=9942bf2f-da71-41d8-b716-73ff91544350"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%206%20history%20chapter%202.epub?alt=media&token=d9b201ab-1c02-42d5-99f8-a2a47529f2ce",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%206%20history%20chapter%202%20cleaned.pickle?alt=media&token=4bd5f9d9-9dca-4760-b93f-38d8bfe13750",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%206%20history%20chapter%202%20embedded.pickle?alt=media&token=6b10da95-8f0a-482c-9adf-7f029fd7fffe"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%206%20history%20chapter%203.epub?alt=media&token=9fa77cfc-b384-40b6-9564-a310a6cd4f93",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%206%20history%20chapter%203%20cleaned.pickle?alt=media&token=76d171b0-807b-45bc-9206-87356c454b97",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%206%20history%20chapter%203%20embedded.pickle?alt=media&token=5ee6507b-f35f-4ea6-bd50-58a0b550d966"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%206%20history%20chapter%204.epub?alt=media&token=81e48a1c-2e45-457a-a165-dd3911f10f31",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%206%20history%20chapter%204%20cleaned.pickle?alt=media&token=046f6f6f-a604-4ece-a41c-bbafcf108ffd",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%206%20history%20chapter%204%20embedded.pickle?alt=media&token=b207cf19-c17c-439c-9dba-6faa71b3f796"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%206%20history%20chapter%205.epub?alt=media&token=288723ab-2fff-4e05-8a95-ec37caa99852",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%206%20history%20chapter%205%20cleaned.pickle?alt=media&token=0534c01e-9fea-4a61-a605-00d5af674827",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%206%20history%20chapter%205%20embedded.pickle?alt=media&token=3622d642-f2f7-4a8b-b7cd-0da91e1fa9c3"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%206%20history%20chapter%206.epub?alt=media&token=24e4dd85-2aea-4261-b6ff-3bc50c2cba2e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%206%20history%20chapter%206%20cleaned.pickle?alt=media&token=492d6d12-9e5b-4ce8-9785-4a11df2b3578",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%206%20history%20chapter%206%20embedded.pickle?alt=media&token=8e764620-d915-4052-b68d-6cf5d2086b90"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%206%20history%20chapter%207.epub?alt=media&token=d5003411-325b-4fb5-9136-1780eb2437eb",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%206%20history%20chapter%207%20cleaned.pickle?alt=media&token=9752a798-101f-4e6f-af24-7a622db18825",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%206%20history%20chapter%207%20embedded.pickle?alt=media&token=0a03dfb2-61e4-4546-b1a7-323d35a1b664"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%206%20history%20chapter%208.epub?alt=media&token=ffe17f59-c86c-41e9-9ee8-6e4669823d3d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%206%20history%20chapter%208%20cleaned.pickle?alt=media&token=38a1d9ec-7c02-4649-93a5-acdce4dfea35",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%206%20history%20chapter%208%20embedded.pickle?alt=media&token=f409dd28-a088-4e8c-8d83-dfa16402b517"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%206%20history%20chapter%209.epub?alt=media&token=0e883afe-dfd8-4243-8f59-0df0163a5f95",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%206%20history%20chapter%209%20cleaned.pickle?alt=media&token=1d505253-1396-4228-8ec5-36ca4a0cbf15",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%206%20history%20chapter%209%20embedded.pickle?alt=media&token=2bc21d4a-85f8-40a0-87ef-5e2e1b7550ab"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%206%20history%20chapter%2010.epub?alt=media&token=7a14e6c6-6200-4bee-bace-7a794061f9d0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%206%20history%20chapter%2010%20cleaned.pickle?alt=media&token=e4925d00-30bb-4238-bf13-265962d18d32",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%206%20history%20chapter%2010%20embedded.pickle?alt=media&token=e58b5614-e022-41a1-8e40-e9f30e43b86b"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%2011%2Fclass%206%20history%20chapter%2011.epub?alt=media&token=3be519d7-48dd-4f32-8e94-b5550c07e208",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%2011%2Fclass%206%20history%20chapter%2011%20cleaned.pickle?alt=media&token=7f77910b-c991-4b29-961c-0c70b9059807",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%206th%2Fsocial_science%2Fhistory%2Fchapter%2011%2Fclass%206%20history%20chapter%2011%20embedded.pickle?alt=media&token=b0a6df3f-b2a2-4f9c-a357-088967339dee"
    }

}

mathematics7ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%201%2Fclass%207%20math%20chapter%201.epub?alt=media&token=0afac9ac-56d3-4dab-83c3-46e50209b030",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%201%2Fclass%207%20math%20chapter%201%20cleaned.pickle?alt=media&token=3669f040-6dea-4f2e-92b0-9b4f02478968",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%201%2Fclass%207%20math%20chapter%201%20embedded.pickle?alt=media&token=950e989f-c4bd-402e-8009-22e68a2a2148"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%202%2Fclass%207%20math%20chapter%202.epub?alt=media&token=39f0e572-2669-47d6-b125-9ffdb96036b5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%202%2Fclass%207%20math%20chapter%202%20cleaned.pickle?alt=media&token=2a100973-dcf5-41e9-b627-3deb1af86b89",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%202%2Fclass%207%20math%20chapter%202%20embedded.pickle?alt=media&token=8d410c87-784a-4b9c-a674-5ea07f9a735e"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%203%2Fclass%207%20math%20chapter%203.epub?alt=media&token=f41d3f93-87db-4c91-ae0d-5266c069137a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%203%2Fclass%207%20math%20chapter%203%20cleaned.pickle?alt=media&token=f087b2fc-b5ca-4161-82c9-a2f794b565f1",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%203%2Fclass%207%20math%20chapter%203%20embedded.pickle?alt=media&token=47bf8863-f576-4152-943a-8c134853adaf"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%204%2Fclass%207%20math%20chapter%204.epub?alt=media&token=f43f7636-3470-44df-a6f7-9aa863a03768",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%204%2Fclass%207%20math%20chapter%204%20cleaned.pickle?alt=media&token=a0415996-fbad-4278-9bc1-1ef01c28f179",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%204%2Fclass%207%20math%20chapter%204%20embedded.pickle?alt=media&token=1dfee553-f9a8-4446-94b6-ab119fcf688d"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%205%2Fclass%207%20math%20chapter%205.epub?alt=media&token=2406ffeb-795c-40c3-ad2c-6b6ea3061a70",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%205%2Fclass%207%20math%20chapter%205%20cleaned.pickle?alt=media&token=65aac9d7-5d0f-446c-88f6-f16275e00aa4",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%205%2Fclass%207%20math%20chapter%205%20embedded.pickle?alt=media&token=35f0ee31-97ac-42e1-90de-8ef0f8300e5d"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%206%2Fclass%207%20math%20chapter%206.epub?alt=media&token=c1f12802-3271-42c3-93ad-1e702a6d7874",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%206%2Fclass%207%20math%20chapter%206%20cleaned.pickle?alt=media&token=85305288-4c55-405a-81ec-34b310ac9104",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%206%2Fclass%207%20math%20chapter%206%20embedded.pickle?alt=media&token=def7eb3e-9a20-4caf-a518-da80605bbd7d"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%207%2Fclass%207%20math%20chapter%207.epub?alt=media&token=fbcb2b59-fe63-4e48-964e-ba7a70b8e712",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%207%2Fclass%207%20math%20chapter%207%20cleaned.pickle?alt=media&token=b401b1cd-47da-4f3e-b9c2-606c8129590b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%207%2Fclass%207%20math%20chapter%207%20embedded.pickle?alt=media&token=7750067c-f978-4e3a-a662-355bf74f86aa"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%208%2Fclass%207%20math%20chapter%208.epub?alt=media&token=a4bc3796-5c13-405f-953c-3489a4032adc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%208%2Fclass%207%20math%20chapter%208%20cleaned.pickle?alt=media&token=a441f56e-c405-4a4c-b4fa-5686cfd24eb5",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%208%2Fclass%207%20math%20chapter%208%20embedded.pickle?alt=media&token=543c84a7-68a0-4a34-b32a-71ac84a05dda"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%209%2Fclass%207%20math%20chapter%209.epub?alt=media&token=cca07446-f97c-4495-a9ea-5c2063f67c49",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%209%2Fclass%207%20math%20chapter%209%20cleaned.pickle?alt=media&token=89bd3364-0ec2-4ceb-a667-05e8cde3c0d0",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%209%2Fclass%207%20math%20chapter%209%20embedded.pickle?alt=media&token=3326ce7c-64a5-453e-a5ea-e57dfebbcdf4"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2010%2Fclass%207%20math%20chapter%2010.epub?alt=media&token=a656713c-8183-48b0-8b22-b2ee4c43fb73",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2010%2Fclass%207%20math%20chapter%2010%20cleaned.pickle?alt=media&token=9b8fd056-cd45-4e54-bd6a-80a25f3cd64a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2010%2Fclass%207%20math%20chapter%2010%20embedded.pickle?alt=media&token=acaf8ffb-2c50-4a78-8a20-261faa216785"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2011%2Fclass%207%20math%20chapter%2011.epub?alt=media&token=f2a1bbe4-6936-490e-bfc9-2c7bf455a57f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2011%2Fclass%207%20math%20chapter%2011%20cleaned.pickle?alt=media&token=a9929055-1701-4e50-ae94-e2cac6264ecc",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2011%2Fclass%207%20math%20chapter%2011%20embedded.pickle?alt=media&token=9f9c45da-38ac-4fcc-8138-5db4b0d71d84"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2012%2Fclass%207%20math%20chapter%2012.epub?alt=media&token=0cd976bd-c45e-412f-8ba4-5039a69e7dc5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2012%2Fclass%207%20math%20chapter%2012%20cleaned.pickle?alt=media&token=0f10ab28-c237-4b83-9645-dfd5a86a6d00",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2012%2Fclass%207%20math%20chapter%2012%20embedded.pickle?alt=media&token=8f98d606-2096-4806-9405-bcecb60a1ae8"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2013%2Fclass%207%20math%20chapter%2013.epub?alt=media&token=8a7da4a6-83c8-4d34-bbc7-fd4e2c3b59f7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2013%2Fclass%207%20math%20chapter%2013%20cleaned.pickle?alt=media&token=7e07300a-e3d3-4e3c-8fb2-9d45c1f0bbbc",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2013%2Fclass%207%20math%20chapter%2013%20embedded.pickle?alt=media&token=5379b7c5-7691-44b4-b6ac-c0e8367ac235"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2014%2Fclass%207%20math%20chapter%2014.epub?alt=media&token=9ccac058-404a-4437-8815-04564d263caf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2014%2Fclass%207%20math%20chapter%2014%20cleaned.pickle?alt=media&token=df178b53-4e74-44d2-b1cd-e6d333525dfb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2014%2Fclass%207%20math%20chapter%2014%20embedded.pickle?alt=media&token=0a2a9bfc-f68a-42fb-8af8-4dc83463ed6b"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2015%2Fclass%207%20math%20chapter%2015.epub?alt=media&token=983242e8-de44-4d47-b23a-54d4314467bf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2015%2Fclass%207%20math%20chapter%2015%20cleaned.pickle?alt=media&token=a724b5d6-3eb7-473a-a3c4-64fdabb61f21",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fmathematics%2Fchapter%2015%2Fclass%207%20math%20chapter%2015%20embedded.pickle?alt=media&token=eef4d4f9-25f9-4844-9a86-df4c0d959227"
    }
}

science7ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%201%2Fclass%207%20science%20chapter%201.epub?alt=media&token=63530940-2b90-4ed0-91a5-cf4c53061d3f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%201%2Fclass%207%20science%20chapter%201%20cleaned.pickle?alt=media&token=d58318d4-9048-445a-baf8-405a26b85c86",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%201%2Fclass%207%20science%20chapter%201%20embedded.pickle?alt=media&token=50c338be-08d0-4345-b4dc-b0544bb874a5"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%202%2Fclass%207%20science%20chapter%202.epub?alt=media&token=6708d27a-faa8-4bf6-96ee-b64e9be9f917",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%202%2Fclass%207%20science%20chapter%202%20cleaned.pickle?alt=media&token=9686fbd7-e167-4e12-8983-bec9d1c4d9bb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%202%2Fclass%207%20science%20chapter%202%20embedded.pickle?alt=media&token=bcfd6a53-3ba6-4cc0-bd31-95066e9955e7"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%203%2Fclass%207%20science%20chapter%203.epub?alt=media&token=6855ffff-cdfc-4bf6-a922-93713b928c87",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%203%2Fclass%207%20science%20chapter%203%20cleaned.pickle?alt=media&token=913ac25e-710d-4c50-b213-6b8f8be1f0a2",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%203%2Fclass%207%20science%20chapter%203%20embedded.pickle?alt=media&token=0d2165fe-c1f9-46d3-b115-a073ff131f2b"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%204%2Fclass%207%20science%20chapter%204.epub?alt=media&token=b627f649-85c6-492a-bfe0-b8ebcd682f88",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%204%2Fclass%207%20science%20chapter%204%20cleaned.pickle?alt=media&token=fd89b52b-cd7e-4a46-8077-01f3c1923959",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%204%2Fclass%207%20science%20chapter%204%20embedded.pickle?alt=media&token=7d2e10f6-c01e-48d5-885e-b2926ee78a38"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%205%2Fclass%207%20science%20chapter%205.epub?alt=media&token=12c1369a-07b1-4e0a-80fd-29aac3388d88",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%205%2Fclass%207%20science%20chapter%205%20cleaned.pickle?alt=media&token=82060c12-e133-4d53-9b8b-76a0fb00275c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%205%2Fclass%207%20science%20chapter%205%20embedded.pickle?alt=media&token=be7c6843-0589-4ee0-bba7-b3ad800b51f4"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%206%2Fclass%207%20science%20chapter%206.epub?alt=media&token=62b5dcbd-f143-4551-a0ad-a1b7c5071d50",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%206%2Fclass%207%20science%20chapter%206%20cleaned.pickle?alt=media&token=eb271b10-71ea-4f5d-8faf-b519178cd7eb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%206%2Fclass%207%20science%20chapter%206%20embedded.pickle?alt=media&token=11da9db8-0194-4541-b024-7ab56e8f260e"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%207%2Fclass%207%20science%20chapter%207.epub?alt=media&token=8230001b-9147-4b8d-85fb-7d1af0642dad",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%207%2Fclass%207%20science%20chapter%207%20cleaned.pickle?alt=media&token=2b451e03-7ca1-48d2-8497-4da894d3222f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%207%2Fclass%207%20science%20chapter%207%20embedded.pickle?alt=media&token=1d9b7eb4-48f0-4052-a394-b8fa0737517f"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%208%2Fclass%207%20science%20chapter%208.epub?alt=media&token=e385f1e1-0d77-4b22-a39a-baa1a6f24030",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%208%2Fclass%207%20science%20chapter%208%20cleaned.pickle?alt=media&token=3ea43519-12c9-4569-908c-47dafc25d996",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%208%2Fclass%207%20science%20chapter%208%20embedded.pickle?alt=media&token=d49e6be7-a752-4abf-b808-587287b91d89"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%209%2Fclass%207%20science%20chapter%209.epub?alt=media&token=b684553f-8704-4a2c-af91-c6c09dd782ea",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%209%2Fclass%207%20science%20chapter%209%20cleaned.pickle?alt=media&token=e8e6d6f8-07b5-4000-b2c9-50262f571269",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%209%2Fclass%207%20science%20chapter%209%20embedded.pickle?alt=media&token=4dab3409-d1ad-4b9a-a2a9-52ee0ea0c15f"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2010%2Fclass%207%20science%20chapter%2010.epub?alt=media&token=37f5294a-aa90-4e98-8df3-d3b4c41cce1b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2010%2Fclass%207%20science%20chapter%2010%20cleaned.pickle?alt=media&token=4cedb9c5-f68d-4fe8-a33e-3f0cebcd6e40",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2010%2Fclass%207%20science%20chapter%2010%20embedded.pickle?alt=media&token=0eefa49a-d8ac-4ef5-a6a6-0f0a9faefe33"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2011%2Fclass%207%20science%20chapter%2011.epub?alt=media&token=5fca2436-d6df-4d76-a959-16aa7b051cf7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2011%2Fclass%207%20science%20chapter%2011%20cleaned.pickle?alt=media&token=2ed3d5ae-2a5f-4431-b521-9037dbc136e1",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2011%2Fclass%207%20science%20chapter%2011%20embedded.pickle?alt=media&token=e4532b67-bbfc-4803-bfe2-1ec4001d9a8d"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2012%2Fclass%207%20science%20chapter%2012.epub?alt=media&token=09efddff-5d0c-4d17-91a6-f72619eba323",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2012%2Fclass%207%20science%20chapter%2012%20cleaned.pickle?alt=media&token=3ac52a2b-86ea-4216-a428-4336dfccf64c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2012%2Fclass%207%20science%20chapter%2012%20embedded.pickle?alt=media&token=bfafc080-5bce-4863-aa65-c19576474808"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2013%2Fclass%207%20science%20chapter%2013.epub?alt=media&token=507a60c4-ede0-49fd-b873-455d81e78a77",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2013%2Fclass%207%20science%20chapter%2013%20cleaned.pickle?alt=media&token=0e093c96-3f7f-48d6-88f3-72549cfd4035",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2013%2Fclass%207%20science%20chapter%2013%20embedded.pickle?alt=media&token=6691b356-8c24-44c8-a084-da0173a4a5bf"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2014%2Fclass%207%20science%20chapter%2014.epub?alt=media&token=59990690-3afa-47c8-91f4-540fcd1e0314",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2014%2Fclass%207%20science%20chapter%2014%20cleaned.pickle?alt=media&token=c6fe5a4b-fab9-4196-b532-bc56ffc418f4",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2014%2Fclass%207%20science%20chapter%2014%20embedded.pickle?alt=media&token=17bddac0-923a-4771-9f5b-f24e5f9d133d"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2015%2Fclass%207%20science%20chapter%2015.epub?alt=media&token=1468f55c-6a1c-4b64-a1a5-7d429a56c466",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2015%2Fclass%207%20science%20chapter%2015%20cleaned.pickle?alt=media&token=9b3df025-f9d6-4547-902f-ceea3a89cc43",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2015%2Fclass%207%20science%20chapter%2015%20embedded.pickle?alt=media&token=8b32018e-4b1c-4f08-8ffe-36fca57f1590"
    },
    "Chapter16": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2016%2Fclass%207%20science%20chapter%2016.epub?alt=media&token=85eccb6d-87a5-4fb6-b61e-a519f33f4b3b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2016%2Fclass%207%20science%20chapter%2016%20cleaned.pickle?alt=media&token=2f83b7c0-ca5a-428a-9e3d-4d86db1079b8",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2016%2Fclass%207%20science%20chapter%2016%20embedded.pickle?alt=media&token=25f2e357-2e95-41f5-860a-3d082b6760eb"
    },
    "Chapter17": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2017%2Fclass%207%20science%20chapter%2017.epub?alt=media&token=6ec16cf9-fc30-4b54-a6be-f0704d27ac3f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2017%2Fclass%207%20science%20chapter%2017%20cleaned.pickle?alt=media&token=64bfe5ad-a8f4-435e-8c97-285e11bce9c3",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2017%2Fclass%207%20science%20chapter%2017%20embedded.pickle?alt=media&token=107d2721-7c1b-4cfd-a669-a1ca7ff4a6b2"
    },
    "Chapter18": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2018%2Fclass%207%20science%20chapter%2018.epub?alt=media&token=4d3b1ddd-1f6a-456b-b637-5bbfc7138b89",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2018%2Fclass%207%20science%20chapter%2018%20cleaned.pickle?alt=media&token=45ae342b-c105-4d4a-a98f-13dd49d76fc8",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fscience%2Fchapter%2018%2Fclass%207%20science%20chapter%2018%20embedded.pickle?alt=media&token=1a090131-435e-40aa-a5a0-fdf3d5219911"
    }
}

geography7ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%207%20geography%20chapter%201.epub?alt=media&token=853f2a44-6d75-4ba7-960f-4ff52bdd852a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%207%20geography%20chapter%201%20cleaned.pickle?alt=media&token=ec3057d7-dda1-42f1-8b9e-da72aa1ccce9",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%207%20geography%20chapter%201%20embedded.pickle?alt=media&token=62ee1c09-193d-4f14-9b02-180c6a922fcd"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%207%20geography%20chapter%202.epub?alt=media&token=c10288bd-4df4-423c-9e0b-4e9d51026b8e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%207%20geography%20chapter%202%20cleaned.pickle?alt=media&token=06825da3-7023-4697-bf15-e9359f779599",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%207%20geography%20chapter%202%20embedded.pickle?alt=media&token=fc3d683d-6b7b-41a2-9c0d-7d0c44e24cff"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%207%20geography%20chapter%203.epub?alt=media&token=b44e6eec-f63e-48de-abb3-d088be952e01",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%207%20geography%20chapter%203%20cleaned.pickle?alt=media&token=f7e9eb5c-4413-4779-aa52-3a40ecf66cc1",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%207%20geography%20chapter%203%20embedded.pickle?alt=media&token=969eef26-593c-4ce0-96d4-cd81089f1d75"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%207%20geography%20chapter%204.epub?alt=media&token=5e998bb0-a6c4-4f68-8331-4195282f2c05",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%207%20geography%20chapter%204%20cleaned.pickle?alt=media&token=39a7575c-c023-44d2-9689-6cec3f55938a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%207%20geography%20chapter%204%20embedded.pickle?alt=media&token=57d15b60-ef06-4002-8c0f-335cf01d0b76"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%207%20geography%20chapter%205.epub?alt=media&token=beceb076-648c-43f5-b9f6-4571be99b139",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%207%20geography%20chapter%205%20cleaned.pickle?alt=media&token=5ceab88d-c58b-48fd-b513-d4f6bc5bfb33",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%207%20geography%20chapter%205%20embedded.pickle?alt=media&token=25d5ab17-3d22-43bb-8d6c-93c63c221782"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%207%20geography%20chapter%206.epub?alt=media&token=ce2ad43f-bf71-4b6c-8ff7-ab1b2a6b3a7f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%207%20geography%20chapter%206%20cleaned.pickle?alt=media&token=1c3f7619-fa40-4455-aa4e-58cbb10dac58",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%207%20geography%20chapter%206%20embedded.pickle?alt=media&token=6f1c3010-b121-4232-ad03-61e299e8859a"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%207%2Fclass%207%20geography%20chapter%207.epub?alt=media&token=b76b7efd-8020-49d8-8752-cdaf26f2c43b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%207%2Fclass%207%20geography%20chapter%207%20cleaned.pickle?alt=media&token=8657f722-882d-4eba-a7fd-a0a62da23c02",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%207%2Fclass%207%20geography%20chapter%207%20embedded.pickle?alt=media&token=722b1120-f458-4c66-b590-32265e28ecc4"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%208%2Fclass%207%20geography%20chapter%208.epub?alt=media&token=3e03217e-a952-4408-8b49-14431a693fec",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%208%2Fclass%207%20geography%20chapter%208%20cleaned.pickle?alt=media&token=2bf1febd-b94e-4c7e-8984-ac01eba84166",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%208%2Fclass%207%20geography%20chapter%208%20embedded.pickle?alt=media&token=afeeb0c4-1da4-450d-b79a-1a1fd5dfc283"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%209%2Fclass%207%20geography%20chapter%209.epub?alt=media&token=a48d2a6f-c317-4598-b4a3-d341b9b1e5d6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%209%2Fclass%207%20geography%20chapter%209%20cleaned.pickle?alt=media&token=9c639583-8656-4ecc-b44d-ea67e328beb1",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%209%2Fclass%207%20geography%20chapter%209%20embedded.pickle?alt=media&token=4970bd13-90ee-4c4d-a4e9-8a91ae584f9d"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%2010%2Fclass%207%20geography%20chapter%2010.epub?alt=media&token=b86ac7d0-9667-4f75-9039-8a2ba3ee4fe5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%2010%2Fclass%207%20geography%20chapter%2010%20cleaned.pickle?alt=media&token=efb4b2b0-c20b-41e9-9bcb-f9abf523c955",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fgeography%2Fchapter%2010%2Fclass%207%20geography%20chapter%2010%20embedded.pickle?alt=media&token=a434fbd4-ae43-4281-b953-bbf1bc2a5f88"
    }

}
history7ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%207%20history%20chapter%201.epub?alt=media&token=e7c991f8-6e31-49e9-824a-19820c7cd443",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%207%20history%20chapter%201%20cleaned.pickle?alt=media&token=31dc5476-390b-4851-bc90-43b8cc1a8adc",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%207%20history%20chapter%201%20embedded.pickle?alt=media&token=c21b6201-0ad8-42a9-8bd4-72369c7de44f"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%207%20history%20chapter%202.epub?alt=media&token=c80753f5-d0c8-4903-8229-11ae2da9129c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%207%20history%20chapter%202%20cleaned.pickle?alt=media&token=e270860e-fe24-4c47-9d25-22a8f6e10895",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%207%20history%20chapter%202%20embedded.pickle?alt=media&token=588b53d2-39b3-42b7-9de7-a55cd5169a09"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%207%20history%20chapter%203.epub?alt=media&token=69222377-1a36-4c8e-a525-34c251374175",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%207%20history%20chapter%203%20cleaned.pickle?alt=media&token=da772ac5-a594-4dce-a2e0-79b6dae78d68",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%207%20history%20chapter%203%20embedded.pickle?alt=media&token=345c8b26-9af8-4553-9717-89572065631a"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%207%20history%20chapter%204.epub?alt=media&token=6514a0d7-9e78-464d-8138-89b53a29c6f9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%207%20history%20chapter%204%20cleaned.pickle?alt=media&token=9d7be3c6-2f12-470e-a677-4f4b39adbb11",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%207%20history%20chapter%204%20embedded.pickle?alt=media&token=d9bb146f-a10d-4730-873d-dba6251afde1"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%207%20history%20chapter%205.epub?alt=media&token=0dda5099-e12c-417f-a314-ddb0e7dacec4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%207%20history%20chapter%205%20cleaned.pickle?alt=media&token=17ced921-789c-471d-9a1f-061c7c14a7bd",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%207%20history%20chapter%205%20embedded.pickle?alt=media&token=1cd59c9e-bac1-4790-9376-5945654bef6b"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%207%20history%20chapter%206.epub?alt=media&token=4a0b690c-9357-4b49-b91b-8feba4b74958",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%207%20history%20chapter%206%20cleaned.pickle?alt=media&token=6c44a563-2ece-4920-a5b3-2ca7aad51d35",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%207%20history%20chapter%206%20embedded.pickle?alt=media&token=66a5b97f-6859-4ddd-97ed-48c520d0ee30"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%207%20history%20chapter%207.epub?alt=media&token=1ca145ab-bb2f-4347-b658-a04d48c37962",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%207%20history%20chapter%207%20cleaned.pickle?alt=media&token=369aab54-f483-42ca-b6be-cba5e741fc4b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%207%20history%20chapter%207%20embedded.pickle?alt=media&token=45e3c5f4-8a8e-4921-a120-3b1c7611b25a"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%207%20history%20chapter%208.epub?alt=media&token=f8a5b280-8237-45a4-83a7-8d75a4d8bc9b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%207%20history%20chapter%208%20cleaned.pickle?alt=media&token=470b8eae-38b2-4aad-863e-97578219f2eb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%207%20history%20chapter%208%20embedded.pickle?alt=media&token=44d59272-737a-442c-961a-5449452b0ca9"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%207%20history%20chapter%209.epub?alt=media&token=ffbaf6a1-3b67-45f3-896c-d045c07e2134",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%207%20history%20chapter%209%20cleaned.pickle?alt=media&token=642f197f-4551-496e-8fbf-a0e4ea92db00",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%207%20history%20chapter%209%20embedded.pickle?alt=media&token=e0866da3-5c09-471e-815a-ebf7b5606e20"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%207%20history%20chapter%2010.epub?alt=media&token=d21e3f1c-2977-4bf3-b7cb-555c366fe5c8",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%207%20history%20chapter%2010%20cleaned.pickle?alt=media&token=7bfb1131-b602-4f39-bc53-552d15e2544c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%207th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%207%20history%20chapter%2010%20embedded.pickle?alt=media&token=1a8d7555-0137-49b0-8ab1-ca158e706f16"
    }

}

mathematics8ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%201%2Fclass%208%20math%20chapter%201.epub?alt=media&token=35045260-c4f4-4b6d-a5e5-2940183246b2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%201%2Fclass%208%20math%20chapter%201%20cleaned.pickle?alt=media&token=6d45a8b5-4370-49d9-86f3-7c1e7b72301a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%201%2Fclass%208%20math%20chapter%201%20embedded.pickle?alt=media&token=e4afb145-40fe-414e-beec-4a879424a4da"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%202%2Fclass%208%20math%20chapter%202.epub?alt=media&token=745afd46-bedd-4690-b590-258eed379033",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%202%2Fclass%208%20math%20chapter%202%20cleaned.pickle?alt=media&token=a9d466a9-a48e-411a-bbd3-f71734860b1a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%202%2Fclass%208%20math%20chapter%202%20embedded.pickle?alt=media&token=f10b33ee-ddad-4657-94dd-f93e66323c5c"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%203%2Fclass%208%20math%20chapter%203.epub?alt=media&token=df5ebaa5-a991-491a-b721-98c0c0dd4f1a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%203%2Fclass%208%20math%20chapter%203%20cleaned.pickle?alt=media&token=b8aa6b99-16c1-4cb4-b583-54e159b2e4db",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%203%2Fclass%208%20math%20chapter%203%20embedded.pickle?alt=media&token=de910570-f86a-45c2-9984-bd15aa07d916"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%204%2Fclass%208%20math%20chapter%204.epub?alt=media&token=9792d1f0-1e9c-42bb-b9b7-c89140dd855f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%204%2Fclass%208%20math%20chapter%204%20cleaned.pickle?alt=media&token=69d485b2-cf94-4e5b-9105-7b6f720edb7c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%204%2Fclass%208%20math%20chapter%204%20embedded.pickle?alt=media&token=d389a08f-e2a1-48a5-8a57-4e00fcb47b76"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%205%2Fclass%208%20math%20chapter%205.epub?alt=media&token=3e5fdfd6-b64c-4a06-8c00-ead8a37a751f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%205%2Fclass%208%20math%20chapter%205%20cleaned.pickle?alt=media&token=bcea5c40-e6bd-461b-8b19-7681ceff4f20",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%205%2Fclass%208%20math%20chapter%205%20embedded.pickle?alt=media&token=40a8cc1f-5e01-4751-8103-0b5d9b64fe75"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%206%2Fclass%208%20math%20chapter%206.epub?alt=media&token=78ab0dd7-2c7c-439c-affe-1c00142fa90b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%206%2Fclass%208%20math%20chapter%206%20cleaned.pickle?alt=media&token=63f0e71a-da85-49bc-b16b-f5e13294efa4",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%206%2Fclass%208%20math%20chapter%206%20embedded.pickle?alt=media&token=579e2231-e4ee-46c7-98da-4aa9b276d638"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%207%2Fclass%208%20math%20chapter%207.epub?alt=media&token=c6f7baf5-2c94-4d49-bb5a-5bb3094af3fa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%207%2Fclass%208%20math%20chapter%207%20cleaned.pickle?alt=media&token=8c23d823-0700-4bdc-bd3a-b25af4a1994f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%207%2Fclass%208%20math%20chapter%207%20embedded.pickle?alt=media&token=6e2f821f-d4b7-45c4-ae43-c7719f7b2716"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%208%2Fclass%208%20math%20chapter%208.epub?alt=media&token=473650fc-715c-47b8-bd87-b44a0410c1e6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%208%2Fclass%208%20math%20chapter%208%20cleaned.pickle?alt=media&token=72068186-e8f3-46b2-b976-017448d3862e",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%208%2Fclass%208%20math%20chapter%208%20embedded.pickle?alt=media&token=faff04f5-b1fb-4eaf-bfdc-7ff9ea2516ec"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%209%2Fclass%208%20math%20chapter%209.epub?alt=media&token=6bf9af26-816e-45ef-a570-70694941a091",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%209%2Fclass%208%20math%20chapter%209%20cleaned.pickle?alt=media&token=8bf00d1d-e579-4c0b-a89c-53dafe8e9bfc",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%209%2Fclass%208%20math%20chapter%209%20embedded.pickle?alt=media&token=6cdda9dd-0041-4f82-86b8-85a9115e3c07"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2010%2Fclass%208%20math%20chapter%2010.epub?alt=media&token=e6744c6b-887f-49b6-823b-e610a113a2a2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2010%2Fclass%208%20math%20chapter%2010%20cleaned.pickle?alt=media&token=19860a6f-8cb8-475e-8bd4-7889e31e3339",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2010%2Fclass%208%20math%20chapter%2010%20embedded.pickle?alt=media&token=acd232bd-22f5-49f4-ae77-751bad35a09c"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2011%2Fclass%208%20math%20chapter%2011.epub?alt=media&token=77b4662e-4281-4fce-a4a7-557cd4fe54d1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2011%2Fclass%208%20math%20chapter%2011%20cleaned.pickle?alt=media&token=f378ef5f-6d5e-4e36-884d-b775de139008",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2011%2Fclass%208%20math%20chapter%2011%20embedded.pickle?alt=media&token=85791298-3a6f-4fe2-b5ee-61af99cbc738"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2012%2Fclass%208%20math%20chapter%2012.epub?alt=media&token=5576e35d-80a8-4068-b106-8412bba75ca9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2012%2Fclass%208%20math%20chapter%2012%20cleaned.pickle?alt=media&token=c4faaa4a-be1e-4ddf-bf87-fe7dc341f65c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2012%2Fclass%208%20math%20chapter%2012%20embedded.pickle?alt=media&token=78970f9b-9039-49c8-a693-c90c8a6ca1c6"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2013%2Fclass%208%20math%20chapter%2013.epub?alt=media&token=21ba0440-9485-4a6c-acf1-2c803330306e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2013%2Fclass%208%20math%20chapter%2013%20cleaned.pickle?alt=media&token=71928a7e-e9c7-4251-8534-d468e65e2293",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2013%2Fclass%208%20math%20chapter%2013%20embedded.pickle?alt=media&token=94ffa51e-34a3-4b97-8776-dbce39a495a8"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2014%2Fclass%208%20math%20chapter%2014.epub?alt=media&token=277e84b1-51a4-4e5d-b0fb-eaeb45bdcf2d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2014%2Fclass%208%20math%20chapter%2014%20cleaned.pickle?alt=media&token=f0359b43-8ecb-4b40-82b1-ba17b82937c0",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2014%2Fclass%208%20math%20chapter%2014%20embedded.pickle?alt=media&token=345b2957-643d-48a5-b60a-03e9a9184779"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2015%2Fclass%208%20math%20chapter%2015.epub?alt=media&token=629f4f52-41f0-4032-9456-4cf67a8ba290",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2015%2Fclass%208%20math%20chapter%2015%20cleaned.pickle?alt=media&token=8b52bf19-6916-44cc-a9cd-38eac069a8d6",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2015%2Fclass%208%20math%20chapter%2015%20embedded.pickle?alt=media&token=533b6498-6540-4627-a567-3848cd74ec72"
    },
    "Chapter16": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2016%2Fclass%208%20math%20chapter%2016.epub?alt=media&token=ffcafd7c-61af-4d7a-b103-cd8bfec6caa7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2016%2Fclass%208%20math%20chapter%2016%20cleaned.pickle?alt=media&token=789fdf16-0d30-4e0e-a836-3c4a55d63892",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fmathematics%2Fchapter%2016%2Fclass%208%20math%20chapter%2016%20embedded.pickle?alt=media&token=ad08b831-c05c-4e0d-926a-2a9d7d4476df"
    }

}

science8ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%201%2Fclass%208%20science%20chapter%201.epub?alt=media&token=bf84afca-d2d7-44ec-b939-d0ac53ac1a61",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%201%2Fclass%208%20science%20chapter%201%20cleaned.pickle?alt=media&token=18fdf532-61a0-40d1-b6a1-88cdda39abea",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%201%2Fclass%208%20science%20chapter%201%20embedded.pickle?alt=media&token=f0799feb-be46-4b5e-ad8c-8d136de2c1ad"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%202%2Fclass%208%20science%20chapter%202.epub?alt=media&token=f49ee6d3-af4a-4bb2-8ef1-92a2c4d7870e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%202%2Fclass%208%20science%20chapter%202%20cleaned.pickle?alt=media&token=08ed25f9-8fdd-47f7-8fba-1cffd87a1b85",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%202%2Fclass%208%20science%20chapter%202%20embedded.pickle?alt=media&token=2ca80283-b78a-4a19-a728-af2424182154"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%203%2Fclass%208%20science%20chapter%203.epub?alt=media&token=e6aa8650-56b2-4f5b-9094-fa6b7e17aeb3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%203%2Fclass%208%20science%20chapter%203%20cleaned.pickle?alt=media&token=3ff14277-3218-4f3f-b080-5aa78aed5efc",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%203%2Fclass%208%20science%20chapter%203%20embedded.pickle?alt=media&token=a6f335c7-caa5-443b-a953-b35a17feecef"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%204%2Fclass%208%20science%20chapter%204.epub?alt=media&token=7cf71658-38e0-4821-a76c-75c6693ea5e5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%204%2Fclass%208%20science%20chapter%204%20cleaned.pickle?alt=media&token=47b3f60a-5a82-4fcd-a393-5c324b85621a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%204%2Fclass%208%20science%20chapter%204%20embedded.pickle?alt=media&token=c117dd79-1ec9-4934-be32-acf17893540a"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%205%2Fclass%208%20science%20chapter%205.epub?alt=media&token=2694e47d-9755-46c0-863e-b968cac36602",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%205%2Fclass%208%20science%20chapter%205%20cleaned.pickle?alt=media&token=693c42f1-c5d2-4d23-a977-8495f0511d8d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%205%2Fclass%208%20science%20chapter%205%20embedded.pickle?alt=media&token=45f71c89-760a-4c6b-b3fd-cba152a0ce0f"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%206%2Fclass%208%20science%20chapter%206.epub?alt=media&token=c7ac9326-22fe-41e4-b5d6-1557146cfac7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%206%2Fclass%208%20science%20chapter%206%20cleaned.pickle?alt=media&token=c0dee847-92af-41b6-8a50-c3b91900a18b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%206%2Fclass%208%20science%20chapter%206%20embedded.pickle?alt=media&token=52514e2b-c991-4b59-9d3a-8018966bc34d"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%207%2Fclass%208%20science%20chapter%207.epub?alt=media&token=167f7cf5-45c5-4ab2-a2f3-62b44d31d7c7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%207%2Fclass%208%20science%20chapter%207%20cleaned.pickle?alt=media&token=99600757-e4dd-4ca8-8a55-52b84cc74269",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%207%2Fclass%208%20science%20chapter%207%20embedded.pickle?alt=media&token=8bc8aa3b-c0d2-4ae0-9794-7d6dafca34a7"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%208%2Fclass%208%20science%20chapter%208.epub?alt=media&token=9bea98b1-c9f2-46a3-a06c-a2a7a9fdd0b4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%208%2Fclass%208%20science%20chapter%208%20cleaned.pickle?alt=media&token=8c6d2ae9-5841-4388-949e-be397d3d1a6d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%208%2Fclass%208%20science%20chapter%208%20embedded.pickle?alt=media&token=72aa5c3a-8824-4406-b989-022306bcd9a3"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%209%2Fclass%208%20science%20chapter%209.epub?alt=media&token=77df0684-d837-4ef5-8b27-d08fa2cedae6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%209%2Fclass%208%20science%20chapter%209%20cleaned.pickle?alt=media&token=aa7aa0a2-0cd8-42fc-b09f-7ebfd39074d0",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%209%2Fclass%208%20science%20chapter%209%20embedded.pickle?alt=media&token=18597fbd-b993-4847-a675-c85456636af0"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2010%2Fclass%208%20science%20chapter%2010.epub?alt=media&token=ee4a20d2-2fd7-4899-acd1-7bf1567fa5b1",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2010%2Fclass%208%20science%20chapter%2010%20cleaned.pickle?alt=media&token=71076717-e4b4-4487-9ac3-9a5e7aa83564",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2010%2Fclass%208%20science%20chapter%2010%20embedded.pickle?alt=media&token=ee27f37c-a0c9-4d18-ba4c-4b5a3ef013e3"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2011%2Fclass%208%20science%20chapter%2011.epub?alt=media&token=b2b4b585-27cf-4408-8bbe-3f05bcf864f7",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2011%2Fclass%208%20science%20chapter%2011%20cleaned.pickle?alt=media&token=c75efd7f-5c20-4d2e-bbc7-f4664ab7fee6",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2011%2Fclass%208%20science%20chapter%2011%20embedded.pickle?alt=media&token=4363385b-6611-4bee-8ff4-61a2c8e78572"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2012%2Fclass%208%20science%20chapter%2012.epub?alt=media&token=b80d4fd3-4772-46f9-9e2a-74f4d7536816",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2012%2Fclass%208%20science%20chapter%2012%20cleaned.pickle?alt=media&token=086c4a65-c710-4f87-b4e9-f9970c93b589",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2012%2Fclass%208%20science%20chapter%2012%20embedded.pickle?alt=media&token=416a079c-344d-4449-9868-708be411e709"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2013%2Fclass%208%20science%20chapter%2013.epub?alt=media&token=6da576c4-9c1d-4c0e-b773-fad37b40a6d3",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2013%2Fclass%208%20science%20chapter%2013%20cleaned.pickle?alt=media&token=9581c7ed-d458-4c59-8f7b-74483aa2fa43",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2013%2Fclass%208%20science%20chapter%2013%20embedded.pickle?alt=media&token=84693203-ab26-46ec-a222-66d6b2a2b699"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2014%2Fclass%208%20science%20chapter%2014.epub?alt=media&token=2836b1f7-4c88-4f10-aa14-e08a29edaf62",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2014%2Fclass%208%20science%20chapter%2014%20cleaned.pickle?alt=media&token=5538a7de-643d-4c44-86ec-34a2dd84e59d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2014%2Fclass%208%20science%20chapter%2014%20embedded.pickle?alt=media&token=231fb089-92c6-4839-99d8-57fbb74731fa"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2015%2Fclass%208%20science%20chapter%2015.epub?alt=media&token=dff82e9c-b7a4-4a97-97a6-31708b702c0e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2015%2Fclass%208%20science%20chapter%2015%20cleaned.pickle?alt=media&token=d0a15882-844b-4e68-ba23-4887a111fc9a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2015%2Fclass%208%20science%20chapter%2015%20embedded.pickle?alt=media&token=7fa4086d-b5aa-434d-951d-4cd53155a81a"
    },
    "Chapter16": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2016%2Fclass%208%20science%20chapter%2016.epub?alt=media&token=c449a0a9-0708-46c5-973f-c02c1c7cb7bb",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2016%2Fclass%208%20science%20chapter%2016%20cleaned.pickle?alt=media&token=4ebbe417-7d1a-47a9-b1ff-33517db019ed",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2016%2Fclass%208%20science%20chapter%2016%20embedded.pickle?alt=media&token=80bba4aa-05ef-4f1c-8c48-42574ca8642a"
    },
    "Chapter17": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2017%2Fclass%208%20science%20chapter%2017.epub?alt=media&token=7c32fc84-045d-45c5-af7e-b1fef9c60fd4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2017%2Fclass%208%20science%20chapter%2017%20cleaned.pickle?alt=media&token=dfa334c2-e015-41dd-b86d-a3b2c7ddd262",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2017%2Fclass%208%20science%20chapter%2017%20embedded.pickle?alt=media&token=feca203c-569c-4d21-80e4-49d04eb9efaf"
    },
    "Chapter18": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2018%2Fclass%208%20science%20chapter%2018.epub?alt=media&token=1368c88b-5293-48b0-9c16-6c60208d2431",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2018%2Fclass%208%20science%20chapter%2018%20cleaned.pickle?alt=media&token=06a07fc8-58ea-42e3-8594-212221b8d0f1",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fscience%2Fchapter%2018%2Fclass%208%20science%20chapter%2018%20embedded.pickle?alt=media&token=e42afe86-c82b-4018-a677-1091ecf68fb4"
    }
}

geography8ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%208%20geography%20chapter%201.epub?alt=media&token=90f661f4-f4c7-42d1-83f5-9cb13d3563b6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%208%20geography%20chapter%201%20cleaned.pickle?alt=media&token=d008c103-63ea-4d95-98a6-5fb3e627935c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%208%20geography%20chapter%201%20embedded.pickle?alt=media&token=dffb4541-8450-482c-9f7e-0bf2895258a4"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%208%20geography%20chapter%202.epub?alt=media&token=c724459b-c2bf-4aff-9c00-14e7d0746338",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%208%20geography%20chapter%202%20cleaned.pickle?alt=media&token=0f5e1b6c-3d38-46e4-b16a-c27195c19f9e",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%208%20geography%20chapter%202%20embedded.pickle?alt=media&token=32cd2890-bc65-4a30-9288-cfd92cdb20a5"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%208%20geography%20chapter%203.epub?alt=media&token=02cd3b53-0688-4027-b9fa-f84bfbd518e5",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%208%20geography%20chapter%203%20cleaned.pickle?alt=media&token=b458aa53-fdee-473c-b14f-d53bfd6d4b09",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%208%20geography%20chapter%203%20embedded.pickle?alt=media&token=c8e74be2-97e5-4fe3-a6e0-fd9a6947afd7"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%208%20geography%20chapter%204.epub?alt=media&token=ed93428a-7ba0-4f95-8655-82bd0c5c753e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%208%20geography%20chapter%204%20cleaned.pickle?alt=media&token=83f7c026-1445-4b1b-af62-1aa036c44fa6",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%208%20geography%20chapter%204%20embedded.pickle?alt=media&token=43cf45cc-e806-4cfd-9698-3bb2b01b1438"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%208%20geography%20chapter%205.epub?alt=media&token=ef1de88a-e16a-4335-85db-8f65efd82e6c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%208%20geography%20chapter%205%20cleaned.pickle?alt=media&token=500df78c-12b3-4d34-9d66-1236c5d0c44f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%208%20geography%20chapter%205%20embedded.pickle?alt=media&token=8a0c274a-038e-46b9-94d2-633df9c88e06"
    }

}

history8ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%208%20history%20chapter%201.epub?alt=media&token=646d7e95-039d-4c77-9073-727fb51b46aa",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%208%20history%20chapter%201%20cleaned.pickle?alt=media&token=ce4b7c58-1fa0-42e5-b3e5-058f5f026401",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%208%20history%20chapter%201%20embedded.pickle?alt=media&token=b84ce069-1806-4ca1-b8a7-723f3eca5ad3"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%208%20history%20chapter%202.epub?alt=media&token=29f1e091-279c-46dd-9ec3-7a24b8ed1137",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%208%20history%20chapter%202%20cleaned.pickle?alt=media&token=7ee250db-bbe2-4c47-bf4a-5318d97d668b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%208%20history%20chapter%202%20embedded.pickle?alt=media&token=4b1d4d9d-a874-47aa-9727-b4e96d12887d"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%208%20history%20chapter%203.epub?alt=media&token=92243ddc-de19-434c-a769-e4a8ed4f66d9",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%208%20history%20chapter%203%20cleaned.pickle?alt=media&token=9a31120c-7823-4822-8481-c2dd5ec3aa1d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%208%20history%20chapter%203%20embedded.pickle?alt=media&token=89e2aceb-9c16-4bca-b3d9-bfc18f529a4e"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%208%20history%20chapter%204.epub?alt=media&token=2eb066da-7ec0-4279-8ae3-2609f6a93f8c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%208%20history%20chapter%204%20cleaned.pickle?alt=media&token=bd59fce6-f549-4513-a6ee-fcc268a372e9",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%208%20history%20chapter%204%20embedded.pickle?alt=media&token=8aa307e2-81ea-4a76-a4ce-bd5644b03254"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%208%20history%20chapter%205.epub?alt=media&token=2d76393f-742a-46e6-b9db-c1c2095fa76a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%208%20history%20chapter%205%20cleaned.pickle?alt=media&token=27f0d940-0720-4781-828e-a95b544c743d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%208%20history%20chapter%205%20embedded.pickle?alt=media&token=d8b7ae8d-4b5c-4454-ba88-49cf91fa70ff"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%208%20history%20chapter%206.epub?alt=media&token=10200028-0e97-4391-a95e-479f5e407c11",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%208%20history%20chapter%206%20cleaned.pickle?alt=media&token=6f2fb4f0-22c1-4795-b4e7-1a148ed28ae4",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%206%2Fclass%208%20history%20chapter%206%20embedded.pickle?alt=media&token=9292af1a-2583-4fa8-a454-d11e298d409e"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%208%20history%20chapter%207.epub?alt=media&token=a5786bf3-d284-465d-a62c-e7d8bbc6de6b",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%208%20history%20chapter%207%20cleaned.pickle?alt=media&token=ccaa02e4-e0bc-43a6-8c8a-dc6dbeb3301c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%207%2Fclass%208%20history%20chapter%207%20embedded.pickle?alt=media&token=6b1b5fde-04ef-4a58-befa-9dee035fb0bb"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%208%20history%20chapter%208.epub?alt=media&token=a55f175f-466f-4cd3-bdda-d195b00b860f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%208%20history%20chapter%208%20cleaned.pickle?alt=media&token=2654130e-70c6-4761-a9d6-ca26cbbcc9d5",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%208%2Fclass%208%20history%20chapter%208%20embedded.pickle?alt=media&token=09a14db0-3c36-4ad1-a6bb-f85807558dbd"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%208%20history%20chapter%209.epub?alt=media&token=c7a7c2f3-6593-46c9-95cd-144b45962c8f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%208%20history%20chapter%209%20cleaned.pickle?alt=media&token=20fe6558-1ce0-483f-b96f-a6a7cdf80f08",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%209%2Fclass%208%20history%20chapter%209%20embedded.pickle?alt=media&token=3c51c931-5eaa-4957-bf65-4b2873f46d6c"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%208%20history%20chapter%2010.epub?alt=media&token=48bd3d3a-68be-4628-984f-10cbbb3e767a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%208%20history%20chapter%2010%20cleaned.pickle?alt=media&token=94d04fef-2ade-40bd-b86a-78a97c87a40f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%208th%2Fsocial_science%2Fhistory%2Fchapter%2010%2Fclass%208%20history%20chapter%2010%20embedded.pickle?alt=media&token=66665bce-c318-4e98-9cbc-4f2b8625ed5a"
    }
}

mathematics9ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%201%2Fclass%209%20math%20chapter%201.epub?alt=media&token=a42a604d-9087-4f29-9408-84c07637f53d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%201%2Fclass%209%20math%20chapter%201%20cleaned.pickle?alt=media&token=e5549cb1-2ccb-4fd9-8799-6f6e78657cc5",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%201%2Fclass%209%20math%20chapter%201%20embedded.pickle?alt=media&token=cda2ef19-5030-42be-a387-21d0ed34b315"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%202%2Fclass%209%20math%20chapter%202.epub?alt=media&token=5efd9961-0147-49dd-aa4e-f9949968dd29",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%202%2Fclass%209%20math%20chapter%202%20cleaned.pickle?alt=media&token=11fefdf3-8ffc-4e5b-8fbd-c0a119203251",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%202%2Fclass%209%20math%20chapter%202%20embedded.pickle?alt=media&token=58420f4a-466a-449a-a264-96f6ab31d154"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%203%2Fclass%209%20math%20chapter%203.epub?alt=media&token=1e434129-437f-4f5b-8f9d-e755d482b8a2",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%203%2Fclass%209%20math%20chapter%203%20cleaned.pickle?alt=media&token=d9b0fe68-a9cb-418a-baa1-f98b626eb633",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%203%2Fclass%209%20math%20chapter%203%20embedded.pickle?alt=media&token=2d27c370-90ef-4a3f-bfd5-9f3f765f2b71"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%204%2Fclass%209%20math%20chapter%204.epub?alt=media&token=640ee2e0-fd4a-4c6e-8862-d15c5a9f040d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%204%2Fclass%209%20math%20chapter%204%20cleaned.pickle?alt=media&token=8182d98a-fa79-4fdd-aee6-4d3dfd2f4414",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%204%2Fclass%209%20math%20chapter%204%20embedded.pickle?alt=media&token=4744fad3-c127-4655-b159-60d2fe07b910"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%205%2Fclass%209%20math%20chapter%205.epub?alt=media&token=06d84b99-d196-4bb5-95ef-48661b5c1329",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%205%2Fclass%209%20math%20chapter%205%20cleaned.pickle?alt=media&token=4a1c25bc-cc29-47fe-b48a-b38ec8d2321b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%205%2Fclass%209%20math%20chapter%205%20embedded.pickle?alt=media&token=cbba0d02-b784-4356-9f2c-058d0145b46b"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%206%2Fclass%209%20math%20chapter%206.epub?alt=media&token=4e6a36d5-c792-49c6-9ff9-36ffd7974c92",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%206%2Fclass%209%20math%20chapter%206%20cleaned.pickle?alt=media&token=66de7db5-f7ed-421e-a5b1-f4aab53ecc34",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%206%2Fclass%209%20math%20chapter%206%20embedded.pickle?alt=media&token=44218bf8-f9eb-4e6e-a8f9-54d001c1c78a"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%207%2Fclass%209%20math%20chapter%207.epub?alt=media&token=c69031c6-e897-40fa-83e0-8f6abca7dfea",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%207%2Fclass%209%20math%20chapter%207%20cleaned.pickle?alt=media&token=9aaabb46-aa37-49c3-b301-d4a9312d1012",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%207%2Fclass%209%20math%20chapter%207%20embedded.pickle?alt=media&token=1df17ce1-8698-47d9-94af-a9cd61659ab7"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%208%2Fclass%209%20math%20chapter%208.epub?alt=media&token=22269688-ebae-4e15-a4f8-7738a7710961",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%208%2Fclass%209%20math%20chapter%208%20cleaned.pickle?alt=media&token=e5fa6ccc-b087-4ba0-be43-fcd82045078f",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%208%2Fclass%209%20math%20chapter%208%20embedded.pickle?alt=media&token=f55ea5ab-3412-4523-ad45-801240e10aaa"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%209%2Fclass%209%20math%20chapter%209.epub?alt=media&token=325b780e-fc20-43e6-9492-f9627b35566e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%209%2Fclass%209%20math%20chapter%209%20cleaned.pickle?alt=media&token=cdab3a26-ba5a-4d5d-9eed-6ed855b0846d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%209%2Fclass%209%20math%20chapter%209%20embedded.pickle?alt=media&token=8e929159-d255-47ce-a587-0d8e14405ddb"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2010%2Fclass%209%20math%20chapter%2010.epub?alt=media&token=9547dbe9-b8bf-4bf1-8b49-71228f513d57",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2010%2Fclass%209%20math%20chapter%2010%20cleaned.pickle?alt=media&token=c2f607ba-707e-432b-93fb-22ae9bf60c95",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2010%2Fclass%209%20math%20chapter%2010%20embedded.pickle?alt=media&token=970fcb3d-a5b6-43d2-81f9-8c5b3c2c04a0"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2011%2Fclass%209%20math%20chapter%2011.epub?alt=media&token=7f8cb41c-6334-4335-87b1-0929d643a8df",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2011%2Fclass%209%20math%20chapter%2011%20cleaned.pickle?alt=media&token=3a3ed605-d378-4169-8213-6ef4b24349df",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2011%2Fclass%209%20math%20chapter%2011%20embedded.pickle?alt=media&token=a26d0c38-86eb-41be-82b6-41bb5dbdb5b6"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2012%2Fclass%209%20math%20chapter%2012.epub?alt=media&token=ab3bca01-dfdf-44f1-86f5-b358f0b8580c",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2012%2Fclass%209%20math%20chapter%2012%20cleaned.pickle?alt=media&token=957a0ed2-f9d7-4278-9799-1deab0b03d8b",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2012%2Fclass%209%20math%20chapter%2012%20embedded.pickle?alt=media&token=b14e5fc8-d39c-4280-823e-60cdada84204"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2013%2Fclass%209%20math%20chapter%2013.epub?alt=media&token=35facd85-01de-4c75-809a-bc1799aa1513",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2013%2Fclass%209%20math%20chapter%2013%20cleaned.pickle?alt=media&token=4bf88e4f-268a-47c6-abdf-c133ad4271ed",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2013%2Fclass%209%20math%20chapter%2013%20embedded.pickle?alt=media&token=b86c3b68-e75d-480f-81a3-d34e67e7e832"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2014%2Fclass%209%20math%20chapter%2014.epub?alt=media&token=e5e6da7f-a395-4fd0-8751-b222cf04cb63",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2014%2Fclass%209%20math%20chapter%2014%20cleaned.pickle?alt=media&token=913798c7-dbfe-4724-820d-0b8c7211f019",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2014%2Fclass%209%20math%20chapter%2014%20embedded.pickle?alt=media&token=d976d028-f754-4085-ac44-69d9e8f9621c"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2015%2Fclass%209%20math%20chapter%2015.epub?alt=media&token=eb16c55c-b278-4cc1-8fe4-37a137cf1678",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2015%2Fclass%209%20math%20chapter%2015%20cleaned.pickle?alt=media&token=e4f66abd-20de-411a-98f4-99c5ab8ef9b0",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fmathematics%2Fchapter%2015%2Fclass%209%20math%20chapter%2015%20embedded.pickle?alt=media&token=c189bc4f-21b2-4ad7-ad6d-ab904562df73"
    }

}

science9ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%201%2Fclass%209%20science%20chapter%201.epub?alt=media&token=623c592c-afaf-4254-a0e5-c273b804429e",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%201%2Fclass%209%20science%20chapter%201%20cleaned.pickle?alt=media&token=ffa11ea0-c4f5-49f3-9020-6e03c2c3c55c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%201%2Fclass%209%20science%20chapter%201%20embedded.pickle?alt=media&token=02ba7280-899e-4fca-9773-6c80dc3f031a"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%202%2Fclass%209%20science%20chapter%202.epub?alt=media&token=8f6dd467-3ed2-457e-afe0-ce8e5a737147",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%202%2Fclass%209%20science%20chapter%202%20cleaned.pickle?alt=media&token=b85f4590-b496-441d-b4b8-c8db510168d2",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%202%2Fclass%209%20science%20chapter%202%20embedded.pickle?alt=media&token=fd894878-5246-4737-a5b2-cf21714e91b1"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%203%2Fclass%209%20science%20chapter%203.epub?alt=media&token=db4d143a-b8b2-4980-a020-a730471a180a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%203%2Fclass%209%20science%20chapter%203%20cleaned.pickle?alt=media&token=54cad01c-64c0-4e13-b829-657ed384da2a",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%203%2Fclass%209%20science%20chapter%203%20embedded.pickle?alt=media&token=05554611-c48e-41c4-869b-3c66b6120bfe"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%204%2Fclass%209%20science%20chapter%204.epub?alt=media&token=b57a097e-1e59-4c50-a465-ec0e3426697f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%204%2Fclass%209%20science%20chapter%204%20cleaned.pickle?alt=media&token=1634253b-85ff-4e2e-804f-2ec753409ba6",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%204%2Fclass%209%20science%20chapter%204%20embedded.pickle?alt=media&token=2fc0d28e-9da4-4d40-ad08-78c29ef9a178"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%205%2Fclass%209%20science%20chapter%205.epub?alt=media&token=a851901b-898d-4349-b54b-f0bb0e2aa7ef",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%205%2Fclass%209%20science%20chapter%205%20cleaned.pickle?alt=media&token=3c0017a1-fe37-4c2d-b392-d28843b47fd2",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%205%2Fclass%209%20science%20chapter%205%20embedded.pickle?alt=media&token=7657d9da-92ac-44da-8575-8c1c311fbdca"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%206%2Fclass%209%20science%20chapter%206.epub?alt=media&token=665f1856-90a2-4513-bd89-b0c8530e8de6",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%206%2Fclass%209%20science%20chapter%206%20cleaned.pickle?alt=media&token=ef0fee2f-2540-47be-b675-cb42da8caf09",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%206%2Fclass%209%20science%20chapter%206%20embedded.pickle?alt=media&token=e368dfd8-5628-48fc-8b20-2602f126c661"
    },
    "Chapter7": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%207%2Fclass%209%20science%20chapter%207.epub?alt=media&token=f27888c6-60a6-4adc-bf50-4123f659c2b4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%207%2Fclass%209%20science%20chapter%207%20cleaned.pickle?alt=media&token=44c60a30-ce74-4da6-88a3-fc1afe2de26c",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%207%2Fclass%209%20science%20chapter%207%20embedded.pickle?alt=media&token=92c4240c-44bd-46b4-ab1e-89e2f3b2db37"
    },
    "Chapter8": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%208%2Fclass%209%20science%20chapter%208.epub?alt=media&token=6e68c7e1-f517-41bf-80e2-f00a94c3ef15",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%208%2Fclass%209%20science%20chapter%208%20cleaned.pickle?alt=media&token=89af2618-c40f-4b62-8cec-b0fa083a73f8",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%208%2Fclass%209%20science%20chapter%208%20embedded.pickle?alt=media&token=7bb7b096-ccc0-407e-8d80-f9ac6691a4d5"
    },
    "Chapter9": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%209%2Fclass%209%20science%20chapter%209.epub?alt=media&token=a72c31e0-68d8-43b0-950a-1519e39c8492",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%209%2Fclass%209%20science%20chapter%209%20cleaned.pickle?alt=media&token=166a1618-501c-4d39-a843-ffe5cd2723f6",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%209%2Fclass%209%20science%20chapter%209%20embedded.pickle?alt=media&token=98203770-f05e-4b23-8ecf-13449532bafb"
    },
    "Chapter10": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2010%2Fclass%209%20science%20chapter%2010.epub?alt=media&token=90fcc966-46d9-4c23-a179-8d4a16bc7848",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2010%2Fclass%209%20science%20chapter%2010%20cleaned.pickle?alt=media&token=ddf54c7c-c3bf-4e05-9bbb-490d07487dd2",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2010%2Fclass%209%20science%20chapter%2010%20embedded.pickle?alt=media&token=f2a251c2-85ff-4e90-827e-8b10b71d7b86"
    },
    "Chapter11": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2011%2Fclass%209%20science%20chapter%2011.epub?alt=media&token=c2f44898-71de-404b-b534-7336b5e26950",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2011%2Fclass%209%20science%20chapter%2011%20cleaned.pickle?alt=media&token=e8b9a3ff-dcb2-4490-b60c-490c6ac5b709",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2011%2Fclass%209%20science%20chapter%2011%20embedded.pickle?alt=media&token=96c05667-fde9-493d-9a7b-3643db386db5"
    },
    "Chapter12": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2012%2Fclass%209%20science%20chapter%2012.epub?alt=media&token=d631e772-be88-4f7f-b567-48be0c46b2cc",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2012%2Fclass%209%20science%20chapter%2012%20cleaned.pickle?alt=media&token=fca44afc-620b-4351-b5fc-33ef0b4f4bec",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2012%2Fclass%209%20science%20chapter%2012%20embedded.pickle?alt=media&token=878f2dda-3e61-4cd2-b2d1-bf8917308f18"
    },
    "Chapter13": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2013%2Fclass%209%20science%20chapter%2013.epub?alt=media&token=68282787-bcb7-45c6-bf24-2f5338c5fba4",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2013%2Fclass%209%20science%20chapter%2013%20cleaned.pickle?alt=media&token=54bcec84-78ae-4932-af14-e628ef523d56",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2013%2Fclass%209%20science%20chapter%2013%20embedded.pickle?alt=media&token=7396eda9-d8e2-4f88-a675-09498ef22a25"
    },
    "Chapter14": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2014%2Fclass%209%20science%20chapter%2014.epub?alt=media&token=0dbbe593-a7f2-46f7-8f57-8f5add89677d",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2014%2Fclass%209%20science%20chapter%2014%20cleaned.pickle?alt=media&token=941614a2-f95c-4ac7-b0c6-babfd33fa6c9",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2014%2Fclass%209%20science%20chapter%2014%20embedded.pickle?alt=media&token=1221c121-5c42-4e24-8d5f-442e9ea0bb1f"
    },
    "Chapter15": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2015%2Fclass%209%20science%20chapter%2015.epub?alt=media&token=c7f51886-4ef2-4142-8fda-e1a90115af42",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2015%2Fclass%209%20science%20chapter%2015%20cleaned.pickle?alt=media&token=2282b202-1c5a-494e-986d-5949baee78b0",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fscience%2Fchapter%2015%2Fclass%209%20science%20chapter%2015%20embedded.pickle?alt=media&token=3cbd38fa-9319-47ff-b5c6-ac02636c8470"
    }

}

economics9ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%201%2Fclass%209%20economics%20chapter%201.epub?alt=media&token=5dcd396c-edf6-4f76-85ed-c19646fe3055",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%201%2Fclass%209%20economics%20chapter%201%20cleaned.pickle?alt=media&token=a34481ee-c68e-432b-b9d9-64f6fea1a862",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%201%2Fclass%209%20economics%20chapter%201%20embedded.pickle?alt=media&token=9831f682-9c91-4b66-83e1-9e32611816c8"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%202%2Fclass%209%20economics%20chapter%202.epub?alt=media&token=3834a1ff-040c-418d-896c-fbce21aa4322",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%202%2Fclass%209%20economics%20chapter%202%20cleaned.pickle?alt=media&token=dbd2100a-53c6-4cf2-945e-be6939c87896",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%202%2Fclass%209%20economics%20chapter%202%20embedded.pickle?alt=media&token=5d76ea72-53cb-4d45-bcf8-2e6b983d64d1"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%203%2Fclass%209%20economics%20chapter%203.epub?alt=media&token=45db0e76-80f6-4dd8-8167-f2711a877ef0",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%203%2Fclass%209%20economics%20chapter%203%20cleaned.pickle?alt=media&token=3d2ebd3d-42be-4143-8000-490d5fac36bb",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%203%2Fclass%209%20economics%20chapter%203%20embedded.pickle?alt=media&token=0de46114-612e-4801-a2f4-97f7c30e1bc4"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%204%2Fclass%209%20economics%20chapter%204.epub?alt=media&token=c653fa96-72ac-4188-be66-9690808999da",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%204%2Fclass%209%20economics%20chapter%204%20cleaned.pickle?alt=media&token=f0a79612-9a0a-4a23-963a-ddba69c33ca3",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Feconomics%2Fchapter%204%2Fclass%209%20economics%20chapter%204%20embedded.pickle?alt=media&token=834d8de9-92dc-4daa-ac65-6fcf73cc1cfe"
    }

}

geography9ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%209%20geography%20chapter%201.epub?alt=media&token=f852e53a-f0fc-4d3d-bad3-6410d4fa7956",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%209%20geography%20chapter%201%20cleaned.pickle?alt=media&token=e46bf427-1800-41e9-b240-a8babf16aa4e",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%201%2Fclass%209%20geography%20chapter%201%20embedded.pickle?alt=media&token=1e6ff538-217a-4123-ab64-18d03787a3e8"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%209%20geography%20chapter%202.epub?alt=media&token=5a871b51-bce5-4c87-be5e-c41e3c554c1f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%209%20geography%20chapter%202%20cleaned.pickle?alt=media&token=36481448-40d3-4e1f-9b19-9207ec256c2d",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%202%2Fclass%209%20geography%20chapter%202%20embedded.pickle?alt=media&token=a1836060-85ef-40e6-b93d-7984faebd5af"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%209%20geography%20chapter%203.epub?alt=media&token=6a9fac7b-fe9a-4ccd-96e2-c81482fb58ce",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%209%20geography%20chapter%203%20cleaned.pickle?alt=media&token=c5604fe9-e171-4eae-bf83-69ce4b2be183",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%203%2Fclass%209%20geography%20chapter%203%20embedded.pickle?alt=media&token=7d4305ac-9b15-4fa7-8c92-e23a1594e910"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%209%20geography%20chapter%204.epub?alt=media&token=fa97408c-1466-483e-b1ac-1324fc04dbab",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%209%20geography%20chapter%204%20cleaned.pickle?alt=media&token=a2f023a4-4e15-47a6-9b9d-ed95c9335224",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%204%2Fclass%209%20geography%20chapter%204%20embedded.pickle?alt=media&token=5295035a-90ef-49ea-98ac-c694fff61a75"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%209%20geography%20chapter%205.epub?alt=media&token=3c79c762-efe5-463e-82b6-9aa8775d4366",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%209%20geography%20chapter%205%20cleaned.pickle?alt=media&token=0e94447b-6ea2-4eaa-84b8-e66abc0e0944",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%205%2Fclass%209%20geography%20chapter%205%20cleaned.pickle?alt=media&token=0e94447b-6ea2-4eaa-84b8-e66abc0e0944"
    },
    "Chapter6": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%209%20geography%20chapter%206.epub?alt=media&token=d417116e-45ae-4536-9f68-a8fe701bc2cf",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%209%20geography%20chapter%206%20cleaned.pickle?alt=media&token=d64d5d25-592b-46e8-a54b-628ca6e20918",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fgeography%2Fchapter%206%2Fclass%209%20geography%20chapter%206%20cleaned.pickle?alt=media&token=d64d5d25-592b-46e8-a54b-628ca6e20918"
    }
}

history9ncert01 = {
    "Chapter1": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%209%20history%20chapter%201.epub?alt=media&token=8c6873ee-d81e-455a-b7f3-f61e88a2dd1f",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%209%20history%20chapter%201%20cleaned.pickle?alt=media&token=10e4ad42-c527-4a2f-afef-6dce44e6e004",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%201%2Fclass%209%20history%20chapter%201%20embedded.pickle?alt=media&token=947e8d31-a5e1-47b2-932d-c1fe4c3e9f6c"
    },
    "Chapter2": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%209%20history%20chapter%202.epub?alt=media&token=cb1e69a5-7a57-4161-b0fb-62fb86b3c619",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%209%20history%20chapter%202%20cleaned.pickle?alt=media&token=82740bc8-5978-4135-ac66-c8f17b349230",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%202%2Fclass%209%20history%20chapter%202%20embedded.pickle?alt=media&token=6f3163a8-1c51-4bd9-a9a9-9d362d424c98"
    },
    "Chapter3": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%209%20history%20chapter%203.epub?alt=media&token=5018b197-ad34-409b-ab8c-1920d7c18b28",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%209%20history%20chapter%203%20cleaned.pickle?alt=media&token=4fce1b57-863d-4a11-9990-30bd32409d99",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%203%2Fclass%209%20history%20chapter%203%20embedded.pickle?alt=media&token=2851b9c4-cbd8-4bec-b6e2-6066d91e5376"
    },
    "Chapter4": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%209%20history%20chapter%204.epub?alt=media&token=ff5d31e3-70bd-420d-952d-821b47fc4a9a",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%209%20history%20chapter%204%20cleaned.pickle?alt=media&token=2bb6951f-df5e-448d-98db-3906e4f9766e",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%204%2Fclass%209%20history%20chapter%204%20embedded.pickle?alt=media&token=20f4f492-a49b-4e84-9d3f-b46ca6d78d65"
    },
    "Chapter5": {
        "EPUB_link": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%209%20history%20chapter%205.epub?alt=media&token=270d952d-ba88-4c66-84df-51d9fea0ca55",
        "Text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%209%20history%20chapter%205%20cleaned.pickle?alt=media&token=59cad51f-5de1-4770-a909-28736abf92d7",
        "Embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%209th%2Fsocial_science%2Fhistory%2Fchapter%205%2Fclass%209%20history%20chapter%205%20embedded.pickle?alt=media&token=ad0914ee-e842-4353-9a78-496744ef4a1f"
    }

}

mathematics10cbseqp = {"2011": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011_emb.pickle?alt=media&token=8cda6557-326e-407d-997d-6736e3a9114f",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011_text.pickle?alt=media&token=2fd2e82f-9da4-4bcd-96d0-6e551cc7b273",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011.epub?alt=media&token=3c2f09ea-bed4-419b-abc3-1430836427c7",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011_cluster.pkl?alt=media&token=ab494bc1-854a-4f8c-8a06-6dea944706e5"},
    "2012": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012_emb.pickle?alt=media&token=b6607530-602f-435e-8c56-f5cb39372529",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012_text.pickle?alt=media&token=72034f2a-f4d4-44e9-b466-ae579852cdaa",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012.epub?alt=media&token=3a083886-f4fc-42d5-ba0c-14a468e30601",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012_cluster.pkl?alt=media&token=f67747f1-806a-482d-88c0-e965f359e90a"},
    "2013": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013_emb.pickle?alt=media&token=be5a7c13-57d6-45a4-8227-9f5a23aadcb4",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013_text.pickle?alt=media&token=085995bf-c6c2-469d-8c9b-2e2c29817823",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013.epub?alt=media&token=bf2d9a38-adca-4064-894d-d81fff516945",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013_cluster.pkl?alt=media&token=e730e294-0d8b-445c-8cd0-a7f43fb0cf86"},
    "2014": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_emb.pickle?alt=media&token=6059a573-8134-479e-9c98-8ba29f512150",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_text.pickle?alt=media&token=ddb22b32-2333-40d2-9597-223f37a69129",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_1.epub?alt=media&token=363d59c8-038d-4f18-ae44-1e7730dcb98b",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_cluster.pkl?alt=media&token=4993788d-db82-4346-b10d-e1dea29060b4"},
    "2015": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_emb.pickle?alt=media&token=2d882810-7617-4f06-85be-400e7bb1cffc",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_text.pickle?alt=media&token=d3298f7d-ae95-4064-bd33-55817c9e48f2",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_1.epub?alt=media&token=1ad7b23b-7d10-4c94-9498-737089d49ea3",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_cluster.pkl?alt=media&token=0ffff999-3d27-4525-af8f-b4f35e188dff"},
    "2016": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_emb.pickle?alt=media&token=57879e83-2b6d-4bcc-980e-53b06b14a531",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_text.pickle?alt=media&token=d4324089-63c3-440d-9333-a6bf48601c1d",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_1.epub?alt=media&token=202282e2-587c-4c75-8a42-293da97a0e21",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_cluster.pkl?alt=media&token=6fe31eb4-2b50-4ffa-9051-ef4152ace5f0"},
    "2017": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_emb.pickle?alt=media&token=b0012395-71d5-4b3b-888d-292ffa296596",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_text.pickle?alt=media&token=eef25d2a-56df-4d0c-b7f0-c8e455836772",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_1.epub?alt=media&token=e0f6a475-555d-4d4f-84f9-efa05cec90f5",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_cluster.pkl?alt=media&token=172829ed-39c4-49ba-b09f-553f2940fd64"},
    "2018": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018_emb.pickle?alt=media&token=e9a90d3a-e258-4385-a803-ce1efcbd6994",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018_text.pickle?alt=media&token=b12517e7-b241-4861-8a47-63e639d8508d",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018.epub?alt=media&token=6288245c-4bdd-4a9c-bc5b-b83276bcf8dd",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018_cluster.pkl?alt=media&token=ca996f8b-4f33-4588-998e-9fa3c1678aa4"},
    "2019": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019_emb.pickle?alt=media&token=6da2b71d-a8a5-4838-9abe-08f265714dda",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019_text.pickle?alt=media&token=5788071e-157b-4c75-955d-cbb1e915d5b8",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019.epub?alt=media&token=76097a32-ceda-4c7d-820e-01f2934f92f6",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019_cluster.pkl?alt=media&token=6d23adaf-91df-4a76-b273-67bd4ded1c51"}
}

science10cbseqp = {"2012": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2012_embedded.pickle?alt=media&token=4b94da89-3467-406d-be10-78a0a141d12f",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2012.pickle?alt=media&token=a09e4d73-6d01-4c38-9d9c-79ab508c6f9a",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2012.epub?alt=media&token=fb00f8e4-5bbb-4024-8837-ace3058794f4",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_12_cluster.pickle?alt=media&token=2fbf1661-5b74-4890-94fc-8ce879c9e30c"},
    "2013": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2013_embedded.pickle?alt=media&token=160b758d-4437-4228-b09a-d6a57864e712",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2013.pickle?alt=media&token=5dc4282d-ce8b-4cde-aca1-930dbec1dcc0",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2013.epub?alt=media&token=a4350843-053a-4039-88b1-cc82098e6429",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_13_cluster.pickle?alt=media&token=6bfbd88b-330b-43b9-b549-ae72f60994c0"},
    "2014": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2014_embedded.pickle?alt=media&token=7d616642-4b38-42fc-acda-2507988a438f",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2014.pickle?alt=media&token=bb57dccb-32a5-4f93-b0de-c487dc15c3d4",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2014.epub?alt=media&token=e2dfe2f8-e3f6-4618-be02-c2b1b3904385",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_14_cluster.pickle?alt=media&token=97cdb137-8f5d-4018-b6b8-d8938cb1486c"},
    "2015": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2015_embedded.pickle?alt=media&token=1a013130-1997-4f94-9495-89234ca0e57d",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2015.pickle?alt=media&token=cf2343a7-0b65-41e9-ad13-6c20189be5fa",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2015.epub?alt=media&token=cbb9f2fa-1a6c-4b8f-a3de-9c609bd50e66",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_15_cluster.pickle?alt=media&token=08a215af-d2d1-4a81-b5d7-c5bc4b183c24"},
    "2016": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2016_embedded.pickle?alt=media&token=ddeb871b-c8c8-4d2e-88d3-a9d366199aed",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2016.pickle?alt=media&token=bdbe32d7-a210-40b4-b5b4-9613127d3081",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2016.epub?alt=media&token=9aa3b919-a69d-40cc-8672-869fa551d823",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_16_cluster.pickle?alt=media&token=8e113cde-bdde-4629-9808-d6a01ee780aa"},
    "2017": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2017_embedded.pickle?alt=media&token=a95c58e2-043c-4658-b918-7ce16bdb1d42",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2017.pickle?alt=media&token=590f275a-b9c0-4b20-b9fc-75fd47235d10",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2017.epub?alt=media&token=75a13f78-afe5-4e68-a62f-b7f7b4458ad0",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_17_cluster.pickle?alt=media&token=34acff80-aa59-4890-888f-e185851bc7d3"},
    "2018": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2018_embedded.pickle?alt=media&token=782894fb-0472-4ae6-baaf-7e6f8a4b28a4",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2018.pickle?alt=media&token=9c6f79d8-f1c8-40fb-8f7f-f1fec10d700d",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_2018.epub?alt=media&token=8bf45d36-c5a6-4bc3-822c-2728e2d0d4dd",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_18_cluster.pickle?alt=media&token=b8d1d027-4449-41a7-836d-0b95d5175c77"},
    "2019": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2019_embedded.pickle?alt=media&token=6fe10feb-cff4-450a-ba34-026fc88e3553",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2019.pickle?alt=media&token=a2b8cf88-6ba2-4105-8fc6-18c249a082d3",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_2019.epub?alt=media&token=1f733f27-9e27-48a5-9228-0a31a73c553d",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_19_cluster.pickle?alt=media&token=c0304f99-d672-4682-8289-ee0e01a7cfec"},
    "2020": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2020_embedded.pickle?alt=media&token=be6dc2c3-23cd-4a00-9492-1f8e43193079",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2020.pickle?alt=media&token=6aa78b26-a43c-4b22-84c7-1a799667c4d5",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_2020.epub?alt=media&token=2ea3c96d-1701-44a2-9681-65e9b7db65c1",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_20_cluster.pickle?alt=media&token=799a09f8-3b85-4005-9735-3d471bc98620"},
}

socialScience10cbseqp = {"2011": {
    "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst_emb.pickle?alt=media&token=363887b5-c9b6-4691-b73d-0dd6480dc620",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst_text.pickle?alt=media&token=8a89723b-89ce-4b42-960e-1a19765419a9",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst.epub?alt=media&token=58b1fe97-28b6-4ae6-958a-1a94e480021a",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst_cluster.pkl?alt=media&token=6a54309a-5078-4b91-a2f5-aceeb3373c96"},
    "2012": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst_emb.pickle?alt=media&token=73d24331-048b-4c41-8d8d-bfb69b2896ea",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst_text.pickle?alt=media&token=d1923f9d-37a4-40c2-b236-f130b4fd1c1c",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst.epub?alt=media&token=aa3cd7a5-622e-4677-afc7-b023ab518bd8",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst_cluster.pkl?alt=media&token=eb422dee-51a6-4ee3-96b4-e8d77f876640"},
    "2013": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst_emb.pickle?alt=media&token=b95f954e-9720-467a-a432-f4e13b3e4ee4",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst_text.pickle?alt=media&token=ca43166a-e8a5-4f42-976f-031ab16fb664",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst.epub?alt=media&token=f13e65f4-359d-4954-ae41-d00ff5b7621a",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst_cluster.pkl?alt=media&token=3711354b-d97c-48cd-8cfa-51350124603a"},
    "2014": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst_emb.pickle?alt=media&token=39bd27d0-ce0b-4c00-8b50-57ebee5f998a",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst_text.pickle?alt=media&token=297de573-404b-4157-b90a-3711dd0b07dd",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst.epub?alt=media&token=be5fdd8a-413c-47de-8e70-ff47be747c1e",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst_cluster.pkl?alt=media&token=c04fedcc-f3ab-4ce6-b645-b27bc807edf1"},
    "2015": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst_emb.pickle?alt=media&token=2a254d25-5fe6-4096-90fc-b43148c895fb",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst_text.pickle?alt=media&token=387bcc97-b17e-432e-8cfb-49afbd166a79",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst.epub?alt=media&token=116a0129-d20e-4201-a2f1-2d37ba15edcd",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst_cluster.pkl?alt=media&token=c98eb266-be78-48f9-8ce0-40f5a74b35a8"},
    "2016": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst_emb.pickle?alt=media&token=4dfc4f4d-b3c7-4471-a46a-1525512c97a7",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst_text.pickle?alt=media&token=edfb98ed-cd29-41bd-9571-c9b5ee369387",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst.epub?alt=media&token=a370fcd8-4068-4522-8cfd-569efe237525",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst_cluster.pkl?alt=media&token=669dd222-bc2d-4447-bbf1-9e29ed15285d"},
    "2017": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst_emb.pickle?alt=media&token=e4ec2f4d-34be-4581-a06d-3a74c9f90f3c",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst_text.pickle?alt=media&token=8b496bb1-e8fc-4087-9d5d-b9398ca0dece",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst.epub?alt=media&token=70a3c4fa-34ac-435e-b446-09750eab3ea3",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst_cluster.pkl?alt=media&token=7f67e795-c3be-4d3b-a558-9b04b738680c"},
    "2018": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst_emb.pickle?alt=media&token=1d4eeb73-4d34-41b4-9d3a-4aec87a37ad8",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst_text.pickle?alt=media&token=19d92b13-eee5-46a3-b399-46b8010e2bb2",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst.epub?alt=media&token=7c47228e-6238-4fa8-9b75-dc0c09de74c9",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst_cluster.pkl?alt=media&token=e59f092d-c044-444d-97aa-c3773f6ab89f"},
    "2019": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst_emb.pickle?alt=media&token=5aa4f8e6-6c1f-4691-9bd0-6c746edc5a3d",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst_text.pickle?alt=media&token=93b2936e-3aad-4b63-ae0e-72e602371181",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst.epub?alt=media&token=da1bedff-36df-4989-8902-3e4f04a11908",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst_cluster.pkl?alt=media&token=b2bf2d98-05a9-433b-800f-c9d71e978557"},
    "2020": {
        "chapterImageURL": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/live%20books%20cover%20images%2F10th_qp_cover.png?alt=media&token=1280ddb3-de67-43aa-a959-51fd28313364",
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst_emb.pickle?alt=media&token=0c548d9a-e88a-4fb5-99bb-c5c81b34690d",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst_text.pickle?alt=media&token=a80797ba-6ee0-4256-8943-594268b619c0",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst.epub?alt=media&token=2c5fa47a-e196-4541-85ae-4c97fc22d3a5",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst_cluster.pkl?alt=media&token=629ca8d7-250d-4a34-8b94-0e34fcde88d7"}
}

accountancy12cbseqp = {"2015": {
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2015_acc_emb.pickle?alt=media&token=8f020c26-c16a-46be-a10c-b4334328d4e5",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2015_acc_text.pickle?alt=media&token=5aafcc80-c61d-485e-b639-6f8ea1629d5b",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2015_acc.epub?alt=media&token=38407e85-52f1-49d3-861e-6a288719a62e",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2015_acc_cluster.pkl?alt=media&token=a41af5ff-fe50-4ea2-94bc-54044f4b740e"},
    "2016": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2016_acc_emb.pickle?alt=media&token=66707a5f-8999-44cd-b903-3ef49f339059",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2016_acc_text.pickle?alt=media&token=9a5cad85-023b-4850-bef0-be9c0b47be4e",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2016_acc.epub?alt=media&token=7be40382-f244-46b8-b18d-f30095e7ae29",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2016_acc_cluster.pkl?alt=media&token=3b05141d-8ef9-4baf-bfa7-7f71f79df5ac"},
    "2017": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2017_acc_emb.pickle?alt=media&token=85ba1b13-cb25-4c29-b426-5c6f3230ae88",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2017_acc_text.pickle?alt=media&token=bbd9bb95-c243-409a-97d7-05d81ba52eb1",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2017_acc.epub?alt=media&token=4de307fa-df38-4afe-b0e5-ce98b443478c",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2017_acc_cluster.pkl?alt=media&token=3e4d6171-81d8-49d1-8176-38680742b6d6"},
    "2018": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2018_acc_emb.pickle?alt=media&token=9226a27e-f3cc-4345-9f1e-a14f61f0b69c",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2018_acc_text.pickle?alt=media&token=f65bc3a5-e2b5-4450-99ab-26b2f6e91993",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2018_acc.epub?alt=media&token=2ddcebb3-85cd-4761-b70d-29c99e75d941",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2018_acc_cluster.pkl?alt=media&token=29b0a5bd-779c-494e-a910-0b3eedb17d4d"},
    "2019": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2019_acc_emb.pickle?alt=media&token=82cad36f-5cf9-44f1-a70d-762b6c438f57",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2019_acc_text.pickle?alt=media&token=857ec26f-8346-49c1-a609-0103bbda7fe7",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2019_acc.epub?alt=media&token=c41d52de-59f3-4cfe-b3f2-48d285fe815d",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2019_acc_cluster.pkl?alt=media&token=d7421fcd-4f2d-49a9-a47f-9169c392fb15"},
    "2020": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2020_acc_emb.pickle?alt=media&token=f6259ab0-77b1-48db-a1a7-52cde847479a",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2020_acc_text.pickle?alt=media&token=f878dfe4-2c5d-4343-8c42-f07b4c52a40d",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2020_acc.epub?alt=media&token=0ee8da77-2c4f-4285-88a4-42e91aec1482",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Faccountancy%2F2020_acc_cluster.pkl?alt=media&token=81a92835-b899-4d06-8540-05e3a0f06824"}
}

biology12cbseqp = {"2011": {
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2011_epub_emb.pickle?alt=media&token=74c5f18b-10d5-4d68-b787-878798130dc0",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2011_epub_text.pickle?alt=media&token=c2f8bb37-016f-4b37-9992-195b3fa1c36a",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2011_epub.epub?alt=media&token=f5bcc94d-823a-4ec9-a336-e7e72f9a08b1",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2011_epub_cluster.pkl?alt=media&token=dd7e28f1-3a15-4175-a25f-e140ae658682"},
    "2012": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2012_epub_emb.pickle?alt=media&token=48d3a9e1-a75f-40ff-8136-79b4a84fe529",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2012_epub_text.pickle?alt=media&token=c9db7e9d-0560-48ba-9474-010eb8f429b0",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2012_epub.epub?alt=media&token=4a7a14dd-40be-439a-96aa-890ca1b97095",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2012_epub_cluster.pkl?alt=media&token=8163141f-b392-4d5b-a4be-e76f9a16eff7"},
    "2013": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2013_epub_emb.pickle?alt=media&token=c34154b5-cdcf-4971-8610-7987c1af1ffe",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2013_epub_text.pickle?alt=media&token=3595f23f-1301-4071-9c60-772e417054c2",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2013_epub.epub?alt=media&token=e48b9adb-8bfd-47cb-8f09-2234ae48e4b8",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2013_epub_cluster.pkl?alt=media&token=bc2ed5a3-90d1-4a43-b103-3139c8b1b4de"},
    "2014": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2014_epub_emb.pickle?alt=media&token=bd4c46f7-c37c-4a82-b7d4-0ec89b5bcbad",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2014_epub_text.pickle?alt=media&token=aabee756-9cc8-4ace-b056-7093bceea18f",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2014_epub.epub?alt=media&token=5166fcaa-fd79-40cb-9b04-f2c582398b21",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2014_epub_cluster.pkl?alt=media&token=be52c51c-7757-4103-be51-fd9b234733ec"},
    "2015": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2015_epub_emb.pickle?alt=media&token=45a3416e-656e-4561-b1a6-18606d689db0",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2015_epub_text.pickle?alt=media&token=affd3ed3-d5ac-4d1e-b2f4-31ed81b7a522",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2015_epub.epub?alt=media&token=cb1058a5-9e2e-4e16-8359-71f8c6f03b4a",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2015_epub_cluster.pkl?alt=media&token=3048be66-1eb5-4d3a-81aa-dba45bacd751"},
    "2016": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2016_epub_emb.pickle?alt=media&token=583426d0-98d9-496b-bb57-42eb85807d4c",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2016_epub_text.pickle?alt=media&token=b8a99093-9076-4ac2-8938-224215a2f1ea",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2016_epub.epub?alt=media&token=09cc12b5-b39b-4cb9-b26d-e4a407d3c899",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2016_epub_cluster.pkl?alt=media&token=10938851-2529-4d83-a8cc-9b1fe80a4705"},
    "2017": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2017_epub_emb.pickle?alt=media&token=5bc7038e-39a1-4dc2-aaac-7fbf733455d4",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2017_epub_text.pickle?alt=media&token=8f570306-4a14-4045-bd1d-5623fcc24eaa",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2017_epub.epub?alt=media&token=785026f6-ca98-4765-b08f-10bbe98c5d01",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2017_epub_cluster.pkl?alt=media&token=7ee1178d-899e-4845-a536-810ca3ec29f4"},
    "2018": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2018_epub_emb.pickle?alt=media&token=e8f1b2a9-5c39-4d17-bcc1-c5ed5efafd9f",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2018_epub_text.pickle?alt=media&token=bfe0d990-2556-40d2-8ac6-b68eecc4bdb7",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2018_epub.epub?alt=media&token=5f3f91ed-7ada-43b0-bbdb-603563c0484e",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2018_epub_cluster.pkl?alt=media&token=9694f3e3-b33f-4c8f-bcb2-d0d9b0b4d723"},
    "2019": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2019_epub_emb.pickle?alt=media&token=d0fd76fd-5e88-4ee9-bb9c-e80e14cc657c",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2019_epub_text.pickle?alt=media&token=87682dee-65f2-45f7-93a8-0a6e6666edd5",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2019_epub.epub?alt=media&token=02193fb4-8cf8-4615-9388-c20bf4077d58",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2019_epub_cluster.pkl?alt=media&token=2876065b-5f79-405c-ba9b-6d87c4abaeeb"},
    "2020": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2020_epub_emb.pickle?alt=media&token=c3956090-6502-48b6-b653-f5bb6bf3d34b",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2020_epub_text.pickle?alt=media&token=b2072498-d410-4359-b3df-26fcfb919cd3",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2020_epub.epub?alt=media&token=b2854b3a-d6f5-4dfe-bb6f-132c42f13d7d",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbiology%2F2020_epub_cluster.pkl?alt=media&token=41f73228-c842-465d-b2bf-847009e1ca35"}
}

businessStudies12cbseqp = {"2012": {
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_12_emb.pickle?alt=media&token=3842f018-138e-4199-b016-e0b76c3ef293",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_12_text.pickle?alt=media&token=99297e7a-2876-4713-809f-03ac472adfa5",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_12_epub.epub?alt=media&token=98e15e29-9d88-4d11-ae7b-b3a8a3e4a42d",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_12_cluster.pkl?alt=media&token=56b5ec5f-d7dc-4442-aaad-863f0c0873f5"},
    "2013": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_13_emb.pickle?alt=media&token=2c1b88c4-c3b1-4aee-b40a-5117fce61739",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_13_text.pickle?alt=media&token=b7368881-1d8c-4dd0-91a8-d25a4edc70d5",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_13_epub.epub?alt=media&token=60d7dfed-db82-4f16-b487-30be23c134de",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_13_cluster.pkl?alt=media&token=4a0ffeb7-2a52-4a5a-a24a-ccbf442fb24b"},
    "2014": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_14_emb.pickle?alt=media&token=94ceed91-af2c-418b-854a-9166ea60fece",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_14_text.pickle?alt=media&token=e00bc804-fce2-4d1a-b52c-f067d762cbd2",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_14_epub.epub?alt=media&token=829a72d2-7add-42ba-9827-7d7083823b93",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_14_cluster.pkl?alt=media&token=15d610a0-cc5f-4774-ab86-cc7ddad2e2ab"},
    "2015": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_15_emb.pickle?alt=media&token=d5e274f1-b578-45f8-8353-3bfa724acf12",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_15_text.pickle?alt=media&token=4d723b99-179f-4e67-886e-a0548da536bc",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_15_epub.epub?alt=media&token=a337eba3-a468-492e-bd2b-38c62533c0c3",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_15_cluster.pkl?alt=media&token=99487af3-cf4d-48e7-bb52-64e011328c9a"},
    "2016": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_16_emb.pickle?alt=media&token=0a6f1092-9e69-4e4d-a734-8af7cab52471",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_16_text.pickle?alt=media&token=4a3cb40c-fb8d-475e-b51e-88a3ab98a425",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_16_epub.epub?alt=media&token=f99e4b47-0fed-4fdb-a1f7-4873daa70b26",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_16_cluster.pkl?alt=media&token=cb2c569f-7dbe-4453-9db9-54e93432fa01"},
    "2018": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_18_emb.pickle?alt=media&token=3c2332c7-dbb7-4914-8d1d-c7005130e2bb",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_18_text.pickle?alt=media&token=0a4e624d-bd03-4009-aa6e-64b463dbabe1",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_18_epub.epub?alt=media&token=2af36108-cdb1-4c76-9e93-fccb2ecbaf69",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_18_cluster.pkl?alt=media&token=6dddcf3b-eda0-49ea-b246-3f3354c58bb8"},
    "2019": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_19_emb.pickle?alt=media&token=8d3c40fe-bc98-4106-96a2-42689e7abec5",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_19_text.pickle?alt=media&token=a7dfbf5a-06d0-453d-81f1-fb1cda39e644",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_19_epub.epub?alt=media&token=b6fe5bd2-04ae-4aac-9f09-98a87aa2e3c4",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fbusiness%20studies%2Fbusiness_19_cluster.pkl?alt=media&token=6350b239-b69a-43a4-b620-83ede56d0530"}
}

chemistry12cbseqp = {"2012": {
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2012_chem12_emb.pickle?alt=media&token=19f4377b-7770-4d3f-b892-dd031122a5bb",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2012_chem12_text.pickle?alt=media&token=9aa3ec1d-1650-4185-9b80-3135dc84a77e",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2012_chem12.epub?alt=media&token=c5cef708-337d-4bbb-a47b-6c178c079077",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2012_chem12_cluster.pkl?alt=media&token=96815786-70ef-43af-a7de-598ea52799a9"},
    "2013": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2013_chem12_emb.pickle?alt=media&token=57bdd2de-0182-4ab4-9d69-1649568854ef",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2013_chem12_text.pickle?alt=media&token=aba50eb2-68dd-4d92-bdbe-e7ecb0e18252",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2013_chem12.epub?alt=media&token=11d169a7-095a-4bc0-add6-17dba1c2c1d5",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2013_chem12_cluster.pkl?alt=media&token=b476e69e-9219-485b-8ac2-f5aeca523183"},
    "2014": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2014_chem12_emb.pickle?alt=media&token=9ab741a4-16a5-4a19-b8fd-795fd2c914af",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2014_chem12_text.pickle?alt=media&token=16236db8-2438-4bf6-ae34-080a7215d551",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2014_chem12.epub?alt=media&token=12939eb4-5e41-433c-82e6-904454f7bd16",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2014_chem12_cluster.pkl?alt=media&token=b6a33117-0c08-42d7-9b24-b2cee751c541"},
    "2015": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2015_chem12_emb.pickle?alt=media&token=6abd9c28-fd66-463f-ac98-4e496e575dbd",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2015_chem12_text.pickle?alt=media&token=2b8ea9e8-cb90-4d73-8b60-ca0d55fa7457",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2015_chem12.epub?alt=media&token=f831cf30-38f5-43f0-932d-2a253fdbc610",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2015_chem12_cluster.pkl?alt=media&token=580d90b6-b1ba-4eab-bc37-26671f623ff6"},
    "2016": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2016_chem12_emb.pickle?alt=media&token=6bc3f7a7-1af2-4638-8d5a-237d79fe9c70",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2016_chem12_text.pickle?alt=media&token=ba7bc64a-4ff2-4c62-ad98-bb4cc3939afb",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2016_chem12.epub?alt=media&token=1d23f653-48e6-4aad-82d1-069891e4f766",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2016_chem12_cluster.pkl?alt=media&token=1b9aaeb2-af50-4de9-92ea-9c209fd8a40c"},
    "2017": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2017_chem12_emb.pickle?alt=media&token=ca4fd241-ee4a-4535-bf27-76be694e2d1c",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2017_chem12_text.pickle?alt=media&token=0d703e6b-2d3a-453d-b499-37c8189f8de7",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2017_chem12.epub?alt=media&token=4830f2c4-c3c0-4dd8-9750-485b6b1d78e6",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2017_chem12_cluster.pkl?alt=media&token=c7ca9a9a-0bd3-4804-82c7-f4a4b76c3c1c"},
    "2018": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2018_chem12_emb.pickle?alt=media&token=cab5c285-1b2a-4fea-b03b-b0b66a465aac",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2018_chem12_text.pickle?alt=media&token=c285daae-42d3-47a3-b293-c20c6b3c1240",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2018_chem12.epub?alt=media&token=f791e005-0af6-4940-807f-c8037b52986d",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2018_chem12_cluster.pkl?alt=media&token=03b36e22-d583-4af5-a73f-7395882f9966"},
    "2019": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2019_chem12_emb.pickle?alt=media&token=a06cfb4c-fbef-48fa-8f1e-6aba9940559d",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2019_chem12_text.pickle?alt=media&token=98cdea83-8958-4fbc-9137-467139cb30aa",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2019_chem12.epub?alt=media&token=887e5187-2c1e-4cdd-8f1d-e483f25b3885",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2019_chem12_cluster.pkl?alt=media&token=dc05797b-39eb-4c84-85c7-4e9edee1c337"},
    "2020": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2020_chem12_emb.pickle?alt=media&token=16bb3889-3def-4a25-bcd6-cb4fdedaf7ce",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2020_chem12_text.pickle?alt=media&token=ac5fc4c7-4d6f-490b-9463-9af197d661b9",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2020_chem12.epub?alt=media&token=b8a357c5-694e-4073-874f-26c018d56b7f",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2020_chem12_cluster.pkl?alt=media&token=1ce0d74a-fdfb-480e-b032-dc9e76f4f7e7"},
    "2021": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2021_chem12_emb.pickle?alt=media&token=305e6858-ea9a-4447-91f5-ebf70e31729c",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2021_chem12_text.pickle?alt=media&token=c9e7a8c6-a59d-4bdb-81d1-c032b5c49535",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2021_chem12.epub?alt=media&token=31be4d00-30bc-41ef-8738-43305d9dbe8f",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fchemistry%2F2021_chem12_cluster.pkl?alt=media&token=dd56203c-828b-4d29-ba87-962b8ff6574b"}
}

history12cbseqp = {"2011": {
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2011%2FCBSE%202011%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=2dbeb7ff-07a6-4638-8ff8-5a9279d994f9",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2011%2FCBSE%202011%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=58eb211b-8634-44d4-9f4b-a5b3a5aaaa4b",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2011%2FCBSE%202011%20class%2012%20history%20paper.epub?alt=media&token=32d2c32a-ec20-4855-a62e-41b8d7a956f2",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2011%2FCBSE%202011%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=ab7dc33c-cb36-496c-8d59-b7342a1e2e43"},
    "2012": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2012%2FCBSE%202012%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=d43019ef-d910-4cbc-bf43-23320eda2e02",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2012%2FCBSE%202012%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=11d4dd86-4c4e-4b5b-b4ba-3d3666f4708a",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2012%2FCBSE%202012%20class%2012%20history%20paper.epub?alt=media&token=6cd20aca-e3c9-4d1f-a76e-9576e70da6fa",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2012%2FCBSE%202012%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=a86ebe9b-c7b1-43c3-b7aa-95f817829ed6"},
    "2013": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2013%2FCBSE%202013%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=17e694ac-db0d-4837-a0dd-a9b417af8657",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2013%2FCBSE%202013%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=cd1136f2-6035-4e5f-9c5c-dbe98ea62505",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2013%2FCBSE%202013%20class%2012%20history%20paper.epub?alt=media&token=b3504323-30aa-48d2-bf1d-54b5dbc21c84",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2013%2FCBSE%202013%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=e930e6d3-eac3-42e4-b7e4-dace5ebddc7e"},
    "2014": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2014%2FCBSE%202014%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=66fc76cb-816c-48b1-8d2c-7c2629c9ad33",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2014%2FCBSE%202014%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=3cf10f7f-87c6-4129-be1d-7e852a69d17f",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2014%2FCBSE%202014%20class%2012%20history%20paper.epub?alt=media&token=33b4ee3c-4b89-47ca-b7aa-3cc76fa4c75d",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2014%2FCBSE%202014%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=98f42932-30e8-4857-97ca-ee4c3aafaa09"},
    "2015": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2015%2FCBSE%202015%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=7f5abe7f-c3c0-4f33-9e10-eaf756266d39",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2015%2FCBSE%202015%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=77eb84ba-ecfa-413f-a776-fb4dbb476c1d",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2015%2FCBSE%202015%20class%2012%20history%20paper.epub?alt=media&token=b7dcaaf1-1722-44d1-8f63-4ac8304b816b",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2015%2FCBSE%202015%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=2d3f4e93-40c9-4b74-b1bf-d992d645b0e4"},
    "2016": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2016%2FCBSE%202016%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=aaed3040-94ea-4e15-944f-7b9f9bcfbf37",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2016%2FCBSE%202016%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=dd0001bf-62a9-482f-ac3f-d53be7ea5387",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2016%2FCBSE%202016%20class%2012%20history%20paper.epub?alt=media&token=da9de484-ef73-49b8-945e-9f0ef0fa3bea",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2016%2FCBSE%202016%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=9c0d8edd-0b36-428f-b8c3-0d0b4abd8f0f"},
    "2017": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2017%2FCBSE%202017%20class%2012%20history%20paper%20embedded.pickle?alt=media&token=7b029c19-b4b5-4d89-a00c-df4cc730929e",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2017%2FCBSE%202017%20class%2012%20history%20paper%20cleaned.pickle?alt=media&token=bd5ccfa0-3618-4c18-9845-b93c45413356",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2017%2FCBSE%202017%20class%2012%20history%20paper.epub?alt=media&token=cc7cdd86-85ba-42df-b1a9-95c3117dfec3",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2017%2FCBSE%202017%20class%2012%20history%20paper%20embedded%20cluster.pickle?alt=media&token=57a84c8a-b4da-4e26-ba79-d8b76fce318b"},
    "2018": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2018%2FCBSE%202018%20class%2012%20history%20question%20paper%20embedded.pickle?alt=media&token=b77763c5-0560-47fa-9d14-0940a433fde1",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2018%2FCBSE%202018%20class%2012%20history%20question%20paper%20cleaned.pickle?alt=media&token=5b0bb4db-92ec-4ceb-9fef-b7963d40164a",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2018%2FCBSE%202018%20class%2012%20history%20question%20paper.epub?alt=media&token=59bcbae8-a943-49b6-969f-d2043f67e8cf",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fhistory%2F2018%2FCBSE%202018%20class%2012%20history%20question%20paper%20embedded%20cluster.pickle?alt=media&token=150e3ccc-dfe2-4273-bf9b-1cbfcb97c9c9"}
}

physics12cbseqp = {"2011": {
    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2011%2Fpaper11_emb?alt=media&token=d1a59882-ad59-4c74-a38e-3754a03cbbe1",
    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2011%2Fquestion_paper_2011?alt=media&token=72678eff-03b7-4bb2-b218-08a6e0040ddc",
    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2011%2F2011.epub?alt=media&token=d0f87f5a-cc41-49f2-aa50-a41b3407b530",
    "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2011%2Fcluster11_model?alt=media&token=3506210a-14f0-4668-869b-d880298182be"},
    "2012": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2012%2Fpaper12_emb?alt=media&token=9b53fe92-df63-4d07-be5f-94327e93b23e",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2012%2Fquestion_paper_2012?alt=media&token=4183fa4a-8dbf-4ed2-9ac5-f38e049484af",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2012%2F2012.epub?alt=media&token=d9d8c6e5-0f05-45d4-aa75-24f9b7b35c09",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2012%2Fcluster12_model?alt=media&token=d5759878-bfc4-4125-9760-d00686887674"},
    "2013": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2013%2Fpaper13_emb?alt=media&token=9d98cbd7-e85d-4ff6-a76b-d38ee834c722",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2013%2Fquestion_paper_2013?alt=media&token=2e7247d7-0afb-4b3d-865d-4a63cf4f27ae",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2013%2F2013.epub?alt=media&token=716dd35e-5d0b-4e31-b330-73c7f38c0d39",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2013%2Fcluster13_model?alt=media&token=3d41caff-f5c9-4add-8e44-c18f4a23d5dd"},
    "2014": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2014%2Fpaper14_emb?alt=media&token=685e0ee3-aaf6-448b-8c8b-2f853e1332f4",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2014%2Fquestion_paper_2014?alt=media&token=50411663-1226-43af-ad1b-54ae8a551d78",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2014%2F2014.epub?alt=media&token=2ef68442-59e6-4e36-a3a2-7787581c1d6f",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2014%2Fcluster14_model?alt=media&token=59b497e9-b98d-436e-babc-b0041f645f56"},
    "2015": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2015%2Fpaper15_emb?alt=media&token=a2e81e8f-965c-4a69-878a-26c8f339aa93",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2015%2Fquestion_paper_2015?alt=media&token=f52b543e-f118-4974-8221-d7e86ea3fb97",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2015%2F2015.epub?alt=media&token=22893772-b88c-4554-8741-b4128b4ff92d",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2015%2Fcluster15_model?alt=media&token=45828b1d-9bb0-41b8-82de-4503994997d5"},
    "2016": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2016%2Fpaper16_emb?alt=media&token=6b3028ac-b272-4f2e-a98a-7d09387766a9",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2016%2Fquestion_paper_2016?alt=media&token=2b1e31bb-0de3-4076-ae12-0c24fc17ea3c",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2016%2F2016.epub?alt=media&token=21932123-d362-48e3-8f45-bc234dc1ba5b",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2016%2Fcluster16_model?alt=media&token=75b31de7-2dbb-44ec-a43b-83929cfe6acd"},
    "2017": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2017%2Fpaper17_emb?alt=media&token=72256f5f-4497-47ca-9e6d-f41f57274f13",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2017%2Fquestion_paper_2017?alt=media&token=a171b01c-03c2-47f5-a905-59a37bf00ed3",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2017%2F2017.epub?alt=media&token=bedfb246-c186-4742-ba7d-c0c980af190c",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2017%2Fcluster17_model?alt=media&token=24f1f770-2ed7-4457-9b2f-43a1ac8f48b3"},
    "2018": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2018%2Fpaper18_emb?alt=media&token=39f7e88e-fc7e-4450-98cf-9b5db8498359",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2018%2Fquestion_paper_2018?alt=media&token=1fac5b71-83f8-4d99-b6a1-fe0cfb48b2c9",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2018%2F2018.epub?alt=media&token=254fe8ea-f75d-4ada-a094-c6089b1d9e7f",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2018%2Fcluster18_model?alt=media&token=d5639c9b-ecce-41aa-b25a-023d374b8a93"},
    "2019": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2019%2Fpaper19_emb?alt=media&token=984528ce-68e2-417b-b851-a710aa4ea9f8",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2019%2Fquestion_paper_2019?alt=media&token=7a697535-23a3-478e-8cc5-5ea0f705c5f4",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2019%2F2019.epub?alt=media&token=c7aa4c5f-f77c-4c0e-9063-471a6984e061",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2019%2Fcluster19_model?alt=media&token=f61ecbd8-0596-438a-a095-fb2a0afc7a80"},
    "2020": {
        "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2020%2Fpaper20_emb?alt=media&token=55a403d4-07b8-4ac2-883e-29b1139a9910",
        "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2020%2Fquestion_paper_2020?alt=media&token=04dc20c1-626e-406d-b66c-8e5caeb4595b",
        "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2020%2F2020.epub?alt=media&token=2fcb2a4d-9ec3-40b3-bcec-a87fdf4e9f0b",
        "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2012%20question%20paper%2Fphysics%2F2020%2Fcluster20_model?alt=media&token=9d646daa-e1f4-49bc-9977-d1d970e79c55"}
}
accountancy11cbseqp={	"2010":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2010_accounts_emb.pickle?alt=media&token=7ce444f1-9d00-454c-8800-47e23b5c2acb","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2010_accounts_text.pickle?alt=media&token=cf2aec37-f8b6-4ba2-8126-ed1ff7b08a70","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2010_accounts_epub.epub?alt=media&token=7194a4b8-645b-4430-9d49-980a8b4f4786","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2010_accounts_cluster.pkl?alt=media&token=49fc4ef6-1285-4ea8-a8a5-7f1a64e9c71b"},
				"2011":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2011_accounts_emb.pickle?alt=media&token=445ba191-a4dc-426b-bbe7-f64abe7fbcf0","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2011_accounts_text.pickle?alt=media&token=0beac37b-49fe-4a64-aae0-81667c05a587","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2011_accounts_epub.epub?alt=media&token=3ec22429-d1ca-4fc0-901c-9d19c66456a7","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2011_accounts_cluster.pkl?alt=media&token=ebf0583e-2735-4fb9-9703-9e16b532898b"},
				"2012":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2012_accounts_emb.pickle?alt=media&token=df60bc8e-cbba-4e9d-ae41-f7dc07912211","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2012_accounts_text.pickle?alt=media&token=e556b198-d1d6-4d3f-aefe-7ed4e3f9ef5c","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2012_accounts_epub.epub?alt=media&token=f1bfdc6e-1fad-4eeb-9a39-0c86a191cf93","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2012_accounts_cluster.pkl?alt=media&token=13df82bc-747a-45a9-94e4-f195c4f55bbe"},
				"2013":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2013_accounts_emb.pickle?alt=media&token=f04abdcf-8da5-4495-9947-9f91fc2adb04","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2013_accounts_text.pickle?alt=media&token=db801f73-bffb-456a-8830-53adfc08c40d","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2013_accounts_epub.epub?alt=media&token=6f14d098-bc3e-4404-ac5e-a54bc6d335e5","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2013_accounts_cluster.pkl?alt=media&token=be1694f9-f15a-4158-b213-522b7737fc7f"},
				"2014":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2014_accounts_emb.pickle?alt=media&token=7046298b-f251-40a4-a856-fca963b01825","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2014_accounts_text.pickle?alt=media&token=4c006499-2712-41df-b1eb-1b203373b689","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2014_accounts_epub.epub?alt=media&token=66ba63aa-19b0-4e16-b7ed-1fac28055c7d","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2014_accounts_cluster.pkl?alt=media&token=14d7d7ce-2b2a-40ea-90d3-5ca5c659f5db"},
				"2015":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2015_accounts_emb.pickle?alt=media&token=17fd29d1-97b7-41ce-aafa-d39298aa8915","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2015_accounts_text.pickle?alt=media&token=e4f9cab6-995e-4e25-8757-e64b7fa26804","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2015_accounts_epub.epub?alt=media&token=3c1801dd-8035-48fa-a5d1-a6e67c821702","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2015_accounts_cluster.pkl?alt=media&token=9d8f3ccb-8c8b-4197-bb9e-a32a32456bf5"},
				"2016":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2016_accounts_emb.pickle?alt=media&token=7b253e4c-865e-4efe-8dfc-6dd76d0e7442","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2016_accounts_text.pickle?alt=media&token=b6b24ce2-3d6e-432c-886c-76e6dcfe3780","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2016_accounts_epub.epub?alt=media&token=3bf3c44a-71eb-4597-bc7a-fef6b003db8f","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2016_accounts_cluster.pkl?alt=media&token=22de8c26-fcdd-4b1d-baba-6a66c27b9455"},
				"2018":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2018_accounts_emb.pickle?alt=media&token=a4190c61-a3dc-4b66-bf87-ecf8aa17e0b2","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2018_accounts_text.pickle?alt=media&token=8c8483a0-403b-4361-a0cb-0e5875c13dac","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2018_accounts_epub.epub?alt=media&token=8fbbf0df-660b-4f2e-b9ef-fbe2dc0c01e7","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Faccountancy%2F2018_accounts_cluster.pkl?alt=media&token=8451315b-57d7-4042-a199-fe369cf99aac"}
			}
biology11cbseqp={	"2011":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2011%2F2011_biology_emb.pickle?alt=media&token=c94030b5-4ea8-437b-a663-a32fa8161004","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2011%2F2011_biology_text.pickle?alt=media&token=d5b380f7-aaab-4463-ad8f-a074e8154fe4","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2011%2F2011_biology_epub.epub?alt=media&token=3d103b4c-49ab-494b-a7b0-f7fb748d2a38","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2011%2F2011_biology_cluster.pkl?alt=media&token=be50e6a4-5231-4078-a030-49448e00e7f2"},
			"2012":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2012%2F2012_biology_emb.pickle?alt=media&token=251c286b-ed44-4200-8c34-705f4b8e7fc5","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2012%2F2012_biology_text.pickle?alt=media&token=8a0de576-8105-4e83-9e76-2dfdeb7da26e","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2012%2F2012_biology_epub.epub?alt=media&token=b46de5aa-976c-4a91-b7db-27142e7d0356","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2012%2F2012_biology_cluster.pkl?alt=media&token=be190502-0687-4356-9051-f9a2fbdde33f"},
			"2013":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2013%2F2013_biology_emb.pickle?alt=media&token=e2ea134d-915f-4122-9bd1-13f39bc63483","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2013%2F2013_biology_text.pickle?alt=media&token=a29f7604-35de-49cb-81ba-78e70f0eb052","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2013%2F2013_biology_epub.epub?alt=media&token=3fb859f0-aa1c-4f30-b11e-389885134539","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2013%2F2013_biology_cluster.pkl?alt=media&token=a9f479ad-e711-4610-b7dc-ea4a8783045f"},
			"2014":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2014%2F2014_biology_emb.pickle?alt=media&token=ef3698a6-89a6-46aa-9cd1-bf260da9b177","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2014%2F2014_biology_text.pickle?alt=media&token=c069fdf4-b119-47bc-80eb-21f2e9b6fcff","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2014%2F2014_biology_epub.epub?alt=media&token=30b16e5d-ab61-4708-8009-5a4eeff7dfe9","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2014%2F2014_biology_cluster.pkl?alt=media&token=34625d80-4af5-447d-8adf-b1e7cfef62ca"},
			"2015":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2015%2F2015_biology_emb.pickle?alt=media&token=c3d7dc2f-3487-480b-8ae2-dc3ea4e27b1d","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2015%2F2015_biology_text.pickle?alt=media&token=e5b51fe2-c171-488d-a66c-7c53b7238eea","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2015%2F2015_biology_epub.epub?alt=media&token=cc64f5e9-660f-4582-8b21-832e1f9affaf","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2015%2F2015_biology_cluster.pkl?alt=media&token=99ba17b0-5587-4923-ade6-ae533dd62e26"},
			"2016":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2016%2F2016_biology_emb.pickle?alt=media&token=d7336873-d6ca-46fe-803e-d8e48b0b11c7","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2016%2F2016_biology_text.pickle?alt=media&token=7ccb03a4-726b-4b4a-8fe7-2738e4b7223b","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2016%2F2016_biology_epub.epub?alt=media&token=5bf05d24-3160-49fb-a273-000ee9d3d1b1","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2016%2F2016_biology_cluster.pkl?alt=media&token=5c9795aa-d67b-4eb2-9190-504b05c7d6b1"},
			"2017":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2017%2F2017_biology_emb.pickle?alt=media&token=8fb44aba-82d5-4761-b62d-175af4bfee6b","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2017%2F2017_biology_text.pickle?alt=media&token=52a2b5c8-aa5e-427e-baec-20d336faa3b1","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2017%2F2017_biology_epub.epub?alt=media&token=ad6fa7eb-4618-4e62-94ed-113e535800e7","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2017%2F2017_biology_cluster.pkl?alt=media&token=6fc9ae6c-79e9-4f79-a389-6a52c6aeb3a4"},
			"2019":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2019%2F2019_biology_emb.pickle?alt=media&token=b084792a-d016-4772-bf3e-44b6864ba1a2","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2019%2F2019_biology_text.pickle?alt=media&token=355c096e-7e0a-40f4-9ff2-cf1f05363159","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2019%2F2019_biology_epub.epub?alt=media&token=7a767622-be9e-4b98-a435-d3fab6f6cb56","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2019%2F2019_biology_cluster.pkl?alt=media&token=40d8d9d2-e2a8-4f3b-8b9e-48359652c451"},
			"2020":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2020%2F2020_biology_emb.pickle?alt=media&token=29eb664a-57e1-4eeb-ae52-e32be6bb6624","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2020%2F2020_biology_text.pickle?alt=media&token=4b600002-a9b4-4244-8181-c9f256593e74","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2020%2F2020_biology_epub.epub?alt=media&token=9a776e22-d1df-469b-aceb-a24bb60adddb","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbiology%2F2020%2F2020_biology_cluster.pkl?alt=media&token=b907f440-60cb-4bbc-a7e9-44a5bd2f9ff8"}
		}
businessStudies11cbseqp={	"2011":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2011_business_emb.pickle?alt=media&token=58ac3741-2791-48de-85e6-a47d95c72150","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2011_business_text.pickle?alt=media&token=82627ad4-0e9a-4add-89fe-4e7cd7f11a6f","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2011_business_epub.epub?alt=media&token=78301bb2-a367-4065-bd73-f41f8613ce11","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2011_business_cluster.pkl?alt=media&token=591a46d0-3d90-46a1-a818-8ee024bb814a"},
					"2013":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2013_business_emb.pickle?alt=media&token=83531f02-bf5e-4bd7-99a8-e6eb828f56a8","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2013_business_text.pickle?alt=media&token=d2debb25-e61d-4947-9382-cecbf092f117","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2013_business_epub.epub?alt=media&token=1d896e6c-4e72-4a83-b8eb-751c8d406d75","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2013_business_cluster.pkl?alt=media&token=2b273ed4-32e9-4f96-9170-0966046be681"},
					"2014":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2014_business_emb.pickle?alt=media&token=4f1487cb-a993-4dca-b23f-c7836f2e5d3c","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2014_business_text.pickle?alt=media&token=c1346e60-355d-46d7-a2c2-85636645af0b","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2014_business_epub.epub?alt=media&token=94e8c5db-d2f1-4653-bfcf-233c426c2361","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2014_business_cluster.pkl?alt=media&token=e44ffa9e-e686-44b8-b1f1-78be8623674d"},
					"2015":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2015_business_emb.pickle?alt=media&token=faed06e3-b300-4917-9048-f57ff51860d8","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2015_business_text.pickle?alt=media&token=8099200d-cbb2-4821-84e5-cd5ad8ffb735","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2015_business_epub.epub?alt=media&token=37b24c42-9b78-47fa-8e89-3ea1b0e2eeed","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2015_business_cluster.pkl?alt=media&token=6281b334-6733-4611-b571-24d13430041b"},
					"2016":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2016_business_emb.pickle?alt=media&token=62d3ae03-1d5f-42f1-a16b-1952d6d03cd7","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2016_business_text.pickle?alt=media&token=ceddfee9-5f75-4e82-8b38-df905b7e3b11","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2016_business_epub.epub?alt=media&token=0a732749-b643-434a-9ced-a9f8c942f164","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fbusiness%20Studies%2F2016_business_cluster.pkl?alt=media&token=4f9500f1-da44-4e8b-9444-e85717d1c77b"}
				}
chemistry11cbseqp={	"2011":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2011%2F2011_chemistry_emb.pickle?alt=media&token=7b97c1d0-1a2d-4a48-88dc-2abc5f0c2e8f","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2011%2F2011_chemistry_text.pickle?alt=media&token=040c5b74-8797-4ea6-b5df-d5ca85556541","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2011%2F2011_chemistry_epub.epub?alt=media&token=7c60b276-18d2-47e2-b705-366e155e573b","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2011%2F2011_chemistry_cluster.pkl?alt=media&token=521256aa-0be1-45ac-bba5-a9b1f10ea2f0"},
				"2012":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2012%2F2012_chemistry_emb.pickle?alt=media&token=d75a2e3c-8e9b-4e6b-aaad-dd8daabcdefa","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2012%2F2012_chemistry_text.pickle?alt=media&token=f02bb9b2-4431-49e5-b7f8-1d38cbf63cf8","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2012%2F2012_chemistry_epub.epub?alt=media&token=cad6524a-02a6-45f9-9538-951319ec166e","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2012%2F2012_chemistry_cluster.pkl?alt=media&token=b5e77d95-0551-4021-b83f-db607c3b78b6"},
				"2013":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2013%2F2013_chemistry_emb.pickle?alt=media&token=52ea8f3d-2234-4a13-9234-096f50f2508e","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2013%2F2013_chemistry_text.pickle?alt=media&token=f4efd6e0-872d-4a01-a6f3-232849156ed4","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2013%2F2013_chemistry_epub.epub?alt=media&token=e1598739-19fe-475c-90cb-1218c5f52e0a","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2013%2F2013_chemistry_cluster.pkl?alt=media&token=ffe2b15b-d52d-40fd-b83a-e439502d4047"},
				"2014":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2014%2F2014_chemistry_emb.pickle?alt=media&token=86db2259-3c0a-441a-ab70-ac27cbec3ba6","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2014%2F2014_chemistry_text.pickle?alt=media&token=92f6913a-662d-414c-99b9-25e649aff67d","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2014%2F2014_chemistry_epub.epub?alt=media&token=898d2d96-1885-4370-8e5e-a8666a5ad728","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2014%2F2014_chemistry_cluster.pkl?alt=media&token=84e1d25d-f4c5-4284-a111-9c133e7d8772"},
				"2015":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2015%2F2015_chemistry_emb.pickle?alt=media&token=840adcbc-e840-480a-b218-8cc0dcafebaf","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2015%2F2015_chemistry_text.pickle?alt=media&token=bd6ba9e7-1647-4ab9-8bb7-386349274a31","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2015%2F2015_chemistry_epub.epub?alt=media&token=f7fb3552-63b9-4701-891f-f0dd430340c4","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2015%2F2015_chemistry_cluster.pkl?alt=media&token=0d0b25fa-d2ce-4366-b4b5-1b3078d165ef"},
				"2016":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2016%2F2016_chemistry_emb.pickle?alt=media&token=e8b1c00e-9981-4809-84ab-b6b1d0b2a78d","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2016%2F2016_chemistry_text.pickle?alt=media&token=f7375127-3a89-4019-a618-a7bd741c8200","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2016%2F2016_chemistry_epub.epub?alt=media&token=5d42906e-504d-4233-9719-ea157d35aa2d","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2016%2F2016_chemistry_cluster.pkl?alt=media&token=9e5a4eee-935b-43e1-ab6b-34f988326ab4"},
				"2019":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2019%2F2019_chemistry_emb.pickle?alt=media&token=9a4e5937-88d8-49e1-b64f-9a9f56b8c710","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2019%2F2019_chemistry_text.pickle?alt=media&token=31bfb4a5-f706-4391-beb7-730f3b2bae6c","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2019%2F2019_chemistry_epub.epub?alt=media&token=9cff913e-a225-4e80-9d9d-55a7cb0af2e1","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fchemistry%2F2019%2F2019_chemistry_cluster.pkl?alt=media&token=0af38685-d2eb-4e25-80fb-12840df4557b"}
			}
mathematics11cbseqp={	"2013":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2013_emb.pickle?alt=media&token=249957c9-2c56-4975-9293-99ed3e7b42ca","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2013_text.pickle?alt=media&token=1ce138ff-f2ca-498e-ba53-0e3c48adc1a8","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2013_epub.epub?alt=media&token=86348da6-0ddb-475a-a938-d158dbdfb8e5","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2013_cluster.pkl?alt=media&token=8c2ea6b2-fe63-4bbf-b2e3-65799b5fb696"},
				"2014":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2014_emb.pickle?alt=media&token=0d856eb4-081a-438c-8dcf-72c8898e6609","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2014_text.pickle?alt=media&token=c003463c-4563-4b4b-b3c7-576fbd5ea73b","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2014_epub.epub?alt=media&token=3368643e-161e-4e1e-9ae6-794c5234e36b","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2014_cluster.pkl?alt=media&token=87b47f66-6926-4b7b-a4af-295d6e4124d7"},
				"2015":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2015_emb.pickle?alt=media&token=f8f4b95a-c21b-4773-9c86-37d5482d9bef","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2015_text.pickle?alt=media&token=52eb0bc4-961d-44a8-bfbc-4fa751a4a112","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2015_epub.epub?alt=media&token=510e650e-3af8-437d-906d-e93168bc1187","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2015_cluster.pkl?alt=media&token=660f1f82-fc9d-45cd-9436-d9fb48ddfe44"},
				"2016":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2016_emb.pickle?alt=media&token=3efce5ed-5bdf-406f-a60b-e6bb8bedbd88","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2016_text.pickle?alt=media&token=16e003eb-9061-4164-a390-382e57fb4cfa","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2016_epub.epub?alt=media&token=5a7c8533-ee04-4d06-bdb9-2b92004c4e37","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2016_cluster.pkl?alt=media&token=9fb0bf83-0d40-4a25-b5f7-bb3b71abbed1"},
				"2017":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2017_emb.pickle?alt=media&token=02030fb8-665c-4f59-a8f9-7244380b9f78","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2017_text.pickle?alt=media&token=ab366957-00ed-41f2-bf8f-9bccfac3b963","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2017_epub.epub?alt=media&token=575c413a-9ba3-4a52-ab9c-899a93bcb67e","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2017_cluster.pkl?alt=media&token=aff3e64a-6f87-4132-8364-3108e941ba29"},
				"2019":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2019_emb.pickle?alt=media&token=2d9732a2-62e5-4d51-a49d-9c95ae969aa2","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2019_text.pickle?alt=media&token=93741d6b-ea17-4d4f-850c-409585f13beb","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2019_epub.epub?alt=media&token=8ee18c02-bb28-4695-bdef-972baa1f6c3e","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fmathematics%2Fmaths_2019_cluster.pkl?alt=media&token=44e91a1b-2ee8-49d8-9a97-b02d22ac995f"}
			  }
physics11cbseqp={	"2011":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2011_physics_emb.pickle?alt=media&token=3311af65-fcb8-4ae3-81e4-65dd1ef57add","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2011_physics_text.pickle?alt=media&token=a757507c-425d-44d7-8e17-24f5d95e8708","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2011_physics_epub.epub?alt=media&token=918b9bf3-81ba-4eed-a306-d90b3bfbe467","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2011_physics_cluster.pkl?alt=media&token=104d467b-9114-4ba0-9031-ddb37d9ae6ad"},
			"2012":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2012_physics_emb.pickle?alt=media&token=a91ee001-0fbd-46b8-bca2-120c2e720b59","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2012_physics_text.pickle?alt=media&token=8fea77bc-37cb-429a-8f88-a2b9330915cb","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2012_physics_epub.epub?alt=media&token=55d124e4-3300-4776-9cb5-0c348ab83878","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2012_physics_cluster.pkl?alt=media&token=6a7e0cf7-2f43-48cc-9142-3c775f3f78a1"},
			"2013":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2013_physics_emb.pickle?alt=media&token=f5e6816f-8710-4965-af35-cddbc18ec1f0","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2013_physics_text.pickle?alt=media&token=296dbb69-e4ca-4cc7-9c75-2398e934dde3","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2013_physics_epub.epub?alt=media&token=6efc7369-b3b6-47f6-8a50-52f569c3c58b","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2013_physics_cluster.pkl?alt=media&token=d2987890-28c4-4abb-bcbb-d9503e91d624"},
			"2014":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2014_physics_emb.pickle?alt=media&token=002b9372-6ad9-4a84-9c5b-ca0c2ae01d21","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2014_physics_text.pickle?alt=media&token=6f3b132a-caf0-4c36-bcff-446b39eaeb9b","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2014_physics_epub.epub?alt=media&token=40f63743-af88-47e9-8263-d7e4da891069","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2014_physics_cluster.pkl?alt=media&token=12fe58b8-56cf-4042-be19-15ccd472bf84"},
			"2015":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2015_physics_emb.pickle?alt=media&token=cb55e105-db0a-4847-abe9-6355f8bfdc45","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2015_physics_text.pickle?alt=media&token=b80d08af-9180-49e0-88af-074ea1d8cacf","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2015_physics_epub.epub?alt=media&token=4323f1a7-9884-489a-9651-8da57760eccf","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2015_physics_cluster.pkl?alt=media&token=f28eaae4-2051-4b84-9219-2b26d2c4bc77"},
			"2016":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2016_physics_emb.pickle?alt=media&token=2688e56c-0df1-4413-b426-d15cd357f8a7","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2016_physics_text.pickle?alt=media&token=96d1182f-1edb-4c01-a4c2-ea6520cdea94","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2016_physics_epub.epub?alt=media&token=1c9bc5d6-68d2-4ee2-9571-fc8d4674d7c3","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2016_physics_cluster.pkl?alt=media&token=34901111-6fd7-4e26-bb6b-4843368aa11f"},
			"2017":{"embeddings":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2017_physics_emb.pickle?alt=media&token=a9661314-21a3-4a3e-8f41-6cb27a275675","text":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2017_physics_text.pickle?alt=media&token=4d67a7e6-07fe-49a1-a3ff-e3dbf1fc0c3f","epub":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2017_physics_epub.epub?alt=media&token=791a3c84-c450-4149-8162-74111daa1ef4","cluster":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2011%20question%20paper%2Fphysics%2F2017_physics_cluster.pkl?alt=media&token=5b7ce1ab-94ce-4ca0-b3ef-ebe943755156"}
			}

app = Flask(__name__)
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'u736502961_HyS'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Hys@31197'
app.config['MYSQL_DATABASE_DB'] = 'u736502961_hys'
app.config['MYSQL_DATABASE_HOST'] = '217.21.87.1'
mysql.init_app(app)


# User Personal and School details
@app.route('/get_all_user_ids', methods=['GET'])
def get_all_user_ids():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.users;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_new_user', methods=['PUT'])
@cross_origin()
def add_user():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        # validate the received values
        if _id and request.method == 'PUT':
            # save edits
            sql = "INSERT INTO u736502961_hys.users(user_id) VALUES(%s)"
            data = _id
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_personal_data', methods=['POST'])
@cross_origin()
def add_user_personal_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _f_name = _json['first_name']
        _l_name = _json['last_name']
        _profile_pic = _json['profilepic']
        _email_id = _json['email_id']
        _mobile_no = _json['mobile_no']
        _gender = _json['gender']
        _dob = _json['user_dob']
        _address = _json['address']
        _street = _json['street']
        _city = _json['city']
        _state = _json['state']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_personal_details(user_id,first_name,last_name,profilepic,gender,user_dob," \
                  "address,street,city,state,email_id,mobile_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
            data = (
                _id, _f_name, _l_name, _profile_pic, _gender, _dob, _address, _street, _city, _state, _email_id,
                _mobile_no)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User personal data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_data/<string:id>', methods=['GET'])
def get_user_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_personal_details pd inner join u736502961_hys.user_school_details sd on pd.user_id=sd.user_id where pd.user_id=%s;",
            id)
        row = cursor.fetchall()
        cursor.execute(
            "select * from u736502961_hys.user_hobbies where user_id=%s;", id)
        hobbies = cursor.fetchall()
        row[0]['hobbies'] = hobbies
        cursor.execute(
            "select * from u736502961_hys.user_ambition where user_id=%s;", id)
        ambitions = cursor.fetchall()
        row[0]['ambitions'] = ambitions
        cursor.execute(
            "select * from u736502961_hys.user_dream_vacations where user_id=%s;", id)
        user_dream_vacations = cursor.fetchall()
        row[0]['dream_vacations'] = user_dream_vacations
        cursor.execute(
            "select * from u736502961_hys.user_novels_read where user_id=%s;", id)
        user_novels_read = cursor.fetchall()
        row[0]['novels_read'] = user_novels_read
        cursor.execute(
            "select * from u736502961_hys.user_place_visited where user_id=%s;", id)
        user_place_visited = cursor.fetchall()
        row[0]['place_visited'] = user_place_visited
        cursor.execute(
            "select * from u736502961_hys.user_strength where user_id=%s;", id)
        user_strength = cursor.fetchall()
        row[0]['strength'] = user_strength
        cursor.execute(
            "select * from u736502961_hys.user_weakness where user_id=%s;", id)
        user_weakness = cursor.fetchall()
        row[0]['weakness'] = user_weakness
        cursor.execute(
            "select * from u736502961_hys.user_preferred_languages where user_id=%s;", id)
        user_preferred_languages = cursor.fetchall()
        row[0]['preferred_languages'] = user_preferred_languages
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_users_data_for_tagging', methods=['GET'])
def get_all_users_data_for_tagging():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.gender gender, pd.user_dob user_dob, pd.address address, pd.street street, pd.city city, pd.state state, pd.email_id email_id, pd.mobile_no mobile_no, sd.school_name school_name, sd.grade grade, sd.stream stream, sd.board board,sd.address school_address, sd.street school_street, sd.city school_city, sd.state school_state from u736502961_hys.user_personal_details pd inner join u736502961_hys.user_school_details sd on pd.user_id=sd.user_id;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_preferred_language_data', methods=['POST'])
@cross_origin()
def add_user_preferred_languages_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _preferred_lang_list = _json['preferred_lang_list']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_preferred_languages(user_id,preferred_lang) VALUES(%s,%s);"
            conn = mysql.connect()
            cursor = conn.cursor()
            for i in range(len(_preferred_lang_list)):
                data = (_id, _preferred_lang_list[i])
                cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User preferred languages added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_preferred_languages_data/<string:id>', methods=['GET'])
def get_user_preferred_languages_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select preferred_lang from u736502961_hys.user_preferred_languages where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_school_data', methods=['POST'])
@cross_origin()
def add_user_school_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _school_name = _json['school_name']
        _grade = _json['grade']
        _stream = _json['stream']
        _board = _json['board']
        _address = _json['address']
        _street = _json['street']
        _city = _json['city']
        _state = _json['state']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_school_details(user_id,school_name,grade,stream,board,address,street,city,state) VALUES(%s,%s,%s,%s," \
                  "%s,%s,%s,%s,%s); "
            data = (_id, _school_name, _grade, _stream, _board, _address, _street, _city, _state)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User school data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_strength_data', methods=['POST'])
@cross_origin()
def add_user_strength_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _grade = _json['grade']
        _subject_list = _json['subject_list']
        _topic_list = _json['topic_list']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_strength(user_id,grade,subject,topic) VALUES(%s,%s,%s,%s);"
            conn = mysql.connect()
            cursor = conn.cursor()
            for i in range(len(_subject_list)):
                for j in range(len(_topic_list[i])):
                    data = (_id, _grade, _subject_list[i], _topic_list[i][j])
                    cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User strength added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_strength_data/<string:id>', methods=['GET'])
def get_user_strength_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_strength where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_weakness_data', methods=['POST'])
@cross_origin()
def add_user_weakness_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _grade = _json['grade']
        _subject_list = _json['subject_list']
        _topic_list = _json['topic_list']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_weakness(user_id,grade,subject,topic) VALUES(%s,%s,%s,%s);"
            conn = mysql.connect()
            cursor = conn.cursor()
            for i in range(len(_subject_list)):
                for j in range(len(_topic_list[i])):
                    data = (_id, _grade, _subject_list[i], _topic_list[i][j])
                    cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User weakness data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_weakness_data/<string:id>', methods=['GET'])
def get_user_weakness_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_weakness where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Questions and answer details
@app.route('/add_user_question_details', methods=['POST'])
@cross_origin()
def add_user_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _answer_count = _json['answer_count']
        _answer_preference = _json['answer_preference']
        _audio_reference = _json['audio_reference']
        _call_date = _json['call_date']
        _call_end_time = _json['call_end_time']
        _call_now = _json['call_now']
        _call_preferred_lang = _json['call_preferred_lang']
        _call_start_time = _json['call_start_time']
        _answer_credit = _json['answer_credit']
        _question_credit = _json['question_credit']
        _view_count = _json['view_count']
        _examlikelyhood_count = _json['examlikelyhood_count']
        _grade = _json['grade']
        _like_count = _json['like_count']
        _note_reference = _json['note_reference']
        _ocr_image = _json['ocr_image']
        _compare_date = _json['compare_date']
        _question = _json['question']
        _question_type = _json['question_type']
        _is_identity_visible = _json['is_identity_visible']
        _subject = _json['subject']
        _topic = _json['topic']
        _text_reference = _json['text_reference']
        _toughness_count = _json['toughness_count']
        _video_reference = _json['video_reference']
        _impression_count = _json['impression_count']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _question_id, _user_id, _answer_count, _answer_preference, _audio_reference, _call_date, _call_end_time,
                _call_now, _call_preferred_lang, _call_start_time, _answer_credit, _question_credit, _view_count,
                _examlikelyhood_count, _grade, _like_count, _note_reference, _ocr_image, _compare_date, _question,
                _question_type, _is_identity_visible, _subject, _topic, _text_reference, _toughness_count,
                _video_reference,
                _impression_count)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_question_details(question_id, user_id, answer_count, answer_preference, audio_reference, call_date, call_end_time, call_now, call_preferred_lang, call_start_time, answer_credit, question_credit, view_count, examlikelyhood_count, grade, like_count,note_reference, ocr_image, compare_date, question, question_type, is_identity_visible, subject, topic, text_reference, toughness_count, video_reference, impression_count) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('User posted question successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_tagged_in_question', methods=['POST'])
@cross_origin()
def add_users_tagged_in_question():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.users_tagged_with_question(question_id, user_id) values (%s, %s);", data)
            conn.commit()
            resp = jsonify('Users tagged with question added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_questions_posted/<string:id>', methods=['GET'])
def get_user_questions_posted(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (id, id, id, id, id, id)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference, floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name ,ld.like_type, ed.examlikelyhood_level, td.toughness_level, sa.user_id is_save, ba.user_id is_bookmark from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id left join u736502961_hys.questions_like_details ld on qd.question_id=ld.question_id and ld.user_id=%s left join u736502961_hys.questions_examlikelyhood_details ed on qd.question_id=ed.question_id and ed.user_id=%s left join u736502961_hys.questions_toughness_details td on qd.question_id=td.question_id and td.user_id=%s left join u736502961_hys.questions_saved_details sa on qd.question_id=sa.question_id and sa.user_id=%s left join u736502961_hys.questions_bookmarked_details ba on qd.question_id=ba.question_id and ba.user_id=%s where qd.user_id=%s order by qd.compare_date desc;",
            data)

        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_question_posted/<string:id>/<string:userid>', methods=['GET'])
def get_question_posted(id, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, userid, userid, userid, userid, id)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference, floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name ,ld.like_type, ed.examlikelyhood_level, td.toughness_level, sa.user_id is_save, ba.user_id is_bookmark from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id left join u736502961_hys.questions_like_details ld on qd.question_id=ld.question_id and ld.user_id=%s left join u736502961_hys.questions_examlikelyhood_details ed on qd.question_id=ed.question_id and ed.user_id=%s left join u736502961_hys.questions_toughness_details td on qd.question_id=td.question_id and td.user_id=%s left join u736502961_hys.questions_saved_details sa on qd.question_id=sa.question_id and sa.user_id=%s left join u736502961_hys.questions_bookmarked_details ba on qd.question_id=ba.question_id and ba.user_id=%s where qd.question_id=%s order by qd.compare_date desc;",
            data)
        row = cursor.fetchall()
        data = (userid, userid, row[0]["question_id"])
        cursor.execute(
            " select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade, case when ld.like_type is null then '' else ld.like_type end as like_type, case when vd.vote_type is null then '' else vd.vote_type end as vote_type from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id left join u736502961_hys.answers_like_details ld on ld.answer_id = ad.answer_id and ld.user_id=%s left join u736502961_hys.answers_vote_details vd on vd.answer_id = ad.answer_id and vd.user_id=%s where ad.question_id=%s order by ad.compare_date desc;",
            data)
        answerList = cursor.fetchall()
        for i in range(len(answerList)):
            data = (userid, answerList[i]["answer_id"])
            cursor.execute(
                "select cd.*, pd.*, sd.*, case when cld.like_type is null then '' else cld.like_type end like_type from u736502961_hys.user_answer_comment_details cd inner join u736502961_hys.user_personal_details pd on cd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id left join u736502961_hys.answers_comment_like_details cld on cd.comment_id = cld.comment_id and cld.user_id=%s  where cd.answer_id=%s order by cd.compare_date desc;",
                data)
            commentlist = cursor.fetchall()
            for j in range(len(commentlist)):
                data = (userid, commentlist[j]['comment_id'])
                cursor.execute(
                    "select rd.reply_id reply_id, rd.image image, rd.comment_id comment_id, rd.answer_id answer_id, rd.question_id question_id, rd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, rd.reply reply, rd.reply_type, rd.like_count like_count, rd.compare_date compare_date, case when rld.like_type is null then '' else rld.like_type end like_type from u736502961_hys.user_answer_reply_details rd left join u736502961_hys.answers_reply_like_details rld on rld.reply_id=rd.reply_id and rld.user_id = %s inner join u736502961_hys.user_personal_details pd on rd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on rd.user_id=sd.user_id where rd.comment_id=%s order by rd.compare_date desc;",
                    data)
                replyList = cursor.fetchall()
                commentlist[j]['reply_list'] = replyList
            answerList[i]["comment_list"] = commentlist
        row[0]["answer_list"] = answerList
        cursor.execute(
            "select * from u736502961_hys.users_tagged_with_question tag inner join u736502961_hys.user_personal_details pd on tag.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on tag.user_id=sd.user_id where tag.question_id=%s;",
            row[0]["question_id"])
        tagList = cursor.fetchall()
        row[0]["tag_list"] = tagList
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_questions_posted/<string:userid>', methods=['GET'])
def get_all_question_posted(userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, userid, userid, userid, userid)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference, floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name ,ld.like_type, ed.examlikelyhood_level, td.toughness_level, sa.user_id is_save, ba.user_id is_bookmark from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id left join u736502961_hys.questions_like_details ld on qd.question_id=ld.question_id and ld.user_id=%s left join u736502961_hys.questions_examlikelyhood_details ed on qd.question_id=ed.question_id and ed.user_id=%s left join u736502961_hys.questions_toughness_details td on qd.question_id=td.question_id and td.user_id=%s left join u736502961_hys.questions_saved_details sa on qd.question_id=sa.question_id and sa.user_id=%s left join u736502961_hys.questions_bookmarked_details ba on qd.question_id=ba.question_id and ba.user_id=%s order by qd.compare_date desc;",
            data)
        row = cursor.fetchall()
        for i in range(len(row)):
            data = (userid, userid, row[0]["question_id"])
            cursor.execute(
                " select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade, case when ld.like_type is null then '' else ld.like_type end as like_type, case when vd.vote_type is null then '' else vd.vote_type end as vote_type from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id left join u736502961_hys.answers_like_details ld on ld.answer_id = ad.answer_id and ld.user_id=%s left join u736502961_hys.answers_vote_details vd on vd.answer_id = ad.answer_id and vd.user_id=%s where ad.question_id=%s order by ad.compare_date desc;",
                data)
            answerList = cursor.fetchall()
            row[i]["answer_list"] = answerList
            cursor.execute(
                "select * from u736502961_hys.users_tagged_with_question tag inner join u736502961_hys.user_personal_details pd on tag.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on tag.user_id=sd.user_id where tag.question_id=%s;",
                row[i]["question_id"])
            tagList = cursor.fetchall()
            row[i]["tag_list"] = tagList

        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_questions_like_details', methods=['POST'])
@cross_origin()
def add_questions_like_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _like_type = _json['like_type']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _like_type)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_like_details(question_id, user_id, like_type) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users like details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_questions_like_details', methods=['DELETE'])
@cross_origin()
def delete_questions_like_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from u736502961_hys.questions_like_details where question_id=%s and user_id=%s;",
                           data)
            conn.commit()
            resp = jsonify('Users like details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_questions_toughness_details', methods=['POST'])
@cross_origin()
def add_questions_toughness_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _toughness_level = _json['toughness_level']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _toughness_level)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_toughness_details(question_id, user_id, toughness_level) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users toughness details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_questions_toughness_details', methods=['DELETE'])
@cross_origin()
def delete_questions_toughness_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_toughness_details where question_id=%s and user_id=%s;", data)
            conn.commit()
            resp = jsonify('Users toughness details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_questions_examlikelyhood_details', methods=['POST'])
@cross_origin()
def add_questions_examlikelyhood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _examlikelyhood_level = _json['examlikelyhood_level']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _examlikelyhood_level)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_examlikelyhood_details(question_id, user_id, examlikelyhood_level) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users examlikelyhood details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_questions_examlikelyhood_details', methods=['DELETE'])
@cross_origin()
def delete_questions_examlikelyhood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_examlikelyhood_details where question_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Users examlikelyhood details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_counts_in_question_details', methods=['PUT'])
@cross_origin()
def update_counts_in_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _answer_count = _json["answer_count"]
        _like_count = _json["like_count"]
        _view_count = _json["view_count"]
        _examlikelyhood_count = _json["examlikelyhood_count"]
        _toughness_count = _json["toughness_count"]
        _impression_count = _json["impression_count"]
        # validate the received values
        if _user_id and request.method == 'PUT':
            data = (_answer_count, _view_count, _examlikelyhood_count, _like_count, _toughness_count, _impression_count,
                    _user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_question_details set answer_count=%s, view_count=%s, examlikelyhood_count=%s, like_count=%s, toughness_count=%s, impression_count=%s where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Answers
@app.route('/post_answer_on_question_details', methods=['POST'])
@cross_origin()
def post_answer_on_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json["user_id"]
        _comment_count = _json["comment_count"]
        _audio_reference = _json["audio_reference"]
        _like_count = _json["like_count"]
        _upvote_count = _json["upvote_count"]
        _downvote_count = _json["downvote_count"]
        _note_reference = _json["note_reference"]
        _image = _json["image"]
        _compare_date = _json["compare_date"]
        _answer = _json["answer"]
        _answer_type = _json["answer_type"]
        _text_reference = _json["text_reference"]
        _video_reference = _json["video_reference"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_answer_id, _question_id, _user_id, _comment_count, _audio_reference, _like_count, _upvote_count,
                    _downvote_count, _note_reference, _image, _compare_date, _answer, _answer_type, _text_reference,
                    _video_reference)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_answer_details(answer_id, question_id, user_id, comment_count, audio_reference, like_count, upvote_count, downvote_count, note_reference, image, compare_date, answer, answer_type, text_reference,video_reference) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users posted answer successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_tagged_in_answer', methods=['POST'])
@cross_origin()
def add_users_tagged_in_answer():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["answer_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into u736502961_hys.users_tagged_with_answer(answer_id, user_id) values (%s, %s);",
                           data)
            conn.commit()
            resp = jsonify('Users tagged with answer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_counts_in_answer_details', methods=['POST'])
@cross_origin()
def update_counts_in_answer_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _answer_id = _json["answer_id"]
        _user_id = _json['user_id']
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _upvote_count = _json["upvote_count"]
        _downvote_count = _json["downvote_count"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_comment_count, _like_count, _upvote_count, _downvote_count, _user_id, _answer_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_answer_details set comment_count=%s, like_count=%s, upvote_count=%s, downvote_count=%s where user_id=%s and answer_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_answer_posted', methods=['GET'])
def get_all_answer_posted():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name,pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id order by ad.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_answers_posted/<string:id>', methods=['GET'])
def get_user_answers_posted(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ad.answer_id, ad.question_id, ad.user_id, ad.comment_count, ad.audio_reference, ad.like_count, ad.upvote_count, ad.downvote_count, ad.note_reference, ad.image, ad.compare_date, ad.answer, ad.answer_type, ad.text_reference, ad.video_reference, qd.subject,qd.topic from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_question_details qd on ad.question_id=qd.question_id where ad.user_id=%s order by ad.createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_answer_posted/<string:ansid>/<string:userid>', methods=['GET'])
def get_answer_posted(ansid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, userid, ansid)
        cursor.execute(
            " select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade, case when ld.like_type is null then '' else ld.like_type end as like_type, case when vd.vote_type is null then '' else vd.vote_type end as vote_type from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id left join u736502961_hys.answers_like_details ld on ld.answer_id = ad.answer_id and ld.user_id=%s left join u736502961_hys.answers_vote_details vd on vd.answer_id = ad.answer_id and vd.user_id=%s where ad.answer_id=%s order by ad.compare_date desc;",
            data)
        answerList = cursor.fetchall()
        data = (userid, ansid)
        cursor.execute(
            "select cd.*, pd.*, sd.*, case when cld.like_type is null then '' else cld.like_type end like_type from u736502961_hys.user_answer_comment_details cd inner join u736502961_hys.user_personal_details pd on cd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id left join u736502961_hys.answers_comment_like_details cld on cd.comment_id = cld.comment_id and cld.user_id=%s where cd.answer_id=%s order by cd.compare_date desc;",
            data)
        commentlist = cursor.fetchall()
        for i in range(len(commentlist)):
            data = (userid, commentlist[i]['comment_id'])
            cursor.execute(
                "select rd.*, pd.*, sd.*, case when rld.like_type is null then '' else rld.like_type end like_type from u736502961_hys.user_answer_reply_details rd left join u736502961_hys.answers_reply_like_details rld on rld.reply_id=rd.reply_id and rld.user_id = %s inner join u736502961_hys.user_personal_details pd on rd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on rd.user_id=sd.user_id where rd.comment_id=%s order by rd.compare_date desc;",
                data)
            replyList = cursor.fetchall()
            commentlist[i]['reply_list'] = replyList
        answerList[0]["comment_list"] = commentlist
        resp = jsonify(answerList)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_answer_comment', methods=['POST'])
@cross_origin()
def add_users_answer_comment():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _comment = _json["comment"]
        _comment_type = _json["comment_type"]
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        _note_reference = _json["note_reference"]
        _text_reference = _json["text_reference"]
        _video_reference = _json["video_reference"]
        _audio_reference = _json["audio_reference"]
        _compare_date = _json["compare_date"]
        _image = _json["image"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_comment_id, _answer_id, _question_id, _user_id, _comment, _comment_type, _like_count, _reply_count,
                    _audio_reference, _note_reference, _text_reference, _video_reference, _compare_date, _image)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_answer_comment_details(comment_id,answer_id,question_id,user_id,comment,comment_type,like_count,reply_count,audio_reference,note_reference,text_reference,video_reference,compare_date, image) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Comment on answer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_comment_with_replies/<string:cmntid>/<string:userid>', methods=['GET'])
def get_comment_with_replies(cmntid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, cmntid)
        cursor.execute(
            "select cd.*, pd.*, sd.*, case when cld.like_type is null then '' else cld.like_type end like_type from u736502961_hys.user_answer_comment_details cd inner join u736502961_hys.user_personal_details pd on cd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id left join u736502961_hys.answers_comment_like_details cld on cd.comment_id = cld.comment_id and cld.user_id=%s where cd.comment_id=%s order by cd.compare_date desc;",
            data)
        commentlist = cursor.fetchall()
        data = (userid, commentlist[0]['comment_id'])
        cursor.execute(
            "select rd.reply_id reply_id, rd.image image, rd.comment_id comment_id, rd.answer_id answer_id, rd.question_id question_id, rd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, rd.reply reply, rd.reply_type, rd.like_count like_count, rd.compare_date compare_date, case when rld.like_type is null then '' else rld.like_type end like_type from u736502961_hys.user_answer_reply_details rd left join u736502961_hys.answers_reply_like_details rld on rld.reply_id=rd.reply_id and rld.user_id = %s inner join u736502961_hys.user_personal_details pd on rd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on rd.user_id=sd.user_id where rd.comment_id=%s order by rd.compare_date desc;",
            data)
        replyList = cursor.fetchall()
        commentlist[0]['reply_list'] = replyList
        resp = jsonify(commentlist)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_counts_in_answer_comment_details', methods=['POST'])
@cross_origin()
def update_counts_in_answer_comment_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _user_id = _json['user_id']
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_like_count, _reply_count, _user_id, _comment_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_answer_comment_details set like_count=%s, reply_count=%s where user_id=%s and comment_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_answer_reaction', methods=['POST'])
@cross_origin()
def update_answer_reaction():
    conn = None
    cursor = None
    try:
        _json = request.json
        _answer_id = _json["answer_id"]
        _user_id = _json["user_id"]
        _reaction = _json["reaction"]
        _reaction_type = _json['reaction_type']
        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _answer_id)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            if _reaction == 'like':
                cursor.execute(
                    "select like_type from u736502961_hys.answers_like_details where user_id=%s and answer_id=%s;",
                    data)
                row = cursor.fetchall()
                print(row)
                if len(row) == 0:
                    if _reaction_type == 'like':
                        cursor.execute(
                            "insert into u736502961_hys.answers_like_details(user_id,answer_id,like_type) values(%s, %s,'like');",
                            data)
                    elif _reaction_type == 'markasimp':
                        cursor.execute(
                            "insert into u736502961_hys.answers_like_details(user_id,answer_id,like_type) values(%s, %s,'markasimp');",
                            data)
                    elif _reaction_type == 'helpful':
                        cursor.execute(
                            "insert into u736502961_hys.answers_like_details(user_id,answer_id,like_type) values(%s, %s,'helpful');",
                            data)
                elif row[0]['like_type'] == 'like':
                    if _reaction_type == 'like':
                        cursor.execute(
                            "delete from u736502961_hys.answers_like_details where user_id=%s and answer_id=%s;", data)
                    elif _reaction_type == 'markasimp':
                        cursor.execute(
                            "update u736502961_hys.answers_like_details set like_type='markasimp' where user_id=%s and answer_id=%s;",
                            data)
                    elif _reaction_type == 'helpful':
                        cursor.execute(
                            "update u736502961_hys.answers_like_details set like_type='helpful' where user_id=%s and answer_id=%s;",
                            data)
                elif row[0]['like_type'] == 'markasimp':
                    if _reaction_type == 'like':
                        cursor.execute(
                            "update u736502961_hys.answers_like_details set like_type='like' where user_id=%s and answer_id=%s;",
                            data)
                    elif _reaction_type == 'markasimp':
                        cursor.execute(
                            "delete from u736502961_hys.answers_like_details where user_id=%s and answer_id=%s;",
                            data)
                    elif _reaction_type == 'helpful':
                        cursor.execute(
                            "update u736502961_hys.answers_like_details set like_type='helpful' where user_id=%s and answer_id=%s;",
                            data)
                elif row[0]['like_type'] == 'helpful':
                    if _reaction_type == 'like':
                        cursor.execute(
                            "update u736502961_hys.answers_like_details set like_type='like' where user_id=%s and answer_id=%s;",
                            data)
                    elif _reaction_type == 'markasimp':
                        cursor.execute(
                            "update u736502961_hys.answers_like_details set like_type='markasimp' where user_id=%s and answer_id=%s;",
                            data)
                    elif _reaction_type == 'helpful':
                        cursor.execute(
                            "delete from u736502961_hys.answers_like_details where user_id=%s and answer_id=%s;",
                            data)
            if _reaction == 'vote':
                cursor.execute(
                    "select vote_type from u736502961_hys.answers_vote_details where user_id=%s and answer_id=%s;",
                    data)
                row = cursor.fetchall()
                if len(row) == 0:
                    if _reaction_type == 'upvote':
                        cursor.execute(
                            "insert into u736502961_hys.answers_vote_details(user_id,answer_id,vote_type) values(%s, %s,'upvote');",
                            data)
                    elif _reaction_type == 'downvote':
                        cursor.execute(
                            "insert into u736502961_hys.answers_vote_details(user_id,answer_id,vote_type) values(%s, %s,'downvote');",
                            data)
                elif row[0]['vote_type'] == 'upvote':
                    if _reaction_type == 'upvote':
                        cursor.execute(
                            "delete from u736502961_hys.answers_vote_details where user_id=%s and answer_id=%s;", data)
                    elif _reaction_type == 'downvote':
                        cursor.execute(
                            "update u736502961_hys.answers_vote_details set vote_type='downvote' where user_id=%s and answer_id=%s;",
                            data)
                elif row[0]['vote_type'] == 'downvote':
                    if _reaction_type == 'upvote':
                        cursor.execute(
                            "update u736502961_hys.answers_vote_details set vote_type='upvote' where user_id=%s and answer_id=%s;",
                            data)
                    elif _reaction_type == 'downvote':
                        cursor.execute(
                            "delete from u736502961_hys.answers_vote_details where user_id=%s and answer_id=%s;",
                            data)
            conn.commit()
            resp = jsonify('Reaction updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_post_view_count', methods=['POST'])
@cross_origin()
def update_post_view_count():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _post_type = _json["post_type"]
        _user_id = _json['user_id']
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            if _post_type == 'qa':
                data = (_user_id, _post_id, _compare_date)
                cursor.execute(
                    "select post_id from u736502961_hys.user_post_view_details where user_id=%s and post_id=%s and compare_date=%s;",
                    data)
                row = cursor.fetchall()
                print(row)
                if len(row) == 0:
                    data = (_post_id, _post_type, _user_id, _compare_date)
                    cursor.execute(
                        "insert into u736502961_hys.user_post_view_details(post_id, post_type, user_id, compare_date) values(%s, %s, %s, %s);",
                        data)
                    cursor.execute(
                        "select view_count from u736502961_hys.user_question_details  where question_id=%s;", _post_id)
                    viewcount = cursor.fetchall()
                    updatecount = viewcount[0]['view_count'] + 1
                    data = (updatecount, _post_id)
                    cursor.execute(
                        "update u736502961_hys.user_question_details set view_count =%s where question_id=%s;", data)
            conn.commit()
            resp = jsonify('impression count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_answer_comment_reaction', methods=['POST'])
@cross_origin()
def update_answer_comment_reaction():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _user_id = _json['user_id']
        _like_type = _json["like_type"]
        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = (_user_id, _comment_id)
            cursor.execute(
                "select like_type from u736502961_hys.answers_comment_like_details where user_id=%s and comment_id=%s;",
                data)
            row = cursor.fetchall()
            print(row)
            if len(row) == 0:
                data = (_comment_id, _user_id)
                cursor.execute(
                    "insert into u736502961_hys.answers_comment_like_details(comment_id, user_id, like_type) values(%s, %s, 'like');",
                    data)
            elif row[0]['like_type'] == 'like':
                data = (_comment_id, _user_id)
                cursor.execute(
                    "delete from u736502961_hys.answers_comment_like_details where user_id=%s and comment_id=%s;",
                    data)
            conn.commit()
            resp = jsonify('reaction of comment updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_answer_reply', methods=['POST'])
@cross_origin()
def add_users_answer_reply():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _comment_id = _json["comment_id"]
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _reply = _json["reply"]
        _reply_type = _json["reply_type"]
        _like_count = _json["like_count"]
        _compare_date = _json["compare_date"]
        _image = _json["image"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _reply_id, _comment_id, _answer_id, _question_id, _user_id, _reply, _reply_type, _like_count,
                _compare_date, _image)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_answer_reply_details(reply_id, comment_id, answer_id, question_id, user_id, reply, reply_type, like_count, compare_date, image) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('reply on comment added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_counts_in_answer_reply_details', methods=['POST'])
@cross_origin()
def update_counts_in_answer_reply_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _user_id = _json['user_id']
        _like_count = _json["like_count"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_like_count, _user_id, _reply_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_answer_reply_details set like_count=%s where user_id=%s and reply_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_answer_reply', methods=['GET'])
def get_all_answer_reply():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select rd.reply_id reply_id, rd.comment_id comment_id, rd.answer_id answer_id, rd.question_id question_id, rd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, rd.reply reply, rd.reply_type, rd.like_count like_count, rd.compare_date compare_date from u736502961_hys.user_answer_reply_details rd inner join u736502961_hys.user_personal_details pd on rd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on rd.user_id=sd.user_id order by rd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_details', methods=['POST'])
@cross_origin()
def add_sm_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json['user_id']
        _post_type = _json["post_type"]
        _comment = _json["comment"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_post_id, _user_id, _post_type, _comment, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_post_details(post_id, user_id, post_type, comment, compare_date) values(%s ,%s ,%s ,%s ,%s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_mood_details', methods=['POST'])
@cross_origin()
def add_sm_mood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json['user_id']
        _message = _json["message"]
        _user_mood = _json["user_mood"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_post_id, _user_id, _message, _user_mood, _imagelist_id, _videolist_id, _usertaglist_id, _privacy,
                    _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_mood_details(post_id, user_id, message, user_mood, imagelist_id, videolist_id, usertaglist_id, privacy, like_count, comment_count, view_count, impression_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_images', methods=['POST'])
@cross_origin()
def add_sm_post_images():
    conn = None
    cursor = None
    try:
        _json = request.json
        _imagelist_id = _json["imagelist_id"]
        _image = _json['image']
        # validate the received values
        if request.method == 'POST':
            data = (_imagelist_id, _image)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into u736502961_hys.sm_post_images(imagelist_id, image) values(%s ,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_videos', methods=['POST'])
@cross_origin()
def add_sm_post_videos():
    conn = None
    cursor = None
    try:
        _json = request.json
        _videolist_id = _json["videolist_id"]
        _video = _json['video']
        _thumbnail = _json['thumbnail']
        # validate the received values
        if request.method == 'POST':
            data = (_videolist_id, _video, _thumbnail)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.sm_post_videos(videolist_id, video, thumbnail) values(%s ,%s,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_users_tagged', methods=['POST'])
@cross_origin()
def add_sm_post_users_tagged():
    conn = None
    cursor = None
    try:
        _json = request.json
        _usertaglist_id = _json["usertaglist_id"]
        _user_id = _json['user_id']
        # validate the received values
        if request.method == 'POST':
            data = (_usertaglist_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into u736502961_hys.sm_post_users_tagged(usertaglist_id, user_id) values(%s ,%s);",
                           data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_posts', methods=['GET'])
def get_all_sm_post():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select postd.post_id post_id, postd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city,sd.school_name school_name, floor(sd.grade) grade,postd.post_type post_type,postd.comment comment, postd.compare_date compare_date from u736502961_hys.user_sm_post_details postd inner join u736502961_hys.user_personal_details pd on postd.user_id = pd.user_id inner join u736502961_hys.user_school_details sd on postd.user_id = sd.user_id order by postd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_images', methods=['GET'])
def get_all_sm_images():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select imagelist_id, image from u736502961_hys.sm_post_images;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_videos', methods=['GET'])
def get_all_sm_videos():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_usertagged', methods=['GET'])
def get_all_sm_usertagged():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select usertaglist_id, user_id from u736502961_hys.sm_post_users_tagged;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_mood_posts/<string:userid>', methods=['GET'])
def get_all_sm_mood_posts(userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.*, md.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_mood_details md inner join u736502961_hys.user_personal_details pd on md.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on md.user_id=sd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = md.post_id and ld.user_id=%s order by md.compare_date desc;",
            userid)
        row = cursor.fetchall()
        for i in range(len(row)):
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[i]['usertaglist_id'])
            row[i]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[i]['videolist_id'])
            row[i]['video_list'] = cursor.fetchall()
            cursor.execute(
                "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                row[i]['imagelist_id'])
            row[i]['image_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_sm_mood_posts/<string:postid>/<string:userid>', methods=['GET'])
def get_sm_mood_posts(postid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, postid)
        cursor.execute(
            "select pd.*, md.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_mood_details md inner join u736502961_hys.user_personal_details pd on md.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on md.user_id=sd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = md.post_id and ld.user_id=%s where md.post_id=%s order by md.compare_date desc;",
            data)
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[0]['usertaglist_id'])
            row[0]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[0]['videolist_id'])
            row[0]['video_list'] = cursor.fetchall()
            cursor.execute(
                "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                row[0]['imagelist_id'])
            row[0]['image_list'] = cursor.fetchall()
            data = (userid, row[0]['post_id'])
            cursor.execute(
                "select cd.*, pd.*, sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=cd.comment_id and pld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",
                data)
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
                    row[0]['comment_list'][i]['image_list'] = cursor.fetchall()
                    data = (userid, row[0]['comment_list'][i]['comment_id'])
                    cursor.execute(
                        "select rd.*,pd.*,sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from  u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id=rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=rd.reply_id and pld.user_id=%s where rd.comment_id=%s order by rd.compare_date desc;",
                        data)
                    row[0]['comment_list'][i]['reply_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_comment_details', methods=['POST'])
@cross_origin()
def add_user_sm_comment_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _comment = _json["comment"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _comment_id, _post_id, _user_id, _comment, _imagelist_id, _videolist_id, _usertaglist_id, _like_count,
                _reply_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_comment_details(comment_id, post_id, user_id, comment, imagelist_id, videolist_id, usertaglist_id, like_count, reply_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_comment_posts', methods=['GET'])
def get_all_sm_comment_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.profilepic profilepic, cd.comment_id comment_id, cd.post_id post_id, cd.user_id user_id, cd.comment comment, cd.imagelist_id imagelist_id, cd.videolist_id videolist_id, cd.usertaglist_id usertaglist_id, cd.like_count like_count, cd.reply_count reply_count, cd.compare_date compare_date, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city, sd.school_name school_name, sd.grade grade from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id = cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id order by cd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_comment_details/<string:commentid>/<string:userid>', methods=['GET'])
def get_comment_details(commentid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, commentid)
        cursor.execute(
            "select cd.*, pd.*, sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=cd.comment_id and pld.user_id=%s where cd.comment_id=%s order by cd.compare_date desc;",
            data)
        row = cursor.fetchall()
        cursor.execute(
            "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
            row[0]['imagelist_id'])
        row[0]['image_list'] = cursor.fetchall()
        data = (userid, commentid)
        cursor.execute(
            "select rd.*,pd.*,sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from  u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id=rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=rd.reply_id and pld.user_id=%s where rd.comment_id=%s order by rd.compare_date desc;",
            data)
        row[0]['reply_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_reply_details', methods=['POST'])
@cross_origin()
def add_user_sm_reply_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _comment_id = _json["comment_id"]
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _reply = _json["reply"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _like_count = _json["like_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (_reply_id, _comment_id, _post_id, _user_id, _reply, _imagelist_id, _videolist_id, _usertaglist_id,
                    _like_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_reply_details(reply_id, comment_id, post_id, user_id, reply, imagelist_id, videolist_id, usertaglist_id, like_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_reply_posts', methods=['GET'])
def get_all_sm_reply_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.profilepic profilepic,rd.reply_id reply_id, rd.comment_id comment_id, rd.post_id post_id, rd.user_id user_id, rd.reply reply, rd.imagelist_id imagelist_id, rd.videolist_id videolist_id, rd.usertaglist_id usertaglist_id, rd.like_count like_count, rd.compare_date compare_date, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city, sd.school_name school_name, sd.grade grade from u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id = rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id order by rd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_cause_details', methods=['POST'])
@cross_origin()
def add_user_sm_cause_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _message = _json["message"]
        _datetime = _json["datetime"]
        _address = _json["address"]
        _date = _json["date"]
        _eventcategory = _json["eventcategory"]
        _eventname = _json["eventname"]
        _eventsubcategory = _json["eventsubcategory"]
        _eventtype = _json["eventtype"]
        _feedtype = _json["feedtype"]
        _frequency = _json["frequency"]
        _from_ = _json["from_"]
        _from24hrs = _json["from24hrs"]
        _fromtime = _json["fromtime"]
        _grade = _json["grade"]
        _latitude = _json["latitude"]
        _longitude = _json["longitude"]
        _meetingid = _json["meetingid"]
        _subject = _json["subject"]
        _theme = _json["theme"]
        _themeindex = _json["themeindex"]
        _to_ = _json["to_"]
        _to24hrs = _json["to24hrs"]
        _totime = _json["totime"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _message, _datetime, _address, _date, _eventcategory, _eventname, _eventsubcategory,
                _eventtype, _feedtype, _frequency, _from_, _from24hrs, _fromtime, _grade, _latitude, _longitude,
                _meetingid,
                _subject, _theme, _themeindex, _to_, _to24hrs, _totime, _imagelist_id, _videolist_id, _usertaglist_id,
                _privacy, _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_cause_details(post_id,user_id,message,datetime,address,date,eventcategory,eventname,eventsubcategory,eventtype,feedtype,frequency,from_,from24hrs,fromtime,grade,latitude,longitude,meetingid,subject,theme,themeindex ,to_ ,to24hrs,totime,imagelist_id ,videolist_id ,usertaglist_id ,privacy ,like_count ,comment_count ,view_count ,impression_count ,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_cause_posts/<string:userid>', methods=['GET'])
def get_all_sm_cause_posts(userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select cd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_cause_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=cd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = cd.post_id and ld.user_id=%s order by cd.compare_date desc;",
            userid)
        row = cursor.fetchall()
        for i in range(len(row)):
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[i]['usertaglist_id'])
            row[i]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[i]['videolist_id'])
            row[i]['video_list'] = cursor.fetchall()
            cursor.execute(
                "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                row[i]['imagelist_id'])
            row[i]['image_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_sm_cause_posts/<string:postid>/<string:userid>', methods=['GET'])
def get_sm_cause_posts(postid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, postid)
        cursor.execute(
            "select cd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_cause_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=cd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = cd.post_id and ld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",
            data)
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[0]['usertaglist_id'])
            row[0]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[0]['videolist_id'])
            row[0]['video_list'] = cursor.fetchall()
            cursor.execute(
                "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                row[0]['imagelist_id'])
            row[0]['image_list'] = cursor.fetchall()
            data = (userid, row[0]['post_id'])
            cursor.execute(
                "select cd.*, pd.*, sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=cd.comment_id and pld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",
                data)
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
                    row[0]['comment_list'][i]['image_list'] = cursor.fetchall()
                    data = (userid, row[0]['comment_list'][i]['comment_id'])
                    cursor.execute(
                        "select rd.*,pd.*,sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from  u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id=rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=rd.reply_id and pld.user_id=%s where rd.comment_id=%s order by rd.compare_date desc;",
                        data)
                    row[0]['comment_list'][i]['reply_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_bideas_details', methods=['POST'])
@cross_origin()
def add_user_sm_bideas_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _content = _json["content"]
        _theme = _json["theme"]
        _title = _json["title"]
        _identification = _json["identification"]
        _solution = _json["solution"]
        _target = _json["target"]
        _competitors = _json["competitors"]
        _swot = _json["swot"]
        _strategy = _json["strategy"]
        _funds = _json["funds"]
        _documentlist_id = _json["documentlist_id"]
        _videolist_id = _json["videolist_id"]
        _memberlist_id = _json["memberlist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _content, _theme, _title, _identification, _solution, _target, _competitors, _swot,
                _strategy, _funds, _documentlist_id, _videolist_id, _memberlist_id, _privacy, _like_count,
                _comment_count,
                _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_b_ideas_details(post_id, user_id, content, theme, title, identification, solution, target, competitors, swot, strategy, funds, documentlist_id, videolist_id, memberlist_id, privacy,like_count, comment_count, view_count, impression_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_bideas_posts/<string:userid>', methods=['GET'])
def get_all_sm_bideas_posts(userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select bd.*, pd.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_b_ideas_details bd inner join u736502961_hys.user_personal_details pd on bd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on bd.user_id = sd.user_id  left join u736502961_hys.sm_post_like_details ld on ld.post_id = bd.post_id and ld.user_id=%s order by bd.compare_date desc;",
            userid)
        row = cursor.fetchall()
        for i in range(len(row)):
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where tag.usertaglist_id = %s",
                row[i]['memberlist_id'])
            row[i]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select * from u736502961_hys.sm_upload_files_details where upload_id=%s", row[i]['documentlist_id'])
            row[i]['document_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[i]['videolist_id'])
            row[i]['video_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_sm_bideas_posts/<string:postid>/<string:userid>', methods=['GET'])
def get_sm_bideas_posts(postid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, postid)
        cursor.execute(
            "select bd.*, pd.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_b_ideas_details bd inner join u736502961_hys.user_personal_details pd on bd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on bd.user_id = sd.user_id  left join u736502961_hys.sm_post_like_details ld on ld.post_id = bd.post_id and ld.user_id=%s where bd.post_id=%s order by bd.compare_date desc;",
            data)
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where tag.usertaglist_id = %s",
                row[0]['memberlist_id'])
            row[0]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select * from u736502961_hys.sm_upload_files_details where upload_id=%s", row[0]['documentlist_id'])
            row[0]['document_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[0]['videolist_id'])
            row[0]['video_list'] = cursor.fetchall()
            data = (userid, row[0]['post_id'])
            cursor.execute(
                "select cd.*, pd.*, sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=cd.comment_id and pld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",
                data)
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
                    row[0]['comment_list'][i]['image_list'] = cursor.fetchall()
                    data = (userid, row[0]['comment_list'][i]['comment_id'])
                    cursor.execute(
                        "select rd.*,pd.*,sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from  u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id=rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=rd.reply_id and pld.user_id=%s where rd.comment_id=%s order by rd.compare_date desc;",
                        data)
                    row[0]['comment_list'][i]['reply_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_project_details', methods=['POST'])
@cross_origin()
def add_user_sm_project_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _content = _json["content"]
        _theme = _json["theme"]
        _title = _json["title"]
        _grade = _json["grade"]
        _subject = _json["subject"]
        _topic = _json["topic"]
        _requirements = _json["requirements"]
        _purchasedfrom = _json["purchasedfrom"]
        _procedure = _json["procedure_"]
        _theory = _json["theory"]
        _findings = _json["findings"]
        _similartheory = _json["similartheory"]
        _memberlist_id = _json["memberlist_id"]
        _projectvideourl = _json["projectvideourl"]
        _reqvideourl = _json["reqvideourl"]
        _summarydoc = _json["summarydoc"]
        _otherdoc = _json["otherdoc"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _content, _theme, _title, _grade, _subject, _topic, _requirements, _purchasedfrom,
                _procedure, _theory, _findings, _similartheory, _memberlist_id, _projectvideourl, _reqvideourl,
                _summarydoc,
                _otherdoc, _privacy, _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_project_details (post_id,user_id,content,theme,title,grade,subject,topic,requirements,purchasedfrom,procedure_,theory,findings,similartheory,memberlist_id,projectvideourl,reqvideourl,summarydoc,otherdoc,privacy,like_count,comment_count,view_count,impression_count,compare_date)  values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_project_posts/<string:userid>', methods=['GET'])
def get_all_sm_project_posts(userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_project_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s order by prd.compare_date desc;",
            userid)
        row = cursor.fetchall()
        for i in range(len(row)):
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[i]['memberlist_id'])
            row[i]['tag_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_sm_project_posts/<string:postid>/<string:userid>', methods=['GET'])
def get_sm_project_posts(postid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, postid)
        cursor.execute(
            "select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_project_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s where prd.post_id=%s order by prd.compare_date desc;",
            data)
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[0]['memberlist_id'])
            row[0]['tag_list'] = cursor.fetchall()
            data = (userid, row[0]['post_id'])
            cursor.execute(
                "select cd.*, pd.*, sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=cd.comment_id and pld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",
                data)
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
                    row[0]['comment_list'][i]['image_list'] = cursor.fetchall()
                    data = (userid, row[0]['comment_list'][i]['comment_id'])
                    cursor.execute(
                        "select rd.*,pd.*,sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from  u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id=rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=rd.reply_id and pld.user_id=%s where rd.comment_id=%s order by rd.compare_date desc;",
                        data)
                    row[0]['comment_list'][i]['reply_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_uploads_details', methods=['POST'])
@cross_origin()
def add_user_sm_uploads_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _upload_id = _json["upload_id"]
        _upload_type = _json["upload_type"]
        _user_id = _json["user_id"]
        _school_name = _json["school_name"]
        _exam_name = _json["exam_name"]
        _grade = _json["grade"]
        _subject = _json["subject"]
        _chapter = _json["chapter"]
        _topic = _json["topic"]
        _term = _json["term"]
        _year = _json["year"]
        _tags = _json["tags"]
        _description = _json["description"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _upload_id, _upload_type, _user_id, _school_name, _exam_name, _grade, _subject, _chapter, _topic, _term,
                _year, _tags, _description, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_uploads_details(upload_id, upload_type, user_id, school_name, exam_name, grade, subject, chapter, topic, term, year, tags, description, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_upload_file_details', methods=['POST'])
@cross_origin()
def add_sm_upload_file_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _upload_id = _json["upload_id"]
        _file_url = _json["file_url"]
        _file_ext = _json["file_ext"]
        _file_name = _json["file_name"]
        # validate the received values
        if request.method == 'POST':
            data = (_upload_id, _file_url, _file_ext, _file_name)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.sm_upload_files_details(upload_id, file_url, file_ext, file_name) values(%s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_uploads/<string:id>', methods=['GET'])
def get_user_uploads(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select upload_id, user_id, upload_type, school_name, exam_name, grade, subject, chapter, topic, term, year, tags, description, compare_date from u736502961_hys.user_sm_uploads_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_upload_files', methods=['GET'])
def get_user_upload_files():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select upload_id, file_url, file_name, file_ext,createdate from u736502961_hys.sm_upload_files_details order by createdate;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_achievement_details', methods=['POST'])
@cross_origin()
def add_user_achievement_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _achievement_id = _json["achievement_id"]
        _user_id = _json["user_id"]
        _scorecard_school_name = _json["scorecard_school_name"]
        _scorecard_board_name = _json["scorecard_board_name"]
        _ach_description = _json["ach_description"]
        _ach_image_url = _json["ach_image_url"]
        _ach_title = _json["ach_title"]
        _scorecard_grade = _json["scorecard_grade"]
        _scorecard_total_score = _json["scorecard_total_score"]
        _ach_type = _json["ach_type"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _achievement_id, _user_id, _scorecard_school_name, _scorecard_board_name, _ach_description,
                _ach_image_url,
                _ach_title, _scorecard_grade, _scorecard_total_score, _ach_type, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_achievement_details(achievement_id, user_id, scorecard_school_name, scorecard_board_name, ach_description, ach_image_url, ach_title, scorecard_grade, scorecard_total_score, ach_type, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_scorecard_details', methods=['POST'])
@cross_origin()
def add_user_scorecard_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _achievement_id = _json["achievement_id"]
        _user_id = _json["user_id"]
        _subject = _json["subject"]
        _marks = _json["marks"]
        # validate the received values
        if request.method == 'POST':
            data = (_achievement_id, _user_id, _subject, _marks)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_scorecard_details(achievement_id, user_id, subject, marks) values(%s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_privacy', methods=['POST'])
@cross_origin()
def add_user_privacy():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _comparedate = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _comparedate)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_privacy(user_id,address,ambition,dreamvacations,email,friends,mygroups,hobbies,library,mobileno,novels,placesvisited,schooladdress,scorecards,uploads,weakness,compare_date) values(%s,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,%s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_privacy/<string:id>', methods=['GET'])
def get_user_privacy(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, address, ambition, dreamvacations, email, friends, mygroups, hobbies, library, mobileno, novels, placesvisited, schooladdress, scorecards, uploads, weakness, compare_date from u736502961_hys.user_privacy where user_id=%s;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_user_privacy', methods=['POST'])
@cross_origin()
def update_user_privacy():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _address = _json["address"]
        _ambition = _json["ambition"]
        _dreamvacations = _json["dreamvacations"]
        _email = _json["email"]
        _friends = _json["friends"]
        _mygroups = _json["mygroups"]
        _hobbies = _json["hobbies"]
        _library = _json["library"]
        _mobileno = _json["mobileno"]
        _novels = _json["novels"]
        _placesvisited = _json["placesvisited"]
        _schooladdress = _json["schooladdress"]
        _scorecards = _json["scorecards"]
        _uploads = _json["uploads"]
        _weakness = _json["weakness"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _address, _ambition, _dreamvacations, _email, _friends, _mygroups, _hobbies, _library, _mobileno,
                _novels,
                _placesvisited, _schooladdress, _scorecards, _uploads, _weakness, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_privacy set address = %s ,ambition = %s ,dreamvacations = %s ,email = %s ,friends = %s ,mygroups = %s ,hobbies = %s ,library = %s ,mobileno = %s ,novels = %s ,placesvisited = %s ,schooladdress = %s ,scorecards = %s ,uploads = %s ,weakness = %s where user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_achievement_details/<string:id>', methods=['GET'])
def get_user_achievement_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select achievement_id, user_id, scorecard_school_name, scorecard_board_name, ach_description, ach_image_url, ach_title, scorecard_grade, scorecard_total_score, ach_type, compare_date from u736502961_hys.user_achievement_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_scorecard_details/<string:id>', methods=['GET'])
def get_user_scorecard_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select achievement_id, user_id, subject,marks from u736502961_hys.user_scorecard_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_like_post_details', methods=['POST'])
@cross_origin()
def add_sm_like_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_type = _json["like_type"]

        # validate the received values
        if request.method == 'POST':
            data = (_post_id, _user_id, _like_type)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.sm_post_like_details(post_id, user_id, like_type) values(%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_sm_like_post_details', methods=['POST'])
@cross_origin()
def update_sm_like_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_type = _json["like_type"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_type, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.sm_post_like_details set like_type=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_sm_like_post_details', methods=['POST'])
@cross_origin()
def delete_sm_like_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_type = _json["like_type"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_type, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.sm_post_like_details where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_sm_like_post_details/<string:id>', methods=['GET'])
def get_sm_like_post_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, post_id,post_type, like_type from u736502961_hys.sm_post_like_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_sm_mood_post_count_details', methods=['POST'])
@cross_origin()
def update_sm_mood_post_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_mood_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_user_sm_cause_count_details', methods=['POST'])
@cross_origin()
def update_user_sm_cause_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_cause_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_user_sm_b_ideas_count_details', methods=['POST'])
@cross_origin()
def update_user_sm_b_ideas_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_b_ideas_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_user_sm_project_count_details', methods=['POST'])
@cross_origin()
def update_user_sm_project_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_project_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_blog_post_details', methods=['POST'])
@cross_origin()
def add_sm_blog_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _blogger_name = _json["blogger_name"]
        _blog_title = _json["blog_title"]
        _blog_intro = _json['blog_intro']
        _blog_content = _json["blog_content"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _image_url = _json["image_url"]
        _personal_bio = _json["personal_bio"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _post_id, _user_id, _blogger_name, _blog_title, _blog_intro, _blog_content, _like_count, _comment_count,
                _view_count, _impression_count, _image_url, _personal_bio, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_blog_details(post_id, user_id, blogger_name, blog_title,blog_intro,blog_content,like_count,comment_count, view_count,impression_count, image_url, personal_bio,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_blog_category_details', methods=['POST'])
@cross_origin()
def add_sm_blog_category_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _blog_category = _json["blog_category"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _blog_category, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_blog_category_details(post_id, blog_category,compare_date) values(%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_blog_posts/<string:id>', methods=['GET'])
def get_all_sm_blog_posts(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (id)
        cursor.execute(
            "select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_blog_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s order by prd.compare_date desc;",
            data)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_sm_blog_posts/<string:postid>/<string:userid>', methods=['GET'])
def get_sm_blog_posts(postid, userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, postid)
        cursor.execute(
            "select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_blog_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s where prd.post_id=%s order by prd.compare_date desc;",
            data)
        row = cursor.fetchall()
        if len(row) > 0:
            data = (userid, row[0]['post_id'])
            cursor.execute(
                "select cd.*, pd.*, sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=cd.comment_id and pld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",
                data)
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
                    row[0]['comment_list'][i]['image_list'] = cursor.fetchall()
                    data = (userid, row[0]['comment_list'][i]['comment_id'])
                    cursor.execute(
                        "select rd.*,pd.*,sd.*, case when pld.like_type is null then '' else pld.like_type end like_type from  u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id=rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id left join u736502961_hys.sm_post_like_details pld on pld.post_id=rd.reply_id and pld.user_id=%s where rd.comment_id=%s order by rd.compare_date desc;",
                        data)
                    row[0]['comment_list'][i]['reply_list'] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_reaction_details', methods=['POST'])
@cross_origin()
def add_sm_reaction_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _do_post = _json["do_post"]

        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _post_type = _json["post_type"]
        _like_type = _json["like_type"]

        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _reply_count = _json["reply_count"]

        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_post_id, _user_id)
            cursor.execute("delete from u736502961_hys.sm_post_like_details where post_id=%s and user_id=%s;", data)
            if _do_post == 'TRUE':
                # TRUE is used to insert as well as update reaction
                data = (_post_id, _user_id, _post_type, _like_type)
                cursor.execute(
                    "insert into u736502961_hys.sm_post_like_details(post_id, user_id, post_type, like_type) values(%s, %s, %s, %s);",
                    data)
            if _post_type == 'Mood':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_mood_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'blog':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_blog_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'cause|teachunprevilagedKids':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_cause_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'projectdiscuss':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_project_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'businessideas':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_b_ideas_details like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'comment':
                data = (_like_count, _reply_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_comment_details set like_count=%s, reply_count=%s where comment_id=%s;",
                    data)
            elif _post_type == 'reply':
                data = (_like_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_reply_details set like_count=%s where reply_id=%s;",
                    data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_question_saved_details', methods=['POST'])
@cross_origin()
def add_question_saved_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]
        _compare_date = _json["compare_date"]

        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = (_user_id, _question_id)
            cursor.execute(
                "select * from u736502961_hys.questions_saved_details where user_id = %s and question_id = %s;",
                data)
            row = cursor.fetchall()
            if len(row) == 0:
                data = (_user_id, _question_id, _compare_date)
                cursor.execute(
                    "insert into u736502961_hys.questions_saved_details(user_id, question_id, compare_date) values(%s, %s, %s);",
                    data)
            else:
                data = (_user_id, _question_id)
                cursor.execute(
                    "delete from u736502961_hys.questions_saved_details where user_id=%s and question_id=%s;",
                    data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_question_saved_details', methods=['POST'])
@cross_origin()
def delete_question_saved_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]
        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_saved_details where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_question_saved_details/<string:id>', methods=['GET'])
def get_question_saved_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, question_id, compare_date from u736502961_hys.questions_saved_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_question_bookmarked_details', methods=['POST'])
@cross_origin()
def add_question_bookmarked_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]
        _compare_date = _json["compare_date"]

        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = (_user_id, _question_id)
            cursor.execute(
                "select * from u736502961_hys.questions_bookmarked_details where user_id=%s and question_id=%s;",
                data)
            row = cursor.fetchall()
            if len(row) == 0:
                data = (_user_id, _question_id, _compare_date)
                cursor.execute(
                    "insert into u736502961_hys.questions_bookmarked_details(user_id, question_id, compare_date) values(%s, %s, %s);",
                    data)
            else:
                data = (_user_id, _question_id)
                cursor.execute(
                    "delete from u736502961_hys.questions_bookmarked_details where user_id=%s and question_id=%s;",
                    data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_notification_details', methods=['POST'])
@cross_origin()
def add_notification_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _notify_id = _json["notify_id"]
        _notify_type = _json["notify_type"]
        _section = _json["section"]
        _sender_id = _json["sender_id"]
        _receiver_id = _json["receiver_id"]
        _token = _json["token"]
        _title = _json["title"]
        _message = _json["message"]
        _post_id = _json["post_id"]
        _post_type = _json["post_type"]
        _is_clicked = _json["is_clicked"]
        _compare_date = _json["compare_date"]
        _addordelete = _json["addordelete"]

        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data1 = (_notify_type, _section, _sender_id, _post_id)
            cursor.execute(
                "select * from u736502961_hys.notification_details where notify_type=%s and section=%s and sender_id=%s and post_id=%s;",
                data1)
            row = cursor.fetchall()
            print(row)
            cursor.close()
            if row.__gt__(0):
                if _addordelete == "delete":
                    cursor = conn.cursor()
                    data2 = (_notify_type, _section, _sender_id, _post_id)
                    cursor.execute(
                        "delete from u736502961_hys.notification_details where notify_type=%s and section=%s and sender_id=%s and post_id=%s;",
                        data2)
                    print("delete")
                    conn.commit()
                    resp = jsonify('data added successfully!')
                    resp.status_code = 200
                    return resp
                else:
                    cursor = conn.cursor()
                    data2 = (_notify_type, _section, _sender_id, _post_id)
                    cursor.execute(
                        "delete from u736502961_hys.notification_details where notify_type=%s and section=%s and sender_id=%s and post_id=%s;",
                        data2)
                    print("delete")
                    data = (
                        _notify_id, _notify_type, _section, _sender_id, _receiver_id, _token, _title, _message,
                        _post_id,
                        _post_type, _is_clicked, _compare_date)
                    cursor.execute(
                        "insert into u736502961_hys.notification_details(notify_id, notify_type, section, sender_id, receiver_id, token, title, message, post_id, post_type, is_clicked, compare_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                        data)
                    print("inserted")
                    conn.commit()
                    resp = jsonify('data added successfully!')
                    resp.status_code = 200
                    return resp
            else:
                cursor = conn.cursor()
                data = (
                    _notify_id, _notify_type, _section, _sender_id, _receiver_id, _token, _title, _message, _post_id,
                    _post_type, _is_clicked, _compare_date)
                cursor.execute(
                    "insert into u736502961_hys.notification_details(notify_id, notify_type, section, sender_id, receiver_id, token, title, message, post_id, post_type, is_clicked, compare_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    data)
                print("inserted only")
                conn.commit()
                resp = jsonify('data added successfully!')
                resp.status_code = 200
                return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_question_bookmarked_details', methods=['POST'])
@cross_origin()
def delete_question_bookmarked_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]

        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_bookmarked_details where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_question_bookmarked_details/<string:id>', methods=['GET'])
def get_question_bookmarked_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, question_id, compare_date from u736502961_hys.questions_bookmarked_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_notifications/<string:id>', methods=['GET'])
def get_all_notifications(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.notification_details nd inner join u736502961_hys.user_personal_details pd on nd.sender_id=pd.user_id inner join u736502961_hys.user_school_details sd on nd.sender_id=sd.user_id   where nd.receiver_id = %s order by nd.compare_date desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_notification_details', methods=['POST'])
@cross_origin()
def update_notification_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _notify_id = _json["notify_id"]

        # validate the received values
        if request.method == 'POST':
            data = _notify_id
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.notification_details set is_clicked='true' where notify_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_notification_details', methods=['POST'])
@cross_origin()
def delete_notification_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _notify_id = _json["notify_id"]

        # validate the received values
        if request.method == 'POST':
            data = (_notify_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.notification_details where notify_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_userlogs_details', methods=['POST'])
@cross_origin()
def add_userlogs_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _post_type = _json["post_type"]
        _post_section = _json["post_section"]
        _compare_date = _json["compare_date"]
        _current_status = _json["status"]
        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _post_id, _post_type, _post_section, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "select * from u736502961_hys.userlogs where user_id=%s and post_id=%s and post_type=%s and post_section=%s and compare_date=%s;",
                data)
            row = cursor.fetchall()
            print(row)
            cursor.close()
            if row.__gt__(0):
                print("")
            else:
                _log_id = _user_id + _post_id + _compare_date
                data = (_log_id, _user_id, _post_id, _post_type, _post_section, 0, 0, _compare_date)
                cursor.execute(
                    "insert into u736502961_hys.userlogs(log_id, user_id, post_id, post_type, post_section, activetime, visitcounts, compare_date) values (%s, %s, %s, %s, %s, %s, %s, %s);",
                    data)
                print("inserted")
                conn.commit()
                resp = jsonify('data added successfully!')
                resp.status_code = 200
                return resp
                resp.headers.add("Access-Control-Allow-Origin", "*")
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_live_books_categories/<int:grade>', methods=['GET'])
def get_live_books_categories(grade):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select distinct subject_ from u736502961_hys.live_books where grade=%s;", grade)
        row = cursor.fetchall()
        if len(row) > 0:
            for i in range(len(row)):
                data = (grade, row[i]["subject_"])
                cursor.execute(
                    "select distinct publication, part, dictionary_id,'https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/ncrt_class_10_cover.jpg?alt=media&token=39acd6e2-f598-4b1a-babc-565fd556cf6e' as publicationImageURL from u736502961_hys.live_books where grade=%s and subject_=%s;",
                    data)
                row[i]["distinct_publication"] = cursor.fetchall()
                row[i][
                    "subjectImageURL"] = "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/OIP.jpg?alt=media&token=5000c2f0-4c56-42d0-bb5e-6a1e95584cb7"
        resp = jsonify({"grade": grade,
                        "distinct_subjects": row
                        })
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_live_books/<string:dictionary_id>', methods=['GET'])
def get_live_books(dictionary_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from u736502961_hys.live_books where dictionary_id=%s;", dictionary_id)
        row = cursor.fetchall()
        if len(row) > 0:
            if row[0]["dictionary_id"] == 'economics10ncert01':
                row[0]["dictionary_list"] = economics10ncert01
            elif row[0]["dictionary_id"] == 'geography10ncert01':
                row[0]["dictionary_list"] = geography10ncert01
            elif row[0]["dictionary_id"] == 'history10ncert01':
                row[0]["dictionary_list"] = history10ncert01
            elif row[0]["dictionary_id"] == 'mathematics10ncert01':
                row[0]["dictionary_list"] = mathematics10ncert01
            elif row[0]["dictionary_id"] == 'civics10ncert01':
                row[0]["dictionary_list"] = civics10ncert01
            elif row[0]["dictionary_id"] == 'science10ncert01':
                row[0]["dictionary_list"] = science10ncert01
            elif row[0]["dictionary_id"] == 'accountancy12ncert01p01':
                row[0]["dictionary_list"] = accountancy12ncert01p01
            elif row[0]["dictionary_id"] == 'accountancy12ncert01p02':
                row[0]["dictionary_list"] = accountancy12ncert01p02
            elif row[0]["dictionary_id"] == 'accountancy12ncert01p03':
                row[0]["dictionary_list"] = accountancy12ncert01p03
            elif row[0]["dictionary_id"] == 'biology12ncert01':
                row[0]["dictionary_list"] = biology12ncert01
            elif row[0]["dictionary_id"] == 'businessStudies12ncert01p01':
                row[0]["dictionary_list"] = businessStudies12ncert01p01
            elif row[0]["dictionary_id"] == 'businessStudies12ncert01p02':
                row[0]["dictionary_list"] = businessStudies12ncert01p02
            elif row[0]["dictionary_id"] == 'chemistry12ncert01p01':
                row[0]["dictionary_list"] = chemistry12ncert01p01
            elif row[0]["dictionary_id"] == 'chemistry12ncert01p02':
                row[0]["dictionary_list"] = chemistry12ncert01p02
            elif row[0]["dictionary_id"] == 'mathematics12ncert01':
                row[0]["dictionary_list"] = mathematics12ncert01
            elif row[0]["dictionary_id"] == 'physics12ncert01':
                row[0]["dictionary_list"] = physics12ncert01
            elif row[0]["dictionary_id"] == 'economics12ncert01':
                row[0]["dictionary_list"] = economics12ncert01
            elif row[0]["dictionary_id"] == 'geography12ncert01p01':
                row[0]["dictionary_list"] = geography12ncert01p01
            elif row[0]["dictionary_id"] == 'geography12ncert01p02':
                row[0]["dictionary_list"] = geography12ncert01p02
            elif row[0]["dictionary_id"] == 'geography12ncert01p03':
                row[0]["dictionary_list"] = geography12ncert01p03
            elif row[0]["dictionary_id"] == 'history12ncert01':
                row[0]["dictionary_list"] = history12ncert01
            elif row[0]["dictionary_id"] == 'civics12ncert01p01':
                row[0]["dictionary_list"] = civics12ncert01p01
            elif row[0]["dictionary_id"] == 'civics12ncert01p02':
                row[0]["dictionary_list"] = civics12ncert01p02
            elif row[0]["dictionary_id"] == 'accountancy11ncert01p01':
                row[0]["dictionary_list"] = accountancy11ncert01p01
            elif row[0]["dictionary_id"] == 'accountancy11ncert01p02':
                row[0]["dictionary_list"] = accountancy11ncert01p02
            elif row[0]["dictionary_id"] == 'biology11ncert01':
                row[0]["dictionary_list"] = biology11ncert01
            elif row[0]["dictionary_id"] == 'businessStudies11ncert01':
                row[0]["dictionary_list"] = businessStudies11ncert01
            elif row[0]["dictionary_id"] == 'chemistry11ncert01':
                row[0]["dictionary_list"] = chemistry11ncert01
            elif row[0]["dictionary_id"] == 'computerScience11ncert01':
                row[0]["dictionary_list"] = computerScience11ncert01
            elif row[0]["dictionary_id"] == 'mathematics11ncert01':
                row[0]["dictionary_list"] = mathematics11ncert01
            elif row[0]["dictionary_id"] == 'physics11ncert01':
                row[0]["dictionary_list"] = physics11ncert01
            elif row[0]["dictionary_id"] == 'economics11ncert01p01':
                row[0]["dictionary_list"] = economics11ncert01p01
            elif row[0]["dictionary_id"] == 'economics11ncert01p02':
                row[0]["dictionary_list"] = economics11ncert01p02
            elif row[0]["dictionary_id"] == 'geography11ncert01p01':
                row[0]["dictionary_list"] = geography11ncert01p01
            elif row[0]["dictionary_id"] == 'geography11ncert01p02':
                row[0]["dictionary_list"] = geography11ncert01p02
            elif row[0]["dictionary_id"] == 'geography11ncert01p03':
                row[0]["dictionary_list"] = geography11ncert01p03
            elif row[0]["dictionary_id"] == 'history11ncert01':
                row[0]["dictionary_list"] = history11ncert01
            elif row[0]["dictionary_id"] == 'civics11ncert01':
                row[0]["dictionary_list"] = civics11ncert01
            elif row[0]["dictionary_id"] == 'mathematics6ncert01':
                row[0]["dictionary_list"] = mathematics6ncert01
            elif row[0]["dictionary_id"] == 'science6ncert01':
                row[0]["dictionary_list"] = science6ncert01
            elif row[0]["dictionary_id"] == 'geography6ncert01':
                row[0]["dictionary_list"] = geography6ncert01
            elif row[0]["dictionary_id"] == 'history6ncert01':
                row[0]["dictionary_list"] = history6ncert01
            elif row[0]["dictionary_id"] == 'mathematics7ncert01':
                row[0]["dictionary_list"] = mathematics7ncert01
            elif row[0]["dictionary_id"] == 'science7ncert01':
                row[0]["dictionary_list"] = science7ncert01
            elif row[0]["dictionary_id"] == 'geography7ncert01':
                row[0]["dictionary_list"] = geography7ncert01
            elif row[0]["dictionary_id"] == 'history7ncert01':
                row[0]["dictionary_list"] = history7ncert01
            elif row[0]["dictionary_id"] == 'mathematics8ncert01':
                row[0]["dictionary_list"] = mathematics8ncert01
            elif row[0]["dictionary_id"] == 'science8ncert01':
                row[0]["dictionary_list"] = science8ncert01
            elif row[0]["dictionary_id"] == 'geography8ncert01':
                row[0]["dictionary_list"] = geography8ncert01
            elif row[0]["dictionary_id"] == 'history8ncert01':
                row[0]["dictionary_list"] = history8ncert01
            elif row[0]["dictionary_id"] == 'mathematics9ncert01':
                row[0]["dictionary_list"] = mathematics9ncert01
            elif row[0]["dictionary_id"] == 'science9ncert01':
                row[0]["dictionary_list"] = science9ncert01
            elif row[0]["dictionary_id"] == 'economics9ncert01':
                row[0]["dictionary_list"] = economics9ncert01
            elif row[0]["dictionary_id"] == 'geography9ncert01':
                row[0]["dictionary_list"] = geography9ncert01
            elif row[0]["dictionary_id"] == 'history9ncert01':
                row[0]["dictionary_list"] = history9ncert01

        resp = jsonify({"createdate": row[0]["createdate"],
                        "publication": row[0]["publication"],
                        "pub_edition": row[0]["pub_edition"],
                        "dictionary_id": row[0]["dictionary_id"],
                        "subject_": row[0]["subject_"],
                        "grade": row[0]["grade"],
                        "dictionary_list": row[0]["dictionary_list"]})
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_live_books_initial/<int:grade>', methods=['GET'])
def get_live_books_initial(grade):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from u736502961_hys.live_books where grade=%s;", grade)
        row = cursor.fetchall()
        if len(row) > 0:
            for i in range(len(row)):
                if row[i]["dictionary_id"] == 'economics10ncert01':
                    row[i]["dictionary_list"] = economics10ncert01
                elif row[i]["dictionary_id"] == 'geography10ncert01':
                    row[i]["dictionary_list"] = geography10ncert01
                elif row[i]["dictionary_id"] == 'history10ncert01':
                    row[i]["dictionary_list"] = history10ncert01
                elif row[i]["dictionary_id"] == 'mathematics10ncert01':
                    row[i]["dictionary_list"] = mathematics10ncert01
                elif row[i]["dictionary_id"] == 'civics10ncert01':
                    row[i]["dictionary_list"] = civics10ncert01
                elif row[i]["dictionary_id"] == 'science10ncert01':
                    row[i]["dictionary_list"] = science10ncert01
                elif row[i]["dictionary_id"] == 'accountancy12ncert01p01':
                    row[i]["dictionary_list"] = accountancy12ncert01p01
                elif row[i]["dictionary_id"] == 'accountancy12ncert01p02':
                    row[i]["dictionary_list"] = accountancy12ncert01p02
                elif row[i]["dictionary_id"] == 'accountancy12ncert01p03':
                    row[i]["dictionary_list"] = accountancy12ncert01p03
                elif row[i]["dictionary_id"] == 'biology12ncert01':
                    row[i]["dictionary_list"] = biology12ncert01
                elif row[i]["dictionary_id"] == 'businessStudies12ncert01p01':
                    row[i]["dictionary_list"] = businessStudies12ncert01p01
                elif row[i]["dictionary_id"] == 'businessStudies12ncert01p02':
                    row[i]["dictionary_list"] = businessStudies12ncert01p02
                elif row[i]["dictionary_id"] == 'chemistry12ncert01p01':
                    row[i]["dictionary_list"] = chemistry12ncert01p01
                elif row[i]["dictionary_id"] == 'chemistry12ncert01p02':
                    row[i]["dictionary_list"] = chemistry12ncert01p02
                elif row[i]["dictionary_id"] == 'mathematics12ncert01':
                    row[i]["dictionary_list"] = mathematics12ncert01
                elif row[i]["dictionary_id"] == 'physics12ncert01':
                    row[i]["dictionary_list"] = physics12ncert01
                elif row[i]["dictionary_id"] == 'economics12ncert01':
                    row[i]["dictionary_list"] = economics12ncert01
                elif row[i]["dictionary_id"] == 'geography12ncert01p01':
                    row[i]["dictionary_list"] = geography12ncert01p01
                elif row[i]["dictionary_id"] == 'geography12ncert01p02':
                    row[i]["dictionary_list"] = geography12ncert01p02
                elif row[i]["dictionary_id"] == 'geography12ncert01p03':
                    row[i]["dictionary_list"] = geography12ncert01p03
                elif row[i]["dictionary_id"] == 'history12ncert01':
                    row[i]["dictionary_list"] = history12ncert01
                elif row[i]["dictionary_id"] == 'civics12ncert01p01':
                    row[i]["dictionary_list"] = civics12ncert01p01
                elif row[i]["dictionary_id"] == 'civics12ncert01p02':
                    row[i]["dictionary_list"] = civics12ncert01p02
                elif row[i]["dictionary_id"] == 'accountancy11ncert01p01':
                    row[i]["dictionary_list"] = accountancy11ncert01p01
                elif row[i]["dictionary_id"] == 'accountancy11ncert01p02':
                    row[i]["dictionary_list"] = accountancy11ncert01p02
                elif row[i]["dictionary_id"] == 'biology11ncert01':
                    row[i]["dictionary_list"] = biology11ncert01
                elif row[i]["dictionary_id"] == 'businessStudies11ncert01':
                    row[i]["dictionary_list"] = businessStudies11ncert01
                elif row[i]["dictionary_id"] == 'chemistry11ncert01':
                    row[i]["dictionary_list"] = chemistry11ncert01
                elif row[i]["dictionary_id"] == 'computerScience11ncert01':
                    row[i]["dictionary_list"] = computerScience11ncert01
                elif row[i]["dictionary_id"] == 'mathematics11ncert01':
                    row[i]["dictionary_list"] = mathematics11ncert01
                elif row[i]["dictionary_id"] == 'physics11ncert01':
                    row[i]["dictionary_list"] = physics11ncert01
                elif row[i]["dictionary_id"] == 'economics11ncert01p01':
                    row[i]["dictionary_list"] = economics11ncert01p01
                elif row[i]["dictionary_id"] == 'economics11ncert01p02':
                    row[i]["dictionary_list"] = economics11ncert01p02
                elif row[i]["dictionary_id"] == 'geography11ncert01p01':
                    row[i]["dictionary_list"] = geography11ncert01p01
                elif row[i]["dictionary_id"] == 'geography11ncert01p02':
                    row[i]["dictionary_list"] = geography11ncert01p02
                elif row[i]["dictionary_id"] == 'geography11ncert01p03':
                    row[i]["dictionary_list"] = geography11ncert01p03
                elif row[i]["dictionary_id"] == 'history11ncert01':
                    row[i]["dictionary_list"] = history11ncert01
                elif row[i]["dictionary_id"] == 'civics11ncert01':
                    row[i]["dictionary_list"] = civics11ncert01
                elif row[i]["dictionary_id"] == 'mathematics6ncert01':
                    row[i]["dictionary_list"] = mathematics6ncert01
                elif row[i]["dictionary_id"] == 'science6ncert01':
                    row[i]["dictionary_list"] = science6ncert01
                elif row[i]["dictionary_id"] == 'geography6ncert01':
                    row[i]["dictionary_list"] = geography6ncert01
                elif row[i]["dictionary_id"] == 'history6ncert01':
                    row[i]["dictionary_list"] = history6ncert01
                elif row[i]["dictionary_id"] == 'mathematics7ncert01':
                    row[i]["dictionary_list"] = mathematics7ncert01
                elif row[i]["dictionary_id"] == 'science7ncert01':
                    row[i]["dictionary_list"] = science7ncert01
                elif row[i]["dictionary_id"] == 'geography7ncert01':
                    row[i]["dictionary_list"] = geography7ncert01
                elif row[i]["dictionary_id"] == 'history7ncert01':
                    row[i]["dictionary_list"] = history7ncert01
                elif row[i]["dictionary_id"] == 'mathematics8ncert01':
                    row[i]["dictionary_list"] = mathematics8ncert01
                elif row[i]["dictionary_id"] == 'science8ncert01':
                    row[i]["dictionary_list"] = science8ncert01
                elif row[i]["dictionary_id"] == 'geography8ncert01':
                    row[i]["dictionary_list"] = geography8ncert01
                elif row[i]["dictionary_id"] == 'history8ncert01':
                    row[i]["dictionary_list"] = history8ncert01
                elif row[i]["dictionary_id"] == 'mathematics9ncert01':
                    row[i]["dictionary_list"] = mathematics9ncert01
                elif row[i]["dictionary_id"] == 'science9ncert01':
                    row[i]["dictionary_list"] = science9ncert01
                elif row[i]["dictionary_id"] == 'economics9ncert01':
                    row[i]["dictionary_list"] = economics9ncert01
                elif row[i]["dictionary_id"] == 'geography9ncert01':
                    row[i]["dictionary_list"] = geography9ncert01
                elif row[i]["dictionary_id"] == 'history9ncert01':
                    row[i]["dictionary_list"] = history9ncert01

        cursor.execute("select distinct subject_ from u736502961_hys.live_books where grade=%s;", grade)
        row[0]["distinct_subjects"] = cursor.fetchall()
        cursor.execute("select distinct publication from u736502961_hys.live_books where grade=%s;", grade)
        row[0]["distinct_publication"] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_live_book_question_papers/<string:subject>/<string:grade>', methods=['GET'])
def get_live_book_question_papers(subject, grade):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (grade, subject)
        cursor.execute("select * from u736502961_hys.live_books_question_papers where grade=%s and subject_=%s;", data)
        row = cursor.fetchall()
        if len(row) > 0:
            for i in range(len(row)):
                if row[i]["dictionary_id"] == 'mathematics10cbseqp':
                    row[i]["dictionary_list"] = mathematics10cbseqp
                elif row[i]["dictionary_id"] == 'science10cbseqp':
                    row[i]["dictionary_list"] = science10cbseqp
                elif row[i]["dictionary_id"] == 'socialScience10cbseqp':
                    row[i]["dictionary_list"] = socialScience10cbseqp
                elif row[i]["dictionary_id"] == 'accountancy12cbseqp':
                    row[i]["dictionary_list"] = accountancy12cbseqp
                elif row[i]["dictionary_id"] == 'biology12cbseqp':
                    row[i]["dictionary_list"] = biology12cbseqp
                elif row[i]["dictionary_id"] == 'businessStudies12cbseqp':
                    row[i]["dictionary_list"] = businessStudies12cbseqp
                elif row[i]["dictionary_id"] == 'chemistry12cbseqp':
                    row[i]["dictionary_list"] = chemistry12cbseqp
                elif row[i]["dictionary_id"] == 'history12cbseqp':
                    row[i]["dictionary_list"] = history12cbseqp
                elif row[i]["dictionary_id"] == 'physics12cbseqp':
                    row[i]["dictionary_list"] = physics12cbseqp
                elif row[i]["dictionary_id"] == 'accountancy11cbseqp':
                    row[i]["dictionary_list"] = accountancy11cbseqp
                elif row[i]["dictionary_id"] == 'biology11cbseqp':
                    row[i]["dictionary_list"] = biology11cbseqp
                elif row[i]["dictionary_id"] == 'businessStudies11cbseqp':
                    row[i]["dictionary_list"] = businessStudies11cbseqp
                elif row[i]["dictionary_id"] == 'chemistry11cbseqp':
                    row[i]["dictionary_list"] = chemistry11cbseqp
                elif row[i]["dictionary_id"] == 'physics11cbseqp':
                    row[i]["dictionary_list"] = physics11cbseqp
        resp = jsonify({
            "dictionary_id": row[0]["dictionary_id"],
            "dictionary_list": row[0]["dictionary_list"],
            "grade": row[0]["grade"],
            "subject_": row[0]["subject_"],
            "createdate": row[0]["createdate"]
        })
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_epub_selected_text', methods=['POST'])
@cross_origin()
def add_user_epub_selected_text():
    conn = None
    cursor = None
    try:
        _json = request.json
        _book_id = _json["book_id"]
        _chapter_id = _json["chapter_id"]
        _user_id = _json["user_id"]
        _base_offset = _json["base_offset"]
        _extent_offset = _json["extent_offset"]
        _tag_index = _json["tag_index"]
        _color = _json["color"]
        _selection_type = _json["selection_type"]
        _level = _json["level"]
        _text_selected = _json["text_selected"]
        # validate the received values
        if request.method == 'POST':
            data = (
            _book_id, _chapter_id, _user_id, _base_offset, _extent_offset, _tag_index, _color, _selection_type, _level,
            _text_selected)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "insert into u736502961_hys.user_epub_select(book_id,chapter_id,user_id,base_offset,extent_offset,tag_index,color,selection_type,level_, text_selected) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                data)
            cursor.close()
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
            resp.headers.add("Access-Control-Allow-Origin", "*")
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_epub_selected_text/<string:id>', methods=['GET'])
def get_user_epub_selected_text(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from u736502961_hys.user_epub_select where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_user_epub_selected_text', methods=['POST'])
@cross_origin()
def delete_user_epub_selected_text():
    conn = None
    cursor = None
    try:
        _json = request.json
        _book_id = _json["book_id"]
        _chapter_id = _json["chapter_id"]
        _user_id = _json["user_id"]
        _base_offset = _json["base_offset"]
        _extent_offset = _json["extent_offset"]
        _tag_index = _json["tag_index"]
        _selection_type = _json["selection_type"]
        # validate the received values
        if request.method == 'POST':
            data = (_book_id, _chapter_id, _user_id, _base_offset, _extent_offset, _tag_index, _selection_type)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "delete from u736502961_hys.user_epub_select where book_id=%s and chapter_id=%s and user_id=%s and base_offset=%s and extent_offset=%s and tag_index=%s and selection_type=%s;",
                data)
            cursor.close()
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
            resp.headers.add("Access-Control-Allow-Origin", "*")
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


######################################################################web#####################################################
@app.route('/web_get_all_user_ids', methods=['GET'])
def web_get_all_user_ids():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.users;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_new_user', methods=['PUT'])
@cross_origin()
def web_add_user():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        # validate the received values
        if _id and request.method == 'PUT':
            # save edits
            sql = "INSERT INTO u736502961_hys.users(user_id) VALUES(%s)"
            data = _id
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_personal_data', methods=['POST'])
@cross_origin()
def web_add_user_personal_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _f_name = _json['first_name']
        _l_name = _json['last_name']
        _profile_pic = _json['profilepic']
        _email_id = _json['email_id']
        _mobile_no = _json['mobile_no']
        _gender = _json['gender']
        _dob = _json['user_dob']
        _address = _json['address']
        _street = _json['street']
        _city = _json['city']
        _state = _json['state']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_personal_details(user_id,first_name,last_name,profilepic,gender,user_dob," \
                  "address,street,city,state,email_id,mobile_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
            data = (
                _id, _f_name, _l_name, _profile_pic, _gender, _dob, _address, _street, _city, _state, _email_id,
                _mobile_no)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User personal data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_data/<string:id>', methods=['GET'])
def web_get_user_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.gender gender, pd.user_dob user_dob, pd.address address, pd.street street, pd.city city, pd.state state, pd.email_id email_id, pd.mobile_no mobile_no, sd.school_name school_name, sd.grade grade, sd.stream stream, sd.board board,sd.address school_address, sd.street school_street, sd.city school_city, sd.state school_state from u736502961_hys.user_personal_details pd inner join u736502961_hys.user_school_details sd on pd.user_id=sd.user_id where pd.user_id=%s;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_users_data_for_tagging', methods=['GET'])
def web_get_all_users_data_for_tagging():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.user_id user_id, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, sd.school_name school_name, sd.grade grade from u736502961_hys.user_personal_details pd inner join u736502961_hys.user_school_details sd on pd.user_id=sd.user_id;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_preferred_language_data', methods=['POST'])
@cross_origin()
def web_add_user_preferred_languages_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _preferred_lang = _json['preferred_lang']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_preferred_languages(user_id,preferred_lang) VALUES(%s,%s); "
            data = (_id, _preferred_lang)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User preferred languages added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_preferred_languages_data/<string:id>', methods=['GET'])
def web_get_user_preferred_languages_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select preferred_lang from u736502961_hys.user_preferred_languages where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_school_data', methods=['POST'])
@cross_origin()
def web_add_user_school_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _school_name = _json['school_name']
        _grade = _json['grade']
        _stream = _json['stream']
        _board = _json['board']
        _address = _json['address']
        _street = _json['street']
        _city = _json['city']
        _state = _json['state']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_school_details(user_id,school_name,grade,stream,board,address,street,city,state) VALUES(%s,%s,%s,%s," \
                  "%s,%s,%s,%s,%s); "
            data = (_id, _school_name, _grade, _stream, _board, _address, _street, _city, _state)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User school data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_strength_data', methods=['POST'])
@cross_origin()
def web_add_user_strength_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _grade = _json['grade']
        _subject = _json['subject']
        _topic = _json['topic']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_strength(user_id,grade,subject,topic) VALUES(%s,%s,%s,%s);"
            data = (_id, _grade, _subject, _topic)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User strength added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_strength_data/<string:id>', methods=['GET'])
def web_get_user_strength_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_strength where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_weakness_data', methods=['POST'])
@cross_origin()
def web_add_user_weakness_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _grade = _json['grade']
        _subject = _json['subject']
        _topic = _json['topic']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO u736502961_hys.user_weakness(user_id,grade,subject,topic) VALUES(%s,%s,%s,%s);"
            data = (_id, _grade, _subject, _topic)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User weakness data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_weakness_data/<string:id>', methods=['GET'])
def web_get_user_weakness_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_weakness where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Questions and answer details
@app.route('/web_add_user_question_details', methods=['POST'])
@cross_origin()
def web_add_user_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _answer_count = _json['answer_count']
        _answer_preference = _json['answer_preference']
        _audio_reference = _json['audio_reference']
        _call_date = _json['call_date']
        _call_end_time = _json['call_end_time']
        _call_now = _json['call_now']
        _call_preferred_lang = _json['call_preferred_lang']
        _call_start_time = _json['call_start_time']
        _answer_credit = _json['answer_credit']
        _question_credit = _json['question_credit']
        _view_count = _json['view_count']
        _examlikelyhood_count = _json['examlikelyhood_count']
        _grade = _json['grade']
        _like_count = _json['like_count']
        _note_reference = _json['note_reference']
        _ocr_image = _json['ocr_image']
        _compare_date = _json['compare_date']
        _question = _json['question']
        _question_type = _json['question_type']
        _is_identity_visible = _json['is_identity_visible']
        _subject = _json['subject']
        _topic = _json['topic']
        _text_reference = _json['text_reference']
        _toughness_count = _json['toughness_count']
        _video_reference = _json['video_reference']
        _impression_count = _json['impression_count']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _question_id, _user_id, _answer_count, _answer_preference, _audio_reference, _call_date, _call_end_time,
                _call_now, _call_preferred_lang, _call_start_time, _answer_credit, _question_credit, _view_count,
                _examlikelyhood_count, _grade, _like_count, _note_reference, _ocr_image, _compare_date, _question,
                _question_type, _is_identity_visible, _subject, _topic, _text_reference, _toughness_count,
                _video_reference,
                _impression_count)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_question_details(question_id, user_id, answer_count, answer_preference, audio_reference, call_date, call_end_time, call_now, call_preferred_lang, call_start_time, answer_credit, question_credit, view_count, examlikelyhood_count, grade, like_count,note_reference, ocr_image, compare_date, question, question_type, is_identity_visible, subject, topic, text_reference, toughness_count, video_reference, impression_count) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('User posted question successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_users_tagged_in_question', methods=['POST'])
@cross_origin()
def web_add_users_tagged_in_question():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.users_tagged_with_question(question_id, user_id) values (%s, %s);", data)
            conn.commit()
            resp = jsonify('Users tagged with question added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_questions_posted/<string:id>', methods=['GET'])
def web_get_user_questions_posted(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference,floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id where qd.user_id=%s order by qd.createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_questions_posted', methods=['GET'])
def web_get_all_question_posted():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference,floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id order by qd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_questions_like_details', methods=['POST'])
@cross_origin()
def web_add_questions_like_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _like_type = _json['like_type']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _like_type)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_like_details(question_id, user_id, like_type) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users like details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_questions_like_details', methods=['DELETE'])
@cross_origin()
def web_delete_questions_like_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from u736502961_hys.questions_like_details where question_id=%s and user_id=%s;",
                           data)
            conn.commit()
            resp = jsonify('Users like details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_questions_toughness_details', methods=['POST'])
@cross_origin()
def web_add_questions_toughness_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _toughness_level = _json['toughness_level']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _toughness_level)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_toughness_details(question_id, user_id, toughness_level) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users toughness details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_questions_toughness_details', methods=['DELETE'])
@cross_origin()
def web_delete_questions_toughness_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_toughness_details where question_id=%s and user_id=%s;", data)
            conn.commit()
            resp = jsonify('Users toughness details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_questions_examlikelyhood_details', methods=['POST'])
@cross_origin()
def web_add_questions_examlikelyhood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _examlikelyhood_level = _json['examlikelyhood_level']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _examlikelyhood_level)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_examlikelyhood_details(question_id, user_id, examlikelyhood_level) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users examlikelyhood details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_questions_examlikelyhood_details', methods=['DELETE'])
@cross_origin()
def web_delete_questions_examlikelyhood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_examlikelyhood_details where question_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Users examlikelyhood details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_counts_in_question_details', methods=['PUT'])
@cross_origin()
def web_update_counts_in_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _answer_count = _json["answer_count"]
        _like_count = _json["like_count"]
        _view_count = _json["view_count"]
        _examlikelyhood_count = _json["examlikelyhood_count"]
        _toughness_count = _json["toughness_count"]
        _impression_count = _json["impression_count"]
        # validate the received values
        if _user_id and request.method == 'PUT':
            data = (_answer_count, _view_count, _examlikelyhood_count, _like_count, _toughness_count, _impression_count,
                    _user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_question_details set answer_count=%s, view_count=%s, examlikelyhood_count=%s, like_count=%s, toughness_count=%s, impression_count=%s where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Answers
@app.route('/web_post_answer_on_question_details', methods=['POST'])
@cross_origin()
def web_post_answer_on_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json["user_id"]
        _comment_count = _json["comment_count"]
        _audio_reference = _json["audio_reference"]
        _like_count = _json["like_count"]
        _upvote_count = _json["upvote_count"]
        _downvote_count = _json["downvote_count"]
        _note_reference = _json["note_reference"]
        _image = _json["image"]
        _compare_date = _json["compare_date"]
        _answer = _json["answer"]
        _answer_type = _json["answer_type"]
        _text_reference = _json["text_reference"]
        _video_reference = _json["video_reference"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_answer_id, _question_id, _user_id, _comment_count, _audio_reference, _like_count, _upvote_count,
                    _downvote_count, _note_reference, _image, _compare_date, _answer, _answer_type, _text_reference,
                    _video_reference)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_answer_details(answer_id, question_id, user_id, comment_count, audio_reference, like_count, upvote_count, downvote_count, note_reference, image, compare_date, answer, answer_type, text_reference,video_reference) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users posted answer successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_users_tagged_in_answer', methods=['POST'])
@cross_origin()
def web_add_users_tagged_in_answer():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["answer_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into u736502961_hys.users_tagged_with_answer(answer_id, user_id) values (%s, %s);",
                           data)
            conn.commit()
            resp = jsonify('Users tagged with answer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_counts_in_answer_details', methods=['POST'])
@cross_origin()
def web_update_counts_in_answer_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _answer_id = _json["answer_id"]
        _user_id = _json['user_id']
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _upvote_count = _json["upvote_count"]
        _downvote_count = _json["downvote_count"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_comment_count, _like_count, _upvote_count, _downvote_count, _user_id, _answer_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_answer_details set comment_count=%s, like_count=%s, upvote_count=%s, downvote_count=%s where user_id=%s and answer_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_answer_posted', methods=['GET'])
def web_get_all_answer_posted():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name,pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id order by ad.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_answers_posted/<string:id>', methods=['GET'])
def web_get_user_answers_posted(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ad.answer_id, ad.question_id, ad.user_id, ad.comment_count, ad.audio_reference, ad.like_count, ad.upvote_count, ad.downvote_count, ad.note_reference, ad.image, ad.compare_date, ad.answer, ad.answer_type, ad.text_reference, ad.video_reference, qd.subject,qd.topic from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_question_details qd on ad.question_id=qd.question_id where ad.user_id=%s order by ad.createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_users_answer_comment', methods=['POST'])
@cross_origin()
def web_add_users_answer_comment():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _comment = _json["comment"]
        _comment_type = _json["comment_type"]
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        _note_reference = _json["note_reference"]
        _text_reference = _json["text_reference"]
        _video_reference = _json["video_reference"]
        _audio_reference = _json["audio_reference"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_comment_id, _answer_id, _question_id, _user_id, _comment, _comment_type, _like_count, _reply_count,
                    _audio_reference, _note_reference, _text_reference, _video_reference, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_answer_comment_details(comment_id,answer_id,question_id,user_id,comment,comment_type,like_count,reply_count,audio_reference,note_reference,text_reference,video_reference,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Comment on answer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_answer_comments', methods=['GET'])
def web_get_all_answer_comments():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select acd.comment_id comment_id, acd.answer_id answer_id, acd.question_id question_id, acd.user_id user_id, acd.comment comment, acd.comment_type comment_type, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, acd.like_count like_count, acd.reply_count reply_count, acd.audio_reference audio_reference, acd.note_reference note_reference, acd.text_reference text_reference, acd.video_reference video_reference, acd.compare_date compare_date from u736502961_hys.user_answer_comment_details acd inner join u736502961_hys.user_personal_details pd on acd.user_id = pd.user_id inner join u736502961_hys.user_school_details sd on acd.user_id = sd.user_id order by acd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_counts_in_answer_comment_details', methods=['POST'])
@cross_origin()
def web_update_counts_in_answer_comment_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _user_id = _json['user_id']
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_like_count, _reply_count, _user_id, _comment_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_answer_comment_details set like_count=%s, reply_count=%s where user_id=%s and comment_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_users_answer_reply', methods=['POST'])
@cross_origin()
def web_add_users_answer_reply():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _comment_id = _json["comment_id"]
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _reply = _json["reply"]
        _reply_type = _json["reply_type"]
        _like_count = _json["like_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _reply_id, _comment_id, _answer_id, _question_id, _user_id, _reply, _reply_type, _like_count,
                _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_answer_reply_details(reply_id, comment_id, answer_id, question_id, user_id, reply, reply_type, like_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('reply on comment added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_counts_in_answer_reply_details', methods=['POST'])
@cross_origin()
def web_update_counts_in_answer_reply_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _user_id = _json['user_id']
        _like_count = _json["like_count"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_like_count, _user_id, _reply_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_answer_reply_details set like_count=%s where user_id=%s and reply_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_answer_reply', methods=['GET'])
def web_get_all_answer_reply():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select rd.reply_id reply_id, rd.comment_id comment_id, rd.answer_id answer_id, rd.question_id question_id, rd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, rd.reply reply, rd.reply_type, rd.like_count like_count, rd.compare_date compare_date from u736502961_hys.user_answer_reply_details rd inner join u736502961_hys.user_personal_details pd on rd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on rd.user_id=sd.user_id order by rd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_post_details', methods=['POST'])
@cross_origin()
def web_add_sm_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json['user_id']
        _post_type = _json["post_type"]
        _comment = _json["comment"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_post_id, _user_id, _post_type, _comment, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_post_details(post_id, user_id, post_type, comment, compare_date) values(%s ,%s ,%s ,%s ,%s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_mood_details', methods=['POST'])
@cross_origin()
def web_add_sm_mood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json['user_id']
        _message = _json["message"]
        _user_mood = _json["user_mood"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_post_id, _user_id, _message, _user_mood, _imagelist_id, _videolist_id, _usertaglist_id, _privacy,
                    _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_mood_details(post_id, user_id, message, user_mood, imagelist_id, videolist_id, usertaglist_id, privacy, like_count, comment_count, view_count, impression_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_post_images', methods=['POST'])
@cross_origin()
def web_add_sm_post_images():
    conn = None
    cursor = None
    try:
        _json = request.json
        _imagelist_id = _json["imagelist_id"]
        _image = _json['image']
        # validate the received values
        if request.method == 'POST':
            data = (_imagelist_id, _image)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into u736502961_hys.sm_post_images(imagelist_id, image) values(%s ,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_post_videos', methods=['POST'])
@cross_origin()
def web_add_sm_post_videos():
    conn = None
    cursor = None
    try:
        _json = request.json
        _videolist_id = _json["videolist_id"]
        _video = _json['video']
        _thumbnail = _json['thumbnail']
        # validate the received values
        if request.method == 'POST':
            data = (_videolist_id, _video, _thumbnail)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.sm_post_videos(videolist_id, video, thumbnail) values(%s ,%s,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_post_users_tagged', methods=['POST'])
@cross_origin()
def web_add_sm_post_users_tagged():
    conn = None
    cursor = None
    try:
        _json = request.json
        _usertaglist_id = _json["usertaglist_id"]
        _user_id = _json['user_id']
        # validate the received values
        if request.method == 'POST':
            data = (_usertaglist_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into u736502961_hys.sm_post_users_tagged(usertaglist_id, user_id) values(%s ,%s);",
                           data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_posts', methods=['GET'])
def web_get_all_sm_post():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select postd.post_id post_id, postd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city,sd.school_name school_name, floor(sd.grade) grade,postd.post_type post_type,postd.comment comment, postd.compare_date compare_date from u736502961_hys.user_sm_post_details postd inner join u736502961_hys.user_personal_details pd on postd.user_id = pd.user_id inner join u736502961_hys.user_school_details sd on postd.user_id = sd.user_id order by postd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_images', methods=['GET'])
def web_get_all_sm_images():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select imagelist_id, image from u736502961_hys.sm_post_images;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_videos', methods=['GET'])
def web_get_all_sm_videos():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_usertagged', methods=['GET'])
def web_get_all_sm_usertagged():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select usertaglist_id, user_id from u736502961_hys.sm_post_users_tagged;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_mood_posts', methods=['GET'])
def web_get_all_sm_mood_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.gender gender, md.post_id post_id, md.user_id user_id, md.message message, md.user_mood user_mood, md.imagelist_id imagelist_id, md.usertaglist_id usertaglist_id, md.privacy privacy, md.like_count like_count, md.comment_count comment_count, md.view_count view_count, md.impression_count impression_count, md.compare_date compare_date, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, pd.gender gender, sd.school_name school_name, sd.grade grade from u736502961_hys.user_sm_mood_details md inner join u736502961_hys.user_personal_details pd on md.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on md.user_id=sd.user_id order by md.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_sm_comment_details', methods=['POST'])
@cross_origin()
def web_add_user_sm_comment_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _comment = _json["comment"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _comment_id, _post_id, _user_id, _comment, _imagelist_id, _videolist_id, _usertaglist_id, _like_count,
                _reply_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_comment_details(comment_id, post_id, user_id, comment, imagelist_id, videolist_id, usertaglist_id, like_count, reply_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_comment_posts', methods=['GET'])
def web_get_all_sm_comment_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.profilepic profilepic, cd.comment_id comment_id, cd.post_id post_id, cd.user_id user_id, cd.comment comment, cd.imagelist_id imagelist_id, cd.videolist_id videolist_id, cd.usertaglist_id usertaglist_id, cd.like_count like_count, cd.reply_count reply_count, cd.compare_date compare_date, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city, sd.school_name school_name, sd.grade grade from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id = cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id order by cd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_sm_reply_details', methods=['POST'])
@cross_origin()
def web_add_user_sm_reply_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _comment_id = _json["comment_id"]
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _reply = _json["reply"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _like_count = _json["like_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (_reply_id, _comment_id, _post_id, _user_id, _reply, _imagelist_id, _videolist_id, _usertaglist_id,
                    _like_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_reply_details(reply_id, comment_id, post_id, user_id, reply, imagelist_id, videolist_id, usertaglist_id, like_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_reply_posts', methods=['GET'])
def web_get_all_sm_reply_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.profilepic profilepic,rd.reply_id reply_id, rd.comment_id comment_id, rd.post_id post_id, rd.user_id user_id, rd.reply reply, rd.imagelist_id imagelist_id, rd.videolist_id videolist_id, rd.usertaglist_id usertaglist_id, rd.like_count like_count, rd.compare_date compare_date, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city, sd.school_name school_name, sd.grade grade from u736502961_hys.user_sm_reply_details rd inner join u736502961_hys.user_personal_details pd on pd.user_id = rd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = rd.user_id order by rd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_sm_cause_details', methods=['POST'])
@cross_origin()
def web_add_user_sm_cause_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _message = _json["message"]
        _datetime = _json["datetime"]
        _address = _json["address"]
        _date = _json["date"]
        _eventcategory = _json["eventcategory"]
        _eventname = _json["eventname"]
        _eventsubcategory = _json["eventsubcategory"]
        _eventtype = _json["eventtype"]
        _feedtype = _json["feedtype"]
        _frequency = _json["frequency"]
        _from_ = _json["from_"]
        _from24hrs = _json["from24hrs"]
        _fromtime = _json["fromtime"]
        _grade = _json["grade"]
        _latitude = _json["latitude"]
        _longitude = _json["longitude"]
        _meetingid = _json["meetingid"]
        _subject = _json["subject"]
        _theme = _json["theme"]
        _themeindex = _json["themeindex"]
        _to_ = _json["to_"]
        _to24hrs = _json["to24hrs"]
        _totime = _json["totime"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _message, _datetime, _address, _date, _eventcategory, _eventname, _eventsubcategory,
                _eventtype, _feedtype, _frequency, _from_, _from24hrs, _fromtime, _grade, _latitude, _longitude,
                _meetingid,
                _subject, _theme, _themeindex, _to_, _to24hrs, _totime, _imagelist_id, _videolist_id, _usertaglist_id,
                _privacy, _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_cause_details(post_id,user_id,message,datetime,address,date,eventcategory,eventname,eventsubcategory,eventtype,feedtype,frequency,from_,from24hrs,fromtime,grade,latitude,longitude,meetingid,subject,theme,themeindex ,to_ ,to24hrs,totime,imagelist_id ,videolist_id ,usertaglist_id ,privacy ,like_count ,comment_count ,view_count ,impression_count ,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_cause_posts', methods=['GET'])
def web_get_all_sm_cause_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select cd.post_id post_id,cd.user_id user_id,cd.message message,cd.datetime datetime,cd.address address,cd.date date,cd.eventcategory eventcategory,cd.eventname eventname,cd.eventsubcategory eventsubcategory,cd.eventtype eventtype,cd.feedtype feedtype,cd.frequency frequency,cd.from_ from_,cd.from24hrs from24hrs,cd.fromtime fromtime,cd.grade grade,cd.latitude latitude,cd.longitude longitude,cd.meetingid meetingid,cd.subject subject,cd.theme theme,cd.themeindex themeindex,cd.to_ to_,cd.to24hrs to24hrs,cd.totime totime,cd.imagelist_id imagelist_id,cd.videolist_id videolist_id,cd.usertaglist_id usertaglist_id,cd.privacy privacy,cd.like_count like_count,cd.comment_count comment_count,cd.view_count view_count,cd.impression_count impression_count,cd.compare_date compare_date,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, pd.gender gender, sd.school_name school_name,sd.grade grade from u736502961_hys.user_sm_cause_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=cd.user_id order by cd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_sm_bideas_details', methods=['POST'])
@cross_origin()
def web_add_user_sm_bideas_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _content = _json["content"]
        _theme = _json["theme"]
        _title = _json["title"]
        _identification = _json["identification"]
        _solution = _json["solution"]
        _target = _json["target"]
        _competitors = _json["competitors"]
        _swot = _json["swot"]
        _strategy = _json["strategy"]
        _funds = _json["funds"]
        _documentlist_id = _json["documentlist_id"]
        _videolist_id = _json["videolist_id"]
        _memberlist_id = _json["memberlist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _content, _theme, _title, _identification, _solution, _target, _competitors, _swot,
                _strategy, _funds, _documentlist_id, _videolist_id, _memberlist_id, _privacy, _like_count,
                _comment_count,
                _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_b_ideas_details(post_id, user_id, content, theme, title, identification, solution, target, competitors, swot, strategy, funds, documentlist_id, videolist_id, memberlist_id, privacy,like_count, comment_count, view_count, impression_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_bideas_posts', methods=['GET'])
def web_get_all_sm_bideas_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select bd.post_id post_id, bd.user_id user_id, bd.content content, bd.theme theme, bd.title title, bd.identification identification, bd.solution solution,bd.target target, bd.competitors competitors, bd.swot swot, bd.strategy strategy, bd.funds funds, bd.documentlist_id documentlist_id, bd.videolist_id videolist_id,bd.memberlist_id memberlist_id, bd.privacy privacy, bd.like_count like_count, bd.comment_count comment_count, bd.view_count view_count, bd.impression_count impression_count, bd.compare_date compare_date, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city city, sd.school_name school_name,sd.grade grade from u736502961_hys.user_sm_b_ideas_details bd inner join u736502961_hys.user_personal_details pd on bd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on bd.user_id = sd.user_id order by bd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_sm_project_details', methods=['POST'])
@cross_origin()
def web_add_user_sm_project_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _content = _json["content"]
        _theme = _json["theme"]
        _title = _json["title"]
        _grade = _json["grade"]
        _subject = _json["subject"]
        _topic = _json["topic"]
        _requirements = _json["requirements"]
        _purchasedfrom = _json["purchasedfrom"]
        _procedure = _json["procedure_"]
        _theory = _json["theory"]
        _findings = _json["findings"]
        _similartheory = _json["similartheory"]
        _memberlist_id = _json["memberlist_id"]
        _projectvideourl = _json["projectvideourl"]
        _reqvideourl = _json["reqvideourl"]
        _summarydoc = _json["summarydoc"]
        _otherdoc = _json["otherdoc"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _content, _theme, _title, _grade, _subject, _topic, _requirements, _purchasedfrom,
                _procedure, _theory, _findings, _similartheory, _memberlist_id, _projectvideourl, _reqvideourl,
                _summarydoc,
                _otherdoc, _privacy, _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_project_details (post_id,user_id,content,theme,title,grade,subject,topic,requirements,purchasedfrom,procedure_,theory,findings,similartheory,memberlist_id,projectvideourl,reqvideourl,summarydoc,otherdoc,privacy,like_count,comment_count,view_count,impression_count,compare_date)  values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_project_posts', methods=['GET'])
def web_get_all_sm_project_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_sm_project_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id order by prd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_sm_uploads_details', methods=['POST'])
@cross_origin()
def web_add_user_sm_uploads_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _upload_id = _json["upload_id"]
        _upload_type = _json["upload_type"]
        _user_id = _json["user_id"]
        _school_name = _json["school_name"]
        _exam_name = _json["exam_name"]
        _grade = _json["grade"]
        _subject = _json["subject"]
        _chapter = _json["chapter"]
        _topic = _json["topic"]
        _term = _json["term"]
        _year = _json["year"]
        _tags = _json["tags"]
        _description = _json["description"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _upload_id, _upload_type, _user_id, _school_name, _exam_name, _grade, _subject, _chapter, _topic, _term,
                _year, _tags, _description, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_uploads_details(upload_id, upload_type, user_id, school_name, exam_name, grade, subject, chapter, topic, term, year, tags, description, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_upload_file_details', methods=['POST'])
@cross_origin()
def web_add_sm_upload_file_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _upload_id = _json["upload_id"]
        _file_url = _json["file_url"]
        _file_ext = _json["file_ext"]
        _file_name = _json["file_name"]
        # validate the received values
        if request.method == 'POST':
            data = (_upload_id, _file_url, _file_ext, _file_name)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.sm_upload_files_details(upload_id, file_url, file_ext, file_name) values(%s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_uploads/<string:id>', methods=['GET'])
def web_get_user_uploads(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select upload_id, user_id, upload_type, school_name, exam_name, grade, subject, chapter, topic, term, year, tags, description, compare_date from u736502961_hys.user_sm_uploads_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_upload_files', methods=['GET'])
def web_get_user_upload_files():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select upload_id, file_url, file_name, file_ext,createdate from u736502961_hys.sm_upload_files_details order by createdate;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_achievement_details', methods=['POST'])
@cross_origin()
def web_add_user_achievement_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _achievement_id = _json["achievement_id"]
        _user_id = _json["user_id"]
        _scorecard_school_name = _json["scorecard_school_name"]
        _scorecard_board_name = _json["scorecard_board_name"]
        _ach_description = _json["ach_description"]
        _ach_image_url = _json["ach_image_url"]
        _ach_title = _json["ach_title"]
        _scorecard_grade = _json["scorecard_grade"]
        _scorecard_total_score = _json["scorecard_total_score"]
        _ach_type = _json["ach_type"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _achievement_id, _user_id, _scorecard_school_name, _scorecard_board_name, _ach_description,
                _ach_image_url,
                _ach_title, _scorecard_grade, _scorecard_total_score, _ach_type, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_achievement_details(achievement_id, user_id, scorecard_school_name, scorecard_board_name, ach_description, ach_image_url, ach_title, scorecard_grade, scorecard_total_score, ach_type, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_scorecard_details', methods=['POST'])
@cross_origin()
def web_add_user_scorecard_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _achievement_id = _json["achievement_id"]
        _user_id = _json["user_id"]
        _subject = _json["subject"]
        _marks = _json["marks"]
        # validate the received values
        if request.method == 'POST':
            data = (_achievement_id, _user_id, _subject, _marks)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_scorecard_details(achievement_id, user_id, subject, marks) values(%s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_user_privacy', methods=['POST'])
@cross_origin()
def web_add_user_privacy():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _comparedate = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _comparedate)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_privacy(user_id,address,ambition,dreamvacations,email,friends,mygroups,hobbies,library,mobileno,novels,placesvisited,schooladdress,scorecards,uploads,weakness,compare_date) values(%s,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,%s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_privacy/<string:id>', methods=['GET'])
def web_get_user_privacy(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, address, ambition, dreamvacations, email, friends, mygroups, hobbies, library, mobileno, novels, placesvisited, schooladdress, scorecards, uploads, weakness, compare_date from u736502961_hys.user_privacy where user_id=%s;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_user_privacy', methods=['POST'])
@cross_origin()
def web_update_user_privacy():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _address = _json["address"]
        _ambition = _json["ambition"]
        _dreamvacations = _json["dreamvacations"]
        _email = _json["email"]
        _friends = _json["friends"]
        _mygroups = _json["mygroups"]
        _hobbies = _json["hobbies"]
        _library = _json["library"]
        _mobileno = _json["mobileno"]
        _novels = _json["novels"]
        _placesvisited = _json["placesvisited"]
        _schooladdress = _json["schooladdress"]
        _scorecards = _json["scorecards"]
        _uploads = _json["uploads"]
        _weakness = _json["weakness"]
        # validate the received values
        if request.method == 'POST':
            data = (
            _address, _ambition, _dreamvacations, _email, _friends, _mygroups, _hobbies, _library, _mobileno, _novels,
            _placesvisited, _schooladdress, _scorecards, _uploads, _weakness, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_privacy set address = %s ,ambition = %s ,dreamvacations = %s ,email = %s ,friends = %s ,mygroups = %s ,hobbies = %s ,library = %s ,mobileno = %s ,novels = %s ,placesvisited = %s ,schooladdress = %s ,scorecards = %s ,uploads = %s ,weakness = %s where user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_achievement_details/<string:id>', methods=['GET'])
def web_get_user_achievement_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select achievement_id, user_id, scorecard_school_name, scorecard_board_name, ach_description, ach_image_url, ach_title, scorecard_grade, scorecard_total_score, ach_type, compare_date from u736502961_hys.user_achievement_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_user_scorecard_details/<string:id>', methods=['GET'])
def web_get_user_scorecard_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select achievement_id, user_id, subject,marks from u736502961_hys.user_scorecard_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_like_post_details', methods=['POST'])
@cross_origin()
def web_add_sm_like_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_type = _json["like_type"]

        # validate the received values
        if request.method == 'POST':
            data = (_post_id, _user_id, _like_type)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.sm_post_like_details(post_id, user_id, like_type) values(%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_sm_like_post_details', methods=['POST'])
@cross_origin()
def web_update_sm_like_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_type = _json["like_type"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_type, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.sm_post_like_details set like_type=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_sm_like_post_details', methods=['POST'])
@cross_origin()
def web_delete_sm_like_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_type = _json["like_type"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_type, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.sm_post_like_details where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_sm_like_post_details/<string:id>', methods=['GET'])
def web_get_sm_like_post_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, post_id,post_type, like_type from u736502961_hys.sm_post_like_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_sm_mood_post_count_details', methods=['POST'])
@cross_origin()
def web_update_sm_mood_post_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_mood_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_user_sm_cause_count_details', methods=['POST'])
@cross_origin()
def web_update_user_sm_cause_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_cause_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_user_sm_b_ideas_count_details', methods=['POST'])
@cross_origin()
def web_update_user_sm_b_ideas_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_b_ideas_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_user_sm_project_count_details', methods=['POST'])
@cross_origin()
def web_update_user_sm_project_count_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _post_id = _json["post_id"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]

        # validate the received values
        if request.method == 'POST':
            data = (_like_count, _comment_count, _view_count, _impression_count, _post_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.user_sm_project_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s and user_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_blog_post_details', methods=['POST'])
@cross_origin()
def web_add_sm_blog_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _blogger_name = _json["blogger_name"]
        _blog_title = _json["blog_title"]
        _blog_intro = _json['blog_intro']
        _blog_content = _json["blog_content"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _post_id, _user_id, _blogger_name, _blog_title, _blog_intro, _blog_content, _like_count, _comment_count,
                _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_blog_details(post_id, user_id, blogger_name, blog_title,blog_intro,blog_content,like_count,comment_count, view_count,impression_count,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_blog_category_details', methods=['POST'])
@cross_origin()
def web_add_sm_blog_category_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _blog_category = _json["blog_category"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _blog_category, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.user_sm_blog_category_details(post_id, blog_category,compare_date) values(%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_sm_blog_posts', methods=['GET'])
def web_get_all_sm_blog_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.user_sm_blog_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id order by prd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_sm_reaction_details', methods=['POST'])
@cross_origin()
def web_add_sm_reaction_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _do_post = _json["do_post"]

        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _post_type = _json["post_type"]
        _like_type = _json["like_type"]

        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _reply_count = _json["reply_count"]

        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()

            if _do_post == 'TRUE':
                data = (_post_id, _user_id, _post_type, _like_type)
                cursor.execute(
                    "insert into u736502961_hys.sm_post_like_details(post_id, user_id, post_type, like_type) values(%s, %s, %s, %s);",
                    data)
            else:
                data = (_post_id, _user_id)
                cursor.execute("delete from u736502961_hys.sm_post_like_details where post_id=%s and user_id=%s;", data)

            if _post_type == 'Mood':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_mood_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'blog':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_blog_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'cause|teachunprevilagedKids':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_cause_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'projectdiscuss':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_project_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'businessideas':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_b_ideas_details like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;",
                    data)
            elif _post_type == 'comment':
                data = (_like_count, _reply_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_comment_details set like_count=%s, reply_count=%s where comment_id=%s;",
                    data)
            elif _post_type == 'reply':
                data = (_like_count, _post_id)
                cursor.execute(
                    "update u736502961_hys.user_sm_reply_details set like_count=%s where reply_id=%s;",
                    data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_question_saved_details', methods=['POST'])
@cross_origin()
def web_add_question_saved_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]
        _compare_date = _json["compare_date"]

        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _question_id, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_saved_details(user_id, question_id, compare_date) values(%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_question_saved_details', methods=['POST'])
@cross_origin()
def web_delete_question_saved_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]
        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_saved_details where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_question_saved_details/<string:id>', methods=['GET'])
def web_get_question_saved_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, question_id, compare_date from u736502961_hys.questions_saved_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_question_bookmarked_details', methods=['POST'])
@cross_origin()
def web_add_question_bookmarked_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]
        _compare_date = _json["compare_date"]

        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _question_id, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into u736502961_hys.questions_bookmarked_details(user_id, question_id, compare_date) values(%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_add_notification_details', methods=['POST'])
@cross_origin()
def web_add_notification_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _notify_id = _json["notify_id"]
        _notify_type = _json["notify_type"]
        _section = _json["section"]
        _sender_id = _json["sender_id"]
        _receiver_id = _json["receiver_id"]
        _token = _json["token"]
        _title = _json["title"]
        _message = _json["message"]
        _post_id = _json["post_id"]
        _post_type = _json["post_type"]
        _is_clicked = _json["is_clicked"]
        _compare_date = _json["compare_date"]
        _addordelete = _json["addordelete"]

        # validate the received values
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data1 = (_notify_type, _section, _sender_id, _post_id)
            cursor.execute(
                "select * from u736502961_hys.notification_details where notify_type=%s and section=%s and sender_id=%s and post_id=%s;",
                data1)
            row = cursor.fetchall()
            print(row)
            cursor.close()
            if row.__gt__(0):
                if _addordelete == "delete":
                    cursor = conn.cursor()
                    data2 = (_notify_type, _section, _sender_id, _post_id)
                    cursor.execute(
                        "delete from u736502961_hys.notification_details where notify_type=%s and section=%s and sender_id=%s and post_id=%s;",
                        data2)
                    print("delete")
                    conn.commit()
                    resp = jsonify('data added successfully!')
                    resp.status_code = 200
                    return resp
                else:
                    cursor = conn.cursor()
                    data2 = (_notify_type, _section, _sender_id, _post_id)
                    cursor.execute(
                        "delete from u736502961_hys.notification_details where notify_type=%s and section=%s and sender_id=%s and post_id=%s;",
                        data2)
                    print("delete")
                    data = (
                        _notify_id, _notify_type, _section, _sender_id, _receiver_id, _token, _title, _message,
                        _post_id,
                        _post_type, _is_clicked, _compare_date)
                    cursor.execute(
                        "insert into u736502961_hys.notification_details(notify_id, notify_type, section, sender_id, receiver_id, token, title, message, post_id, post_type, is_clicked, compare_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                        data)
                    print("inserted")
                    conn.commit()
                    resp = jsonify('data added successfully!')
                    resp.status_code = 200
                    return resp
            else:
                cursor = conn.cursor()
                data = (
                    _notify_id, _notify_type, _section, _sender_id, _receiver_id, _token, _title, _message, _post_id,
                    _post_type, _is_clicked, _compare_date)
                cursor.execute(
                    "insert into u736502961_hys.notification_details(notify_id, notify_type, section, sender_id, receiver_id, token, title, message, post_id, post_type, is_clicked, compare_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    data)
                print("inserted only")
                conn.commit()
                resp = jsonify('data added successfully!')
                resp.status_code = 200
                return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_question_bookmarked_details', methods=['POST'])
@cross_origin()
def web_delete_question_bookmarked_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _user_id = _json["user_id"]
        _question_id = _json["question_id"]

        # validate the received values
        if request.method == 'POST':
            data = (_user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.questions_bookmarked_details where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_question_bookmarked_details/<string:id>', methods=['GET'])
def web_get_question_bookmarked_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select user_id, question_id, compare_date from u736502961_hys.questions_bookmarked_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_get_all_notifications/<string:id>', methods=['GET'])
def web_get_all_notifications(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u736502961_hys.notification_details nd inner join u736502961_hys.user_personal_details pd on nd.sender_id=pd.user_id   where nd.receiver_id = %s order by nd.createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_update_notification_details', methods=['POST'])
@cross_origin()
def web_update_notification_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _notify_id = _json["notify_id"]

        # validate the received values
        if request.method == 'POST':
            data = (_notify_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update u736502961_hys.notification_details set is_clicked='true' where notify_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/web_delete_notification_details', methods=['POST'])
@cross_origin()
def web_delete_notification_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _notify_id = _json["notify_id"]

        # validate the received values
        if request.method == 'POST':
            data = (_notify_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u736502961_hys.notification_details where notify_id=%s;",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(debug=True)
