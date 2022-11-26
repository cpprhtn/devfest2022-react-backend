INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (0, "두통")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (1, "의식 저하")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (2, "흉통")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (3, "호흡 곤란")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (4, "구역")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (5, "구토")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (6, "어지러움")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (7, "시야흐려짐")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (8, "다뇨")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (9, "다음")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (10, "체중감소")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (11, "탈수")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (12, "쇠약")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (13, "의식변화")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (14, "복부통증")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (15, "떨림")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (16, "식은땀")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (17, "심계항진")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (18, "빈맥")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (19, "사지에 저린 느낌")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (20, "공복감")
INSERT INTO sympotom_schema (sympotomID, sympotomName) VALUES (21, "불안감")




INSERT INTO situation_schema (situationID, situationName) VALUES (1, "호흡곤란")
INSERT INTO situation_schema (situationID, situationName) VALUES (2, "창백")
INSERT INTO situation_schema (situationID, situationName) VALUES (3, "어지러움")
INSERT INTO situation_schema (situationID, situationName) VALUES (4, "두통")
INSERT INTO situation_schema (situationID, situationName) VALUES (5, "피로감")
INSERT INTO situation_schema (situationID, situationName) VALUES (6, "피부의 차고 축축함")
INSERT INTO situation_schema (situationID, situationName) VALUES (7, "가슴의 답답함")
INSERT INTO situation_schema (situationID, situationName) VALUES (8, "미열")
INSERT INTO situation_schema (situationID, situationName) VALUES (9, "맥의 불규칙함")
INSERT INTO situation_schema (situationID, situationName) VALUES (10, "메스꺼움")
INSERT INTO situation_schema (situationID, situationName) VALUES (11, "구토")
INSERT INTO situation_schema (situationID, situationName) VALUES (12, "정신 집중의 어려움")
INSERT INTO situation_schema (situationID, situationName) VALUES (13, "흐린 시력")
INSERT INTO situation_schema (situationID, situationName) VALUES (14, "목마름")
INSERT INTO situation_schema (situationID, situationName) VALUES (15, "감염")
INSERT INTO situation_schema (situationID, situationName) VALUES (16, "잘못된 혈당강하제 사용")
INSERT INTO situation_schema (situationID, situationName) VALUES (17, "뇌혈관질환")
INSERT INTO situation_schema (situationID, situationName) VALUES (18, "심근경색증")
INSERT INTO situation_schema (situationID, situationName) VALUES (19, "외상")
INSERT INTO situation_schema (situationID, situationName) VALUES (20, "인슐린 중단")
INSERT INTO situation_schema (situationID, situationName) VALUES (21, "부적절한 투여")



INSERT INTO userinfo (userID, userName, userBirth, userGender, hpHighblood, hpDiabetes, userDate) VALUES (0, "이준원", '2002-05-13', 1, FALSE, FALSE, '2022-11-23')
INSERT INTO pressureTable (userID, userDate, morningPressure, eveningPressure, spandrelSugar, aftermealSugar, beforesleepSugar) VALUES (0, "이준원", '2022-11-23', 120, 90, 100, 100, 100)
INSERT INTO sympotom (userID, sympotomID) VALUES (0, 0)
INSERT INTO sympotom (userID, sympotomID) VALUES (0, 6)
INSERT INTO sympotom (userID, sympotomID) VALUES (0, 21)
INSERT INTO situation (userid, situationID) VALUES (0, 3)
INSERT INTO situation (userid, situationID) VALUES (0, 4)
INSERT INTO situation (userid, situationID) VALUES (0, 5)