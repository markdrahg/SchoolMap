## NOTE

cd djangoapp

## TO INITIATE APP

puthon mange.py runserver

## TO CONNECT AND MIGRATE MySQL DATA BASE

python manage.py makemigratons my_app
python manage.py migrate

## TO START MySQL SERVICE VIA SERVICES PANEL

Press Win + R, type services.msc, and press Enter.
Find MySQL or MySQL80 in the list, right-click on it, and select Start

## MoST USED MySQL CMD'S FOR PROJECT CHECKUP

show databases;
show tables;
use schoolmap2;
select \* from my_app_customuser;
describe my_app_customuser;

## METHOD OF FEEDING-IN THE DATABASE WITH SCHOOLS DATA

### TYPE 1

INSERT INTO my_app_school(name, acceptance_rate, country, website)
VALUES ('German University', '3', 'Germany', 'germanschool.com');

### TYPE 2 (USA SCHOOL DATA)

INSERT INTO my_app_school (name, acceptance_rate, country, website)
VALUES
('Harvard University', '4', 'USA', 'harvard.edu/'),
('Stanford University', '4', 'USA', 'stanford.edu/'),
('Princeton University', '4', 'USA', 'princeton.edu/'),
('Yale University', '6', 'USA', 'yale.edu/'),
('Columbia University', '61', 'USA', 'columbia.edu/'),
('MIT', '4', 'USA', 'mit.edu/'),
('Caltech', '3', 'USA', 'caltech.edu/'),
('University of Chicago', '6', 'USA', 'uchicago.edu/'),
('Duke University', '6', 'USA', 'duke.edu/'),
('Johns Hopkins University', '7', 'USA', 'www.jhu.edu/'),
('Purdue University', '54', 'USA', 'purdue.edu/'),
('University of Illinois', '52', 'USA', 'illinois.edu/'),
('Arizona State University', '81', 'USA', 'asu.edu/'),
('Texas A&M University', '77.3', 'USA', 'www.tamu.edu/');

### (Canada SCHOOL DATA)

INSERT INTO my_app_school (name, acceptance_rate, country, website)
VALUES
('University of Toronto', '43', 'Canada', 'utoronto.ca/'),
('University of British Columbia', '51', 'Canada', 'ubc.ca/'),
('McGill University', '42', 'Canada', 'mcgill.ca/'),
('McMaster University', '40', 'Canada', 'mcmaster.ca/'),
('University of Alberta', '60', 'Canada', 'ualberta.ca/'),
('University of Waterloo', '53', 'Canada', 'uwaterloo.ca/'),
('Queen\'s University', 42.0, 'Canada', 'https://www.queensu.ca/'),
('Western University', '54', 'Canada', 'westernu.ca/'),
('University of Calgary', '55', 'Canada', 'ucalgary.ca/'),
('University of Manitoba', '65', 'Canada', 'umanitoba.ca/');

## AVAIOABLE USER

Mark
mark@gmail.com
MArk@123
