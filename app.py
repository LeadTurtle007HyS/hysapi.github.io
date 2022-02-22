import pymysql
from flask import Flask, jsonify
from flask import request
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin

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
            return not_found()
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
            cursor.execute("insert into u736502961_hys.users_tagged_with_question(question_id, user_id) values (%s, %s);", data)
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
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference, floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name ,ld.like_type, ed.examlikelyhood_level, td.toughness_level, sa.user_id is_save, ba.user_id is_bookmark from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id left join u736502961_hys.questions_like_details ld on qd.question_id=ld.question_id and ld.user_id=%s left join u736502961_hys.questions_examlikelyhood_details ed on qd.question_id=ed.question_id and ed.user_id=%s left join u736502961_hys.questions_toughness_details td on qd.question_id=td.question_id and td.user_id=%s left join u736502961_hys.questions_saved_details sa on qd.question_id=sa.question_id and sa.user_id=%s left join u736502961_hys.questions_bookmarked_details ba on qd.question_id=ba.question_id and ba.user_id=%s where qd.user_id=%s order by qd.compare_date desc;", data)

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
def get_question_posted(id,userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, userid, userid, userid, userid, id)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference, floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name ,ld.like_type, ed.examlikelyhood_level, td.toughness_level, sa.user_id is_save, ba.user_id is_bookmark from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id left join u736502961_hys.questions_like_details ld on qd.question_id=ld.question_id and ld.user_id=%s left join u736502961_hys.questions_examlikelyhood_details ed on qd.question_id=ed.question_id and ed.user_id=%s left join u736502961_hys.questions_toughness_details td on qd.question_id=td.question_id and td.user_id=%s left join u736502961_hys.questions_saved_details sa on qd.question_id=sa.question_id and sa.user_id=%s left join u736502961_hys.questions_bookmarked_details ba on qd.question_id=ba.question_id and ba.user_id=%s where qd.question_id=%s order by qd.compare_date desc;", data)
        row = cursor.fetchall()
        data = (row[0]["question_id"], userid)
        data = (userid, userid, row[0]["question_id"])
        cursor.execute(
           " select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade, case when ld.like_type is null then '' else ld.like_type end as like_type, case when vd.vote_type is null then '' else vd.vote_type end as vote_type from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id left join u736502961_hys.answers_like_details ld on ld.answer_id = ad.answer_id and ld.user_id=%s left join u736502961_hys.answers_vote_details vd on vd.answer_id = ad.answer_id and vd.user_id=%s where ad.question_id=%s order by ad.compare_date desc;", data)
        answerList = cursor.fetchall()
        for i in range(len(answerList)):
            data = (userid, answerList[i]["answer_id"])
            cursor.execute("select cd.*, pd.*, sd.*, case when cld.like_type is null then '' else cld.like_type end like_type from u736502961_hys.user_answer_comment_details cd inner join u736502961_hys.user_personal_details pd on cd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id left join u736502961_hys.answers_comment_like_details cld on cd.comment_id = cld.comment_id and cld.user_id=%s  where cd.answer_id=%s order by cd.compare_date desc;", data)
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
        cursor.execute("select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference, floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name ,ld.like_type, ed.examlikelyhood_level, td.toughness_level, sa.user_id is_save, ba.user_id is_bookmark from u736502961_hys.user_question_details as qd inner join u736502961_hys.user_personal_details pd on qd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on qd.user_id=sd.user_id left join u736502961_hys.questions_like_details ld on qd.question_id=ld.question_id and ld.user_id=%s left join u736502961_hys.questions_examlikelyhood_details ed on qd.question_id=ed.question_id and ed.user_id=%s left join u736502961_hys.questions_toughness_details td on qd.question_id=td.question_id and td.user_id=%s left join u736502961_hys.questions_saved_details sa on qd.question_id=sa.question_id and sa.user_id=%s left join u736502961_hys.questions_bookmarked_details ba on qd.question_id=ba.question_id and ba.user_id=%s order by qd.compare_date desc;", data)
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
                "insert into u736502961_hys.questions_like_details(question_id, user_id, like_type) values (%s, %s, %s);", data)
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
            cursor.execute("delete from u736502961_hys.questions_like_details where question_id=%s and user_id=%s;", data)
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
            cursor.execute("delete from u736502961_hys.questions_toughness_details where question_id=%s and user_id=%s;", data)
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
            cursor.execute("delete from u736502961_hys.questions_examlikelyhood_details where question_id=%s and user_id=%s;",
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
            cursor.execute("insert into u736502961_hys.users_tagged_with_answer(answer_id, user_id) values (%s, %s);", data)
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
def get_answer_posted(ansid,userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, userid, ansid)
        cursor.execute(
           " select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade, case when ld.like_type is null then '' else ld.like_type end as like_type, case when vd.vote_type is null then '' else vd.vote_type end as vote_type from u736502961_hys.user_answer_details ad inner join u736502961_hys.user_personal_details pd on ad.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on ad.user_id=sd.user_id left join u736502961_hys.answers_like_details ld on ld.answer_id = ad.answer_id and ld.user_id=%s left join u736502961_hys.answers_vote_details vd on vd.answer_id = ad.answer_id and vd.user_id=%s where ad.answer_id=%s order by ad.compare_date desc;", data)
        answerList = cursor.fetchall()
        data = (userid, ansid)
        cursor.execute(
            "select cd.*, pd.*, sd.*, case when cld.like_type is null then '' else cld.like_type end like_type from u736502961_hys.user_answer_comment_details cd inner join u736502961_hys.user_personal_details pd on cd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = cd.user_id left join u736502961_hys.answers_comment_like_details cld on cd.comment_id = cld.comment_id and cld.user_id=%s where cd.answer_id=%s order by cd.compare_date desc;",
            data)
        commentlist = cursor.fetchall()
        for i in range(len(commentlist)):
            data = (userid, commentlist[i]['comment_id'])
            cursor.execute(
                "select rd.*, pd.*, sd.*, case when rld.like_type is null then '' else rld.like_type end like_type from u736502961_hys.user_answer_reply_details rd left join u736502961_hys.answers_reply_like_details rld on rld.reply_id=rd.reply_id and rld.user_id = %s inner join u736502961_hys.user_personal_details pd on rd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on rd.user_id=sd.user_id where rd.comment_id=%s order by rd.compare_date desc;", data)
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
                        "select view_count from u736502961_hys.user_question_details  where question_id=%s;",_post_id)
                    viewcount = cursor.fetchall()
                    updatecount = viewcount[0]['view_count'] + 1
                    data = (updatecount, _post_id)
                    cursor.execute(
                        "update u736502961_hys.user_question_details set view_count =%s where question_id=%s;",data)
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
            elif row[0]['like_type']=='like':
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
            data = (_post_id, _user_id, _post_type,_comment, _compare_date)
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
            cursor.execute("insert into u736502961_hys.sm_post_videos(videolist_id, video, thumbnail) values(%s ,%s,%s);", data)
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
            cursor.execute("insert into u736502961_hys.sm_post_users_tagged(usertaglist_id, user_id) values(%s ,%s);", data)
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
            "select pd.*, md.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_mood_details md inner join u736502961_hys.user_personal_details pd on md.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on md.user_id=sd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = md.post_id and ld.user_id=%s order by md.compare_date desc;", userid)
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
def get_sm_mood_posts(postid,userid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (userid, postid)
        cursor.execute(
            "select pd.*, md.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_mood_details md inner join u736502961_hys.user_personal_details pd on md.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on md.user_id=sd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = md.post_id and ld.user_id=%s where md.post_id=%s order by md.compare_date desc;", data)
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
            cursor.execute(
                "select * from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id where post_id=%s;",
                row[0]['post_id'])
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
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
            "select cd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_cause_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=cd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = cd.post_id and ld.user_id=%s order by cd.compare_date desc;",userid)
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
            "select cd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_cause_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=cd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = cd.post_id and ld.user_id=%s where cd.post_id=%s order by cd.compare_date desc;",data)
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
            cursor.execute(
                "select * from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id where post_id=%s;",
                row[0]['post_id'])
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
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
        cursor.execute("select bd.*, pd.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_b_ideas_details bd inner join u736502961_hys.user_personal_details pd on bd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on bd.user_id = sd.user_id  left join u736502961_hys.sm_post_like_details ld on ld.post_id = bd.post_id and ld.user_id=%s order by bd.compare_date desc;",userid)
        row = cursor.fetchall()
        for i in range(len(row)):
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where tag.usertaglist_id = %s",
                row[i]['memberlist_id'])
            row[i]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select * from u736502961_hys.sm_upload_files_details where upload_id=%s",row[i]['documentlist_id'])
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
        cursor.execute("select bd.*, pd.*, sd.*,case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_b_ideas_details bd inner join u736502961_hys.user_personal_details pd on bd.user_id=pd.user_id inner join u736502961_hys.user_school_details sd on bd.user_id = sd.user_id  left join u736502961_hys.sm_post_like_details ld on ld.post_id = bd.post_id and ld.user_id=%s where bd.post_id=%s order by bd.compare_date desc;",data)
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where tag.usertaglist_id = %s",
                row[0]['memberlist_id'])
            row[0]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select * from u736502961_hys.sm_upload_files_details where upload_id=%s",row[0]['documentlist_id'])
            row[0]['document_list'] = cursor.fetchall()
            cursor.execute(
                "select videolist_id, video, thumbnail from u736502961_hys.sm_post_videos where videolist_id = %s",
                row[0]['videolist_id'])
            row[0]['video_list'] = cursor.fetchall()
            cursor.execute(
                "select * from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id where post_id=%s;",
                row[0]['post_id'])
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
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
        cursor.execute("select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_project_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s order by prd.compare_date desc;",userid)
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
        cursor.execute("select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_project_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s where prd.post_id=%s order by prd.compare_date desc;",data)
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute(
                "select pd.*, sd.* from u736502961_hys.sm_post_users_tagged tag inner join u736502961_hys.user_personal_details pd on pd.user_id = tag.user_id inner join u736502961_hys.user_school_details sd on sd.user_id = tag.user_id where usertaglist_id = %s",
                row[0]['memberlist_id'])
            row[0]['tag_list'] = cursor.fetchall()
            cursor.execute(
                "select * from u736502961_hys.user_sm_comment_details cd inner join u736502961_hys.user_personal_details pd on pd.user_id=cd.user_id inner join u736502961_hys.user_school_details sd on cd.user_id=sd.user_id where post_id=%s;",
                row[0]['post_id'])
            row[0]['comment_list'] = cursor.fetchall()
            if len(row[0]['comment_list']) > 0:
                for i in range(len(row[0]['comment_list'])):
                    cursor.execute(
                        "select imagelist_id, image from u736502961_hys.sm_post_images where imagelist_id = %s",
                        row[0]['comment_list'][i]['imagelist_id'])
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
            data = (_address, _ambition, _dreamvacations, _email, _friends, _mygroups, _hobbies, _library, _mobileno, _novels, _placesvisited, _schooladdress, _scorecards, _uploads, _weakness, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("update u736502961_hys.user_privacy set address = %s ,ambition = %s ,dreamvacations = %s ,email = %s ,friends = %s ,mygroups = %s ,hobbies = %s ,library = %s ,mobileno = %s ,novels = %s ,placesvisited = %s ,schooladdress = %s ,scorecards = %s ,uploads = %s ,weakness = %s where user_id=%s;",data)
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
                _post_id, _user_id, _blogger_name, _blog_title, _blog_intro, _blog_content, _like_count, _comment_count, _view_count, _impression_count, _image_url, _personal_bio, _compare_date)
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
        cursor.execute("select prd.*, pd.*, sd.*, case when ld.like_type is null then '' else ld.like_type end like_type from u736502961_hys.user_sm_blog_details prd inner join u736502961_hys.user_personal_details pd on pd.user_id=prd.user_id inner join u736502961_hys.user_school_details sd on sd.user_id=prd.user_id left join u736502961_hys.sm_post_like_details ld on ld.post_id = prd.post_id and ld.user_id=%s order by prd.compare_date desc;", data)
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
                cursor.execute("insert into u736502961_hys.sm_post_like_details(post_id, user_id, post_type, like_type) values(%s, %s, %s, %s);", data)
            if _post_type == 'Mood':
                data = (_like_count, _comment_count, _view_count, _impression_count, _post_id)
                cursor.execute("update u736502961_hys.user_sm_mood_details set like_count=%s, comment_count=%s, view_count=%s, impression_count=%s where post_id=%s;", data)
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
            else :
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
        cursor.execute("select * from u736502961_hys.notification_details nd inner join u736502961_hys.user_personal_details pd on nd.sender_id=pd.user_id   where nd.receiver_id = %s order by nd.createdate desc;", id)
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
            data = (_user_id, _post_id, _post_type, _post_section, compare_date)
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
                data = (_log_id, _user_id, _post_id, _post_type, _post_section, 0, 0, compare_date)
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
