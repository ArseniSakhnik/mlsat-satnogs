from typing import Annotated
from fastapi import Depends
from modules.mongodb.mongodb import MongodbContext
from modules.satnogs_api.dtos.basic_decoder import BasicDecoder, NoradInfo
from satnogsdecoders.decoder import Grbalpha
import os

satnogs_basic_decoders = "basic_decoders"
satnogs_raw_data = "raw_data"


class SatnogsApiService:
    def __init__(self, mongodb: Annotated[MongodbContext, Depends(MongodbContext)]):
        self.mongodb = mongodb
        self.api_token = os.getenv("SATNOGS_API_TOKEN")

    def initialize_basic_decoders(self):
        db = self.mongodb.get_db()

        if satnogs_basic_decoders in db.list_collection_names():
            return

        collection = db.get_collection(satnogs_basic_decoders)

        basic_decoders: Annotated[BasicDecoder] = [
            BasicDecoder("Grizu263a", "TZQT-5140-2201-6886-0585", 51025),
            BasicDecoder("aausat4", "AISX-1350-2546-0237-2310", 41460),
            BasicDecoder("acrux1", "DYYY-0442-0736-6026-2557", 44369),
            BasicDecoder("alsat1n", "UPOC-3374-7750-1640-6748", 41789),
            BasicDecoder("amicalsat", "BHEP-0319-3345-0774-6350", 46287),
            BasicDecoder("armadillo", "RHUX-5355-9162-3098-2723", 44352),
            # BasicDecoder("ascii85test")
            BasicDecoder("asuphoenix", "BZQX-4787-4409-1766-6854", 45258),
            # BasicDecoder("ax25frames"),
            # BasicDecoder("ax25monitor")
            BasicDecoder("azaadisat2", "EKAM-8316-2757-5928-1987", 55563),
            # BasicDecoder("b85decode"),
            BasicDecoder("bdsat", "PPRG-8689-8762-8343-4648", 52175),
            BasicDecoder("bdsat2", "NJFB-9884-9643-7739-4519", 55098),
            BasicDecoder("beesat", "XFUT-4878-1223-5887-3249", 35933),
            BasicDecoder("beesat2", "UTXU-4881-3195-9394-3367", 39136),
            BasicDecoder("bisonsat", "IGGV-1318-5974-9239-7350", 40968),
            BasicDecoder("bobcat1", "RNBQ-9045-6623-3650-8949", 46922),
            BasicDecoder("bugsat1", "GPLA-1467-3987-8284-6460", 40014),
            BasicDecoder("cape1", "CICP-0434-9716-2826-6897", 31130),
            # BasicDecoder("cas4"),
            BasicDecoder("cas5a", "THLP-9709-3501-8618-5195", 54684),
            BasicDecoder("cas9", "WMPC-3806-8308-1122-5138", 50466),
            BasicDecoder("catsat", "EIOW-0233-5270-5407-2865", 99164),
            BasicDecoder("celesta", "XKZZ-2829-5729-9508-2566", 53111),
            BasicDecoder("chomptt", "GYLI-0056-5213-2621-8146", 43855),
            BasicDecoder("cirbe", "PBLF-9792-3382-3546-2243", 56188),
            BasicDecoder("connectat11", "RLGA-3050-8635-4193-2562", 52739),
            BasicDecoder("csim", "CKMD-9513-1025-4842-0352", 43793),
            # BasicDecoder("cspheader"),
            BasicDecoder("ctim", "CSGC-5605-1718-3109-5402", 52950),
            BasicDecoder("cubebel1", "WMQB-0532-9164-6364-5821", 43666),
            BasicDecoder("cubebel2", "PIHV-8715-3112-5892-6258", 57175),
            BasicDecoder("cubesatsim", "HNBU-8319-2760-4279-6218", 99999),
            BasicDecoder("cute", "YMFQ-1347-4330-8510-2436", 49263),
            BasicDecoder("delfin3xt", "LDFA-5547-3453-6167-7352", 39428),
            BasicDecoder("delfipq", "CEIC-4073-2863-5971-9670", 51074),
            BasicDecoder("dhabisat", "UYPX-3709-1953-9939-4507", 49016),
            BasicDecoder("diy1", "UVHJ-3379-3188-8525-8707", 47963),
            BasicDecoder("duchifat3", "YXQQ-6207-4287-8188-9048", 44854),
            # BasicDecoder("elfin"),
            # BasicDecoder("elfin_pp"),
            BasicDecoder("entrysat", "XJEY-1734-2475-9790-3893", 44429),
            BasicDecoder("equisat", "SABJ-3457-7659-3993-3753", 43552),
            # BasicDecoder("eshail2"),
            BasicDecoder("estcube2", "HMYH-8624-2864-5575-0545", 99045),
            # BasicDecoder("foresail1", "CIOM-1903-7117-1067-8603", NoradInfo(99399, 52766)),
            # BasicDecoder("fox"),
            BasicDecoder("gaspacs", "NYPQ-6177-1118-6247-2663", 51439),
            BasicDecoder("geoscanedelveis", "QNCD-8954-6090-5430-2718", 53385),
            BasicDecoder("grbalpha", "HFFD-8697-8440-3101-3937", 47959),
            BasicDecoder("greencube", "KGEF-8685-2681-9687-2264", 53106),
            BasicDecoder("gt1", "ABTD-1506-2343-8499-5530", 51510),
            BasicDecoder("inspiresat1", "KAEG-9794-2542-4829-8548", 51657),
            BasicDecoder("irazu", "QHGB-5011-7406-7134-6581", 43468),
            # BasicDecoder("irvine"),
            # BasicDecoder("iss"),
            BasicDecoder("ksu", "GJTN-2368-5876-8326-4725", 47954),
            BasicDecoder("ledsat", "JLZT-0277-4784-7719-1707", 49069),
            BasicDecoder("lightsail2", "NEYM-8143-9281-1364-3886", 44420),
            BasicDecoder("meznsat", "HXPT-8292-6749-4283-2496", 46489),
            BasicDecoder("minxss", "GUIW-3026-5024-1966-8107", 41474),
            # BasicDecoder("mirsat1"),
            BasicDecoder("mitee1", "WMCD-5300-1478-1818-8347", 47314),
            # BasicDecoder("mxl"),
            # BasicDecoder("mysat"),
            # TODO добавить другие netsat'ы
            BasicDecoder("netsat", "OZSW-9908-0796-8166-3293", 46506),
            # TODO тут я закончил
            # BasicDecoder("neudose"),
            # BasicDecoder("neutron1"),
            # BasicDecoder("nutsat1"),
            # BasicDecoder("opssat1"),
            # BasicDecoder("oresat0"),
            # BasicDecoder("origamisat1"),
            # BasicDecoder("painani"),
            # BasicDecoder("picsat"),
            # BasicDecoder("planetum1"),
            # BasicDecoder("polyitan"),
            # BasicDecoder("pwsat2"),
            # BasicDecoder("qarman"),
            # BasicDecoder("qbee"),
            # BasicDecoder("qubik"),
            # BasicDecoder("quetzal1"),
            # BasicDecoder("ramsat"),
            # BasicDecoder("rhoksat"),
            # BasicDecoder("roseycubesat1"),
            # BasicDecoder("salsat"),
            # BasicDecoder("sanosat1"),
            # BasicDecoder("selfiesat"),
            # BasicDecoder("sharjahsat1"),
            # BasicDecoder("siriussat"),
            # BasicDecoder("skcube"),
            # BasicDecoder("snet"),
            # BasicDecoder("spoc"),
            # BasicDecoder("strand"),
            # BasicDecoder("stratosattk1"),
            # BasicDecoder("suchai2"),
            # BasicDecoder("targit"),
            # BasicDecoder("us6"),
            # BasicDecoder("uwe4"),
            # BasicDecoder("veronika"),
            # BasicDecoder("vzlusat2"),
        ]

        basic_decoders_dict = list(map(lambda x: x.__dict__, basic_decoders))

        collection.insert_many(basic_decoders_dict)

    def initialize_raw_data(self):
        db = self.mongodb.get_db()

        if satnogs_raw_data in db.list_collection_names():
            return

        if satnogs_basic_decoders not in db.list_collection_names():
            self.initialize_basic_decoders()

        cursor = db.basic_decoders.find({}, {'_id': 0})

        basic_decoders = []

        for document in cursor:
            basic_decoders.append(document)

