from flask import Flask,render_template
from flask import request
import flask

import json
app = Flask(__name__)



@app.route("/test_query",methods=['POST'])
def test_query():
    data=request.get_json()
    template_result=dict()
    template_result['code']='185-3I'
    tmp_factor=dict()
    tmp_factor['酒精呼氣濃度']="0.25mg/l-0.54mg/l"
    tmp_factor['交通工具種類'] = 'UNK'
    tmp_factor['行駛及被查獲地點'] = '鄉、鎮、村道路'
    crime_appro=dict()
    crime_appro['車內有搭載其他乘客'] = True
    crime_appro['有酒駕以外，足以影響交通安全之其他違反道路交通安全規則之情事（例如：逆向行駛、嚴重超速、闖紅燈、無照駕駛）'] = True
    tmp_factor['犯罪手段'] = crime_appro
    crime_damage = dict()
    crime_damage['發生事故']= True
    crime_damage['造成他人普通傷害，而未經追訴過失傷害罪'] = '1人'
    crime_damage['造成他人財產損害'] = False
    perpetrator_status=dict()
    perpetrator_status['以駕駛車輛為職業'] = False
    perpetrator_conduct = dict()
    perpetrator_conduct['不構成累犯之不能安全駕駛前案紀錄（包括飲用酒精、服用毒品、麻醉藥品或其他相類之物）'] = '無'
    tmp_factor['犯罪行為人之生活狀況'] = perpetrator_status
    tmp_factor['犯罪所生之危險或損害'] = crime_damage
    tmp_factor['犯罪行為人之品行'] = perpetrator_conduct
    perpetrator_attitude =dict()
    tmp_factor['犯罪後之態度'] = perpetrator_attitude
    perpetrator_attitude['警詢、偵查即已坦承且始終一致'] = False
    perpetrator_attitude['和解'] = '未和解'
    perpetrator_attitude['肇事後造成他人普通傷害，在現場報請送醫'] = False
    template_result['factor'] = tmp_factor
    resp = flask.Response(json.dumps([template_result],ensure_ascii=False))
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000)
