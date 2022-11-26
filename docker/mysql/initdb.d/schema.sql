CREATE TABLE userinfo (
    userID INT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(30) NOT NULL,
    userBirth DATE NOT NULL,              /*'YYYY-MM-DD'*/
    userGender BOOLEAN NOT NULL,          /*여(0)남(1)*/
    hpHighblood BOOLEAN DEFAULT FALSE,    /*False||True*/
    hpDiabetes BOOLEAN DEFAULT FALSE,     /*False||True*/
    userDate DATE DEFAULT (current_date), /*'YYYY-MM-DD'*/
    PRIMARY KEY (userID)
);

CREATE TABLE pressureTable (
    userID INT NOT NULL,
    userDate DATE NOT NULL, /*측정일시*/
    morningPressure FLOAT,  /*아침혈압*/
    eveningPressure FLOAT,  /*저녁혈압*/
    spandrelSugar FLOAT,    /*공복혈당*/
    aftermealSugar FLOAT,   /*식후혈당*/
    beforesleepSugar FLOAT, /*취침전혈당*/
    PRIMARY KEY (userID, userDate)
    FOREIGN KEY (userID)
);

CREATE TABLE sympotom (
    userID INT NOT NULL,
    sympotomID INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (userID, sympotomID)
    FOREIGN KEY (userID, sympotomID)
);

CREATE TABLE sympotom_schema (
    sympotomID INT NOT NULL AUTO_INCREMENT,
    sympotomName VARCHAR(30) NOT NULL,
    PRIMARY KEY (sympotomID)
);

CREATE TABLE situation (
    userID INT NOT NULL,
    situationID INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (userID, situationID)
    FOREIGN KEY (userID, situationID)
);

CREATE TABLE situation_schema (
    situationID INT NOT NULL AUTO_INCREMENT,
    situationName VARCHAR(30) NOT NULL,
    PRIMARY KEY (situationID)
);