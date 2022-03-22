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
        data = (row[0]["question_id"], userid)
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


@app.route('/get_live_books_categories/<int:grade>', methods=['GET'])
def get_live_books_categories(grade):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select distinct subject_ from u736502961_hys.live_books where grade=%s;",grade)
        row = cursor.fetchall()
        if len(row) > 0:
            for i in range(len(row)):
                data = (grade, row[i]["subject_"])
                cursor.execute("select distinct publication, dictionary_id,'https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/ncrt_class_10_cover.jpg?alt=media&token=39acd6e2-f598-4b1a-babc-565fd556cf6e' as publicationImageURL from u736502961_hys.live_books where grade=%s and subject_=%s;", data)
                row[i]["distinct_publication"] = cursor.fetchall()
                row[i]["subjectImageURL"] = "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/OIP.jpg?alt=media&token=5000c2f0-4c56-42d0-bb5e-6a1e95584cb7"
        resp = jsonify({"grade":grade,
                        "distinct_subjects":row
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
        economics10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass_10_economics_chapter_1_emb.pickle?alt=media&token=674d8883-4f85-413b-a531-3b9a03008c2b",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass_10_economics_chapter_1_text.pickle?alt=media&token=217c86ff-8ca0-4a6c-a84e-14ee0bdb284e",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass%2010%20economics%20chapter%201.epub?alt=media&token=8394a6e8-8060-47d0-bfb9-ed1354693563","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_2": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass_10_economics_chapter_2_emb.pickle?alt=media&token=98a5c182-9785-4c38-be01-bb8e65403f83",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass_10_economics_chapter_2_text.pickle?alt=media&token=47fcd060-aa25-4056-92c1-e5a1b1f78f63",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass%2010%20economics%20chapter%202.epub?alt=media&token=9d5f2de2-f765-4c4c-b785-b10accd461a1","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_3": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass_10_economics_chapter_3_emb.pickle?alt=media&token=0b4b7d38-178f-482c-af22-7b9f729945e9",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass_10_economics_chapter_3_text.pickle?alt=media&token=a7f0be66-f944-49a5-9cc3-a65bb4561a2f",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass%2010%20economics%20chapter%203.epub?alt=media&token=cf502005-51b6-4b22-bf12-199b9561eabf","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_4": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass_10_economics_chapter_4_emb.pickle?alt=media&token=f6fcf9e4-ae7a-4ac2-b8b1-a6c2136da12c",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass_10_economics_chapter_4_text.pickle?alt=media&token=17e38fd5-4d46-46db-9704-4f3b13b2b24e",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass%2010%20economics%20chapter%204.epub?alt=media&token=5659e8f6-87c1-4511-86f8-5feb7ee7807e","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_5": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass_10_economics_chapter_5_emb.pickle?alt=media&token=49b185b0-5503-4872-8837-3ed3a2683d33",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass_10_economics_chapter_5_text.pickle?alt=media&token=b5189bee-e4e1-415e-ad61-9fe0e5cfce05",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass%2010%20economics%20chapter%205.epub?alt=media&token=696b9cb6-8eff-4642-bb00-15ec661418fd","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"}
                              }

        geography10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass_10_geography_chapter_1_emb.pickle?alt=media&token=bda5729f-ccef-49d2-8c6d-605a0d1cff26",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass_10_geography_chapter_1_text.pickle?alt=media&token=76dd446c-513a-4e83-b059-62f25a651c6c",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass%2010%20geography%20chapter%201.epub?alt=media&token=4b35de17-5c81-4050-9fb3-02d723abef1a","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_2": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass_10_geography_chapter_2_emb.pickle?alt=media&token=3319a7ed-07cd-4a3b-98b2-2db15ac022a1",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass_10_geography_chapter_2_text.pickle?alt=media&token=67df6458-f929-47b5-b420-924c2f023feb",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass%2010%20geography%20chapter%202.epub?alt=media&token=1b221bce-5f29-4966-9b61-1eb1539354bc","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_3": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass_10_geography_chapter_3_emb.pickle?alt=media&token=80091170-c686-4336-89ab-57722083a5ed",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass_10_geography_chapter_3_text.pickle?alt=media&token=6ca7dbac-ad96-4eff-a675-42c64b02edfa",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass%2010%20geography%20chapter%203.epub?alt=media&token=9dfdbf36-3eb9-4ad3-a693-f827f1b3f1ee","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_4": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass_10_geography_chapter_4_emb.pickle?alt=media&token=daffb7e0-37e1-4cb8-ba72-8c90228e4a1d",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass_10_geography_chapter_4_text.pickle?alt=media&token=ce43268f-67d7-49d7-aaac-d8f8125beb0a",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass%2010%20geography%20chapter%204.epub?alt=media&token=91acd3cb-5943-4285-9a83-aa39d8780cf8","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_5": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass_10_geography_chapter_5_emb.pickle?alt=media&token=e137d09d-748e-46d2-b74b-164ccf13d668",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass_10_geography_chapter_5_text.pickle?alt=media&token=92c96ca7-0529-4b3d-bd4c-bc42ab0582e5",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass%2010%20geography%20chapter%205.epub?alt=media&token=5b114740-c948-48a0-889b-865c7488a4eb","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_6": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass_10_geography_chapter_6_emb.pickle?alt=media&token=ca4a23a3-eae6-4760-8ec7-55e693b2402a",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass_10_geography_chapter_6_text.pickle?alt=media&token=7fa28343-01ac-4854-81f8-4c33bf38ae70",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass%2010%20geography%20chapter%206.epub?alt=media&token=2cf162ec-6f53-4c88-8cc3-119c2adc86de","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                              "chapter_7": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass_10_geography_chapter_7_emb.pickle?alt=media&token=3ff866ec-5357-4131-9bda-8309c460a7b5",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass_10_geography_chapter_7_text.pickle?alt=media&token=ba31f93a-05b0-4ead-abff-584b9dd9370e",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass%2010%20geography%20chapter%207.epub?alt=media&token=f66e4eff-5c1e-464a-8631-ccecd1fc42e0","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"}
                              }

        history10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fclass_10_history_chapter_1_emb.pickle?alt=media&token=a41b3ddd-c650-4188-a007-e9bb96e66360",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fclass_10_history_chapter_1_text.pickle?alt=media&token=4ec6175f-00dc-493e-a078-ab8103a7eb58",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fhistory%20chapter%201.epub?alt=media&token=e6270ebe-8c71-442b-a849-c6f8dd4a0b15","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_2": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fclass_10_history_chapter_2_emb.pickle?alt=media&token=4eb30b43-e0af-4611-b01f-66a4c0de9367",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fclass_10_history_chapter_2_text.pickle?alt=media&token=b12c6518-2a11-4d3f-9a5c-6322eccec8d6",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fhistory%20chapter%202.epub?alt=media&token=9a7fe1c5-d141-4c37-86da-662763973415","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_3": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fclass_10_history_chapter_3_emb.pickle?alt=media&token=e7a8051e-bc22-4a53-94e4-5cf7927aa27d",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fclass_10_history_chapter_3_text.pickle?alt=media&token=5ba30421-8c3d-41e4-ba98-7f160d1a0c99",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fhistory%20chapter%203.epub?alt=media&token=7b6483f0-549f-41b7-a72e-525f224e16e4","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_4": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fclass_10_history_chapter_4_emb.pickle?alt=media&token=572c74b1-5e6a-47c2-8131-e4c19d741635",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fclass_10_history_chapter_4_text.pickle?alt=media&token=66743a78-93ea-4e7a-80d0-459349c770cc",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fhistory%20chapter%204.epub?alt=media&token=5b5e4bd4-ec58-42c7-90d3-2dfe80eccbd6","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_5": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fclass_10_history_chapter_5_emb.pickle?alt=media&token=0cfda65a-65e1-4add-84e0-bc9c51e69600",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fclass_10_history_chapter_5_text.pickle?alt=media&token=e60bd917-a392-4903-9f66-97a62e0017de",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fhistory%20chapter%205.epub?alt=media&token=f4044dea-04a5-43ae-9347-18de1302c778","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"}
                            }

        mathematics10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass_10_math_chapter_1_emb.pickle?alt=media&token=f605809f-1c58-49de-a256-eb4094df0d4e",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass_10_math_chapter_1_text.pickle?alt=media&token=e0934e22-93ae-4a52-af9e-ef03b1c8c2d4",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass%2010%20math%20chapter%201.epub?alt=media&token=6ba9aa62-6ce5-47eb-9a34-a6c5f032b4a7","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_2": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass_10_math_chapter_2_emb.pickle?alt=media&token=2ab22185-37f8-49da-8f12-3b2a201c071c",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass_10_math_chapter_2_text.pickle?alt=media&token=c64adf11-c273-4bd0-805c-4c1a9fbfd1fc",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass%2010%20math%20chapter%202.epub?alt=media&token=95c11b13-2893-4cab-9670-b4e2e6f0f7d8","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_3": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass_10_math_chapter_3_emb.pickle?alt=media&token=087d37f7-8ff2-4b57-8c6a-e6d41967df08",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass_10_math_chapter_3_text.pickle?alt=media&token=204b66ff-e835-4810-ac72-f31cd238e70f",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass%2010%20math%20chapter%203.epub?alt=media&token=29923fd3-7f9c-47ec-8720-f4fff7d8f7fc","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_4": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass_10_math_chapter_4_emb.pickle?alt=media&token=eb4c6842-ea08-44bd-9eae-37d17bdff74a",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass_10_math_chapter_4_text.pickle?alt=media&token=70eb2932-4068-48ff-855c-7247a3e1d398",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass%2010%20math%20chapter%204.epub?alt=media&token=7d8a1ac9-3bb3-4345-891a-ff764d3d3b5e","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_5": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass_10_math_chapter_5_emb.pickle?alt=media&token=6ea17c0f-5773-4e7b-bb36-f632770af032",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass_10_math_chapter_5_text.pickle?alt=media&token=fc4e2905-d93b-4e08-941b-18f803ba5fb2",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass%2010%20math%20chapter%205.epub?alt=media&token=96637ad4-3d58-4b16-89ba-e15cec7e6ebd","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_6": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass_10_math_chapter_6_emb.pickle?alt=media&token=7249f28e-b37a-4de5-9e30-dc3ead3e8531",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass_10_math_chapter_6_text.pickle?alt=media&token=d55e9559-c8e1-44c8-a47b-bba02b35948b",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass%2010%20math%20chapter%206.epub?alt=media&token=5f3c7b92-8b56-470a-a5bf-dcb2c0313256","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_7": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass_10_math_chapter_7_emb.pickle?alt=media&token=5ed2dbdb-460b-4c84-a763-8681b32ff728",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass_10_math_chapter_7_text.pickle?alt=media&token=95390455-6856-4312-8ca8-67716371a3e8",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass%2010%20math%20chapter%207.epub?alt=media&token=23295817-f972-4867-b117-c471f94195b9","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_8": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass_10_math_chapter_8_emb.pickle?alt=media&token=08361518-58ff-4133-884b-d91c1a91f5dd",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass_10_math_chapter_8_text.pickle?alt=media&token=85246b0e-6289-4139-b125-67c74d96edb7",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass%2010%20math%20chapter%208.epub?alt=media&token=a8eda524-b7f6-4d00-b00c-e81f5979d74e","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_9": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass_10_math_chapter_9_emb.pickle?alt=media&token=dbdc9eaf-bf04-42c2-a3cb-359704b0b77b",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass_10_math_chapter_9_text.pickle?alt=media&token=9ecf2283-1a22-4043-a1f3-f5673aa746fa",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass%2010%20math%20chapter%209.epub?alt=media&token=19215403-08e0-4109-9fee-a097e48e77fe","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_10": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass_10_math_chapter_10_emb.pickle?alt=media&token=e91ed504-7c34-4cee-aef1-af230789bd3f",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass_10_math_chapter_10_text.pickle?alt=media&token=c46828a5-b8d1-4f35-b1c6-66f16d0df4c6",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass%2010%20math%20chapter%2010.epub?alt=media&token=3a575a57-c57a-44ef-807b-007bcb4300eb","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_11": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass_10_math_chapter_11_emb.pickle?alt=media&token=ee0ddc86-22b5-4a7b-9ab9-64f0c239df40",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass_10_math_chapter_11_text.pickle?alt=media&token=66947e14-befe-4958-b665-38c42429e841",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass%2010%20math%20chapter%2011.epub?alt=media&token=9503dbe3-b275-4530-88d6-852ee143508a","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_12": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass_10_math_chapter_12_emb.pickle?alt=media&token=16ab50f8-862d-45db-819f-b50d70e075fa",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass_10_math_chapter_12_text.pickle?alt=media&token=67295602-bfde-402e-846e-26f52127085a",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass%2010%20math%20chapter%2012.epub?alt=media&token=e5051833-6981-47d9-b089-bdc533719dfd","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_13": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass_10_math_chapter_13_emb.pickle?alt=media&token=b4fc802d-4879-441f-9458-158c9f4df7ad",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass_10_math_chapter_13_text.pickle?alt=media&token=80ce2a37-a2cd-4baf-8b91-37d8036e0aa0",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass%2010%20math%20chapter%2013.epub?alt=media&token=ed87ee85-68d1-452c-abe9-b35596aebbf1","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_14": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass_10_math_chapter_14_emb.pickle?alt=media&token=a5869929-69a8-4101-9db7-9db74a5d9b1e",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass_10_math_chapter_14_text.pickle?alt=media&token=386afb69-9caf-48fd-9169-c0514eb38c70",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass%2010%20math%20chapter%2014.epub?alt=media&token=78f234ec-75ca-477b-9295-89b9fee4d2da","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                                "chapter_15": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass_10_math_chapter_15_emb.pickle?alt=media&token=9c45e7d6-f2f5-46d1-a22c-d91ea352c2d6",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass_10_math_chapter_15_text.pickle?alt=media&token=f7e2f251-20a2-474e-a6f9-a55dd0bd7a90",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass%2010%20math%20chapter%2015.epub?alt=media&token=f05857f6-3366-40ce-9a1e-8b1cc9b0086a","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"}
                                }

        civics10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass_10_political_science_chapter_1_emb.pickle?alt=media&token=8609c368-55a3-4ccf-8a90-f4552c386d0d",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass_10_political_science_chapter_1_text.pickle?alt=media&token=4ca251ea-d8dd-4bd8-b98d-97b3259d2d13",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass%2010%20political%20science%20chapter%201.epub?alt=media&token=71ac617e-f982-410c-b52f-5f2065c96480","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_2": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass_10_political_science_chapter_2_emb.pickle?alt=media&token=1f4e4381-8b6d-4a47-bc27-8aee7ae2e9ba",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass_10_political_science_chapter_2_text.pickle?alt=media&token=adae8df8-7db7-4f8c-802a-85b6f30fcce0",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass%2010%20political%20science%20chapter%202.epub?alt=media&token=2caea25c-b09e-4d5e-9656-7755151b2691","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_3": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass_10_political_science_chapter_3_emb.pickle?alt=media&token=453fee3e-5cae-4942-9508-81bb52874362",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass_10_political_science_chapter_3_text.pickle?alt=media&token=c8f3ec57-2cb0-43e5-ad9c-9d319631dcae",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass%2010%20political%20science%20chapter%203.epub?alt=media&token=930d0023-2f05-42b7-a1d5-b50f6f2f3790","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_4": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass_10_political_science_chapter_4_emb.pickle?alt=media&token=4720e310-1454-4063-9a58-d0198c864d08",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass_10_political_science_chapter_4_text.pickle?alt=media&token=403d8167-cf5c-4033-b838-53ae2b24018e",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass%2010%20political%20science%20chapter%204.epub?alt=media&token=5db91d4f-6652-4a8d-aa33-06252cfce4b9","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_5": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass_10_political_science_chapter_5_emb.pickle?alt=media&token=66ea431c-6872-4e8d-8243-a8c4f13e03b7",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass_10_political_science_chapter_5_text.pickle?alt=media&token=e40a47b6-f953-4d41-b6c5-40645b0a81c6",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass%2010%20political%20science%20chapter%205.epub?alt=media&token=e6da7ef2-2297-4154-acb6-649636043e74","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_6": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass_10_political_science_chapter_6_emb.pickle?alt=media&token=4287105e-bca4-4265-a052-b35c80820456",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass_10_political_science_chapter_6_text.pickle?alt=media&token=fe8f3d31-e4d6-44b0-80b2-b7982547f08b",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass%2010%20political%20science%20chapter%206.epub?alt=media&token=e3dd04bf-8c9d-4137-a36d-9ac13f52b97c","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_7": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass_10_political_science_chapter_7_emb.pickle?alt=media&token=d2a076ed-e43d-4e7e-b737-0af34c91b88d",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass_10_political_science_chapter_7_text.pickle?alt=media&token=32466b00-732f-4b7b-a095-a8aa4e3c626e",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass%2010%20political%20science%20chapter%207.epub?alt=media&token=497bf325-4d65-4ec4-9bb5-7f96656e0d1e","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                           "chapter_8": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass_10_political_science_chapter_8_emb.pickle?alt=media&token=75d920de-55dc-4310-a52a-ce536af5c236",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass_10_political_science_chapter_8_text.pickle?alt=media&token=a852aecd-a6dc-4e95-9955-cf24503d2ff0",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass%2010%20political%20science%20chapter%208.epub?alt=media&token=bfbd52d9-d963-41ed-95fb-15861f18eae5","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"}
                           }

        science10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fclass_10_science_chapter_1_emb.pickle?alt=media&token=31a4e158-bbc9-4c67-9548-12a4b5120e8c",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fclass_10_science_chapter_1_text.pickle?alt=media&token=872f2398-f240-4417-8938-afab74a66385",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fchapter%201.epub?alt=media&token=c7fc50ac-cb63-4e08-bcaf-99634dd51943","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_2": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fclass_10_science_chapter_2_emb.pickle?alt=media&token=77c18e3a-c145-49e5-b5d0-2571f09485e9",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fclass_10_science_chapter_2_text.pickle?alt=media&token=9de01f8f-211a-4a00-81a4-5758f92c7ca1",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fchapter%202.epub?alt=media&token=e8c5a4af-2dd0-4cc3-bf91-851731280ae5","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_3": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fclass_10_science_chapter_3_emb.pickle?alt=media&token=1dc9163e-3f41-41fe-8452-445802c7fd00",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fclass_10_science_chapter_3_text.pickle?alt=media&token=26ef43b0-141b-4dfb-bbcd-e0270598abeb",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fchapter%203.epub?alt=media&token=3ad1ffb1-a330-4add-b21f-b88ac3f1b1bd","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_4": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fclass_10_science_chapter_4_emb.pickle?alt=media&token=9a34900f-1ac5-43e4-95ed-720bcc3c869e",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fclass_10_science_chapter_4_text.pickle?alt=media&token=2d6361eb-965b-44e6-a2ca-8264de234f20",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fchapter%204.epub?alt=media&token=f2d4e134-0374-4d2c-8b2f-1bb67a90da45","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_5": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fclass_10_science_chapter_5_emb.pickle?alt=media&token=64f04259-d336-4863-b113-18f5ca0f60f7",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fclass_10_science_chapter_5_text.pickle?alt=media&token=047787e5-4192-4812-b6fe-17c266bb7abc",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fchapter%205.epub?alt=media&token=85605022-830d-4715-9200-fd39efbae7e3","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_6": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fclass_10_science_chapter_6_emb.pickle?alt=media&token=175ae258-720a-4558-80bd-9d3c072b3689",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fclass_10_science_chapter_6_text.pickle?alt=media&token=41fa1365-cff0-4044-a162-710eaaa3c115",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fchapter%206.epub?alt=media&token=66662e54-cfd5-4281-bd75-3013a35877fe","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_7": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fclass_10_science_chapter_7_emb.pickle?alt=media&token=59ba84e8-6912-4a0e-af39-f410aa31cb42",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fclass_10_science_chapter_7_text.pickle?alt=media&token=a383c684-6ea3-44ad-95ed-39989b70c692",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fchapter%207.epub?alt=media&token=e6283b35-c36e-4c08-8228-5d3712c57848","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_8": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fclass_10_science_chapter_8_emb.pickle?alt=media&token=3c48eb58-fd9b-4891-99e9-6e01e3e17a94",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fclass_10_science_chapter_8_text.pickle?alt=media&token=074f5ff3-1a07-4729-baf4-1e1c966dffbf",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fchapter%208.epub?alt=media&token=6bf6bfff-58e9-4ddc-879f-c7678e0e4789","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_9": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fclass_10_science_chapter_9_emb.pickle?alt=media&token=5ab6c404-aeca-4f05-9b53-495b17224150",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fclass_10_science_chapter_9_text.pickle?alt=media&token=bdd1c428-9841-4885-9937-cf7a0bdac22a",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fchapter%209.epub?alt=media&token=a47526ab-bfd4-4b88-9a83-963d1d480d8b","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_10": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fclass_10_science_chapter_10_emb.pickle?alt=media&token=8ce75623-28c3-4db2-ba18-9e20823b24a8",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fclass_10_science_chapter_10_text.pickle?alt=media&token=e51f5e77-10f9-4218-b71b-1d106eb1f467",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fchapter%2010.epub?alt=media&token=988a0ab6-5b8f-45a6-ba13-f8d8603cbabb","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_11": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fclass_10_science_chapter_11_emb.pickle?alt=media&token=31fcbfe9-bd93-43d1-9a5c-113a0eb52d19",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fclass_10_science_chapter_11_text.pickle?alt=media&token=d06b8cc4-e14a-4707-8740-ee83c4cda8d3",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fchapter%2011.epub?alt=media&token=e6cf2759-9cba-46c1-b7ef-4462a9a669d7","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_12": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fclass_10_science_chapter_12_emb.pickle?alt=media&token=51e6330e-cb2a-4c17-a437-ed3c0c8acf22",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fclass_10_science_chapter_12_text.pickle?alt=media&token=e7623977-a0c3-4169-8d6e-3c7de6ca1890",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fchapter%2012.epub?alt=media&token=7072bd3e-a992-43ff-8e0d-580045b9aef4","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_13": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fclass_10_science_chapter_13_emb.pickle?alt=media&token=2f8093a1-2b99-4088-bc2c-989caa23c6cd",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fclass_10_science_chapter_13_text.pickle?alt=media&token=782665ce-b872-46a9-a309-0bba1fe964b9",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fchapter%2013.epub?alt=media&token=4808231f-f255-4912-a24c-d52343cef661","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_14": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fclass_10_science_chapter_14_emb.pickle?alt=media&token=dd06c239-068f-4062-80ab-a8ad52b0cfa5",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fclass_10_science_chapter_14_text.pickle?alt=media&token=d48bc2e7-18db-4f6a-9e8c-6dc8b9ab1b48",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fchapter%2014.epub?alt=media&token=4dfce889-f5ea-4ffe-b1e1-d5c8cb64ef09","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"},
                            "chapter_15": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fclass_10_science_chapter_15_emb.pickle?alt=media&token=e6c00313-dea9-47ab-94c1-a4e9fc5fddfd",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fclass_10_science_chapter_15_text.pickle?alt=media&token=3d6166c2-722a-44de-a7bb-aa77e4ef3e32",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fchapter%2015.epub?alt=media&token=787d5bb8-ddcb-49bf-a5ab-82af2f1ee14b","chapterImageURL":"https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/d9a2mq5-23ceded5-d2e1-48c5-8df5-37bea8337143.png?alt=media&token=b1d83bf7-18f4-4208-8272-b30cffde1bbb"}
                            }
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from u736502961_hys.live_books where dictionary_id=%s;",dictionary_id)
        row = cursor.fetchall()
        if len(row) > 0:
            if row[0]["dictionary_id"] == 'economics10ncert01':
                row[0]["dictionary_list"] = [economics10ncert01]
            elif row[0]["dictionary_id"] == 'geography10ncert01':
                row[0]["dictionary_list"] = [geography10ncert01]
            elif row[0]["dictionary_id"] == 'history10ncert01':
                row[0]["dictionary_list"] = [history10ncert01]
            elif row[0]["dictionary_id"] == 'mathematics10ncert01':
                row[0]["dictionary_list"] = [mathematics10ncert01]
            elif row[0]["dictionary_id"] == 'civics10ncert01':
                row[0]["dictionary_list"] = [civics10ncert01]
            elif row[0]["dictionary_id"] == 'science10ncert01':
                row[0]["dictionary_list"] = [science10ncert01]
        resp = jsonify({"createdate":row[0]["createdate"],
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
        economics10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass_10_economics_chapter_1_emb.pickle?alt=media&token=674d8883-4f85-413b-a531-3b9a03008c2b",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass_10_economics_chapter_1_text.pickle?alt=media&token=217c86ff-8ca0-4a6c-a84e-14ee0bdb284e",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%201%2Fclass%2010%20economics%20chapter%201.epub?alt=media&token=8394a6e8-8060-47d0-bfb9-ed1354693563"},
                              "chapter_2": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass_10_economics_chapter_2_emb.pickle?alt=media&token=98a5c182-9785-4c38-be01-bb8e65403f83",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass_10_economics_chapter_2_text.pickle?alt=media&token=47fcd060-aa25-4056-92c1-e5a1b1f78f63",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%202%2Fclass%2010%20economics%20chapter%202.epub?alt=media&token=9d5f2de2-f765-4c4c-b785-b10accd461a1"},
                              "chapter_3": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass_10_economics_chapter_3_emb.pickle?alt=media&token=0b4b7d38-178f-482c-af22-7b9f729945e9",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass_10_economics_chapter_3_text.pickle?alt=media&token=a7f0be66-f944-49a5-9cc3-a65bb4561a2f",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%203%2Fclass%2010%20economics%20chapter%203.epub?alt=media&token=cf502005-51b6-4b22-bf12-199b9561eabf"},
                              "chapter_4": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass_10_economics_chapter_4_emb.pickle?alt=media&token=f6fcf9e4-ae7a-4ac2-b8b1-a6c2136da12c",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass_10_economics_chapter_4_text.pickle?alt=media&token=17e38fd5-4d46-46db-9704-4f3b13b2b24e",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%204%2Fclass%2010%20economics%20chapter%204.epub?alt=media&token=5659e8f6-87c1-4511-86f8-5feb7ee7807e"},
                              "chapter_5": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass_10_economics_chapter_5_emb.pickle?alt=media&token=49b185b0-5503-4872-8837-3ed3a2683d33",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass_10_economics_chapter_5_text.pickle?alt=media&token=b5189bee-e4e1-415e-ad61-9fe0e5cfce05",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Feconomics%2Fchapter%205%2Fclass%2010%20economics%20chapter%205.epub?alt=media&token=696b9cb6-8eff-4642-bb00-15ec661418fd"}
                              }

        geography10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass_10_geography_chapter_1_emb.pickle?alt=media&token=bda5729f-ccef-49d2-8c6d-605a0d1cff26",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass_10_geography_chapter_1_text.pickle?alt=media&token=76dd446c-513a-4e83-b059-62f25a651c6c",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%201%2Fclass%2010%20geography%20chapter%201.epub?alt=media&token=4b35de17-5c81-4050-9fb3-02d723abef1a"},
                              "chapter_2": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass_10_geography_chapter_2_emb.pickle?alt=media&token=3319a7ed-07cd-4a3b-98b2-2db15ac022a1",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass_10_geography_chapter_2_text.pickle?alt=media&token=67df6458-f929-47b5-b420-924c2f023feb",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%202%2Fclass%2010%20geography%20chapter%202.epub?alt=media&token=1b221bce-5f29-4966-9b61-1eb1539354bc"},
                              "chapter_3": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass_10_geography_chapter_3_emb.pickle?alt=media&token=80091170-c686-4336-89ab-57722083a5ed",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass_10_geography_chapter_3_text.pickle?alt=media&token=6ca7dbac-ad96-4eff-a675-42c64b02edfa",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%203%2Fclass%2010%20geography%20chapter%203.epub?alt=media&token=9dfdbf36-3eb9-4ad3-a693-f827f1b3f1ee"},
                              "chapter_4": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass_10_geography_chapter_4_emb.pickle?alt=media&token=daffb7e0-37e1-4cb8-ba72-8c90228e4a1d",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass_10_geography_chapter_4_text.pickle?alt=media&token=ce43268f-67d7-49d7-aaac-d8f8125beb0a",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%204%2Fclass%2010%20geography%20chapter%204.epub?alt=media&token=91acd3cb-5943-4285-9a83-aa39d8780cf8"},
                              "chapter_5": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass_10_geography_chapter_5_emb.pickle?alt=media&token=e137d09d-748e-46d2-b74b-164ccf13d668",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass_10_geography_chapter_5_text.pickle?alt=media&token=92c96ca7-0529-4b3d-bd4c-bc42ab0582e5",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%205%2Fclass%2010%20geography%20chapter%205.epub?alt=media&token=5b114740-c948-48a0-889b-865c7488a4eb"},
                              "chapter_6": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass_10_geography_chapter_6_emb.pickle?alt=media&token=ca4a23a3-eae6-4760-8ec7-55e693b2402a",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass_10_geography_chapter_6_text.pickle?alt=media&token=7fa28343-01ac-4854-81f8-4c33bf38ae70",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%206%2Fclass%2010%20geography%20chapter%206.epub?alt=media&token=2cf162ec-6f53-4c88-8cc3-119c2adc86de"},
                              "chapter_7": {
                                  "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass_10_geography_chapter_7_emb.pickle?alt=media&token=3ff866ec-5357-4131-9bda-8309c460a7b5",
                                  "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass_10_geography_chapter_7_text.pickle?alt=media&token=ba31f93a-05b0-4ead-abff-584b9dd9370e",
                                  "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fgeography%2Fchapter%207%2Fclass%2010%20geography%20chapter%207.epub?alt=media&token=f66e4eff-5c1e-464a-8631-ccecd1fc42e0"}
                              }

        history10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fclass_10_history_chapter_1_emb.pickle?alt=media&token=a41b3ddd-c650-4188-a007-e9bb96e66360",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fclass_10_history_chapter_1_text.pickle?alt=media&token=4ec6175f-00dc-493e-a078-ab8103a7eb58",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%201%2Fhistory%20chapter%201.epub?alt=media&token=e6270ebe-8c71-442b-a849-c6f8dd4a0b15"},
                            "chapter_2": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fclass_10_history_chapter_2_emb.pickle?alt=media&token=4eb30b43-e0af-4611-b01f-66a4c0de9367",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fclass_10_history_chapter_2_text.pickle?alt=media&token=b12c6518-2a11-4d3f-9a5c-6322eccec8d6",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%202%2Fhistory%20chapter%202.epub?alt=media&token=9a7fe1c5-d141-4c37-86da-662763973415"},
                            "chapter_3": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fclass_10_history_chapter_3_emb.pickle?alt=media&token=e7a8051e-bc22-4a53-94e4-5cf7927aa27d",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fclass_10_history_chapter_3_text.pickle?alt=media&token=5ba30421-8c3d-41e4-ba98-7f160d1a0c99",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%203%2Fhistory%20chapter%203.epub?alt=media&token=7b6483f0-549f-41b7-a72e-525f224e16e4"},
                            "chapter_4": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fclass_10_history_chapter_4_emb.pickle?alt=media&token=572c74b1-5e6a-47c2-8131-e4c19d741635",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fclass_10_history_chapter_4_text.pickle?alt=media&token=66743a78-93ea-4e7a-80d0-459349c770cc",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%204%2Fhistory%20chapter%204.epub?alt=media&token=5b5e4bd4-ec58-42c7-90d3-2dfe80eccbd6"},
                            "chapter_5": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fclass_10_history_chapter_5_emb.pickle?alt=media&token=0cfda65a-65e1-4add-84e0-bc9c51e69600",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fclass_10_history_chapter_5_text.pickle?alt=media&token=e60bd917-a392-4903-9f66-97a62e0017de",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fhistory%2Fchapter%205%2Fhistory%20chapter%205.epub?alt=media&token=f4044dea-04a5-43ae-9347-18de1302c778"}
                            }

        mathematics10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass_10_math_chapter_1_emb.pickle?alt=media&token=f605809f-1c58-49de-a256-eb4094df0d4e",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass_10_math_chapter_1_text.pickle?alt=media&token=e0934e22-93ae-4a52-af9e-ef03b1c8c2d4",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%201%2Fclass%2010%20math%20chapter%201.epub?alt=media&token=6ba9aa62-6ce5-47eb-9a34-a6c5f032b4a7"},
                                "chapter_2": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass_10_math_chapter_2_emb.pickle?alt=media&token=2ab22185-37f8-49da-8f12-3b2a201c071c",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass_10_math_chapter_2_text.pickle?alt=media&token=c64adf11-c273-4bd0-805c-4c1a9fbfd1fc",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%202%2Fclass%2010%20math%20chapter%202.epub?alt=media&token=95c11b13-2893-4cab-9670-b4e2e6f0f7d8"},
                                "chapter_3": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass_10_math_chapter_3_emb.pickle?alt=media&token=087d37f7-8ff2-4b57-8c6a-e6d41967df08",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass_10_math_chapter_3_text.pickle?alt=media&token=204b66ff-e835-4810-ac72-f31cd238e70f",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%203%2Fclass%2010%20math%20chapter%203.epub?alt=media&token=29923fd3-7f9c-47ec-8720-f4fff7d8f7fc"},
                                "chapter_4": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass_10_math_chapter_4_emb.pickle?alt=media&token=eb4c6842-ea08-44bd-9eae-37d17bdff74a",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass_10_math_chapter_4_text.pickle?alt=media&token=70eb2932-4068-48ff-855c-7247a3e1d398",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%204%2Fclass%2010%20math%20chapter%204.epub?alt=media&token=7d8a1ac9-3bb3-4345-891a-ff764d3d3b5e"},
                                "chapter_5": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass_10_math_chapter_5_emb.pickle?alt=media&token=6ea17c0f-5773-4e7b-bb36-f632770af032",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass_10_math_chapter_5_text.pickle?alt=media&token=fc4e2905-d93b-4e08-941b-18f803ba5fb2",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%205%2Fclass%2010%20math%20chapter%205.epub?alt=media&token=96637ad4-3d58-4b16-89ba-e15cec7e6ebd"},
                                "chapter_6": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass_10_math_chapter_6_emb.pickle?alt=media&token=7249f28e-b37a-4de5-9e30-dc3ead3e8531",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass_10_math_chapter_6_text.pickle?alt=media&token=d55e9559-c8e1-44c8-a47b-bba02b35948b",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%206%2Fclass%2010%20math%20chapter%206.epub?alt=media&token=5f3c7b92-8b56-470a-a5bf-dcb2c0313256"},
                                "chapter_7": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass_10_math_chapter_7_emb.pickle?alt=media&token=5ed2dbdb-460b-4c84-a763-8681b32ff728",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass_10_math_chapter_7_text.pickle?alt=media&token=95390455-6856-4312-8ca8-67716371a3e8",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%207%2Fclass%2010%20math%20chapter%207.epub?alt=media&token=23295817-f972-4867-b117-c471f94195b9"},
                                "chapter_8": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass_10_math_chapter_8_emb.pickle?alt=media&token=08361518-58ff-4133-884b-d91c1a91f5dd",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass_10_math_chapter_8_text.pickle?alt=media&token=85246b0e-6289-4139-b125-67c74d96edb7",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%208%2Fclass%2010%20math%20chapter%208.epub?alt=media&token=a8eda524-b7f6-4d00-b00c-e81f5979d74e"},
                                "chapter_9": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass_10_math_chapter_9_emb.pickle?alt=media&token=dbdc9eaf-bf04-42c2-a3cb-359704b0b77b",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass_10_math_chapter_9_text.pickle?alt=media&token=9ecf2283-1a22-4043-a1f3-f5673aa746fa",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%209%2Fclass%2010%20math%20chapter%209.epub?alt=media&token=19215403-08e0-4109-9fee-a097e48e77fe"},
                                "chapter_10": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass_10_math_chapter_10_emb.pickle?alt=media&token=e91ed504-7c34-4cee-aef1-af230789bd3f",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass_10_math_chapter_10_text.pickle?alt=media&token=c46828a5-b8d1-4f35-b1c6-66f16d0df4c6",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2010%2Fclass%2010%20math%20chapter%2010.epub?alt=media&token=3a575a57-c57a-44ef-807b-007bcb4300eb"},
                                "chapter_11": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass_10_math_chapter_11_emb.pickle?alt=media&token=ee0ddc86-22b5-4a7b-9ab9-64f0c239df40",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass_10_math_chapter_11_text.pickle?alt=media&token=66947e14-befe-4958-b665-38c42429e841",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2011%2Fclass%2010%20math%20chapter%2011.epub?alt=media&token=9503dbe3-b275-4530-88d6-852ee143508a"},
                                "chapter_12": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass_10_math_chapter_12_emb.pickle?alt=media&token=16ab50f8-862d-45db-819f-b50d70e075fa",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass_10_math_chapter_12_text.pickle?alt=media&token=67295602-bfde-402e-846e-26f52127085a",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2012%2Fclass%2010%20math%20chapter%2012.epub?alt=media&token=e5051833-6981-47d9-b089-bdc533719dfd"},
                                "chapter_13": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass_10_math_chapter_13_emb.pickle?alt=media&token=b4fc802d-4879-441f-9458-158c9f4df7ad",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass_10_math_chapter_13_text.pickle?alt=media&token=80ce2a37-a2cd-4baf-8b91-37d8036e0aa0",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2013%2Fclass%2010%20math%20chapter%2013.epub?alt=media&token=ed87ee85-68d1-452c-abe9-b35596aebbf1"},
                                "chapter_14": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass_10_math_chapter_14_emb.pickle?alt=media&token=a5869929-69a8-4101-9db7-9db74a5d9b1e",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass_10_math_chapter_14_text.pickle?alt=media&token=386afb69-9caf-48fd-9169-c0514eb38c70",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2014%2Fclass%2010%20math%20chapter%2014.epub?alt=media&token=78f234ec-75ca-477b-9295-89b9fee4d2da"},
                                "chapter_15": {
                                    "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass_10_math_chapter_15_emb.pickle?alt=media&token=9c45e7d6-f2f5-46d1-a22c-d91ea352c2d6",
                                    "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass_10_math_chapter_15_text.pickle?alt=media&token=f7e2f251-20a2-474e-a6f9-a55dd0bd7a90",
                                    "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fmathematics%2Fchapter%2015%2Fclass%2010%20math%20chapter%2015.epub?alt=media&token=f05857f6-3366-40ce-9a1e-8b1cc9b0086a"}
                                }

        civics10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass_10_political_science_chapter_1_emb.pickle?alt=media&token=8609c368-55a3-4ccf-8a90-f4552c386d0d",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass_10_political_science_chapter_1_text.pickle?alt=media&token=4ca251ea-d8dd-4bd8-b98d-97b3259d2d13",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%201%2Fclass%2010%20political%20science%20chapter%201.epub?alt=media&token=71ac617e-f982-410c-b52f-5f2065c96480"},
                           "chapter_2": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass_10_political_science_chapter_2_emb.pickle?alt=media&token=1f4e4381-8b6d-4a47-bc27-8aee7ae2e9ba",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass_10_political_science_chapter_2_text.pickle?alt=media&token=adae8df8-7db7-4f8c-802a-85b6f30fcce0",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%202%2Fclass%2010%20political%20science%20chapter%202.epub?alt=media&token=2caea25c-b09e-4d5e-9656-7755151b2691"},
                           "chapter_3": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass_10_political_science_chapter_3_emb.pickle?alt=media&token=453fee3e-5cae-4942-9508-81bb52874362",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass_10_political_science_chapter_3_text.pickle?alt=media&token=c8f3ec57-2cb0-43e5-ad9c-9d319631dcae",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%203%2Fclass%2010%20political%20science%20chapter%203.epub?alt=media&token=930d0023-2f05-42b7-a1d5-b50f6f2f3790"},
                           "chapter_4": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass_10_political_science_chapter_4_emb.pickle?alt=media&token=4720e310-1454-4063-9a58-d0198c864d08",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass_10_political_science_chapter_4_text.pickle?alt=media&token=403d8167-cf5c-4033-b838-53ae2b24018e",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%204%2Fclass%2010%20political%20science%20chapter%204.epub?alt=media&token=5db91d4f-6652-4a8d-aa33-06252cfce4b9"},
                           "chapter_5": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass_10_political_science_chapter_5_emb.pickle?alt=media&token=66ea431c-6872-4e8d-8243-a8c4f13e03b7",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass_10_political_science_chapter_5_text.pickle?alt=media&token=e40a47b6-f953-4d41-b6c5-40645b0a81c6",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%205%2Fclass%2010%20political%20science%20chapter%205.epub?alt=media&token=e6da7ef2-2297-4154-acb6-649636043e74"},
                           "chapter_6": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass_10_political_science_chapter_6_emb.pickle?alt=media&token=4287105e-bca4-4265-a052-b35c80820456",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass_10_political_science_chapter_6_text.pickle?alt=media&token=fe8f3d31-e4d6-44b0-80b2-b7982547f08b",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%206%2Fclass%2010%20political%20science%20chapter%206.epub?alt=media&token=e3dd04bf-8c9d-4137-a36d-9ac13f52b97c"},
                           "chapter_7": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass_10_political_science_chapter_7_emb.pickle?alt=media&token=d2a076ed-e43d-4e7e-b737-0af34c91b88d",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass_10_political_science_chapter_7_text.pickle?alt=media&token=32466b00-732f-4b7b-a095-a8aa4e3c626e",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%207%2Fclass%2010%20political%20science%20chapter%207.epub?alt=media&token=497bf325-4d65-4ec4-9bb5-7f96656e0d1e"},
                           "chapter_8": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass_10_political_science_chapter_8_emb.pickle?alt=media&token=75d920de-55dc-4310-a52a-ce536af5c236",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass_10_political_science_chapter_8_text.pickle?alt=media&token=a852aecd-a6dc-4e95-9955-cf24503d2ff0",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fpolitical%20science%2Fchapter%208%2Fclass%2010%20political%20science%20chapter%208.epub?alt=media&token=bfbd52d9-d963-41ed-95fb-15861f18eae5"}
                           }

        science10ncert01 = {"chapter_1": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fclass_10_science_chapter_1_emb.pickle?alt=media&token=31a4e158-bbc9-4c67-9548-12a4b5120e8c",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fclass_10_science_chapter_1_text.pickle?alt=media&token=872f2398-f240-4417-8938-afab74a66385",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%201%2Fchapter%201.epub?alt=media&token=c7fc50ac-cb63-4e08-bcaf-99634dd51943"},
                            "chapter_2": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fclass_10_science_chapter_2_emb.pickle?alt=media&token=77c18e3a-c145-49e5-b5d0-2571f09485e9",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fclass_10_science_chapter_2_text.pickle?alt=media&token=9de01f8f-211a-4a00-81a4-5758f92c7ca1",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%202%2Fchapter%202.epub?alt=media&token=e8c5a4af-2dd0-4cc3-bf91-851731280ae5"},
                            "chapter_3": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fclass_10_science_chapter_3_emb.pickle?alt=media&token=1dc9163e-3f41-41fe-8452-445802c7fd00",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fclass_10_science_chapter_3_text.pickle?alt=media&token=26ef43b0-141b-4dfb-bbcd-e0270598abeb",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%203%2Fchapter%203.epub?alt=media&token=3ad1ffb1-a330-4add-b21f-b88ac3f1b1bd"},
                            "chapter_4": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fclass_10_science_chapter_4_emb.pickle?alt=media&token=9a34900f-1ac5-43e4-95ed-720bcc3c869e",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fclass_10_science_chapter_4_text.pickle?alt=media&token=2d6361eb-965b-44e6-a2ca-8264de234f20",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%204%2Fchapter%204.epub?alt=media&token=f2d4e134-0374-4d2c-8b2f-1bb67a90da45"},
                            "chapter_5": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fclass_10_science_chapter_5_emb.pickle?alt=media&token=64f04259-d336-4863-b113-18f5ca0f60f7",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fclass_10_science_chapter_5_text.pickle?alt=media&token=047787e5-4192-4812-b6fe-17c266bb7abc",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%205%2Fchapter%205.epub?alt=media&token=85605022-830d-4715-9200-fd39efbae7e3"},
                            "chapter_6": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fclass_10_science_chapter_6_emb.pickle?alt=media&token=175ae258-720a-4558-80bd-9d3c072b3689",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fclass_10_science_chapter_6_text.pickle?alt=media&token=41fa1365-cff0-4044-a162-710eaaa3c115",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%206%2Fchapter%206.epub?alt=media&token=66662e54-cfd5-4281-bd75-3013a35877fe"},
                            "chapter_7": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fclass_10_science_chapter_7_emb.pickle?alt=media&token=59ba84e8-6912-4a0e-af39-f410aa31cb42",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fclass_10_science_chapter_7_text.pickle?alt=media&token=a383c684-6ea3-44ad-95ed-39989b70c692",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%207%2Fchapter%207.epub?alt=media&token=e6283b35-c36e-4c08-8228-5d3712c57848"},
                            "chapter_8": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fclass_10_science_chapter_8_emb.pickle?alt=media&token=3c48eb58-fd9b-4891-99e9-6e01e3e17a94",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fclass_10_science_chapter_8_text.pickle?alt=media&token=074f5ff3-1a07-4729-baf4-1e1c966dffbf",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%208%2Fchapter%208.epub?alt=media&token=6bf6bfff-58e9-4ddc-879f-c7678e0e4789"},
                            "chapter_9": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fclass_10_science_chapter_9_emb.pickle?alt=media&token=5ab6c404-aeca-4f05-9b53-495b17224150",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fclass_10_science_chapter_9_text.pickle?alt=media&token=bdd1c428-9841-4885-9937-cf7a0bdac22a",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%209%2Fchapter%209.epub?alt=media&token=a47526ab-bfd4-4b88-9a83-963d1d480d8b"},
                            "chapter_10": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fclass_10_science_chapter_10_emb.pickle?alt=media&token=8ce75623-28c3-4db2-ba18-9e20823b24a8",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fclass_10_science_chapter_10_text.pickle?alt=media&token=e51f5e77-10f9-4218-b71b-1d106eb1f467",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2010%2Fchapter%2010.epub?alt=media&token=988a0ab6-5b8f-45a6-ba13-f8d8603cbabb"},
                            "chapter_11": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fclass_10_science_chapter_11_emb.pickle?alt=media&token=31fcbfe9-bd93-43d1-9a5c-113a0eb52d19",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fclass_10_science_chapter_11_text.pickle?alt=media&token=d06b8cc4-e14a-4707-8740-ee83c4cda8d3",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2011%2Fchapter%2011.epub?alt=media&token=e6cf2759-9cba-46c1-b7ef-4462a9a669d7"},
                            "chapter_12": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fclass_10_science_chapter_12_emb.pickle?alt=media&token=51e6330e-cb2a-4c17-a437-ed3c0c8acf22",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fclass_10_science_chapter_12_text.pickle?alt=media&token=e7623977-a0c3-4169-8d6e-3c7de6ca1890",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2012%2Fchapter%2012.epub?alt=media&token=7072bd3e-a992-43ff-8e0d-580045b9aef4"},
                            "chapter_13": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fclass_10_science_chapter_13_emb.pickle?alt=media&token=2f8093a1-2b99-4088-bc2c-989caa23c6cd",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fclass_10_science_chapter_13_text.pickle?alt=media&token=782665ce-b872-46a9-a309-0bba1fe964b9",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2013%2Fchapter%2013.epub?alt=media&token=4808231f-f255-4912-a24c-d52343cef661"},
                            "chapter_14": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fclass_10_science_chapter_14_emb.pickle?alt=media&token=dd06c239-068f-4062-80ab-a8ad52b0cfa5",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fclass_10_science_chapter_14_text.pickle?alt=media&token=d48bc2e7-18db-4f6a-9e8c-6dc8b9ab1b48",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2014%2Fchapter%2014.epub?alt=media&token=4dfce889-f5ea-4ffe-b1e1-d5c8cb64ef09"},
                            "chapter_15": {
                                "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fclass_10_science_chapter_15_emb.pickle?alt=media&token=e6c00313-dea9-47ab-94c1-a4e9fc5fddfd",
                                "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fclass_10_science_chapter_15_text.pickle?alt=media&token=3d6166c2-722a-44de-a7bb-aa77e4ef3e32",
                                "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/all%20grade%20subjects%20pickles%2Fclass%2010th%2Fscience%2Fchapter%2015%2Fchapter%2015.epub?alt=media&token=787d5bb8-ddcb-49bf-a5ab-82af2f1ee14b"}
                            }
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from u736502961_hys.live_books where grade=%s;",grade)
        row = cursor.fetchall()
        if len(row) > 0:
            for i in range(len(row)):
                if row[i]["dictionary_id"]=='economics10ncert01':
                    row[i]["dictionary_list"]=economics10ncert01
                elif row[i]["dictionary_id"]=='geography10ncert01':
                    row[i]["dictionary_list"]=geography10ncert01
                elif row[i]["dictionary_id"]=='history10ncert01':
                    row[i]["dictionary_list"]=history10ncert01
                elif row[i]["dictionary_id"]=='mathematics10ncert01':
                    row[i]["dictionary_list"]=mathematics10ncert01
                elif row[i]["dictionary_id"]=='civics10ncert01':
                    row[i]["dictionary_list"]=civics10ncert01
                elif row[i]["dictionary_id"]=='science10ncert01':
                    row[i]["dictionary_list"]=science10ncert01
        cursor.execute("select distinct subject_ from u736502961_hys.live_books where grade=%s;",grade)
        row[0]["distinct_subjects"] = cursor.fetchall()
        cursor.execute("select distinct publication from u736502961_hys.live_books where grade=%s;",grade)
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

        mathematics10cbseqp = {"2011": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011_emb.pickle?alt=media&token=8cda6557-326e-407d-997d-6736e3a9114f",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011_text.pickle?alt=media&token=2fd2e82f-9da4-4bcd-96d0-6e551cc7b273",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011.epub?alt=media&token=3c2f09ea-bed4-419b-abc3-1430836427c7",
            "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2011_cluster.pkl?alt=media&token=ab494bc1-854a-4f8c-8a06-6dea944706e5"},
                               "2012": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012_emb.pickle?alt=media&token=b6607530-602f-435e-8c56-f5cb39372529",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012_text.pickle?alt=media&token=72034f2a-f4d4-44e9-b466-ae579852cdaa",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012.epub?alt=media&token=3a083886-f4fc-42d5-ba0c-14a468e30601",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2012_cluster.pkl?alt=media&token=f67747f1-806a-482d-88c0-e965f359e90a"},
                               "2013": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013_emb.pickle?alt=media&token=be5a7c13-57d6-45a4-8227-9f5a23aadcb4",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013_text.pickle?alt=media&token=085995bf-c6c2-469d-8c9b-2e2c29817823",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013.epub?alt=media&token=bf2d9a38-adca-4064-894d-d81fff516945",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2013_cluster.pkl?alt=media&token=e730e294-0d8b-445c-8cd0-a7f43fb0cf86"},
                               "2014": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_emb.pickle?alt=media&token=6059a573-8134-479e-9c98-8ba29f512150",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_text.pickle?alt=media&token=ddb22b32-2333-40d2-9597-223f37a69129",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_1.epub?alt=media&token=363d59c8-038d-4f18-ae44-1e7730dcb98b",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2014_cluster.pkl?alt=media&token=4993788d-db82-4346-b10d-e1dea29060b4"},
                               "2015": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_emb.pickle?alt=media&token=2d882810-7617-4f06-85be-400e7bb1cffc",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_text.pickle?alt=media&token=d3298f7d-ae95-4064-bd33-55817c9e48f2",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_1.epub?alt=media&token=1ad7b23b-7d10-4c94-9498-737089d49ea3",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2015_cluster.pkl?alt=media&token=0ffff999-3d27-4525-af8f-b4f35e188dff"},
                               "2016": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_emb.pickle?alt=media&token=57879e83-2b6d-4bcc-980e-53b06b14a531",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_text.pickle?alt=media&token=d4324089-63c3-440d-9333-a6bf48601c1d",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_1.epub?alt=media&token=202282e2-587c-4c75-8a42-293da97a0e21",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2016_cluster.pkl?alt=media&token=6fe31eb4-2b50-4ffa-9051-ef4152ace5f0"},
                               "2017": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_emb.pickle?alt=media&token=b0012395-71d5-4b3b-888d-292ffa296596",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_text.pickle?alt=media&token=eef25d2a-56df-4d0c-b7f0-c8e455836772",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_1.epub?alt=media&token=e0f6a475-555d-4d4f-84f9-efa05cec90f5",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2017_cluster.pkl?alt=media&token=172829ed-39c4-49ba-b09f-553f2940fd64"},
                               "2018": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018_emb.pickle?alt=media&token=e9a90d3a-e258-4385-a803-ce1efcbd6994",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018_text.pickle?alt=media&token=b12517e7-b241-4861-8a47-63e639d8508d",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018.epub?alt=media&token=6288245c-4bdd-4a9c-bc5b-b83276bcf8dd",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2018_cluster.pkl?alt=media&token=ca996f8b-4f33-4588-998e-9fa3c1678aa4"},
                               "2019": {
                                   "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019_emb.pickle?alt=media&token=6da2b71d-a8a5-4838-9abe-08f265714dda",
                                   "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019_text.pickle?alt=media&token=5788071e-157b-4c75-955d-cbb1e915d5b8",
                                   "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019.epub?alt=media&token=76097a32-ceda-4c7d-820e-01f2934f92f6",
                                   "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FMaths%2F2019_cluster.pkl?alt=media&token=6d23adaf-91df-4a76-b273-67bd4ded1c51"}
                               }

        science10cbseqp = {"2012": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2012_embedded.pickle?alt=media&token=4b94da89-3467-406d-be10-78a0a141d12f",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2012.pickle?alt=media&token=a09e4d73-6d01-4c38-9d9c-79ab508c6f9a",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2012.epub?alt=media&token=fb00f8e4-5bbb-4024-8837-ace3058794f4",
            "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_12_cluster.pickle?alt=media&token=2fbf1661-5b74-4890-94fc-8ce879c9e30c"},
                           "2013": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2013_embedded.pickle?alt=media&token=160b758d-4437-4228-b09a-d6a57864e712",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2013.pickle?alt=media&token=5dc4282d-ce8b-4cde-aca1-930dbec1dcc0",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2013.epub?alt=media&token=a4350843-053a-4039-88b1-cc82098e6429",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_13_cluster.pickle?alt=media&token=6bfbd88b-330b-43b9-b549-ae72f60994c0"},
                           "2014": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2014_embedded.pickle?alt=media&token=7d616642-4b38-42fc-acda-2507988a438f",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2014.pickle?alt=media&token=bb57dccb-32a5-4f93-b0de-c487dc15c3d4",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2014.epub?alt=media&token=e2dfe2f8-e3f6-4618-be02-c2b1b3904385",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_14_cluster.pickle?alt=media&token=97cdb137-8f5d-4018-b6b8-d8938cb1486c"},
                           "2015": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2015_embedded.pickle?alt=media&token=1a013130-1997-4f94-9495-89234ca0e57d",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2015.pickle?alt=media&token=cf2343a7-0b65-41e9-ad13-6c20189be5fa",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2015.epub?alt=media&token=cbb9f2fa-1a6c-4b8f-a3de-9c609bd50e66",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_15_cluster.pickle?alt=media&token=08a215af-d2d1-4a81-b5d7-c5bc4b183c24"},
                           "2016": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2016_embedded.pickle?alt=media&token=ddeb871b-c8c8-4d2e-88d3-a9d366199aed",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2016.pickle?alt=media&token=bdbe32d7-a210-40b4-b5b4-9613127d3081",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2016.epub?alt=media&token=9aa3b919-a69d-40cc-8672-869fa551d823",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_16_cluster.pickle?alt=media&token=8e113cde-bdde-4629-9808-d6a01ee780aa"},
                           "2017": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2017_embedded.pickle?alt=media&token=a95c58e2-043c-4658-b918-7ce16bdb1d42",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2017.pickle?alt=media&token=590f275a-b9c0-4b20-b9fc-75fd47235d10",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_paper_2017.epub?alt=media&token=75a13f78-afe5-4e68-a62f-b7f7b4458ad0",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_17_cluster.pickle?alt=media&token=34acff80-aa59-4890-888f-e185851bc7d3"},
                           "2018": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2018_embedded.pickle?alt=media&token=782894fb-0472-4ae6-baaf-7e6f8a4b28a4",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2018.pickle?alt=media&token=9c6f79d8-f1c8-40fb-8f7f-f1fec10d700d",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_2018.epub?alt=media&token=8bf45d36-c5a6-4bc3-822c-2728e2d0d4dd",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_18_cluster.pickle?alt=media&token=b8d1d027-4449-41a7-836d-0b95d5175c77"},
                           "2019": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2019_embedded.pickle?alt=media&token=6fe10feb-cff4-450a-ba34-026fc88e3553",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2019.pickle?alt=media&token=a2b8cf88-6ba2-4105-8fc6-18c249a082d3",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_2019.epub?alt=media&token=1f733f27-9e27-48a5-9228-0a31a73c553d",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_19_cluster.pickle?alt=media&token=c0304f99-d672-4682-8289-ee0e01a7cfec"},
                           "2020": {
                               "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2020_embedded.pickle?alt=media&token=be6dc2c3-23cd-4a00-9492-1f8e43193079",
                               "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2FCBSE_SCIENCE_QUESTION_2020.pickle?alt=media&token=6aa78b26-a43c-4b22-84c7-1a799667c4d5",
                               "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fcbse_science_2020.epub?alt=media&token=2ea3c96d-1701-44a2-9681-65e9b7db65c1",
                               "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FScience%2Fscience_paper_20_cluster.pickle?alt=media&token=799a09f8-3b85-4005-9735-3d471bc98620"},
                           }

        socialScience10cbseqp = {"2011": {
            "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst_emb.pickle?alt=media&token=363887b5-c9b6-4691-b73d-0dd6480dc620",
            "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst_text.pickle?alt=media&token=8a89723b-89ce-4b42-960e-1a19765419a9",
            "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst.epub?alt=media&token=58b1fe97-28b6-4ae6-958a-1a94e480021a",
            "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2011_sst_cluster.pkl?alt=media&token=6a54309a-5078-4b91-a2f5-aceeb3373c96"},
                                 "2012": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst_emb.pickle?alt=media&token=73d24331-048b-4c41-8d8d-bfb69b2896ea",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst_text.pickle?alt=media&token=d1923f9d-37a4-40c2-b236-f130b4fd1c1c",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst.epub?alt=media&token=aa3cd7a5-622e-4677-afc7-b023ab518bd8",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2012_sst_cluster.pkl?alt=media&token=eb422dee-51a6-4ee3-96b4-e8d77f876640"},
                                 "2013": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst_emb.pickle?alt=media&token=b95f954e-9720-467a-a432-f4e13b3e4ee4",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst_text.pickle?alt=media&token=ca43166a-e8a5-4f42-976f-031ab16fb664",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst.epub?alt=media&token=f13e65f4-359d-4954-ae41-d00ff5b7621a",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2013_sst_cluster.pkl?alt=media&token=3711354b-d97c-48cd-8cfa-51350124603a"},
                                 "2014": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst_emb.pickle?alt=media&token=39bd27d0-ce0b-4c00-8b50-57ebee5f998a",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst_text.pickle?alt=media&token=297de573-404b-4157-b90a-3711dd0b07dd",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst.epub?alt=media&token=be5fdd8a-413c-47de-8e70-ff47be747c1e",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2014_sst_cluster.pkl?alt=media&token=c04fedcc-f3ab-4ce6-b645-b27bc807edf1"},
                                 "2015": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst_emb.pickle?alt=media&token=2a254d25-5fe6-4096-90fc-b43148c895fb",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst_text.pickle?alt=media&token=387bcc97-b17e-432e-8cfb-49afbd166a79",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst.epub?alt=media&token=116a0129-d20e-4201-a2f1-2d37ba15edcd",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2015_sst_cluster.pkl?alt=media&token=c98eb266-be78-48f9-8ce0-40f5a74b35a8"},
                                 "2016": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst_emb.pickle?alt=media&token=4dfc4f4d-b3c7-4471-a46a-1525512c97a7",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst_text.pickle?alt=media&token=edfb98ed-cd29-41bd-9571-c9b5ee369387",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst.epub?alt=media&token=a370fcd8-4068-4522-8cfd-569efe237525",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2016_sst_cluster.pkl?alt=media&token=669dd222-bc2d-4447-bbf1-9e29ed15285d"},
                                 "2017": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst_emb.pickle?alt=media&token=e4ec2f4d-34be-4581-a06d-3a74c9f90f3c",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst_text.pickle?alt=media&token=8b496bb1-e8fc-4087-9d5d-b9398ca0dece",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst.epub?alt=media&token=70a3c4fa-34ac-435e-b446-09750eab3ea3",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2017_sst_cluster.pkl?alt=media&token=7f67e795-c3be-4d3b-a558-9b04b738680c"},
                                 "2018": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst_emb.pickle?alt=media&token=1d4eeb73-4d34-41b4-9d3a-4aec87a37ad8",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst_text.pickle?alt=media&token=19d92b13-eee5-46a3-b399-46b8010e2bb2",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst.epub?alt=media&token=7c47228e-6238-4fa8-9b75-dc0c09de74c9",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2018_sst_cluster.pkl?alt=media&token=e59f092d-c044-444d-97aa-c3773f6ab89f"},
                                 "2019": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst_emb.pickle?alt=media&token=5aa4f8e6-6c1f-4691-9bd0-6c746edc5a3d",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst_text.pickle?alt=media&token=93b2936e-3aad-4b63-ae0e-72e602371181",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst.epub?alt=media&token=da1bedff-36df-4989-8902-3e4f04a11908",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2019_sst_cluster.pkl?alt=media&token=b2bf2d98-05a9-433b-800f-c9d71e978557"},
                                 "2020": {
                                     "embeddings": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst_emb.pickle?alt=media&token=0c548d9a-e88a-4fb5-99bb-c5c81b34690d",
                                     "text": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst_text.pickle?alt=media&token=a80797ba-6ee0-4256-8943-594268b619c0",
                                     "epub": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst.epub?alt=media&token=2c5fa47a-e196-4541-85ae-4c97fc22d3a5",
                                     "cluster": "https://firebasestorage.googleapis.com/v0/b/hys-pro-41c66.appspot.com/o/class%2010%20question%20paper%2FSocial%20Science%2F2020_sst_cluster.pkl?alt=media&token=629ca8d7-250d-4a34-8b94-0e34fcde88d7"}
                                 }

        accountany12cbseqp = {"2015": {
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

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        data = (grade, subject)
        cursor.execute("select * from u736502961_hys.live_books_question_papers where grade=%s and subject_=%s;", data)
        row = cursor.fetchall()
        if len(row) > 0:
            for i in range(len(row)):
                if row[i]["dictionary_id"]=='mathematics10cbseqp':
                    row[i]["dictionary_list"]=mathematics10cbseqp
                elif row[i]["dictionary_id"]=='science10cbseqp':
                    row[i]["dictionary_list"]=science10cbseqp
                elif row[i]["dictionary_id"]=='socialScience10cbseqp':
                    row[i]["dictionary_list"]=socialScience10cbseqp
                elif row[i]["dictionary_id"]=='accountany12cbseqp':
                    row[i]["dictionary_list"]=accountany12cbseqp
                elif row[i]["dictionary_id"]=='biology12cbseqp':
                    row[i]["dictionary_list"]=biology12cbseqp
                elif row[i]["dictionary_id"]=='businessStudies12cbseqp':
                    row[i]["dictionary_list"]=businessStudies12cbseqp
                elif row[i]["dictionary_id"]=='chemistry12cbseqp':
                    row[i]["dictionary_list"]=chemistry12cbseqp
                elif row[i]["dictionary_id"]=='history12cbseqp':
                    row[i]["dictionary_list"]=history12cbseqp
                elif row[i]["dictionary_id"]=='physics12cbseqp':
                    row[i]["dictionary_list"]=physics12cbseqp
        resp = jsonify(row)
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
            data = (_book_id, _chapter_id, _user_id, _base_offset, _extent_offset, _tag_index, _color, _selection_type, _level, _text_selected)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("insert into u736502961_hys.user_epub_select(book_id,chapter_id,user_id,base_offset,extent_offset,tag_index,color,selection_type,level_, text_selected) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", data)
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
        cursor.execute("select * from u736502961_hys.user_epub_select where user_id=%s;",id)
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





