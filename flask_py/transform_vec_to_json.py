import flask
import json
def basic_template():
    template_result = dict()
    template_result['code'] = '185-3I'
    tmp_factor = dict()
    tmp_factor['酒精呼氣濃度'] = "0.24mg/l以下"
    tmp_factor['交通工具種類'] = 'UNK'
    tmp_factor['行駛及被查獲地點'] = '直轄市、縣市道路'
    crime_appro = dict()
    crime_appro['車內有搭載其他乘客'] = False
    crime_appro['有酒駕以外，足以影響交通安全之其他違反道路交通安全規則之情事（例如：逆向行駛、嚴重超速、闖紅燈、無照駕駛）'] = False
    tmp_factor['犯罪手段'] = crime_appro
    crime_damage = dict()
    crime_damage['發生事故'] = False
    crime_damage['造成他人普通傷害，而未經追訴過失傷害罪'] = '無'
    crime_damage['造成他人財產損害'] = False
    perpetrator_status = dict()
    perpetrator_status['以駕駛車輛為職業'] = False
    perpetrator_conduct = dict()
    perpetrator_conduct['不構成累犯之不能安全駕駛前案紀錄（包括飲用酒精、服用毒品、麻醉藥品或其他相類之物）'] = '無'
    tmp_factor['犯罪行為人之生活狀況'] = perpetrator_status
    tmp_factor['犯罪所生之危險或損害'] = crime_damage
    tmp_factor['犯罪行為人之品行'] = perpetrator_conduct
    perpetrator_attitude = dict()
    tmp_factor['犯罪後之態度'] = perpetrator_attitude
    perpetrator_attitude['警詢、偵查即已坦承且始終一致'] = False
    perpetrator_attitude['和解'] = '未和解'
    perpetrator_attitude['肇事後造成他人普通傷害，在現場報請送醫'] = False
    template_result['factor'] = tmp_factor
    return template_result

def produce_template(vec_result):

    template_result = dict()
    template_result['code'] = '185-3I'
    tmp_factor = dict()
    tmp_factor['酒精呼氣濃度'] = "0.24mg/l以下"
    tmp_factor['交通工具種類'] = 'UNK'
    tmp_factor['行駛及被查獲地點'] = '直轄市、縣市道路'
    crime_appro = dict()
    crime_appro['車內有搭載其他乘客'] = False
    crime_appro['有酒駕以外，足以影響交通安全之其他違反道路交通安全規則之情事（例如：逆向行駛、嚴重超速、闖紅燈、無照駕駛）'] = False
    tmp_factor['犯罪手段'] = crime_appro
    crime_damage = dict()
    crime_damage['發生事故'] = False
    crime_damage['造成他人普通傷害，而未經追訴過失傷害罪'] = '無'
    crime_damage['造成他人財產損害'] = False
    perpetrator_status = dict()
    perpetrator_status['以駕駛車輛為職業'] = False
    perpetrator_conduct = dict()
    perpetrator_conduct['不構成累犯之不能安全駕駛前案紀錄（包括飲用酒精、服用毒品、麻醉藥品或其他相類之物）'] = '無'
    tmp_factor['犯罪行為人之生活狀況'] = perpetrator_status
    tmp_factor['犯罪所生之危險或損害'] = crime_damage
    tmp_factor['犯罪行為人之品行'] = perpetrator_conduct
    perpetrator_attitude = dict()
    tmp_factor['犯罪後之態度'] = perpetrator_attitude
    perpetrator_attitude['警詢、偵查即已坦承且始終一致'] = True
    perpetrator_attitude['和解'] = '未和解'
    perpetrator_attitude['肇事後造成他人普通傷害，在現場報請送醫'] = False
    template_result['factor'] = tmp_factor
    if vec_result[0] == 1:
        tmp_factor['酒精呼氣濃度']='0.24mg/l以下'
    if vec_result[1] == 1:
        tmp_factor['酒精呼氣濃度'] = '0.25mg/l-0.54mg/l'
    if vec_result[2] == 1:
        tmp_factor['酒精呼氣濃度'] = '0.55mg/l-0.74mg/l'
    if vec_result[3] == 1:
        tmp_factor['酒精呼氣濃度'] = '0.75mg/l-0.99mg/l'
    if vec_result[4] == 1:
        tmp_factor['酒精呼氣濃度'] = '1.00mg/l-1.49mg/l'
    if vec_result[5] == 1:
        tmp_factor['酒精呼氣濃度'] = '1.50mg/l-1.99mg/l'
    if vec_result[6] == 1:
        tmp_factor['酒精呼氣濃度'] = '2.00mg/l以上'
    if vec_result[7] == 1:
        tmp_factor['交通工具種類'] = '機車'
    if vec_result[8] == 1:
        tmp_factor['交通工具種類'] = '小客貨車'
    if vec_result[9] == 1:
        tmp_factor['交通工具種類'] = '大型車'
    if vec_result[10] == 1:
        tmp_factor['行駛及被查獲地點'] = '直轄市、縣市道路'
    if vec_result[11] == 1:
        tmp_factor['行駛及被查獲地點'] = '快速公路、高速公路'
    if vec_result[12] == 1:
        tmp_factor['行駛及被查獲地點'] = '鄉、鎮、村道路'
    if vec_result[13] == 1:
        tmp_factor['行駛及被查獲地點'] = '校園、鬧區、廣場等人車繁忙時之周邊道路及人行道'
    if vec_result[14] == 1:
        crime_damage['發生事故'] = True
    if vec_result[15] == 1:
        crime_damage['造成他人財產損害'] = True
    if vec_result[16] == 1:
        perpetrator_status['以駕駛車輛為職業'] = True
    if vec_result[17] == 1:
        perpetrator_attitude['警詢、偵查即已坦承且始終一致'] = False
    return template_result
