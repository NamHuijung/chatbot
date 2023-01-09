import pymysql
# DB 호스트 연경 및 닫기
db = None
try:
    # DB 호스트 정보에 맞게 입력
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='Loeeol0223!',
        db='homestead',
        charset='utf8'
    )
    print('DB 연결 성공')
except Exception as e:
    print(e)  # db 연결 실패 시 오류 내용 출력

finally:
    if db is not None:  # db가 연결된 경우에만 접속 닫기 시도
        db.close()
        print('DB 연결 닫기 성공')

# 데이터 삽입
db = None
try:
    # DB 호스트 정보에 맞게 입력
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='Loeeol0223!',
        db='homestead',
        charset='utf8'
    )

    # 테이블 생성 sql 정의
    sql = '''
        INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
    '''

    # 데이터 삽입
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)  # db 연결 실패 시 오류 내용 출력

finally:
    if db is not None:  # db가 연결된 경우에만 접속 닫기 시도
        db.close()

# 데이터 변경
db = None
try:
    # DB 호스트 정보에 맞게 입력
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='Loeeol0223!',
        db='homestead',
        charset='utf8'
    )

    # 데이터 수정 sql 정의
    id = 1  # 데이터 id(Primary Key)
    sql = '''
        UPDATE tb_student set name="케이", age=36 where id=%d
    ''' % id

    # 데이터 수정
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)  # db 연결 실패 시 오류 내용 출력

finally:
    if db is not None:  # db가 연결된 경우에만 접속 닫기 시도
        db.close()

# 데이터 삭제
db = None
try:
    # DB 호스트 정보에 맞게 입력
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='Loeeol0223!',
        db='homestead',
        charset='utf8'
    )

    # 데이터 삭제 sql 정의
    id = 1  # 데이터 id(Primary Key)
    sql = '''
        DELETE from tb_student where id=%d
    ''' % id

    # 데이터 삭제
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)  # db 연결 실패 시 오류 내용 출력

finally:
    if db is not None:  # db가 연결된 경우에만 접속 닫기 시도
        db.close()

# 데이터 조회
import pandas as pd

db = None
try:
    # DB 호스트 정보에 맞게 입력
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='Loeeol0223!',
        db='homestead',
        charset='utf8'
    )

    # 데이터 db에 추가
    students = [
        {'name': 'Kei', 'age': 36, 'address': 'PUSAN'},
        {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
        {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
        {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
        {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
    ]
    for s in students:
        with db.cursor() as cursor:
            sql = '''
                insert tb_student(name, age, address) values("%s", "%d", "%s")
            ''' % (s['name'], s['age'], s['address'])
            cursor.execute(sql)
    db.commit()  # 커밋

    # 30대 학생만 조회
    cond_age = 30
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            select * from tb_student where age > %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall()
    print(results)

    # fetchall() 함수는 select 구문으로 조회한 모든 데이터를 불러오는 함수이다
    # 불러온 데이터의 각 항목은 딕셔너리 형태이다

    # 이름 검색
    cond_name = 'Grace'
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            select * from tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone()
    print(result['name'], result['age'])

    # fetchone() 함수는 select 구문을 통해 조회한 데이터 중 1개의 행만 불러오는 함수이다

    # pandas 데이터프레임으로 표현
    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print(e)  # db 연결 실패 시 오류 내용 출력

finally:
    if db is not None:  # db가 연결된 경우에만 접속 닫기 시도
        db.close()